import requests
from bs4 import BeautifulSoup

session = requests.Session()
mycookie = {'.ADWASPX7A5C561934E_PCEGGS':'D837093CD606A2FC1F77FC925F9D39F01CE681C4F86497B731E9849DE1F6653A11315FDB752E2696033A8ACD51DDA2E531A5BDB94DEB6238E2A720D5402EEAF24F923CB2E3573CD97F0AAFED7B55C8CE9C5FFABB07D6CB12DA2D69168D3416FEFA186ECEC0A7DF9CD4F9A7F0C60BE2C74CF9D99FA2819F7038AC7DBEB16E7432E122E862'}
requests.utils.add_dict_to_cookiejar(session.cookies,mycookie)
s = session.get('http://www.pceggs.com/play/pxya.aspx')
responseObj = BeautifulSoup(s.text,'html.parser')
myStr = responseObj.find('div',{'class':'xy2820131227_l'}).get_text().strip()

periods = myStr[5:11]
num1 = int(myStr[17:18])
num2 = int(myStr[21:22])
num3 = int(myStr[25:26])
result = sum([num1,num2,num3])
