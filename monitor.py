import psutil
import platform
import wmi
import GPUtil

from misc.disk_accessibility import active_disks_count
from misc.misc import output_preparation

DISK_AMOUNT = active_disks_count()

def run():
    logo = output_preparation('logo.txt', DISK_AMOUNT + 5, [3])
    print(
        logo.format(
            hostname(), os_info(), cpu_stats(), gpu_stats(), memory_stats(), *disk_stats()
        )
    )

def hostname() -> str:
    pu = psutil.users()[0]
    return f"\033[96m{pu.name}\033[00m" + '@' + ("\033[97mhostname\033[00m" if not pu.host else str(pu.host))


def os_info():
    return f"\033[96mOS:\033[00m \033[97m{platform.system()} {platform.release()}\033[00m"


def cpu_stats():
    c = wmi.WMI()
    cpu_name = c.Win32_Processor()[0].Name
    return f"\033[93mCPU:\033[00m \033[97m{cpu_name.strip()}\033[00m - \033[92mUsage: {psutil.cpu_percent()}%\033[00m"

def gpu_stats():
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return "GPU: None detected"
        return f"\033[93mGPU:\033[00m \033[97m{gpus[0].name}\033[00m - \033[92m{gpus[0].memoryUsed}Mib\033[00m / \033[91m{gpus[0].memoryTotal}Mib\033[00m"
    except ModuleNotFoundError:
        return "GPU: None (GPUtil not installed)"

def memory_stats() -> str:
    pvm = psutil.virtual_memory()
    return f"\033[93mMemory:\033[00m \033[92m{(pvm.used * 9.31 * pow(10, -10)):.2f}Gib\033[00m / \033[91m{(pvm.total * 9.31 * pow(10, -10)):.2f}Gib\033[00m"

def disk_stats():
    res = []
    for i, disk in enumerate(psutil.disk_partitions()):
        try:
            disk_total = psutil.disk_usage(disk.mountpoint).total
            disk_used = psutil.disk_usage(disk.mountpoint).used
            res.append(
                f"\033[93mDisk {i}:\033[00m \033[92m{(disk_used * 9.31 * 10**-10):.2f}Gib\033[00m / \033[91m{(disk_total * 9.31 * 10**-10):.2f}Gib\033[00m\t"
            )
        except (PermissionError, OSError):
            continue

    return res if res else ["No accessible disks found"]

def active_disks_count():
    return len([disk for disk in psutil.disk_partitions() if is_disk_accessible(disk.mountpoint)])

def is_disk_accessible(mountpoint):
    try:
        psutil.disk_usage(mountpoint)
        return True
    except (PermissionError, OSError):
        return False


if __name__ == "__main__":
    # functions testing
    print(len(disk_stats()))
    print(*disk_stats())
    print(DISK_AMOUNT)
    text2 = "{} {} {} {}"
    print(text2.format(1, 2, *disk_stats()))