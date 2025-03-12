import psutil


def is_disk_accessible(mountpoint):
    try:
        psutil.disk_usage(mountpoint)
        return True
    except (PermissionError, OSError):
        return False

def active_disks_count():
    return len([disk for disk in psutil.disk_partitions() if is_disk_accessible(disk.mountpoint)])