from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests

session = requests.Session()

r = requests.get('http://www.pceggs.com/nologin.aspx')
print(r.cookies.get_dict())
bsObj = BeautifulSoup(r.text,'html.parser')

imageLocation = bsObj.find('img',{'id':'valiCode'})['src']
viewstate = bsObj.find('input',{'name':'__VIEWSTATE'})['value']
viewstategenerator = bsObj.find('input',{'name':'__VIEWSTATEGENERATOR'})['value']
smoeny = bsObj.find('input',{'name':'SMONEY'})['value']


captchaUrl = 'http://www.pceggs.com' + imageLocation

urlretrieve(captchaUrl,'captcha.jpg')


captchaResponse = input('请收入验证码：')
print('captcha solution attempt: ' + captchaResponse)
username = 'ningbnii'
password = 'chenpn083714'
if len(captchaResponse) == 4:
    params = {'txt_UserName':username,'txt_PWD':password,'txt_VerifyCode':captchaResponse,'__VIEWSTATE':viewstate,'__VIEWSTATEGENERATOR':viewstategenerator,'SMONEY':smoeny,'Login_Submit.x':0,'Login_Submit.y':0,'FromUrl':'http://www.pceggs.com/'}
    r = requests.post('http://www.pceggs.com/nologin.aspx',data=params)
    print(r.cookies.get_dict())
    responseObj = BeautifulSoup(r.text,'html.parser')