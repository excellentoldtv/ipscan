import requests
import json
import time
import _thread
def save(strs,number):
    lists=["局","党","委","学","有限公司","政府","协会","社区"]
    blak=['数据中心','阿里巴巴','云']
    for i in range(0,len(lists)):#只对白名单资产进行保存！排除云服务器
        if lists[i] in strs:
            for j in range(0, len(blak)):#过滤黑名单！排除云服务器
                if blak[j] in strs:
                    return
            file = open("save_str.txt", 'a',encoding='utf-8')
            file.write(str(number)+"线程： "+str(strs))
            file.close()

def check(domains,number):
    file = open(domains, 'r')
    list=['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in file.readlines():
        if 'http' or 'https' in i:
            i=i.replace('http://','')
            i = i.replace('https://', '')
        ip_str = i.split(":", 1)
        rangk(ip_str,number)
        #time.sleep(0.2)#请求间隔
    file.close()
def rangk(ip,number):
    if len(ip)==2:
        rip=ip[0]+":"+ip[1]
    else:
        rip=ip[0]
    headers={
        "Host":"www.iamwawa.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cookie": "PHPSESSID=d41i5vvp52a119knuokqk2ilh0; Hm_lpvt_ca368c21c1d2aa60e6f63d598c4cb02a=1624081986"
    }
    url="https://www.iamwawa.cn/home/ip/ajax"
    data={
        "ip":ip[0]
    }
    proxies={
        "http":"127.0.0.1:8888"
    }
    try:
        r=requests.post(url,headers=headers,data=data,proxies=proxies)
        js = json.loads(r.text)
        save_str = "ip:{} 地区:{}{}{} 归属:{}\n".format(rip.replace('\n',''), js["json"]["country"], js["json"]["region"],
                                                    js["json"]["city"], js["json"]["isp"])
    except:
        print("ip:"+rip+" ：error")

        return
    print(save_str)
    save(save_str,number)
if __name__ == '__main__':
    _thread.start_new_thread(check, ("domains.txt", 1))
    #_thread.start_new_thread(check, ("domains1.txt", 2))
    print("\033[31m\t\t*****输入stop结束扫描*****\033[0m")
    print("\033[33m\t\t*****输入stop结束扫描*****\033[0m")
    while 1:
        print("输入stop结束扫描")
        stop = input()
        if stop == "stop":
            print("结束扫描！！")
            exit()
