

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import os
import time


driver = webdriver.Chrome(executable_path="/Users/ep9k/Desktop/SeleniumTest/drivers/chromedriver")

#driver.get('http://www.python.org')
#
#assert "Python" in driver.title
#
##elem = driver.find_element_by_name('q')
##elem = driver.find_element_by_id('id-search-field')
##elem = driver.find_element_by_class_name('search-field')
#elem.clear()     #clears pre populated text in element field
#
#elem.send_keys('python 2')
#elem.send_keys(Keys.RETURN)
#
#assert "No Results Found" not in driver.page_source
#
##driver.quit()


"""
driver.get('https://www.facebook.com/')
driver.implicitly_wait(5)

driver.find_element_by_name('email').send_keys("ep68891@appstate.edu")
driver.find_element_by_id('pass').send_keys("yuiruprup")
"""

"""
driver.get('https://www.facebook.com/')

driver.implicitly_wait(10)
driver.find_element_by_name('firstname').send_keys('Erich')
driver.find_element_by_name('lastname').send_keys('Purpur')
driver.find_element_by_name('reg_email__').send_keys('epurpur@gmail.com')
driver.find_element_by_name('reg_email_confirmation__').send_keys('epurpur@gmail.com')
driver.find_element_by_name('reg_passwd__').send_keys('testpass')
"""

#Land on Watauga County tax page
driver.get('http://tax.watgov.org/WataugaNC/search/commonsearch.aspx?mode=address')
driver.find_element_by_name('btAgree').click()                                                  #clicks 'Agree' button to agree to site's terms

#Under 'Property Records' Tab, click on 'Parcel ID' option
element_to_hover_over = driver.find_element_by_id('pd_Parent')                             #hover over 'property records' drop down menu
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

menu_options = driver.find_elements_by_class_name('PullDownMenuItem')
parcel_id_button = menu_options[5]                                                #choose this menu option, which is 'Parcel ID'
parcel_id_button.click()

#Enter parcel ID values into input boxes
driver.find_element_by_name('inpParid').send_keys('2911911616001')
driver.find_element_by_name('btSearch').click()

results = driver.find_element_by_class_name('SearchResults')                      #There will only be 1 result when searching by Parcel ID
results.click()

#Now look through results on Parcel ID landing page using Beautiful Soup. This prints all elements on the page
soup = BeautifulSoup(driver.page_source, 'html.parser')

labels = soup.find_all('td', class_='DataletSideHeading')
values = soup.find_all('td', class_='DataletData')

for label, value in zip(labels, values):
    print(label.text, " ", value.text)



#driver.find_element_by_name('inpNumber').send_keys('190')
#driver.find_element_by_name('inpStreet').send_keys('ELI HARTLEY')
#driver.find_element_by_name('btSearch').click()

#results = driver.find_elements_by_class_name('SearchResults')
#first_result = results[1]
#first_result.click()

#soup = BeautifulSoup(driver.page_source, 'html.parser')
#
#
#test = soup.find_all('div', style="margin-left:3px;").click()

#for i in test:
#    print(i.text)
#    print()
#
#driver.quit()




#driver.find_element_by_id("u_0_2").click()

#driver.quit()

#elem = driver.find_element_by_name('email')
#elem.send_keys('ep68891@appstate.edu')
#
#elem2 = driver.find_elements_by_name('pass')
#elem2.send_keys('yuiruprup')
#elem2.send_keys(Keys.RETURN)

