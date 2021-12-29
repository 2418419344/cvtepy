from selenium import webdriver
from time import sleep
wd = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
wd.implicitly_wait(10)
wd.get('http://127.0.0.1:8047/mgr/sign.html')
wd.maximize_window()
wd.find_element_by_id('username').send_keys("byhy")
sleep(2)
wd.find_element_by_id('password').send_keys("88888888\n")
sleep(2)
wd.find_element_by_css_selector('.fa-plus').click()

wd.find_element_by_css_selector('.fa-plus').click()
sleep(1)
wd.find_element_by_css_selector('.fa-user').click()
sleep(1)
wd.find_element_by_css_selector('.fa-paperclip').click()


'''
gt = wd.switch_to.alert.text
print(gt)
wd.switch_to.alert.accept()
wd.switch_to.alert.dismiss()
wd.quit()
'''
