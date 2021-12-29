from selenium import webdriver
from time import sleep

wd = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
wd.get('http://www.baidu.com')
from selenium.webdriver.common.action_chains import ActionChains
wd.maximize_window()
ac = ActionChains(wd)
sleep(2)
ac.move_to_element(
    wd.find_element_by_css_selector('[name="tj_settingicon"]')
).perform()
wd.find_element_by_link_text('搜索设置').click()
sleep(2)
wd.find_element_by_link_text('保存设置').click()
su1 = wd.switch_to.alert.text
print(su1)