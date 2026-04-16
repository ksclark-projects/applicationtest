import argparse
import platform
import sys

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False


def get_cpu_info():
    return {
        "cores": psutil.cpu_count(logical=True),
        "architecture": platform.machine(),
        "usage_percent": psutil.cpu_percent(interval=None),
    }


def get_disk_info():
    partitions = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            partitions.append({
                "mountpoint": part.mountpoint,
                "total": round(usage.total / (1024 ** 3), 1),
                "used": round(usage.used / (1024 ** 3), 1),
                "free": round(usage.free / (1024 ** 3), 1),
            })
        except PermissionError:
            continue
    return partitions


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
    parser.add_argument('--cpu', action='store_true', help='Display CPU cores, architecture, and usage')
    parser.add_argument('--disk', action='store_true', help='Display per-partition disk usage (total, used, free in GB)')
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

    if args.cpu:
        info = get_cpu_info()
        print("=== CPU ===")
        print(f"{CYAN}CPU Cores:{WHITE} {info['cores']}")
        print(f"{CYAN}Architecture:{WHITE} {info['architecture']}")
        print(f"{CYAN}CPU Usage:{WHITE} {info['usage_percent']}%")
        sys.exit(0)

    if args.disk:
        partitions = get_disk_info()
        print("=== Disk ===")
        for p in partitions:
            print(f"{CYAN}Disk {p['mountpoint']}:{WHITE} {CYAN}Total:{WHITE} {p['total']} GB, {CYAN}Used:{WHITE} {p['used']} GB, {CYAN}Free:{WHITE} {p['free']} GB")
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
