import re
import subprocess
import sys

from main import get_python_version


def test_version_includes_python_word():
    """Output must contain the word 'Python'."""
    version = get_python_version()
    assert "Python" in version


def test_version_format_major_minor_micro():
    """Output must match the 'Python X.Y.Z' format with numeric major.minor.micro."""
    version = get_python_version()
    pattern = r"^Python \d+\.\d+\.\d+$"
    assert re.match(pattern, version), f"Version string '{version}' does not match 'Python X.Y.Z'"


def test_version_matches_sys_version_info():
    """The numbers in the output must match sys.version_info."""
    version = get_python_version()
    info = sys.version_info
    expected = f"Python {info.major}.{info.minor}.{info.micro}"
    assert version == expected


def test_main_script_output():
    """Running main.py as a script should print 'Python X.Y.Z' to stdout."""
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    output = result.stdout.strip()
    assert "Python" in output
    pattern = r"^Python \d+\.\d+\.\d+$"
    assert re.match(pattern, output), f"Script output '{output}' does not match 'Python X.Y.Z'"
