# -*- coding: utf8 -*-
import json
import re
import sys
import requests
import time
import pymysql
userID='410928199102031231'
passwd='Ab123456'
dbconn=pymysql.connect(host='sh-cdb-qrserykh.sql.tencentcdb.com', port=63303, user='yxb', passwd='lajiyunxuebang2333', db='yxb')
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
        resetPractise='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/clearRandomRecord?'+str(int(time.time()))+'&appKey='+token+'&practiceUuid='+practiseid
        r=requests.post(resetPractise)
        print(r.content)
        while i<int(itemnum):
            getitem='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/getRandomItem?'+str(int(time.time()))+'000&appKey='+token+'&practiceUuid='+practiseid+'&itemNo='+str(i+1)
            r=requests.post(getitem)
            jsload=json.loads(r.content)
            itemuuid.append(jsload["data"]["itemUuid"])
            print("已获取"+str(i+1)+"道题目"+jsload["data"]["itemUuid"])
            sql="select answer from items where uuid=\""+itemuuid[i]+"\""
            db.execute(sql)
            answer=db.fetchone()
            itemanswer.append(answer[0])
            i+=1
        i=0
        for j in range(20):
            r=requests.post(resetPractise)
            print("重置作答")
            i=0
            while i<int(itemnum):
                getanswer='https://itcprace.bjupi.com:5001/ITCP/app/bh3q/random/getRandomAnswer?'+str(int(time.time()))+'&appKey='+token+'&practiceUuid='+practiseid+'&itemUuid='+itemuuid[i]
                r=requests.post(getanswer,data=itemanswer[i])
                print("正在填写第"+str(i+1)+"题,答案"+itemanswer[i])
                i+=1
            r=requests.get("https://sc.ftqq.com/SCU63368Td0c5aa6a50503309a44c3aea38bff66f5d95c169e3c4c.send",params={'text': username+'签到和答题成功','desp': "完成时间"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})
    except BaseException as e:
        print(str(e))
        r=requests.get("https://sc.ftqq.com/SCU63368Td0c5aa6a50503309a44c3aea38bff66f5d95c169e3c4c.send",params={'text': username+'签到或答题失败', 'desp': jsload})
def main_handler(event, context):
    return start()
if __name__ == '__main__':
    start()