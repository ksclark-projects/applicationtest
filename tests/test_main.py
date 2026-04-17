import platform
import re
import subprocess
import sys


def test_python_in_output():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert "Python" in result.stdout


def test_version_format():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert re.search(r"\d+\.\d+\.\d+", result.stdout)


def test_os_flag():
    result = subprocess.run(
        [sys.executable, "main.py", "--os"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert result.returncode == 0
    os_name = platform.system()
    assert os_name in result.stdout


def test_version_flag():
    result = subprocess.run(
        [sys.executable, "main.py", "--version"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert result.returncode == 0
    # Output must be only the bare version string (no extra labels)
    assert re.fullmatch(r"\d+\.\d+\.\d+\n?", result.stdout.strip() + "\n")


def test_cpu_flag_exit_code():
    result = subprocess.run(
        [sys.executable, "main.py", "--cpu"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert result.returncode == 0


def test_cpu_flag_cores():
    result = subprocess.run(
        [sys.executable, "main.py", "--cpu"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert "CPU Cores:" in result.stdout


def test_cpu_flag_architecture():
    result = subprocess.run(
        [sys.executable, "main.py", "--cpu"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert "Architecture:" in result.stdout


def test_cpu_flag_usage():
    result = subprocess.run(
        [sys.executable, "main.py", "--cpu"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
    assert "CPU Usage:" in result.stdout


def test_all_flag():
    result = subprocess.run(
        [sys.executable, "main.py", "--all"],
        capture_output=True,
        text=True,
        cwd="/Users/kclark/Development/applicationtest",
    )
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
