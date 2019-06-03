import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import ACCOUNT_PATH


def login(driver):
    file = open(ACCOUNT_PATH, 'r', encoding='UTF-8')
    account = json.load(file)

    driver.get('https://adobeid-na1.services.adobe.com/renga-idprovider/pages/login?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fmixamo1%2FAdobeID%2Fcode%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.mixamo.com%252F%2523%252Fimsauth&client_id=mixamo1&scope=openid%2CAdobeID%2Cfetch_sao%2Csao.creative_cloud&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2Fmixamo1%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.mixamo.com%252F%2523%252Fimsauth%26response_type%3Dcode&display=web_v2&relay=49dab126-20fe-4421-a1e7-5dbd2c4b0110&locale=en_US&flow_type=code&ctx_id=mixamo_web&idp_flow_type=login')
    driver.find_element_by_id('adobeid_password').send_keys(account.get('password'))
    driver.find_element_by_id('adobeid_username').send_keys(account.get('account'))
    driver.execute_script('arguments[0].click();', driver.find_element_by_id('sign_in')) # 요즘엔 element.click() 이 안 먹나 보네





