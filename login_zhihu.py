
# coding:utf-8
import requests,time
from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/login/email'
def get_captcha(data):
    with open('captcha.gif','wb') as fb:#在本地查看图片并在python指令界面输入验证码
        fb.write(data)
    return input('captcha')

def login(username,password,oncaptcha):
    sessiona = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    xyz = sessiona.get('https://www.zhihu.com/#signin',headers=headers).content
    _xsrf = BeautifulSoup(sessiona.get('https://www.zhihu.com/#signin',headers=headers).content,'html.parser').find('input',attrs={'name':'_xsrf'}).get('value')
    captcha_content = sessiona.get('https://www.zhihu.com/captcha.gif?r=%d&type=login'%(time.time()*1000),headers=headers).content
    data = {
        "_xsrf":_xsrf,
        "email":username,
        "password":password,
        "remember_me":True,
        "captcha":oncaptcha(captcha_content)
    }
    resp = sessiona.post('https://www.zhihu.com/login/email',data,headers=headers).content
    print(resp)
    return resp 

if __name__ == "__main__":
    login('email','password',get_captcha)#将email，password修改为自己的账号和密码
