# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sshAndMysqlConnect.sshConnect import sshconnect
from os import system
from MySQLdb import connect
# Create your views here.

@csrf_exempt
def ajax_check(request):
	ip = request.POST.get('ipAddress',None)
	username = request.POST.get('userAccount',None)
	passwd= request.POST.get('userPasswd',None)
#输入命令及其描述信息
	cmdAndDescrib = {'systemVersion':"cat /etc/system-release",
					'mysqlVersion':"mysqld --version",
					'cpuCoreSize':"cat /proc/cpuinfo|grep 'model name'|awk -F ':' 'NF{a++;print a,$2;next}'|tail -1",
					'sysMemsize':"cat /proc/meminfo |grep MemTotal|awk -F ':' '{print $2}'|tr -d ' '",
					
			#		 'cpuModel':"cat /proc/cpuinfo |grep 'model name'|uniq |awk -F ':' '{print $2}'",
			#		 'cpuCoreSize':'cat /proc/cpuinfo|grep process|wc -l', 
			#		 'memerySize':"cat /proc/meminfo |grep MemTotal|awk -F ':' '{print $2}'|tr -d ' '",
			#		 'dataPartitionSize':"df |tr -s ' '|cut -d ' ' -f 2|tail -n +2|sort -nr|head -1"
					}

#	ip = str(ipAddress)
	print ip
	print username
	print passwd
	#username = "dba_yix"  #用户名
	#passwd = "yixiang@123"    #密嘛	
	getInfoResult = sshconnect(ip, username, passwd, cmdAndDescrib)


#	getInfoResult = {"a":123,"b":"sdfa"}

	if not getInfoResult:
		print "连接不成功"
		return HttpResponse(json.dumps({"state":"connect_faild"}))	
	else :
#		print("连接成功")
#		print("cpuCoreSize:",getInfoResult["cpuCoreSize"][0])
		for i,j in getInfoResult.items():
			print i,j

		print(type(getInfoResult))
#		getInfoResult={"a":1,"b":"dsfafd"}
		getInfoResult=json.dumps(getInfoResult)
#		return HttpResponse({"cpuCoreSize:"+getInfoResult["cpuCoreSize"][0]+"slaveReadOnly:"+getInfoResult["slaveReadOnly"][0]})
		return HttpResponse(getInfoResult)
#		return HttpResponse("ip1:"+ip+"&user:"+username+"&passwd="+passwd)

def check_vaild(request):

	ip = request.POST.get('ipAddress',None)
	username = request.POST.get('userAccount',None)
	passwd= request.POST.get('userPasswd',None)
		

	res = system("mysql -u%s -p%s -h%s -e 'select version()' >/dev/null"%(username,passwd,ip))
	print res
	return HttpResponse(json.dumps({"state":res}))
	


def ajax_post_save(request):
	ip = request.POST.get('ipAddress',None)
	username = request.POST.get('userAccount',None)
	passwd= request.POST.get('userPasswd',None)
	mysqluser= request.POST.get('mysqluser',None)
	mysqlpasswd= request.POST.get('mysqlpasswd',None)
	systemversion = request.POST.get('systemversion',None) 
	mysqlversion = request.POST.get('mysqlversion',None) 
	cpucoresize = request.POST.get('cpucoresize',None) 
	systemmemsize = request.POST.get('systemmemsize',None) 
	islogical = request.POST.get('islogical', None)
	isphsical = request.POST.get('isphsical', None)
	reservedday = request.POST.get('reservedDay', None)


		
	conn = connect(host='127.0.0.1', user='DBAB', passwd='DBAB@312', db='DBAB')	
	cur = conn.cursor()

	sqlForInsertAccountInfo = "insert into T_HOST_DB_ACCOUNT_INFO(ipaddress, systemUser, systemPasswd,mysqlUser,mysqlPasswd) VALUES ('%s','%s','%s','%s','%s')"%(ip,username,passwd,mysqluser,mysqlpasswd)


	result = {}
	try:
		cur.execute(sqlForInsertAccountInfo)
	
	except BaseException as e:
		result["state"]="failed"
	else:
		if int(islogical) == 1:
			import os
			BASEDIR="/DjangoProject/DBAB/AssetManagement"
			executeFile=os.path.join(BASEDIR, "scripts", "main.py")
			osCmd = "python %s --user %s --password %s --host %s --reserved %d"%(executeFile, mysqluser, mysqlpasswd, ip, int(reservedday))
			os.system(osCmd)
		
		sqlForNextExecuteTime = "SELECT execute_time FROM T_HOST_DB_LOGICAL_BACKUP_RECORD ORDER BY create_time desc limit 1;"
			
		cur.execute(sqlForNextExecuteTime)
		print 
		print "=========================="
		lastBackupTime = cur.fetchone()[0]
		print lastBackupTime
		print type(lastBackupTime)
		print "=========================="
		# 如果是第一次输入，则默认为0，否则加5个小时。避免磁盘。网络集中。
		if lastBackupTime is None:
			lastBackupTime = 0
		else:
			lastBackupTime = (int(lastBackupTime) + 5)%24
		
		sqlForInsertBackupRecord = "INSERT INTO T_HOST_DB_LOGICAL_BACKUP_RECORD(ipaddress, execute_time) values('%s', '%s')"%(ip, lastBackupTime)
		print sqlForInsertBackupRecord
		cur.execute(sqlForInsertBackupRecord)
		
		filename = ip.replace(".","")
		crontEvent = '''echo "00 %d * * * ssh root@192.168.200.57  '/backupdir/backupsh/logical_backup/%s.sh'" >>/var/spool/cron/root'''%(lastBackupTime, filename)
		print crontEvent
		system(crontEvent)
	
		result["state"]="success"
	
	cur.close()
	conn.commit()
	conn.close()
	print result["state"]
	return HttpResponse(json.dumps(result))
	
			



def index(request):
	return render(request, "index.html")

def boots(request, num1):
	
	return render(request,"boots.html") 


def add_mashine(request):
	return render(request, "add_mashine.html")







def backupData(request):
	
	if request.POST.get("host") is None:
		return render(request, "add_backup.html")
	
	else:
		print "================"
		print request
		print "================"
		import os
		BASEDIR="/DjangoProject/DBAB/AssetManagement"
		executeFile=os.path.join(BASEDIR, "scripts", "main.py")
		osCmd = "python %s --user %s --password %s --host %s --reserved %d"%(executeFile, 'backup', 'backup', '192.168.16.55', 20)
		
		os.system(osCmd)





