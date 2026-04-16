import argparse
import platform
import sys


def main():
    try:
        from colorama import Fore, Style, init
        init()
        CYAN = Fore.CYAN
        WHITE = Style.RESET_ALL
        HAS_COLOR = True
    except ImportError:
        CYAN = ""
        WHITE = ""
        HAS_COLOR = False

    parser = argparse.ArgumentParser(description="Application test CLI")
    parser.add_argument('--version', action='store_true', help='Print the Python version number and exit')
    parser.add_argument('--all', action='store_true', help='Display full Python environment info')
    parser.add_argument('--os', action='store_true', help='Print OS name, version, and release')
    args = parser.parse_args()

    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro

    if args.version:
        print(f"{major}.{minor}.{micro}")
        sys.exit(0)

    if args.os:
        print(f"{CYAN}OS name:{WHITE} {platform.system()}")
        print(f"{CYAN}OS release:{WHITE} {platform.release()}")
        print(f"{CYAN}OS version:{WHITE} {platform.version()}")
        sys.exit(0)

    if getattr(args, 'all'):
        print(f"{CYAN}Python version:{WHITE} {major}.{minor}.{micro}")
        print(f"{CYAN}Version info:{WHITE} {sys.version_info}")
        print(f"{CYAN}Platform:{WHITE} {platform.platform()}")
        print(f"{CYAN}OS name:{WHITE} {platform.system()}")
        print(f"{CYAN}OS release:{WHITE} {platform.release()}")
        print(f"{CYAN}OS version:{WHITE} {platform.version()}")
        sys.exit(0)

    print(f"Python {major}.{minor}.{micro}")


if __name__ == "__main__":
    main()
