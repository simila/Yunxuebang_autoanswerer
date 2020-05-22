# Yunxuebang_autoanswerer


##About


	This script is work with CNPC Skills Training and Testing Platform （Powered by Yunxuebang）
	Sign and Train daily automation.
	
	
##How to Use


	Runtime:Python 3.6
	
	
	Install
	
	
		Required mod:
		
		
			pip install requests pymysql
			
			
	Configation
	
	
		Required config:
		
		
			Each Python files must be configed this followings:
			
			UserID:Enter your IDCard Number
			
			Passwd:Enter your password,default password was given.
			
			
			
		Onetime configation:
			
			
			Database:You need to be prepaired a MySQL Database and enter this infomoation
			
				Import items.sql to create the table.
				
				
				
		Opitial:
			Result report to WeChat is supported.Just change SCKEY to yours.
			See http://sc.ftqq.com/ for further infomation.
			
			
	Running
	
	
		Initialion
		
		
			Run get.py firstly to get current questions and answers.Its will be storaged in MySQL.
			You need to run this when the questions updated everytime.
			WARNING: DO NOT RUN THIS FILE CONSTANTLY，IT MAY REDUCE YOUR ACCURATE.
			
			
		Using
		
		
			Run index.py
			If you wants to repeat many times.Run justdo.py . It will default running 20 times to 
			raise accurate.
			
			
		Attation
			Everything is configed in index.py and no args use.
			
#Others

	Cloud service supported
	
	
		This scripts can also running with Tencent Serverless Functions. 
		See https://cloud.tencent.com/document/product/583/ for further infomation.
		
			
