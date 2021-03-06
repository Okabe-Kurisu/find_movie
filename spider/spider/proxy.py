import random

from IPProxyPool.db.DataStore import sqlhelper


# 随便取得一个代理ip
def get_proxy():
    res = random.choice(sqlhelper.select(20, {"type": 0, "country": "国内"}))
    return res


# 不好就扣分,好就加分
def bad_proxy(ip):
    proxy = sqlhelper.select(1, {"ip": ip[0], 'port': ip[1]})[0]
    if int(proxy[2]) <= 1:
        return None
    res = sqlhelper.update({'ip': ip[0], 'port': ip[1]}, {'score': proxy[2] - 1})
    return res


def good_proxy(ip):
    proxy = sqlhelper.select(1, {"ip": ip[0], 'port': ip[1]})
    res = sqlhelper.update({'ip': ip[0], 'port': ip[1]}, {'score': proxy[0][2] + 1})
    return res


# 如果拿到的IP不好就删了吧
def del_proxy(ip):
    res = sqlhelper.delete({'ip': ip[0]})
    return res


if __name__ == "__main__":
    print(get_proxy())
