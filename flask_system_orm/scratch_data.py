import psutil, pymysql


def scratch_memory():
    info = {}
    # 内存
    mem_total = str(round(psutil.virtual_memory().total / (1024 * 1024 * 1024)))
    mem_free = str(round(psutil.virtual_memory().free / (1024 * 1024 * 1024), 2))
    mem_used = str(float(mem_total) - float(mem_free))
    mem_percent = str(float(mem_used) / float(mem_total))
    info['mem_total'] = mem_total
    info['mem_free'] = mem_free
    info['mem_used'] = mem_used
    info['mem_percent'] = mem_percent
    return info


def scratch_prograss():
    # 进程
    p = psutil.pids()
    p_name = []
    p_status = []
    p_gid = []
    p_par = []
    for psid in p:
        pro_name = psutil.Process(psid).name()
        pro_sta = psutil.Process(psid).status()
        pro_gid = psutil.Process(psid).create_time()
        pro_par = psutil.Process(psid).parent()
        p_status.append(pro_sta)
        p_name.append(pro_name)
        p_gid.append(pro_gid)
        p_par.append(pro_par)
    pro_res = list(zip(p, p_name, p_status, p_gid, p_par))
    return pro_res


def storage():
    pass
