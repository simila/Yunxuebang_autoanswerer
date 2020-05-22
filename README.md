# Yunxuebang_autoanswerer


##About
	This program is work with CNPC Skills Training and Testing Platform （Powered by Yunxuebang）
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
	Running
	
	
		Initialion
		
		
			Run get.py firstly to get current questions and answers.Its will be storaged in MySQL.You need to run this when the questions updated everytime.
			
			
		Using
		
		
			Run index.py
			
			
		Attation
			Everything is configed in index.py and no args use.
			
	
		
			
