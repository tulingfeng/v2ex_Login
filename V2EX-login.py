import requests
import pytesseract
from bs4 import BeautifulSoup
from PIL import Image
'''
尝试采用识别验证码的方式模拟网站登录，先登录较为简单的V2EX网站
'''
def captchaInput(captcha_data):
    with open("captcha.jpg","wb") as f:
        f.write(captcha_data)
        f.close()
        image=Image.open("captcha.jpg")
        # 将图片处理成灰度图像
        image=image.convert("L")
        # 选取chi_sim(chinese_simplised)中文简体语言
        text=pytesseract.image_to_string(image,lang='chi_sim')
        return text

def Login(url):
    UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"
    header = { "User-Agent" : UA,
           "Referer": "http://www.v2ex.com/signin"
           }

    v2ex_session=requests.Session()
    f=v2ex_session.get(url,headers=header)
    # print(f.content.decode("utf-8"))
#     采用BeautifulSoup获取name、password、captcha、once值，可以采用的解析器包括：html.parser/lxml/xml/html5lib
    soup=BeautifulSoup(f.content,"lxml")
    name=soup.find('input',{'placeholder':'用户名或电子邮箱地址'})['name']
    password=soup.find('input',{'type':'password'})['name']
    captcha=soup.find('input',{'placeholder':'请输入上图中的验证码'})['name']
    once = soup.find('input', {'name': 'once'})['value']
    captcha_url='https://www.v2ex.com/_captcha?once=%s'%once
    # 2种取字符串的方法：content和text，其中text取出的是文本
    captcha_data=v2ex_session.get(captcha_url,headers=header).content
    text=captchaInput(captcha_data)

    formdata={
        name:'tutuars',
        password:'tu835238',
        captcha:text,
        'once':once,
        'next':'/'
    }
    v2ex_session.post(url,data=formdata,headers=header)
    f = v2ex_session.get('http://www.v2ex.com/settings',headers=header)
    print(f.content.decode('utf-8'))


if __name__ == "__main__":
    url = "http://www.v2ex.com/signin"
    Login(url)
