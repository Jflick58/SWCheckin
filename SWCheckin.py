
from selenium import webdriver
import time




driver = webdriver.Safari()

driver.get("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=12&ved=0ahUKEwjOhZGirpvTAhXHslQKHY5XBEgQFghVMAs&url=https%3A%2F%2Fwww.southwest.com%2Fflight%2FretrieveCheckinDoc.html&usg=AFQjCNH3fU660ZJzhh7NHlLeGH81pFPMWQ&sig2=FqRYvaY8o3otSu52AEK-dg")
driver.find_element_by_name('confirmationNumber').send_keys('#confirmation_number')
driver.find_element_by_name('firstName').send_keys('#Firstname')
driver.find_element_by_name('lastName').send_keys('#lastname')

driver.find_element_by_name('submitButton').click()


time.sleep(2)


driver.find_element_by_id("printDocumentsButton").click()

time.sleep(4)

driver.find_element_by_id("optionEmail").click()

element = driver.find_element_by_name('emailAddress')
element.clear()
element.send_keys("#email")

driver.find_element_by_id("checkin_button").click()

time.sleep(2)
