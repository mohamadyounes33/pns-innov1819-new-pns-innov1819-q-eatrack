"""
Python program to calculate geographic
coordinates of places using google geocoding API
"""

import sys
sys.path.append("..")
import os
package_dir  = os.path.dirname(os.path.abspath(__file__))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

def getLocation():
    '''
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--headless")
    timeout = 20

    driver = webdriver.Chrome(executable_path = package_dir+'/chromedriver', chrome_options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()

    if latitude == '' :
        latitude = '43.708425'
        longitude = '7.291667'
    '''
    return ('43.708425','7.291667')


#if __name__ == '__main__' :
#    loca =  getLocation()
#    print(loca[0])
#    print("-____--")
#    print(loca[1])