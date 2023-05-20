import requests, pyfiglet, termcolor, os, sys, os, sys, time, os, sys, time, webbrowser

import requests
import time
import os
import random
from time import sleep
import pyfiglet
import base64
from bs4 import BeautifulSoup
Z = '\033[1;31m' #احمر
lll = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
os=pyfiglet.figlet_format       ( "     __ F L E X __")
print(Z+os)

print('_'*65)
os=("by: MR ALAA")
print(lll+os)
print('_'*65)
number=("01050892775")
print()
password=("Elmasri##2")
print()
url="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



headers={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
data={
"username":number,

"password":password,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
Ahmed=requests.post(url, headers=headers, data=data)

#print(res)

jwt=Ahmed.json()["access_token"]

urd="https://mobile.vodafone.com.eg/services/dxl/usage/usageConsumptionReport?%40type=aggregated&bucket.product.publicIdentifier="+number+""

hdthd={"Host":"mobile.vodafone.com.eg",
"Connection":"Keep-Alive",
"useCase":"aggregated",
"x-dynatrace": "MT_3_8_297557593_55-0_a556db1b-4506-43f3-854a-1d2527767923_0_207_164",
'msisdn':number,
"api-host":"usageConsumptionHost",
"Accept-Language":"ar",
"Authorization": "Bearer "+(jwt)+"",
"Content-Type":"application/json",
"Accept":"application/json",
"clientId":"AnaVodafoneAndroid",
"User-Agent":"okhttp/4.9.1",
"x-agent-build":"503",
"x-agent-version":"2022.2.1.2",
"Accept-Encoding":"gzip",
"x-agent-device":"a22",
"x-agent-operatingsystem":"A225FXXU3BVF1",
"api-version":"v2"

         }
    
    
loka=requests.get(urd, headers=hdthd).json()

#print(loka)

for x in loka:
 #print(x)
 try:
  bucket=x["bucket"]
  #print(bucket)
  for t in bucket:
  	usageType=t["bucketBalance"]
  	#print(usageType)
  	for yy in usageType:
  		bh=yy["remainingValue"]
  		print(bh)
  		z=(bh[0]["usageType"])
  		print(z)
  		
#  		for ii in bh:
#  			amount2=ii["amount"]
#  			#print(amount)
#  			amount1=(amount2[3]["amount"])
#  			print(amount1)
 except:
  pass


ny=("01008965284")
print()
p1=("Alla@@123")
print()
#time.sleep(1.5)
number2=input(" \033[2;32mEnter Your Number :")
print()
password2=input("Enter Your Password :")
print()
gcv=input("\033[2;36mThe Number Of Flex :")
print()
qwe=13000
zxc=100
jt=int(gcv)
k=(qwe*jt/zxc)
oopl=str(k)
#time.sleep(1.5)
print()
lokae=('              '+(lll+oopl))
print(lokae)
print('\033[2;31mThe Flex')
print()
#time.sleep(1.5)
y=input('Can t go back  (y/n) : ')

if str('y') == str(y):
   	print('ok')
        #break
else:
	print('\033[2;35mThe order has been cancelled ')
	print('\033[2;31m_'*65)
	hhhhgg
	hhhyo
	jfkfifjfj
gcav="0"
print()

qwe=13000
zxc=100
jt=int(gcav)
k=(qwe*jt/zxc)
oopl=str(k)
#time.sleep(1.5)
print()
lokae=('              '+(lll+oopl))
print(lokae)
gs="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"

hhy={

    "Accept":"application/json, text/plain, */*",

    "Connection":"keep-alive",

    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",

    "x-agent-operatingsystem":"1630483957",

    "clientId":"AnaVodafoneAndroid",

    "x-agent-device":"RMX1911",

    "x-agent-version":"2021.12.2",

    "x-agent-build":"493",

    "Content-Type":"application/x-www-form-urlencoded",

    "Content-Length":"143",

    "Host":"mobile.vodafone.com.eg",

    "Accept-Encoding":"gzip",

    "User-Agent":"okhttp/4.9.1"

    }

    

    

Dsl={

"username":number2,

"password":password2,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"

    }    

Gn=requests.post(gs ,headers=hhy,data=Dsl).json()

#print(Ahmed)

if 'access_token' in Gn:

    pj= Gn['access_token']

    pass

else:
    print(lll+"خطأ في الرقم او الباسورد") 
    print(Z+"="*50)
    jfkfifjfj
    hhhyo
urla="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



headersa={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
dataa={
"username":ny,

"password":p1,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
Ahmead=requests.post(urla, headers=headersa, data=dataa)

#print(res)

jwat=Ahmead.json()["access_token"]


#print("\033[1;33m=" * 40)

#print(jwt)


urla2="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"


#print(url2)

hda={
    
    "Host": "mobile.vodafone.com.eg",
    "x-dynatrace":"MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
    "msisdn": ny,
    "api-version":"v2",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": "Bearer "+(jwat)+"",
    "x-agent-device":"RMX1911",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"302",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}

jsona={"category": [{"listHierarchyId": "PackageID", "value": "523"}, {"listHierarchyId": "TemplateID", "value": "47"}, {"listHierarchyId": "TierID", "value": "523"}, {"listHierarchyId": "familybehavior", "value": "percentage"}], "name": "FlexFamily", "parts": {"characteristicsValue": {"characteristicsValue": [{"characteristicName": "quotaDist1", "type": "percentage", "value": gcav,}]}, "member": [{"id": [{"schemeName": "MSISDN", "value":ny,}], "type": "Owner"}, {"id": [{"schemeName": "MSISDN", "value":number2}], "type": "Member"}]}, "type": "SendInvitation"}
    
    
lokaa=requests.patch(urla2, headers=hda, json=jsona).text
#print(loka)
if str('{}') in str(lokaa):
	print("{}")	
else:
	print("الرقم موجود في عيله اخري ") 
	print('\033[2;35m _'*65)
	hdhdhdjd
	djjdhdhdh
	djerje	
urla3="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



headersa3={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
dataa3={
"username":number2,

"password":password2,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
za=requests.post(urla3, headers=headersa3, data=dataa3)

loak=za.json()["access_token"]


#print("=" * 40)


urla4="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"


hda4={
    
    "Host": "mobile.vodafone.com.eg",
    "x-dynatrace":"MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
    "msisdn": number2,
    "api-version":"v2",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": "Bearer "+(loak)+"",
    "x-agent-device":"RMX1911",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"302",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}

jsona4={"category": [{"listHierarchyId": "TemplateID", "value": "47"}], "name": "FlexFamily", "parts": {"member": [{"id": [{"schemeName": "MSISDN", "value":ny}], "type": "Owner"}, {"id": [{"schemeName": "MSISDN", "value":number2}], "type": "Member"}]}, "type": "AcceptInvitation"}
    
    
rreqa4=requests.patch(urla4, headers=hda4, json=jsona4).text
#print(rreq4)
if str('{}') in str(rreqa4):
	print("{}")
else:
	print("الخط عليه نوته برجاء الانتظار حتي يتم الغاء الطلب ") 
	print('\033[2;35m ='*65)

urla5="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"


hda5={
    
    "Host": "mobile.vodafone.com.eg",
    "x-dynatrace":"MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
    "msisdn": ny,
    "api-version":"v2",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": "Bearer "+(jwat)+"",
    "x-agent-device":"RMX1911",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"302",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}

jsona5={"category": [{"listHierarchyId": "TemplateID","value": "47"}], "createdBy": {"value": "MobileApp"},"parts": {"characteristicsValue": {"characteristicsValue": [{"characteristicName": "Disconnect", "value":"0"},{"characteristicName": "LastMemberDeletion", "value": "1"}]},"member": [{"id": [{"schemeName": "MSISDN","value": ny}], "type": "Owner"},{"id": [{"schemeName": "MSISDN", "value": number2}], "type": "Member"}]},"type": "FamilyRemoveMember"}

reqt=requests.patch(urla5, headers=hda5, json=jsona5).text
if str('{}') in str(reqt):
	print('\033[2;32m='*50)
	
else:
	print('\033[1;31m='*50)
	json=pyfiglet.figlet_format('erorr')
	print (json)
	hhhhgg
	hhhyo
	jfkfifjfj

url="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



headers={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
data={
"username":number,

"password":password,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
Ahmed=requests.post(url, headers=headers, data=data)

#print(res)

jwt=Ahmed.json()["access_token"]


print("\033[1;33m=" * 40)

#print(jwt)


url2="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"


#print(url2)

hd={
    
    "Host": "mobile.vodafone.com.eg",
    "x-dynatrace":"MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
    "msisdn": number,
    "api-version":"v2",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": "Bearer "+(jwt)+"",
    "x-agent-device":"RMX1911",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"302",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}

json={"category": [{"listHierarchyId": "PackageID", "value": "523"}, {"listHierarchyId": "TemplateID", "value": "47"}, {"listHierarchyId": "TierID", "value": "523"}, {"listHierarchyId": "familybehavior", "value": "percentage"}], "name": "FlexFamily", "parts": {"characteristicsValue": {"characteristicsValue": [{"characteristicName": "quotaDist1", "type": "percentage", "value": gcv,}]}, "member": [{"id": [{"schemeName": "MSISDN", "value":number,}], "type": "Owner"}, {"id": [{"schemeName": "MSISDN", "value":number2}], "type": "Member"}]}, "type": "SendInvitation"}
    
    
loka=requests.patch(url2, headers=hd, json=json).text
#print(loka)
#if str('{}') in str(loka):
#	print()
#	
	
url3="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



headers3={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
data3={
"username":number2,

"password":password2,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
z=requests.post(url3, headers=headers3, data=data3)

lok=z.json()["access_token"]


print("=" * 40)


url4="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"


hd4={
    
    "Host": "mobile.vodafone.com.eg",
    "x-dynatrace":"MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
    "msisdn": number2,
    "api-version":"v2",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": "Bearer "+(lok)+"",
    "x-agent-device":"RMX1911",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"302",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}

json4={"category": [{"listHierarchyId": "TemplateID", "value": "47"}], "name": "FlexFamily", "parts": {"member": [{"id": [{"schemeName": "MSISDN", "value":number}], "type": "Owner"}, {"id": [{"schemeName": "MSISDN", "value":number2}], "type": "Member"}]}, "type": "AcceptInvitation"}
    
    
rreq4=requests.patch(url4, headers=hd4, json=json4).text
#print(rreq4)

url5="https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"


hd5={
    
    "Host": "mobile.vodafone.com.eg",
    "x-dynatrace":"MT_3_13_2611661057_68-0_a556db1b-4506-43f3-854a-1d2527767923_0_77308_312",
    "msisdn": number,
    "api-version":"v2",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "Authorization": "Bearer "+(jwt)+"",
    "x-agent-device":"RMX1911",
    "Accept": "application/json",
    "x-agent-version":"2022.2.1.2",
    "x-agent-build":"503",
    "Accept-Language":"ar",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"302",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
}

json5={"category": [{"listHierarchyId": "TemplateID","value": "47"}], "createdBy": {"value": "MobileApp"},"parts": {"characteristicsValue": {"characteristicsValue": [{"characteristicName": "Disconnect", "value":"0"},{"characteristicName": "LastMemberDeletion", "value": "1"}]},"member": [{"id": [{"schemeName": "MSISDN","value": number}], "type": "Owner"},{"id": [{"schemeName": "MSISDN", "value": number}], "type": "Member"}]},"type": "FamilyRemoveMember"}

rreq5=requests.patch(url5, headers=hd5, json=json5).text
#print(rreq5)
#if str('{}') in str(rreq5):
#	il=pyfiglet.figlet_format(" Added successfully ")
#	print(il)

time.sleep(3)
print("برجاء التاكد من الاضافه ")
avt=input('Enter Your Number :')
prt=input("Enter Your Password :")
urlay="https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"



headersay={
    "Accept":"application/json, text/plain, */*",
    "Connection":"keep-alive",
    "x-dynatrace":"MT_3_17_998679495_45-0_a556db1b-4506-43f3-854a-1d2527767923_0_18957_273",
    "x-agent-operatingsystem":"1630483957",
    "clientId":"AnaVodafoneAndroid",
    "x-agent-device":"RMX1911",
    "x-agent-version":"2021.12.2",
    "x-agent-build":"493",
    "Content-Type":"application/x-www-form-urlencoded",
    "Content-Length":"143",
    "Host":"mobile.vodafone.com.eg",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/4.9.1"
    }
    
    
dataay={
"username":avt,

"password":prt,

"grant_type":"password",

"client_secret":"a2ec6fff-0b7f-4aa4-a733-96ceae5c84c3",

"client_id":"my-vodafone-app"
    }    
    
    
Ahmead=requests.post(urlay, headers=headersay, data=dataay)

#print(res)

jwaty=Ahmead.json()["access_token"]


urdu="https://mobile.vodafone.com.eg/services/dxl/usage/usageConsumptionReport?%40type=aggregated&bucket.product.publicIdentifier="+avt+""

hdthdu={"Host":"mobile.vodafone.com.eg",
"Connection":"Keep-Alive",
"useCase":"aggregated",
"x-dynatrace": "MT_3_8_297557593_55-0_a556db1b-4506-43f3-854a-1d2527767923_0_207_164",
'msisdn':avt,
"api-host":"usageConsumptionHost",
"Accept-Language":"ar",
"Authorization": "Bearer "+(jwaty)+"",
"Content-Type":"application/json",
"Accept":"application/json",
"clientId":"AnaVodafoneAndroid",
"User-Agent":"okhttp/4.9.1",
"x-agent-build":"503",
"x-agent-version":"2022.2.1.2",
"Accept-Encoding":"gzip",
"x-agent-device":"a22",
"x-agent-operatingsystem":"A225FXXU3BVF1",
"api-version":"v2"

         }
    
    
lokaf=requests.get(urdu, headers=hdthdu).json()

#print(loka)

for x in lokaf:
 #print(x)
 try:
  bucket=x["bucket"]
  #print(bucket)
  for t in bucket:
  	usageType=t["bucketBalance"]
  	#print(usageType)
  	for yy in usageType:
  		bh=yy["remainingValue"]
  		print(bh)
  		z=(bh[0]["usageType"])
  		print(z)
  		
#  		for ii in bh:
#  			amount2=ii["amount"]
#  			#print(amount)
#  			amount1=(amount2[3]["amount"])
#  			print(amount1)
 except:
  pass
	
#else:
#	print('\033[2;35m _'*65)
#	json=pyfiglet.figlet_format('erorr')
#	print (json)