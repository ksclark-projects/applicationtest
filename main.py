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


def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "total_gb": round(mem.total / (1024 ** 3), 2),
        "available_gb": round(mem.available / (1024 ** 3), 2),
        "used_percent": mem.percent,
    }


def get_disk_info():
    disk = psutil.disk_usage("/")
    return {
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2),
        "used_percent": disk.percent,
    }


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
    parser.add_argument('--memory', action='store_true', help='Display memory total, available, and usage percent')
    parser.add_argument('--disk', action='store_true', help='Display disk total, used, free, and usage percent')
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

    if args.memory:
        info = get_memory_info()
        print("=== Memory ===")
        print(f"{CYAN}Total:{WHITE} {info['total_gb']} GB")
        print(f"{CYAN}Available:{WHITE} {info['available_gb']} GB")
        print(f"{CYAN}Used:{WHITE} {info['used_percent']}%")
        sys.exit(0)

    if args.disk:
        info = get_disk_info()
        print("=== Disk ===")
        print(f"{CYAN}Total:{WHITE} {info['total_gb']} GB")
        print(f"{CYAN}Used:{WHITE} {info['used_gb']} GB")
        print(f"{CYAN}Free:{WHITE} {info['free_gb']} GB")
        print(f"{CYAN}Used:{WHITE} {info['used_percent']}%")
        sys.exit(0)

    if getattr(args, 'all'):
        print(f"{CYAN}Python version:{WHITE} {major}.{minor}.{micro}")
        print(f"{CYAN}Version info:{WHITE} {sys.version_info}")
        print(f"{CYAN}Platform:{WHITE} {platform.platform()}")
        print(f"{CYAN}OS name:{WHITE} {platform.system()}")
        print(f"{CYAN}OS release:{WHITE} {platform.release()}")
        print(f"{CYAN}OS version:{WHITE} {platform.version()}")
        sys.exit(0)

    # Default: no flags — show all categories
    print(f"Python {major}.{minor}.{micro}")

    print("=== CPU ===")
    cpu = get_cpu_info()
    print(f"{CYAN}CPU Cores:{WHITE} {cpu['cores']}")
    print(f"{CYAN}Architecture:{WHITE} {cpu['architecture']}")
    print(f"{CYAN}CPU Usage:{WHITE} {cpu['usage_percent']}%")

    print("=== Memory ===")
    mem = get_memory_info()
    print(f"{CYAN}Total:{WHITE} {mem['total_gb']} GB")
    print(f"{CYAN}Available:{WHITE} {mem['available_gb']} GB")
    print(f"{CYAN}Used:{WHITE} {mem['used_percent']}%")

    print("=== Disk ===")
    disk = get_disk_info()
    print(f"{CYAN}Total:{WHITE} {disk['total_gb']} GB")
    print(f"{CYAN}Used:{WHITE} {disk['used_gb']} GB")
    print(f"{CYAN}Free:{WHITE} {disk['free_gb']} GB")
    print(f"{CYAN}Used:{WHITE} {disk['used_percent']}%")


if __name__ == "__main__":
    main()
