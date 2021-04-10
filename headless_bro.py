from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

def headless_bro():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("–proxy-server=http://127.0.0.1:8080")

    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument("--proxy-server=http://127.0.0.1:8080")

    bro = webdriver.Chrome(executable_path='/Users/wei/workspace/chromedriver', chrome_options=chrome_options, options=option)
    return bro


# make_new_cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies.split('; ')}