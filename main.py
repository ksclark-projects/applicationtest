import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Application test CLI")
    parser.add_argument('--version', action='store_true', help='Print the Python version number and exit')
    args = parser.parse_args()

    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro

    if args.version:
        print(f"{major}.{minor}.{micro}")
        sys.exit(0)

    print(f"Python {major}.{minor}.{micro}")


if __name__ == "__main__":
    main()
