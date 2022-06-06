import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui, expected_conditions as EC
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from time import sleep

app = FastAPI()

origins = {
    'https://rgarrettlee.github.io/',
    'https://rgarrettlee.github.io/webhook-testing/',
    'https://rgarrettlee.github.io/Ride-Compare/'
}

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

uberURL = 'https://www.uber.com/global/en/price-estimate/'
lyftURL = 'https://www.lyft.com/rider/fare-estimate'

options = Options()
#options.add_argument('--headless')

returnData = {'Uber': {}, 'Lyft': {}}

class info(BaseModel):
    origin : dict
    dest: dict

@app.get('/', status_code=200)
def index():
    return { 'message': 'hello world!' }

@app.post('/', status_code=201)
def index_post(info: info):
    print('Post incoming')
    jsonData = jsonable_encoder(info)
    print(jsonData)
    getUberPrices(jsonData['origin'], jsonData['dest'])
    #getLyftPrices(jsonData['origin'], jsonData['dest'])
    print(returnData)
    return info

@app.options('/', status_code=201)
def index_options(info: info):
    print('Info incoming')
    return info

if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host="localhost",
        port=5000,
        reload=True
    )

def getUberPrices(start, dest):
    driver = webdriver.Chrome(options=options)
    action = ActionChains(driver)
    driver.get(uberURL)

    originForm = driver.find_element(By.NAME, 'pickup')
    destinationForm = driver.find_element(By.NAME, 'destination')

    originForm.send_keys('{}'.format(start['street']))
    originForm.click()
    sleep(5)
    originForm.send_keys(Keys.ENTER)

    destinationForm.send_keys('{}'.format(dest['street']))
    destinationForm.click()
    sleep(5)
    destinationForm.send_keys(Keys.ENTER)

    sleep(10)

    uberHTML = driver.page_source

    driver.close()

    resp = {}

    try:
        soup = BeautifulSoup(uberHTML, 'lxml')

        products = soup.find('div', {'class':'pe-products nm i2 cj'})

        prices = products.text.replace('UberX', ' UberX').replace('Assist', ' Assist').replace('Connect', ' Connect').replace('WAV', ' WAV').split()

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

        returnData['Uber'] = resp
    except:
        returnData['Uber'] = { 'error': 'No drivers available or some other error occured' }

def getLyftPrices(start, dest):
    driver = webdriver.Chrome(options=options)
    action = ActionChains(driver)
    driver.get(lyftURL)

    originForm = driver.find_element(By.NAME, 'fare-start')
    destinationForm = driver.find_element(By.NAME, 'fare-end')

    originLoc = '{}, {}, {} {}'.format(start['street'], start['city'], start['country'], start['postal_code'])
    destLoc = '{}, {}, {} {}'.format(dest['street'], dest['city'], dest['country'], dest['postal_code'])

    for i in range(originLoc):
        originForm.send_keys(originLoc[i])
        sleep(0.1)

    sleep(0.5)
    originForm.send_keys(Keys.ENTER)

    for i in destLoc:
        destinationForm.send_keys(destLoc[i])
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
        returnData['Lyft'] = resp

    except:
        print('ERROR OCCURED')
        returnData['Lyft'] = { 'error': 'No drivers available or some other error occured' }
