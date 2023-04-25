from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

browser = webdriver.Chrome()
print(f'type(browser): {type(browser)}')

url = 'https://apps.crossref.org/SimpleTextQuery'
browser.get(url)

try:
    with open('data/ch12/PB11112222.txt', encoding='utf8') as fh:
        pyperclip.copy(fh.read())

    elem = browser.find_element(By.CSS_SELECTOR, '#freetext')
    print('Found <%s> element with that class name!' % (elem.tag_name))
    elem.click()

    action = ActionChains(browser)
    action.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL) \
        .send_keys(Keys.TAB).send_keys(Keys.SPACE) \
        .send_keys(Keys.TAB).send_keys(Keys.SPACE) \
        .send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

    result_elem = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent2"]/div/form/font/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[5]/td/table')))

    print("===>", result_elem.get_attribute('innerHTML'))

    # Clicking Browser Buttons
    browser.refresh()
    time.sleep(3)
    browser.quit()
    # browser.forward()
    # browser.back()

except Exception as exc:
    print('Was not able to find an element with that name.', exc)
