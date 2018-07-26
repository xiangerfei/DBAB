# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sshAndMysqlConnect.sshConnect import sshconnect
# Create your views here.

@csrf_exempt
def ajax_check(request):
	ip = request.POST.get('ipAddress',None)
	username = request.POST.get('userAccount',None)
	passwd= request.POST.get('userPasswd',None)
#输入命令及其描述信息
	cmdAndDescrib = {'cpuCoreSize':'cat /proc/cpuinfo|grep process|wc -l', 'slaveReadOnly':"cat /etc/my.cnf|grep log-bin|awk -F '=' '{print $2}'"}

#	ip = str(ipAddress)
	print ip
	print username
	print passwd
	#username = "dba_yix"  #用户名
	#passwd = "yixiang@123"    #密嘛	
	getInfoResult = sshconnect(ip, username, passwd, cmdAndDescrib)


#	getInfoResult = {"a":123,"b":"sdfa"}

	if not getInfoResult:
		return HttpResponse("连接不成功")	
	else :
		print("连接成功")
		print("cpuCoreSize:",getInfoResult["cpuCoreSize"][0])

		print(type(getInfoResult))
#		getInfoResult={"a":1,"b":"dsfafd"}
		getInfoResult=json.dumps(getInfoResult)
#		return HttpResponse({"cpuCoreSize:"+getInfoResult["cpuCoreSize"][0]+"slaveReadOnly:"+getInfoResult["slaveReadOnly"][0]})
		return HttpResponse(getInfoResult)
#		return HttpResponse("ip1:"+ip+"&user:"+username+"&passwd="+passwd)




def index(request):
	return render(request,"index.html") 



