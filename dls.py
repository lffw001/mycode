"""
����˹��Ա����С����
export dlstoken='��ץ����Access-Token'
������:dlstoken
����ֵ:https://durex.ixiliu.cn ����ͷ���Access-Token
���˺�#����
ǩ����tt һ��һ��
cron: 0 8 * * *

"""
import requests,json,time,os
import concurrent.futures

def sign(account):
        token=account
        url = "https://durex.ixiliu.cn/api/sign/applyV2"
        headers = {
        "Host": "durex.ixiliu.cn",
        "Connection": "keep-alive",
        "platform": "MP-WEIXIN",
        "content-type": "application/json;charset=utf-8",
        "Access-Token": token,
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x18002520) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxe11089c85860ec02/21/page-frame.html"
        }
        response = requests.get(url=url,headers=headers).json()
        msg=response['message']
        print(msg)

# �ӻ���������ȡ����˺���Ϣ
accounts = os.environ.get('dlstoken').split('#')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(sign, accounts)
