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
