from selenium import webdriver
import time
def sleepn(n):
    time.sleep(n)
    
def autoDownld(nextLink
                ,xpath_="/html/body/section/main/div/center/center/center/form/span/a"
                ,btn_1='verify_button2'
                ,btn_2='verify_button'
                ,xpath2='/html/body/section/article/center/center/center[3]/a'):
    print(nextLink[0:-60])
    
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get(nextLink)
    btn=browser.find_element_by_xpath(xpath_)
    sleepn(2)
    btn.click()
    sleepn(1)
    browser.find_element_by_id(btn_1).click()
    sleepn(10)
    browser.find_element_by_id(btn_2).click()
    sleepn(9)
    browser.find_element_by_xpath(xpath2).click()
    browser.current_url
    sleepn(100*60)
    browser.close()
