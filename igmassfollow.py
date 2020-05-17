from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import time
import random
import sys
import os
import datetime

def main():
 
 count = 20  # number of profiles you want to get (not recommend more than 20 per hour or 350 per day)
 account = "therock"  # account from
 page = "followers"  # from following or followers

 yourusername = "*******" #your IG username
 yourpassword = "*******"  #your IG password


 #for proxy i recommend 4G mobile proxy: http://www.virtnumber.com/mobile-proxy-4g.php
 #PROXY = "http://84.52.54.2:8011" # IP:PORT or HOST:PORT
 #options.add_argument('--proxy-server=%s' % PROXY)

 uagentlist = ['Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57', 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36', ]
 useragent = random.choice(uagentlist)
 print(useragent)
 options = webdriver.ChromeOptions()
 options.add_argument('--ignore-certificate-errors')
 options.add_argument('--user-agent="%s"' % useragent)

 driver = webdriver.Chrome(options=options)

 driver.get('https://www.instagram.com/accounts/login/')
 sleep(3)
 username_input = driver.find_element_by_css_selector("input[name='username']")
 password_input = driver.find_element_by_css_selector("input[name='password']")
 username_input.send_keys(yourusername)
 password_input.send_keys(yourpassword)
 login_button = driver.find_element_by_xpath("//button[@type='submit']")
 login_button.click()
 WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
 sleep(3)
          
 driver.get('https://www.instagram.com/%s' % account)
 sleep(2) 
 driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
 #scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')


 if page == "following":
   scr3 = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span' )
   followers = int(scr3.text.replace(",",""))
   
 else:
  scr3 = driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span' )
  title1 = [elem.get_attribute('title') for elem in scr3]
  followers = int(title1[0].replace(",",""))
 
 sleep(2)
 print("\033[31m" + (account) + ">>>>" + page, (followers), "\033[0m")

 x = datetime.datetime.now()
 print(x)
 counts2 = 0
 for i in range(1,followers): #main count
    sleep(2)
    scr1 = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[%s]' % i)
    driver.execute_script("arguments[0].scrollIntoView();", scr1)
    sleep(1)
    text = scr1.text
    list = text.split()
    x = len(list)
    a = x - 1
    iffollow = list[a]
    print("\033[34m" + iffollow + " " + list[0] + "\033[0m")
    #subscribe
    if iffollow == "Follow":
      if counts2 == count: # limits count
        limits()
        break
      counts2 += 1  
      driver.execute_script("window.open('');")
      driver.switch_to.window(driver.window_handles[1])
      profile = list[0]
      driver.get('https://instagram.com/%s' % profile)
      WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Follow')]"))).click()
      sleep(2)
      print("\033[1;32m Subscribe \033[1;0m")
      driver.close()
      driver.switch_to.window(driver.window_handles[0])
    else:
      continue

def limits():
 x2 = datetime.datetime.now()
 print (x2)
 print ("\033[31m End \033[0m")    

main()
      
