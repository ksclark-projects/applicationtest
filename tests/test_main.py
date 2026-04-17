import platform
import re
import subprocess
import sys

MAIN_CWD = "/Users/kclark/Development/applicationtest.outworked-worktrees/us-004-default-no-flags-shows-all-categories-mo26b55w"


def run_main(*args):
    return subprocess.run(
        [sys.executable, "main.py", *args],
        capture_output=True,
        text=True,
        cwd=MAIN_CWD,
    )


def test_python_in_output():
    result = run_main()
    assert "Python" in result.stdout


def test_version_format():
    result = run_main()
    assert re.search(r"\d+\.\d+\.\d+", result.stdout)


def test_default_shows_cpu_section():
    result = run_main()
    assert result.returncode == 0
    assert "=== CPU ===" in result.stdout


def test_default_shows_memory_section():
    result = run_main()
    assert result.returncode == 0
    assert "=== Memory ===" in result.stdout


def test_default_shows_disk_section():
    result = run_main()
    assert result.returncode == 0
    assert "=== Disk ===" in result.stdout


def test_default_shows_cpu_cores():
    result = run_main()
    assert "CPU Cores:" in result.stdout


def test_default_shows_memory_total():
    result = run_main()
    assert "Total:" in result.stdout


def test_default_shows_disk_free():
    result = run_main()
    assert "Free:" in result.stdout


def test_os_flag():
    result = run_main("--os")
    assert result.returncode == 0
    os_name = platform.system()
    assert os_name in result.stdout


def test_version_flag():
    result = run_main("--version")
    assert result.returncode == 0
    # Output must be only the bare version string (no extra labels)
    assert re.fullmatch(r"\d+\.\d+\.\d+\n?", result.stdout.strip() + "\n")


def test_cpu_flag_exit_code():
    result = run_main("--cpu")
    assert result.returncode == 0


def test_cpu_flag_cores():
    result = run_main("--cpu")
    assert "CPU Cores:" in result.stdout


def test_cpu_flag_architecture():
    result = run_main("--cpu")
    assert "Architecture:" in result.stdout


def test_cpu_flag_usage():
    result = run_main("--cpu")
    assert "CPU Usage:" in result.stdout


def test_memory_flag_exit_code():
    result = run_main("--memory")
    assert result.returncode == 0


def test_memory_flag_shows_section():
    result = run_main("--memory")
    assert "=== Memory ===" in result.stdout


def test_memory_flag_shows_total():
    result = run_main("--memory")
    assert "Total:" in result.stdout


def test_memory_flag_shows_available():
    result = run_main("--memory")
    assert "Available:" in result.stdout


def test_disk_flag_exit_code():
    result = run_main("--disk")
    assert result.returncode == 0


def test_disk_flag_shows_section():
    result = run_main("--disk")
    assert "=== Disk ===" in result.stdout


def test_disk_flag_shows_free():
    result = run_main("--disk")
    assert "Free:" in result.stdout


def test_all_flag():
    result = run_main("--all")
    assert result.returncode == 0
    # Check version digits appear
    assert re.search(r"\d+\.\d+\.\d+", result.stdout)
    # Check platform info is present
    platform_str = platform.platform()
    # At minimum, a platform keyword should appear (e.g. macOS, Linux, Windows)
    assert any(keyword in result.stdout for keyword in ["macOS", "Linux", "Windows", "Darwin", platform_str[:6]])


def test_default_shows_cpu():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert "CPU Cores:" in result.stdout


def test_default_shows_memory():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert "Memory Total:" in result.stdout


def test_default_shows_disk():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert "Disk" in result.stdout or "Mount" in result.stdout


def test_memory_flag():
    result = subprocess.run(
        [sys.executable, "main.py", "--memory"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert result.returncode == 0
    assert "Memory Total:" in result.stdout


def test_disk_flag():
    result = subprocess.run(
        [sys.executable, "main.py", "--disk"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert result.returncode == 0
    assert "Mount:" in result.stdout
