#semi automated gmail unlimited account By Deepak-glitch
from selenium import webdriver
import time
import random

n=int(input("Enter How many times You want to run the Bot: "))
web = webdriver.Chrome()
web.get('https://accounts.google.com/signup')
FirstName = web.find_element_by_xpath('//*[@id="firstName"]')
FirstName.send_keys('lucifer')
LastName=web.find_element_by_xpath('//*[@id="lastName"]')
LastName.send_keys('Marker')
username=web.find_element_by_xpath('//*[@id="username"]')
#username.send_keys('xsee83452')
for i in range(1,n+1):
    x='xsee8345233515133aad'
    x+= random.choice(x) 
    if len(x)<30 :
        username.send_keys(x)
    else :
        uname=input("Enter username: ")
        username.send_keys(uname)
    #We need to check For username exist //*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div
Password=web.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
Password.send_keys('lucifer@123')    
ConfirmPass=web.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
ConfirmPass.send_keys('lucifer@123')
Next  = web.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button/div[2]')
Next.click()
#Note the country will  be already set by google 
Phno=web.find_element_by_xpath('//*[@id="phoneNumberId"]')
x=input("Enter Your Mobile NUmber: ")
#Because even if u have unlimited numbers it gets mixed up
Phno.send_keys(x)
Next1=web.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
Next1.click()
verification=web.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input')
y=input("Enter verification code: ")
verification.send_keys(y)
verify=web.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/div[2]')
verify.click()