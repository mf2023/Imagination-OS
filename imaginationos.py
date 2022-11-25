from datetime import datetime
import psutil
import platform
import wmi
import os

# __________________________________________初始----------------------


# noinspection PyTypeChecker
def os1():
    osw = input('PS C:\imagination\MF-Windows11>')
    if osw == "Disk Information" or osw == "disk information":
        cp()
    elif osw == "Disk Usage" or osw == "disk usage":
        diskusage()
    elif osw == "file tree" or osw == "File Tree":
        filetree()
    elif osw == "create a new file" or osw == "Create a new file":
        createanewfile()
    elif osw == "information about pc" or osw == "Information About PC":
        cpu()
        cpuz()
    elif osw == "mac" or osw == "Mac":
        mac()
    elif osw == "network" or osw == "Network":
        GetNetWork()
    elif osw == "system" or osw == "System":
        system1()
    elif osw == "help" or osw == "Help":
        help()
    elif osw == "get system environment variables" or osw == "Get system environment variables":
        hjbl()
    elif osw == "modify system environment variables" or osw == "Modify system environment variables":
        xghjbl()
    else:
        print(
            "无法将" "'" + osw + "'""项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路径正确，然后再试一次。")
        os1()


#——————————————————————————————————————————————————————————————————————————
def help():
    import prettytable as pt
    print("感谢您使用盲飞Imagination OS，您可以从这里获取帮助。详情www.mfchina.com.cn/imaginationos.感谢您对理解！")

    tb = pt.PrettyTable()
    tb.field_names = ["指令名称", "描述", "大小写", "其他"]
    tb.add_row(["help", "获取帮助", "不区分", ""])
    tb.add_row(["Brifasdfae", 5905, 1857594, 1146.4])
    tb.add_row(["Darwin", 112, 120900, 171423423423423424.7])
    tb.add_row(["Hobart", 1357, 205556, 619.5])

    print(tb)
    os1()


#——————————————————————————————环境变量——————————————————————————————————————
def hjbl():
    import os
    print(os.environ["TEMP"])
    mydir = "c:\\mydir"

    os.environ["MYDIR"] = mydir

    print(os.environ["MYDIR"])
    pathV = os.environ["PATH"]

    print(pathV)

    os.environ["PATH"] = mydir + ";" + os.environ["PATH"]

    print(os.environ["PATH"])

    os1()

def xghjbl():
    print("Modify system environment variables (operation is irreversible, please use with caution)")
    class MyEnv:
        def __init__(self):
            self.envFile = "c:\\myenv.txt"
            self.envs = {}

        def SetEnvFile(self, filename):
            self.envFile = filename

        def Save(self):
            outf = open(self.envFile, "w")
            if not outf:
                print("env file cannot be opened for write!")
            for k, v in self.envs.items():
                outf.write(k + "=" + v + "\n")
            outf.close()

        def Load(self):
            inf = open(self.envFile, "r")
            if not inf:
                print("env file cannot be opened for open!")
            for line in inf.readlines():
                k, v = line.split("=")
                self.envs[k] = v
            inf.close()

        def ClearAll(self):
            self.envs.clear()

        def AddEnv(self, k, v):
            self.envs[k] = v

        def RemoveEnv(self, k):
            del self.envs[k]

        def PrintAll(self):
            for k, v in self.envs.items():
                print(k + "=" + v)

    if __name__ == "__main__":
        myEnv = MyEnv()
        myEnv.SetEnvFile("c:\\myenv.txt")
        myEnv.Load()
        myEnv.AddEnv("MYDIR", "c:\\mydir")
        myEnv.AddEnv("MYDIR2", "c:\\mydir2")
        myEnv.AddEnv("MYDIR3", "c:\\mydir3")
        myEnv.Save()
        myEnv.PrintAll()


# ——————————————————————————————————————————————————————————————————————————
def yh():
    num = 0
    while True:
        mi = input("密码（请输入有效值）：")
        if mi == "wei20090314":
            print("欢迎！")
            os1()
        else:
            num += 1
            if num == 3:
                print("3次用户名或者密码均有误！退出程序。")
                break
