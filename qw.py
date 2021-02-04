# coding=utf-8
import requests
import json
from time import sleep
payload={}
headers = {
  'q-ua2': 'QV=3&PL=ADR&PR=QQ&PP=com.tencent.mobileqq&PPVN=8.5.5&TBSVC=43973&CO=BK&COVC=045512&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MIX2 &RL=1080*2030&OS=9&API=28',
  'q-guid': 'a76d04084c50fb2707c2cd6913b799cb',
  'q-qimei': 'a9bb0b00442266bc10867c98800010515105',
  'qimei36': 'b37e2cea524ae6d1468c567f10001ff15113',
  'q-auth': '31045b957cf33acf31e40be2f3e71c5217597676a9725f1b',
  'referer': 'https://club.vip.qq.com/card/friend?_wv=16778247&_wwv=68&_wvx=10&_proxy=1&_proxyByURL=1&platform=1&qq=767026787&adtag=geren&aid=mvip.pingtai.mobileqq.androidziliaoka.fromqita',
  'Cookie': 'pvid=7392286914; uin=o2582699514; p_uin=o2582699514; RK=HbTNpSB6Xp; ptcz=5542752676d055ad3b7397db42dfab0970b43b52e0de434c1c0730cc97440b26; skey=MHVjboSqey; pt4_token=PPoEGHPhYG-yNsDkQQ3gMnBRH9DZQrw9nA5fVATUTco_; p_skey=MWRnkYqg-Q1HPo0RKg1QY7lrd2rjEWogNq94pb1SDYo_'
}

qq = open('qq.txt','r')
qqlist =qq.read()
qq.close()
new_f = open('./data.txt','w')
i =1
for k in qqlist.split("\n"):
    url = "https://cgi.vip.qq.com/card/getExpertInfo?ps_tk=397022032&fuin=%s&callback=jsonp2" % str(k)
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        #print(url,response)
        data = json.loads(response.text[7:-2])
        if data['ret'] == 0:
            print(str(i))
            print(str(k)+'----'+str(data['data']['g'][1]))
            new_f.write(k+'----'+str(data['data']['g'][1])+"\r\n")
            new_f.flush()
            i+=1
    except:
        continue
    sleep(0.1)
new_f.close()
