from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions as EC
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from time import sleep


uberURL = 'https://www.uber.com/global/en/price-estimate/'
lyftURL = 'https://www.lyft.com/rider/fare-estimate'

options = Options()
#options.add_argument('--headless')

response = {'Uber': {}, 'Lyft': {}}

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

def getUberPrices(start, dest):
    driver.get(uberURL)

    originForm = driver.find_element(By.NAME, 'pickup')
    destinationForm = driver.find_element(By.NAME, 'destination')

    originForm.send_keys(start)
    originForm.click()
    sleep(5)
    originForm.send_keys(Keys.ENTER)

    destinationForm.send_keys(dest)
    destinationForm.click()
    sleep(5)
    destinationForm.send_keys(Keys.ENTER)

    sleep(7)

    uberHTML = driver.page_source

    driver.back()

    resp = {}

    try:
        soup = BeautifulSoup(uberHTML, 'lxml')

        products = soup.find('div', {'class':'pe-products nm i2 cj'})

        print(products.text)
        prices = products.text.replace('UberX', ' UberX').replace('Assist', ' Assist').split()
        print(prices)

        for i in prices:
            prices[prices.index(i)] = i.replace('CA', ' CA')

        for i in prices:
            key = ''
            value = ''
            for j in i:
                if (j == ' '):
                    for k in range(i.index(j)):
                        key += i[k]
                    for k in range(i.index(j), len(i)):
                        value += i[k]
                    resp[key] = value
                    break

        response['Uber'] = resp
    except:
        response['Uber'] = { 'error': 'No drivers available or some other error occured' }

def getLyftPrices(start, dest):
    driver.get(lyftURL)

    originForm = driver.find_element(By.NAME, 'fare-start')
    destinationForm = driver.find_element(By.NAME, 'fare-end')

    for i in start:
        originForm.send_keys(i)
        sleep(0.1)

    sleep(0.5)
    originForm.send_keys(Keys.ENTER)

    for i in dest:
        destinationForm.send_keys(i)
        sleep(0.1)

    sleep(0.5)
    destinationForm.send_keys(Keys.ENTER)

    sleep(1.5)

    buttons = driver.find_elements(By.CSS_SELECTOR, 'button')

    estimate = buttons[4]

    action.double_click(estimate).perform()

    try:
        lyftHTML = driver.page_source

        driver.close()

        soup = BeautifulSoup(lyftHTML, 'lxml')

        results = soup.find('div', {'role': 'listbox'})

        resp = {}

        prices = results.text.replace('AM', ' ').replace('PM', ' ').replace('Lyft4', 'Lyft ').replace('Lux4', 'Lux ').replace('Black4', 'Black ').replace('XL6', 'XL ')
        print(prices)
        for i in prices:
            key = ''
            value = ''
            if (i == ' '):
                for k in range(prices.index(i)):
                    key += prices[k]
                for k in range(prices.index(i) + 1, len(prices)):
                    if (prices[k] == ' '): break
                    value += prices[k]
                resp[key] = value
                break
        response['Lyft'] = resp

    except:
        print('ERROR OCCURED')
        response['Lyft'] = { 'error': 'No drivers available or some other error occured' }



#getUberPrices('340 St Clair Ave E', '320 St Clair Ave E')
getLyftPrices('340 St Clair Ave E', '320 St Clair Ave E, Toronto, ON')

print(response)