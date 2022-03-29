from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HashtagGenerator:
    # Returns list of tags
    def GenerateTags(self,tag = [],ammount = 0):
        driver = webdriver.Chrome(executable_path='/chromedriver.exe')
        implWait = driver.implicitly_wait(10)
        generatedTags = []
        # Login to Instagram
        driver.get('https://www.instagram.com') ; implWait
        driver.find_element_by_name('username').send_keys("") 
        driver.find_element_by_name('password').send_keys("")
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        # retrieve Search bar drop down result
        for t in tag:
            driver.find_element_by_xpath('//input[@placeholder="Search"]').send_keys(t) ; implWait
            nextTags = driver.find_elements_by_partial_link_text(t.replace('#',''))
            for nt in nextTags[1:ammount]:
                generatedTags.append(nt.get_attribute('href').replace('https://www.instagram.com/explore/tags/','#').replace('/', ''))
            implWait ; driver.find_element_by_class_name('coreSpriteSearchClear').click()
        driver.close()
        return generatedTags