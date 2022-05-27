import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

user = 'INSIRA_O_EMAIL_@DASA'
login = 'SENHA'
dayOfTheWeek = datetime.today().weekday()

if dayOfTheWeek != 5 and dayOfTheWeek != 6:
    options = webdriver.ChromeOptions() 
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)
    driver.get('https://portalpessoas.dasa.com.br')
    time.sleep(1)

    driver.find_element(by=By.XPATH, value='//*[@id="userNameInput"]').send_keys(user)
    driver.find_element(by=By.XPATH, value='//*[@id="passwordInput"]').send_keys(login)
    driver.find_element(by=By.XPATH, value='//*[@id="submitButton"]').click()

    time.sleep(2)

    driver.find_element(by=By.XPATH, value='//*[@id="6f3162e9-000c-46d1-8e4d-f794472cfb12"]/div[2]/div[1]').click()

    time.sleep(2)

    if driver.find_element(by=By.XPATH, value='//*[@id="__button15-inner"]'):
        driver.find_element(by=By.XPATH, value='//*[@id="__button15-inner"]').click()

    driver.find_element(by=By.XPATH, value='//*[@id="marcacoes-tab"]').click()

    time.sleep(1)

    today = "// *[text()='"+datetime.today().strftime('%d/%m/20%y')+"']"
    index = driver.find_element(by=By.XPATH, value=today).get_attribute('id')
    index = index[(len(index) - 2) : len(index)]

    time.sleep(1)

    checkBoxId = '//*[@id="idMarc--idRowBase-idMarc--idMarcacao-' + index + '-selectSingle-Button"]'
    buttonId = '//*[@id="__button3-idMarc--idMarcacao-' + index + '-inner"]'
    driver.find_element(by=By.XPATH, value=checkBoxId).click()
    driver.find_element(by=By.XPATH, value=buttonId).click()

    time.sleep(1)

    driver.find_element(by=By.XPATH, value="// *[text()='Criar']").click()
    driver.find_element(by=By.XPATH, value='//*[@id="idNewTime-Picker-inner"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="idNewTime-Picker-inner"]').send_keys('09:00')
    driver.find_element(by=By.XPATH, value='//*[@id="idNewAbwgr"]').click()

    time.sleep(1)

    driver.find_element(by=By.XPATH, value='//*[@id="__item3-__clone5"]').click()

    time.sleep(1)

    driver.find_element(by=By.XPATH, value="// *[text()='Confirmar']").click()

    time.sleep(1)

    driver.find_element(by=By.XPATH, value="// *[text()='Criar']").click()
    driver.find_element(by=By.XPATH, value='//*[@id="idNewTime-Picker-inner"]').click()

    if dayOfTheWeek == 4:
        driver.find_element(by=By.XPATH, value='//*[@id="idNewTime-Picker-inner"]').send_keys('18:00')
    else:
        driver.find_element(by=By.XPATH, value='//*[@id="idNewTime-Picker-inner"]').send_keys('19:00')
        
    driver.find_element(by=By.XPATH, value='//*[@id="idNewAbwgr"]').click()

    time.sleep(2)

    driver.find_element(by=By.XPATH, value='//*[@id="__item4-__clone12"]').click()

    time.sleep(2)

    driver.find_element(by=By.XPATH, value="// *[text()='Confirmar']").click()

    time.sleep(1)
    driver.quit()
