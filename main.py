import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Application test CLI")
    parser.parse_args()

    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro
    print(f"Python {major}.{minor}.{micro}")


if __name__ == "__main__":
    main()
