#PY script to get related search phrases for iOS keywords
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import sys

#set browser size
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome("PATH_TO_CHROMEDRIVER",chrome_options=chrome_options)
driver.set_window_size(1920, 1080)

#login
driver.get("http://www.appcodes.com/")
time.sleep(2)


elem = driver.find_element_by_xpath('//*[@id="loginDropdown"]').click()
elem = driver.find_element_by_xpath('//*[@id="loginInput"]')
elem.send_keys("YOUR_USERNAME")

elem = driver.find_element_by_xpath('//*[@id="loginForm"]/input[2]')
elem.send_keys("YOUR_EMAIL")

elem.send_keys(Keys.RETURN)
time.sleep(2)

driver.get('https://www.appcodes.com/') #might need to edit the URL depending on site updates
time.sleep(7)


#define the seed keywords and add them to the list
seed_list = ['test','ball']




#main function

dictio = {}

def get_suggestions(seed_list):
    for i in seed_list:
        search_field = driver.find_element_by_id('kwQuery2')
        search_field.click()
        search_field.send_keys(i)
        time.sleep(5) 
        lista_s = []
        #get suggestions
        search_suggestions = driver.find_elements_by_xpath('/html/body/ul/li[@class="ui-menu-item"]')
        for suggestion in search_suggestions:
            
            print (suggestion.get_attribute('innerHTML'))
            lista_s.append(suggestion.get_attribute('innerHTML'))
        #clear search field
        search_field.clear()
        dictio[i] = lista_s
        print (dictio.items())

get_suggestions(seed_list)


with open('PATH_TO_CSV_OUTPUT.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Seed keywords','Search phrases'])
    
    for key, value in dictio.items():
        for j in value:
            writer.writerow([key,j])

 

        
    csvfile.close()
        


