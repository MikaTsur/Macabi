import time
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://online.maccabi4u.co.il/dana-na/auth/url_44/welcome.cgi')
time.sleep(3)


link = driver.find_element_by_link_text("כניסה עם סיסמה")
link.click()
time.sleep(3)


citizenId = driver.find_element_by_id("identifyWithPasswordCitizenId")
citizenId.send_keys("039423769")


password = driver.find_element_by_id("password")
password.send_keys("Mika1984")
password.send_keys(Keys.RETURN)
time.sleep(3)


popup = driver.find_element_by_link_text("הבנתי, תודה")
popup.click()
time.sleep(2)


scheduleAppointment = driver.find_element_by_id(
    "ctl00_ctl00_wcSiteHeaderLobby1_wcSiteHeaderNavigationMenu_rptNavigationMenuHeader_ctl02_lnkHref")
scheduleAppointment.click()
time.sleep(5)

searchService = driver.find_element_by_xpath(
    '//*[@id="app-wrap"]/div/div[3]/div/div[1]/div[2]/div[2]/div[2]/a[2]')
searchService.click()
time.sleep(2)

anotherService = driver.find_element_by_class_name(
    "Filter__text--2oRyX0gBZ2m1bCH")
anotherService.click()
time.sleep(2)


treatmentpopuptext = driver.find_element_by_xpath(
    '//*[@id="react-select-TreatType_select--value"]/div[2]/input')
treatmentpopuptext.send_keys("קולונוסקופיה")
treatmentpopuptext.send_keys(Keys.RETURN)


city = driver.find_element_by_xpath(
    '//*[@id="react-select-City_select--value"]/div/input')
city.send_keys("תל אביב - יפו")
city.send_keys(Keys.RETURN)

searchButton = driver.find_element_by_id(
    "SearchButton")
searchButton.click()
time.sleep(2)

gender = driver.find_element_by_id(
    "Gender2")
gender.click()
time.sleep(2)


#adultsOnly = driver.find_element_by_link_text('גסטרואנטרולוגיה')
print('Found! ' + gender)


# driver.quit()
# python MikaTest.py
# C:\Users\mika.m\OneDrive\Desktop\website_login>
