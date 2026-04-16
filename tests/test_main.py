import platform
import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = str(Path(__file__).parent.parent)


def test_python_in_output():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert "Python" in result.stdout


def test_version_format():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert re.search(r"\d+\.\d+\.\d+", result.stdout)


def test_os_flag():
    result = subprocess.run(
        [sys.executable, "main.py", "--os"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert result.returncode == 0
    os_name = platform.system()
    assert os_name in result.stdout


def test_version_flag():
    result = subprocess.run(
        [sys.executable, "main.py", "--version"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert result.returncode == 0
    # Output must be only the bare version string (no extra labels)
    assert re.fullmatch(r"\d+\.\d+\.\d+\n?", result.stdout.strip() + "\n")


def test_cpu_flag_exit_code():
    result = subprocess.run(
        [sys.executable, "main.py", "--cpu"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert result.returncode == 0


def test_cpu_flag_cores():
    result = subprocess.run(
        [sys.executable, "main.py", "--cpu"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert "CPU Cores:" in result.stdout


def test_cpu_flag_architecture():
    result = subprocess.run(
        [sys.executable, "main.py", "--cpu"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert "Architecture:" in result.stdout


def test_cpu_flag_usage():
    result = subprocess.run(
        [sys.executable, "main.py", "--cpu"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert "CPU Usage:" in result.stdout


def test_all_flag():
    result = subprocess.run(
        [sys.executable, "main.py", "--all"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert result.returncode == 0
    # Check version digits appear
    assert re.search(r"\d+\.\d+\.\d+", result.stdout)
    # Check platform info is present
    platform_str = platform.platform()
    # At minimum, a platform keyword should appear (e.g. macOS, Linux, Windows)
    assert any(keyword in result.stdout for keyword in ["macOS", "Linux", "Windows", "Darwin", platform_str[:6]])


def test_memory_flag_exit_code():
    result = subprocess.run(
        [sys.executable, "main.py", "--memory"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert result.returncode == 0


def test_memory_flag_total():
    result = subprocess.run(
        [sys.executable, "main.py", "--memory"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert "Memory Total:" in result.stdout


def test_memory_flag_used():
    result = subprocess.run(
        [sys.executable, "main.py", "--memory"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert "Memory Used:" in result.stdout


def test_memory_flag_available():
    result = subprocess.run(
        [sys.executable, "main.py", "--memory"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert "Memory Available:" in result.stdout


def test_get_memory_info():
    """Test that get_memory_info returns expected keys with numeric GB values."""
    sys.path.insert(0, PROJECT_ROOT)
    from main import get_memory_info
    info = get_memory_info()
    assert "total" in info
    assert "used" in info
    assert "available" in info
    assert isinstance(info["total"], float)
    assert isinstance(info["used"], float)
    assert isinstance(info["available"], float)
    assert info["total"] > 0
    assert info["used"] > 0
    assert info["available"] >= 0
