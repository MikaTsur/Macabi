import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class DemoGetText():
    def demo_gettext(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://serguide.maccabi4u.co.il/heb/doctors/doctorssearchresults/?City=5000&Gender=2&PageNumber=1&RequestId=6e184a98-1969-5069-83f0-affd9ba8a1d0&Source=SearchPage&TreatPubTypeList=453780005&TreatType=453780005")
        time.sleep(12)
        text = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[2]').text
        print(text)
        time.sleep(2)


findbyxpath = DemoGetText()
findbyxpath.demo_gettext()
