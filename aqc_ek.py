#爱企查京东e卡库存监控，只写了tg推送，改一下第9，10行的内容即可
#不要问cron怎么写，自己看自己机器决定，再问就是* * * * * *
from requests import get, post
from random import choice
import os
def get_ua(brower_name):
    url = 'https://raw.githubusercontent.com/limoruirui/misaka/master/user-agent.json'
    useragent = choice(get(url).json()[brower_name])
    return useragent
def tgpush(content):
    bot_token = token
    user_id = id
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'chat_id': str(user_id), 'text': content, 'disable_web_page_preview': 'true'}
    try:
        req = post(url, headers=headers, data=data)
    except:
        print('推送失败')
def randomstr(numb):
    str = ''
    for i in range(numb):
        str = str + choice('abcdefghijklmnopqrstuvwxyz0123456789')
    return str
def get_status():
    url = 'https://aiqicha.baidu.com/usercenter/getBenefitStatusAjax'
    headers = {
      'User-Agent': get_ua('Safari'),
      'Referer': f'https://aiqicha.baidu.com/m/usercenter/exchangeList?VNK={randomstr(8)}'
    }
    if get(url, headers=headers).json()['data']['AQ03006'] == 1:
        tgpush('爱企查京东e卡有货，请进行兑换')
if __name__ == '__main__':
    id = os.environ["id"]
    token = os.environ["token"]
    get_status()
