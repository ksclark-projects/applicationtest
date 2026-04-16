import sys


def get_python_version():
    """Return the Python version as a formatted string."""
    info = sys.version_info
    return f"Python {info.major}.{info.minor}.{info.micro}"


def main():
    print(get_python_version())


if __name__ == "__main__":
    main()
