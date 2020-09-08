from selenium import webdriver
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
import hajiWaktus as hw
import re
import datetime



hajiName = 'Mohamed Rahim Bin Hassan'
#ACTUAL
hajiEmail = 'hajimohdrahim.232@gmail.com'
hajiNumber = '65657456'

#TEST
#hajiEmail = 'taqiuddin.bmz@outlook.com' #tester
#hajiNumber = '65650443' #tester


#ACTUAL Mukminin
masjidXPATH = "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[6]/div/label"

#TEST HUDA
#masjidXPATH = "/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[3]/div/label"

pageurl = 'https://ourmosques.commonspaces.sg/'


def hajiSubuh():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.close()
        ifhajiSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

        dateValue = driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').text
        if (dateValue == "Invalid Date"):
            driver.close()
            print("hajiSubuh INVALID DATE ERROR")
            ifhajiSubuhError()
        else:
            print(dateValue)

    except Exception:
        print("Can't locate date")
        driver.close()
        ifhajiSubuhError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_1]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.close()
        ifhajiSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.close()
        ifhajiSubuhError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(4)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("HAJI SUBUH Retrieving available capacity... error")
            driver.close()
            ifhajiSubuhError()

        else:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, masjidXPATH)),
                driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

            )


    except Exception:
        print("HAJI SUBUH not clickable uhh MASJID")
        driver.close()
        ifhajiSubuhError()

    else:
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=checkboxTermsAndCond]')),
            driver.find_element_by_css_selector('label[for=checkboxTermsAndCond]').click()

        )

    except Exception:
        driver.switch_to.active_element()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/button'))
        )

    finally:
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()
        print("haji Subuh clicked ok")

    site_key = "6Le2XDIUAAAAAHAZCXZ04Rz9GAgzj0MvsWJ1EwOw"

    with open(r"api_key.txt", "r") as f:
        api_key = f.read()

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key,
            "pageurl": pageurl,
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status'] == 0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
            driver.execute_script(js)
            driver.find_element_by_id("booking__submit_btn").click()
            status = 1

    time.sleep(5)
    result = driver.current_url
    x = re.search("booking-daily-success", result)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print(current_time)
    if x:
        print('hajiSubuh Booked!')
    else:
        print('hajiSubuh TOO LATE')
    driver.close()


def hajiIsyak():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.close()
        ifhajiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

        dateValue = driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').text
        if (dateValue == "Invalid Date"):
            driver.close()
            print("hajiIsyak INVALID DATE ERROR")
            ifhajiIsyakError()
        else:
            print(dateValue)

    except Exception:
        print("Can't locate date")
        driver.close()
        ifhajiIsyakError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_5]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.close()
        ifhajiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_5]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.close()
        ifhajiIsyakError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(4)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("hajiIsyak Retrieving available capacity... error")
            driver.close()
            ifhajiIsyakError()

        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("HAJI ISYAK not clickable uhh MASJID")
        driver.close()
        ifhajiIsyakError()

    else:
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=checkboxTermsAndCond]')),
            driver.find_element_by_css_selector('label[for=checkboxTermsAndCond]').click()

        )

    except Exception:
        driver.switch_to.active_element()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/button'))
        )

    finally:
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()
        print("clicked ok")

    site_key = "6Le2XDIUAAAAAHAZCXZ04Rz9GAgzj0MvsWJ1EwOw"

    with open(r"api_key.txt", "r") as f:
        api_key = f.read()

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key,
            "pageurl": pageurl,
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status'] == 0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
            driver.execute_script(js)
            driver.find_element_by_id("booking__submit_btn").click()
            status = 1

    time.sleep(5)
    result = driver.current_url
    x = re.search("booking-daily-success", result)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print(current_time)
    if x:
        print('hajiIsyak Booked!')
    else:
        print('hajiiIsyak TOO LATE')
    driver.close()


def hajiMaghrib():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.close()
        ifhajiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.close()
        ifhajiMaghribError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_4]'))

        )

    except Exception:
        print("Can't located Maghrib")
        driver.close()
        ifhajiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_4]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.close()
        ifhajiMaghribError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("hajiMaghrib Retrieving available capacity... error")
            driver.close()
            ifhajiMaghribError()
        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("HAJI MAGHRIB not clickable uhh MASJID")
        driver.close()
        ifhajiMaghribError()

    else:
        time.sleep(2)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=checkboxTermsAndCond]')),
            driver.find_element_by_css_selector('label[for=checkboxTermsAndCond]').click()

        )

    except Exception:
        driver.switch_to.active_element()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/button'))
        )

    finally:
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()
        print("clicked ok")

    site_key = "6Le2XDIUAAAAAHAZCXZ04Rz9GAgzj0MvsWJ1EwOw"

    with open(r"api_key.txt", "r") as f:
        api_key = f.read()

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key,
            "pageurl": pageurl,
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status'] == 0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
            driver.execute_script(js)
            driver.find_element_by_id("booking__submit_btn").click()
            status = 1

    time.sleep(5)
    driver.close()
    print('hajiMaghrib Booked!')