# ————————————————————————————————————————————————————文件——————————————————————————————
def filetree():
    """

    :rtype: object
    """
    import os
    tree = input("PC C:\imagination\MF-Windows11\Fe-tree>")
    rootDir = tree
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Folder: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)
    os1()


def createanewfile():
    """

    :rtype: object
    """
    new = input("PC C:\imagination\MF-Windows11\Fe-tree>")

    def mkdir(path):
        """

        :type path: object
        """
        # noinspection PyTypeChecker
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)
            print("---  new folder...  ---")
            print("---  OK  ---")
        else:
            print("---  There is this folder!  ---")

    file = new
    mkdir(file)  # 调用函数
    os1()


# noinspection PyTypeChecker
def copyfile() -> object:
    # noinspection PyCompatibility
    news: str = input("PC C:\imagination\MF-Windows11\Copy flies\Original position>")
    # noinspection PyCompatibility
    newe: str = input("PC C:\imagination\MF-Windows11\Copy flies\Copy to>")
    import shutil
    shutil.copyfile(newe, news)


# noinspection PyTypeChecker
def Writefilecontents():
    filename = input("PC C:\imagination\MF-Windows11\File location（Please ensure that the file exists）>")
    filenr = input("PC C:\imagination\MF-Windows11\Write file contents(Please ensure that the file exists)>")
    with open(filename, 'a') as file_object:
        file_object.write(filenr)
        file_object.write(filenr)


# ——————————————————————————————————————————————————————硬盘—————————————————————————————————
def cp():
    d = psutil.disk_partitions()
    print('C盘信息:', d[0])
    print('D盘信息:', d[1])
    print('E盘信息:', d[2])
    print("F盘信息:", d[3])
    print('G盘信息:', d[4])
    print('获取磁盘字段:', d[0][0], d[1][0], d[2][0], d[3][0], d[4][0])
    print('数据类型:', type(d), '\n')
    os1()


