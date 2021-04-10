import os,time
from headless_bro import headless_bro
from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_proxy():
    cmd = 'mitmdump -s proxy_parsing.py -q'
    os.system(cmd)
def run_bro():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server=http://127.0.0.1:8080")

    browser = webdriver.Chrome(r'/Users/wei/workspace/chromedriver',chrome_options=chrome_options)#r 代表的是强制禁止转义
    # browser = headless_bro()
    base_url = 'https://vip.bljiex.com/?v='
    vedio_url = input('粘贴视频的网址:')
    browser.get(base_url+vedio_url) #访问网站
def down_video():
    with open('get_url.txt', 'r') as f:
        url = f.read()
    down_cmd = f'ffmpeg -i {url} -c copy  output.mp4'
    os.system(down_cmd)
with ThreadPoolExecutor() as pool:
    futures = [pool.submit(run_proxy), pool.submit(run_bro)]

