from selenium import webdriver

url = '<url>'
browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath('<xpath>').click()
browser.find_element_by_xpath('<xpath>').send_keys("**********")
browser.find_element_by_xpath('<xpath>').send_keys("**********")
browser.find_element_by_xpath('<xpath>').click()