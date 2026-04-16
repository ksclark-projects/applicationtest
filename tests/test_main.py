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