def hajiAsar():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.close()
        ifhajiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.close()
        ifhajiAsarError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_3]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.close()
        ifhajiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_3]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.close()
        ifhajiAsarError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("hajiASAR Retrieving available capacity... error")
            driver.close()
            ifhajiAsarError()
        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )

    except Exception:
        print("HAJI ASAR not clickable uhh MASJID")
        driver.close()
        ifhajiAsarError()

    else:
        time.sleep(1)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=checkboxTermsAndCond]')),
            driver.find_element_by_css_selector('label[for=checkboxTermsAndCond]').click()

        )

    except Exception:
        driver.switch_to.active_element()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/button'))
        )

    finally:
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()
        print("clicked ok")

    site_key = "6Le2XDIUAAAAAHAZCXZ04Rz9GAgzj0MvsWJ1EwOw"

    with open(r"api_key.txt", "r") as f:
        api_key = f.read()

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key,
            "pageurl": pageurl,
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status'] == 0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
            driver.execute_script(js)
            driver.find_element_by_id("booking__submit_btn").click()
            status = 1

    time.sleep(5)
    driver.close()
    print('hajiAsar Booked!')


def hajiZohor():
    driver = webdriver.Chrome(executable_path=r'/Users/nabilah/Downloads/chromedriver')
    driver.get(pageurl)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=typeof_prayer_1]'))

        )
    except Exception:
        print("Can't located daily")
        driver.close()
        ifhajiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=typeof_prayer_1]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label'))
        )

    except Exception:
        print("Can't locate date")
        driver.close()
        ifhajiZohorError()

    else:
        driver.find_element_by_xpath(
            '/html/body/div[2]/div/section/div/div/div/div/form/div/div[2]/div/span[2]/label').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=dailyprayer_time_2]'))

        )

    except Exception:
        print("Can't located SUBUH")
        driver.close()
        ifhajiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=dailyprayer_time_2]').click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=cluster_4]'))

        )

    except Exception:
        print("Can't located WEST")
        driver.close()
        ifhajiZohorError()

    else:
        driver.find_element_by_css_selector('label[for=cluster_4]').click()
        time.sleep(3)

    try:
        ##Retrieving available capacity... error
        if driver.find_element_by_xpath('/html/body/div[2]/div/section/div/div/div/div/form/div/div[7]/ul/li[1]/p[1]').is_displayed():
            print("hajiZOHOR Retrieving available capacity... error")
            driver.close()
            ifhajiZohorError()
        else:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, masjidXPATH)),
            driver.find_element_by_xpath(masjidXPATH).is_enabled() == True

        )


    except Exception:
        print("HAJI ZOHOR not clickable uhh MASJID")
        driver.close()
        ifhajiZohorError()

    else:
        time.sleep(1)
        driver.find_element_by_xpath(masjidXPATH).click()

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=first_person_name]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=first_person_name]').send_keys(hajiName)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_email_confirmation]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_email_confirmation]').send_keys(hajiEmail)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[name=contact_num]'))

        )

    finally:
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(Keys.COMMAND + 'a')
        driver.find_element_by_css_selector('[name=contact_num]').send_keys(hajiNumber)

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for=checkboxTermsAndCond]')),
            driver.find_element_by_css_selector('label[for=checkboxTermsAndCond]').click()

        )

    except Exception:
        driver.switch_to.active_element()
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[3]/button'))
        )

    finally:
        time.sleep(1.5)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button').click()
        print("clicked ok")

    site_key = "6Le2XDIUAAAAAHAZCXZ04Rz9GAgzj0MvsWJ1EwOw"

    with open(r"api_key.txt", "r") as f:
        api_key = f.read()

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key,
            "pageurl": pageurl,
            "json": 1}

    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"

    status = 0
    while not status:
        res = requests.get(url)
        if res.json()['status'] == 0:
            time.sleep(3)
        else:
            requ = res.json()['request']
            js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
            driver.execute_script(js)
            driver.find_element_by_id("booking__submit_btn").click()
            status = 1

    time.sleep(5)
    driver.close()
    print('hajiZohor Booked!')


def ifhajiSubuhError():
    hajiSubuh()
    hajiIsyak()
    hajiMaghrib()
    hajiAsar()
    hajiZohor()
    hw.stopRec()
    sys.exit()



def ifhajiIsyakError():
    hajiIsyak()
    hajiMaghrib()
    hajiAsar()
    hajiZohor()
    hw.stopRec()
    sys.exit()


def ifhajiMaghribError():
    hajiMaghrib()
    hajiAsar()
    hajiZohor()
    hw.stopRec()
    sys.exit()


def ifhajiAsarError():
    hajiAsar()
    hajiZohor()
    hw.stopRec()
    sys.exit()


def ifhajiZohorError():
    hajiZohor()
    hw.stopRec()
    sys.exit()