def diskusage():
    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    print("=" * 40, "Disk Information", "=" * 40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    os1()
# ——————————————————————————————CPU及其他————————————————————————————————
def mac():
    import socket
    import uuid
    # 获取主机名
    hostname = socket.gethostname()
    # 获取IP
    ip = socket.gethostbyname(hostname)

    # 获取Mac地址
    def get_mac_address():
        # noinspection PyCompatibility
        mac: str = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    # ipList = socket.gethostbyname_ex(hostname)
    # print(ipList)
    print("主机名：", hostname)
    print("IP：", ip)
    print("Mac地址：", get_mac_address())
    os1()


def cpuz():
    def get_cpu_info():
        cpu_count = psutil.cpu_count(logical=False)  # 1代表单核CPU，2代表双核CPU
        xc_count = psutil.cpu_count()  # 线程数，如双核四线程
        cpu_percent = round((psutil.cpu_percent(1)), 2)  # cpu使用率
        cpu_info = (cpu_count, xc_count, cpu_percent)
        return cpu_info

    get_cpu_info()


def cpu():
    # -*- coding: utf-8 -*-
    import wmi
    import sys
    import time
    import os
    import platform
    import socket
    import uuid
    # 获取主机名
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    class Hardware:
        @staticmethod
        def get_cpu_sn():
            """
            获取CPU序列号
            :return: CPU序列号
            """
            c = wmi.WMI()
            for cpu in c.Win32_Processor():
                # print(cpu.ProcessorId.strip())
                return cpu.ProcessorId.strip()

        @staticmethod
        def get_baseboard_sn():
            """
            获取主板序列号
            :return: 主板序列号
            """
            c = wmi.WMI()
            for board_id in c.Win32_BaseBoard():
                # print(board_id.SerialNumber)
                return board_id.SerialNumber

        @staticmethod
        def get_bios_sn():
            """
            获取BIOS序列号
            :return: BIOS序列号
            """
            c = wmi.WMI()
            for bios_id in c.Win32_BIOS():
                # print(bios_id.SerialNumber.strip)
                return bios_id.SerialNumber.strip()

        @staticmethod
        def get_disk_sn():
            """
            获取硬盘序列号
            :return: 硬盘序列号列表
            """
            c = wmi.WMI()

            disk_sn_list = []
            for physical_disk in c.Win32_DiskDrive():
                # print(physical_disk.SerialNumber)
                # print(physical_disk.SerialNumber.replace(" ", ""))
                disk_sn_list.append(physical_disk.SerialNumber.replace(" ", ""))
            return disk_sn_list

    def start(cishu):
        print("加载中.")
        print("▏")
        time.sleep(0.2)
        os.system("cls")
        print("加载中..")
        print("▎")
        time.sleep(0.2)
        os.system("cls")
        print("加载中...")
        print("▍")
        time.sleep(0.2)
        os.system("cls")
        print("加载中....")
        print("▋")
        time.sleep(0.2)
        os.system("cls")
        print("加载中.....")
        print("▊")
        time.sleep(0.2)
        os.system("cls")
        print("加载中......")
        print("▉")
        time.sleep(0.2)
        os.system("cls")
        print("加载中")
        print("▉▏")
        time.sleep(0.2)
        os.system("cls")
        print("加载中.")
        print("▉▎")
        time.sleep(0.2)
        os.system("cls")
        print("加载中..")
        print("▉▍")
        time.sleep(0.2)
        os.system("cls")
        print("加载中...")
        print("▉▌")
        time.sleep(0.2)
        os.system("cls")
        print("加载中....")
        print("▉▋")
        time.sleep(0.2)
        os.system("cls")
        print("加载中.....")
        print("▉▊")
        time.sleep(0.2)
        os.system("cls")
        print("加载中......")
        print("▉▉")
        time.sleep(0.2)
        os.system("cls")
        print("加载中.")
        print("▉▉▏")
        time.sleep(0.2)
        os.system("cls")
        print("加载中..")
        print("▉▉▎")
        time.sleep(0.2)
        os.system("cls")
        print("加载中...")
        print("▉▉▍")
        time.sleep(0.2)
        os.system("cls")
        print("加载中....")
        print("▉▉▌")
        time.sleep(0.2)
        os.system("cls")
        print("加载中.....")
        print("▉▉▋")
        time.sleep(0.2)
        os.system("cls")
        print("加载中......")
        print("▉▉▊")
        time.sleep(0.2)
        os.system("cls")
        print("加载中.")
        print("▉▉▉▏")
        time.sleep(0.2)
        os.system("cls")
        print("加载中..")
        print("▉▉▉▎")
        time.sleep(0.2)
        os.system("cls")
        print("加载中...")
        print("▉▉▉▍")
        time.sleep(0.2)
        os.system("cls")
        print("加载中...")
        print("▉▉▉▌")
        time.sleep(0.2)
        os.system("cls")
        print("加载中....")
        print("▉▉▉▋")
        time.sleep(0.2)
        os.system("cls")
        print("加载中....")
        print("▉▉▉▋")
        time.sleep(0.2)
        os.system("cls")
        print("加载中.....")
        print("▉▉▉▊")
        time.sleep(0.2)
        os.system("cls")
        print("加载中......")
        print("▉▉▉▉")
        time.sleep(0.2)
        os.system("cls")

    def get_mac_address():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    if __name__ == '__main__':
        start(5)
        print()
        print("正在获取电脑信息...")
        time.sleep(2)
        print("已成功！")
        time.sleep(0.5)
        if sys.platform == "win32":
            print("操作系统:Windows")
            time.sleep(0.5)
        if sys.platform == "darwin":
            print("操作系统:mac")
            time.sleep(0.5)
        print("CPU序列号：{}".format(Hardware.get_cpu_sn()))
        time.sleep(0.5)
        print("主板序列号：{}".format(Hardware.get_baseboard_sn()))
        time.sleep(0.5)
        print("Bios序列号：{}".format(Hardware.get_bios_sn()))
        time.sleep(0.5)
        print("硬盘序列号：{}".format(Hardware.get_disk_sn()))
        time.sleep(0.5)
        print("操作系统:", platform.architecture())
        time.sleep(0.5)
        print("机器类型:", platform.machine())
        time.sleep(0.5)
        print("网络名称:", platform.node())
        time.sleep(0.5)
        print("处理器名称:", end="")
        print(platform.processor())
        time.sleep(0.5)
        print("主机名:", hostname)
        time.sleep(0.5)
        print("电脑ip:", ip)
        cpu1()
        os1()


def cpu1(gpu_free_memory=None):
    print("This is your computer details.")

    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor

    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    # Boot Time
    print("=" * 40, "Boot Time", "=" * 40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    # let's print CPU information
    print("=" * 40, "CPU Info", "=" * 40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    # Memory Information
    print("=" * 40, "Memory Information", "=" * 40)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("=" * 20, "SWAP", "=" * 20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

    # Disk Information
    print("=" * 40, "Disk Information", "=" * 40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")

    # Network information
    print("=" * 40, "Network Information", "=" * 40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

    import GPUtil
    from tabulate import tabulate
    print("=" * 40, "GPU Details", "=" * 40)
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
        # get % percentage of GPU usage of that GPU
        gpu_load = f"{gpu.load * 100}%"
        # get free memory in MB format
        # get used memory
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # get total memory
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # get GPU temperature in Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                       "temperature", "uuid")))


def GetNetWork():
    # Network information
    print("=" * 40, "Network Information", "=" * 40)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f'=== Interface: {interface_name} ===')
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f'  IP Address: {address.address}')
                print(f'  Netmask: {address.netmask}')
                print(f'  Broadcast IP: {address.broadcast}')
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f'  MAC Address: {address.address}')
                print(f'  Netmask: {address.netmask}')
                print(f'  Broadcast MAC: {address.broadcast}')
    os1()


def system1():
    # 系统的内存利用率
    free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2)) + 'GB'
    total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2)) + 'GB'
    memory_use_percent = str(psutil.virtual_memory().percent) + ' %'
    print('可用内存：', free)
    print('总内存：', total)
    print('内存占用率:', memory_use_percent)
    # cpu1秒内的占用率，和任务管理器显示的不一样，大概管理器里面的为一半
    print('cpu占用率:', str(psutil.cpu_percent(interval=1)) + ' %')
    print('物理cpu个数:', psutil.cpu_count(logical=False))
    print("您的系统为:" + platform.system())  # Windows
    print("您的操作系统名称及版本号:" + platform.platform())
    print("您的操作系统版本号:" + platform.version())
    print("您的CPU生产商为:" + platform.machine())
    print("您的CPU信息为:" + platform.processor())
    print("获取操作系统的位数:", platform.architecture())
    print("计算机的网络名称:" + platform.node())
    print("包含上面所有的信息汇总:", platform.uname())
    cpuinfo = wmi.WMI()
    for cpu in cpuinfo.Win32_Processor():
        print("您的CPU序列号为:" + cpu.ProcessorId.strip())
        print("您的CPU名称为:" + cpu.Name)
        print("您的CPU已使用:%d%%" % cpu.LoadPercentage)
        print("您的CPU核心数为:%d" % cpu.NumberOfCores)
        print("您的CPU时钟频率为:%d" % cpu.MaxClockSpeed)
    os1()


def computer():
    import wmi  # 导入库
    computername = input(
        "PS C:\imagination\MF-Windows11\Please enter a new computer name（Irreversible operation, careful selection）>")
    aa = wmi.WMI()

    for system in aa.Win32_ComputerSystem():
        system.Rename(computername)  # 这里就是修改的名字

#————————————————————————————————————————————————进程——————————————————————————————————
def pinfo1():
    import psutil

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            print(pinfo)
# ______________________________________________分界线____________________________________________

print("MF Imagination OS [版本 2.0.22623.891]")
print("(c) MF Corporation。保留所有权利。")
print("请输入您的密码以登录您的计算机")
yh()