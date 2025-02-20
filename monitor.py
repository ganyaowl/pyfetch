import psutil
import platform
import subprocess



def run():
    logo = open('logo.txt', 'r').read()
    print(logo.format(hostname(), os_info(), cpu_stats(), gpu_stats(), memory_stats(), disk_stats()))

def hostname() -> str:
    pu = psutil.users()[0]
    return f"\033[96m{pu.name}\033[00m" + '@' + ("\033[97mhostname\033[00m" if not pu.host else str(pu.host))


def os_info():
    return f"\033[96mOS:\033[00m \033[97m{platform.system()} {platform.release()}\033[00m"


def cpu_stats():
    command = "wmic cpu get name"
    cpu_name = subprocess.check_output(command, shell=True).decode().strip().split('\n')[1]
    return f"\033[93mCPU:\033[00m \033[97m{cpu_name.strip()}\033[00m - \033[92mUsage: {psutil.cpu_percent()}%\033[00m"

def gpu_stats():
    try:
        import GPUtil
    except ModuleNotFoundError:
        return "GPU: None"

    gpus = GPUtil.getGPUs()

    return f"\033[93mGPU:\033[00m \033[97m{gpus[0].name}\033[00m - \033[92m{gpus[0].memoryUsed}Mib\033[00m / \033[91m{gpus[0].memoryTotal}Mib\033[00m"

def memory_stats() -> str:
    pvm = psutil.virtual_memory()
    return f"\033[93mMemory:\033[00m \033[92m{(pvm.used * 9.31 * pow(10, -10)):.2f}Gib\033[00m / \033[91m{(pvm.total * 9.31 * pow(10, -10)):.2f}Gib\033[00m"

def disk_stats():
    res = ''
    for i, disk in enumerate(psutil.disk_partitions()):
        disk_total = psutil.disk_usage(disk.mountpoint).total
        disk_used = psutil.disk_usage(disk.mountpoint).used
        res += f"\033[93mDisk {i}:\033[00m \033[92m{(disk_used * 9.31 * pow(10, -10)):.2f}Gib\033[00m / \033[91m{(disk_total * 9.31 * pow(10, -10)):.2f}Gib\033[00m\t"
    return res
