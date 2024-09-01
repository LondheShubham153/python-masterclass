import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_name = os.path.join(destination, f"backup_{today}.tar.gz")

    try:
        shutil.make_archive(backup_name.replace('.tar.gz', ''), 'gztar', source)
        print(f"Backup created successfully: {backup_name}")
    except Exception as e:
        print(f"Error creating backup: {e}")


def check_disk_space():
    disk_status = os.system('df -h')
    return disk_status

def check_cpu_load():
    cpu_load = os.system('uptime')
    return cpu_load

check_disk_space()
check_cpu_load()
source_dir = "/Users/shubham/Documents/work/TrainWithShubham/python-workshop/practice"
destination_dir = "/Users/shubham/Documents/work/TrainWithShubham/python-workshop/practice"
backup_files(source_dir, destination_dir)

