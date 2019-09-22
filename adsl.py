import re
import subprocess

# ADSL命令,adsl-stop;adsl-start 是.bashrc
# alias adsl-start=pppoe-start
# alias adsl-stop=pppoe-stop
# 在 subprocess.getstatusoutput(ADSL_BASH) 会发生错误，只能执行/bin/sh 中的命令
import time

ADSL_BASH = 'pppoe-stop;pppoe-start'
# 拨号网卡
ADSL_IFNAME = 'ppp0'
# 拨号间隔，保证7秒以上
DELAY = 30
def get_ip(ifname=ADSL_IFNAME):
    """
    获取本机IP
    :param ifname: 网卡名称
    :return:
    """
    (status, output) = subprocess.getstatusoutput('ifconfig')
    if status == 0:
        pattern = re.compile(ifname + '.*?inet.*?(\d+\.\d+\.\d+\.\d+).*?Mask', re.S)
        result = re.search(pattern, output)
        if result:
            ip = result.group(1)
            return ip

def adsl():
    """
    拨号主进程
    """
    try:
        while True:
            # 拨号间隔
            time.sleep(DELAY)
            (status, output) = subprocess.getstatusoutput(ADSL_BASH)
            if status == 0:
                print('ADSL Successfully')
                ip = get_ip()
                print(ip)
    except:
        adsl()

if __name__=="__main__":
    adsl()