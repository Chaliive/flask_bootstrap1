import psutil, datetime, time

# cpu
print('cup数量是:%s个' % psutil.cpu_count(logical=False))
cpu = str(psutil.cpu_percent(1)) + '%'
print('cpu使用情况是: %s' % cpu)

# 内存
free = (round(psutil.virtual_memory().free / (1024 * 1024 * 1024), 2))
total = (round(psutil.virtual_memory().total / (1024 * 1024 * 1024)))
used = total - free
memory = used / total
# print('内存总量是: %sG' % total)
# print('剩余内存有: %sG' % free)
# print('占用内存量: %sG' % used)
print('内存占用百分比: %s' % memory)
# -----------------------------#

# # 硬盘
diskinfo = psutil.disk_partitions()
print(diskinfo)
print(diskinfo[0])
print(diskinfo[0].device)
disk = diskinfo[0].device
usedisk = psutil.disk_usage(disk).used
print(usedisk)
# for i in diskinfo:
#     info = psutil.disk_usage(i.device)
#     print('total:' + str(int(info.total / (1024 * 1024 * 1024))))
#     print('used:' + str(int(info.used / (1024 * 1024 * 1024))))

# 网卡
net = psutil.net_io_counters()
e_net = psutil.net_io_counters(pernic=True)
# psutil.net_io_counters()
print(net)
# bytes_sent 发送字节数
recv = net.bytes_recv / 1024
sent = net.bytes_sent / 1024
print('网卡 sent %s recv %s ' % (sent, recv))

# 系统用户
user_count = len(psutil.users())
user_list = ','.join([u.name for u in psutil.users()])
# print('当前用户有： %s个， 分别是： %s' % (user_count, user_list))

# 系统进程psid
for psid in psutil.pids():
    p = psutil.Process(psid)
    # print('进程名字是： %s，    进程状态是： %s' % (p.name(), p.status()))
