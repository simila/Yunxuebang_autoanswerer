# -*- coding: utf8 -*-
import json
import re
import sys
import requests
import time
import pymysql
userID=''
passwd='Ab123456'
dbconn=pymysql.connect(host='', port=, user='', passwd='', db='yxb')
db=dbconn.cursor()
def start():
    try:
        #header={'content-language': 'zhHans','Content-Type': 'application/text;charset=UTF-8','User-Agent': 'okhttp/3.6.0'}
        loginURL='https://itcprace.bjupi.com:5001/ITCP/common/bh3q/appLogin?'+str(int(time.time()))+'000&clientType=mobile&loginName='+userID+'&other=sdm660&isAndroid=true&versionNumber=8.2.7'
        r=requests.post(loginURL,data=passwd)
        jsload=json.loads(r.content)
        token=jsload["data"]["token"]
        username=jsload["data"]["loginUser"]["name"]
        print(jsload)
        CheckinURL='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/checkIn/studentCheckIn?'+str(int(time.time()))+'000&appKey='+token+'&base64Header=&suffix='
        r=requests.post(CheckinURL,data="")
        jsload=json.loads(r.content)
        print(jsload)
        getRandomPlanURL='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/pageStuRandomPlan?'+str(int(time.time()))+'000+&appKey='+token+'&hideOverDue=true&pageSize=10&pageNo=1'
        r=requests.post(getRandomPlanURL)
        jsload=json.loads(r.content)
        planid=jsload["data"]["datas"][0]["planUuid"]
        print(planid)
        listRandomPlanPractice='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/listRandomPlanPractice?'+str(int(time.time()))+'000&appKey='+token+'&planUuid='+planid+'&history=false'
        r=requests.post(listRandomPlanPractice)
        jsload=json.loads(r.content)
        bhid=jsload["data"][0]["bhPracticeUuid"]
        startPractice='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/startRandomPractice?'+str(int(time.time()))+'000&appKey='+token+'&bhPracticeUuid='+bhid
        r=requests.post(startPractice)
        jsload=json.loads(r.content)
        practiseid=jsload["data"]["practiceUuid"]
        itemnum=jsload["data"]["itemNum"]
        i=0
        itemuuid=list()
        itemanswer=list()
        itemtext=list()
        itemselections=list()
        resetPractise='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/clearRandomRecord?'+str(int(time.time()))+'&appKey='+token+'&practiceUuid='+practiseid
        r=requests.post(resetPractise)
        print(r.content)
        while i<int(itemnum):
            getitem='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/getRandomItem?'+str(int(time.time()))+'000&appKey='+token+'&practiceUuid='+practiseid+'&itemNo='+str(i+1)
            r=requests.post(getitem)
            jsload=json.loads(r.content)
            itemuuid.append(jsload["data"]["itemUuid"])
            itemtext.append(jsload["data"]["itemText"])
            itemselections.append(jsload["data"]["selections"])
            print("已获取"+str(i+1)+"道题目"+jsload["data"]["itemUuid"]+jsload["data"]["itemText"])
            i+=1
        i=0
        getanswer='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/getRandomAnswer?'+str(int(time.time()))+'&appKey='+token+'&practiceUuid='+practiseid+'&itemUuid='+itemuuid[i]
        while i<int(itemnum):
            getanswer='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/getRandomAnswer?'+str(int(time.time()))+'&appKey='+token+'&practiceUuid='+practiseid+'&itemUuid='+itemuuid[i]
            r=requests.post(getanswer,data="A")
            jsload=json.loads(r.content)
            itemanswer.append(jsload["data"]["answer"])
            print("已获取"+str(i+1)+"题答案:"+jsload["data"]["answer"])
            i+=1
        i=0
        while i<int(itemnum):
            try:
                sql="insert into items (uuid,answer) values(\""+str(itemuuid[i])+"\",\""+str(itemanswer[i])+"\");"
                db.execute(sql)
                dbconn.commit()
                print("已写入"+str(i+1)+"题信息")
            except:
                print(str(i+1)+"题写入失败，可能此题目已存在。")
                pass
            i+=1
        r=requests.post(resetPractise)
        db.close()
        print("重置作答")
    except BaseException as e:
        print(str(e))
        db.close()
        #r=requests.get("https://sc.ftqq.com/SCU63368Td0c5aa6a50503309a44c3aea38bff66f5d95c169e3c4c.send",params={'text': username+'签到或答题失败', 'desp': jsload})
def main_handler(event, context):
    return start()
if __name__ == '__main__':
    start()