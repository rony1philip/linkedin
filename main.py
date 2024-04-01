from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3863760975&f_AL=true&geoId=101570771&origin=JOB_SEARCH_PAGE_JOB_FILTER')
time.sleep(5)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()
time.sleep(5)
email_input = driver.find_element(By.XPATH, '//*[@id="username"]')
password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
email_input.send_keys('prony3388@gmail.com')
password_input.send_keys('1122rR33')
next_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
next_button.click()
time.sleep(5)
jobs_elements = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

def abort_application():
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

for job in jobs_elements:
    job.click()
    time.sleep(5)
    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)
        print(1)
        phone_input = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        phone_input.clear()
        phone_input.send_keys('0502643332')
        print(2)
        next_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if next_button.get_attribute("data-control-name") == "continue_unify":
            print("Complex application, skipped.")
            abort_application()
            time.sleep(5)
            continue
        else:
            next_button.click()
            print(3)
            time.sleep(5)
            buttons = driver.find_elements(by=By.TAG_NAME, value="button") 
            print(4)
            if buttons[3].text == 'Next':
                buttons[3].click()
                time.sleep(5)
                print(5)
                labels = driver.find_elements(by=By.CLASS_NAME, value='artdeco-text-input--label')
                inputs = driver.find_elements(by=By.CLASS_NAME, value='artdeco-text-input--input')
                index = 0
                for l in labels:
                    answer = input(f'{l.text}')
                    inputs[index].send_keys(f'{answer}')
                    index += 1
                labels_with_lists = driver.find_elements(by=By.CSS_SELECTOR, value='.fb-dash-form-element .fb-dash-form-element__label')
                options_lists = driver.find_elements(by=By.TAG_NAME, value="select")
                index = 0
                option_index = 0
                for l in labels_with_lists:
                    print(l.text)
                    options_lists[index].click()
                    options = options_lists[index].find_elements(by=By.TAG_NAME, value='option')
                    for option in options:
                        print(f"{option_index}. {option.text}")
                        option_index += 1
                    print(range(option_index))
                    select = int(input('pick option index num: '))
                    options[select].click()
                    index +=1
                print(6)
                buttons = driver.find_elements(by=By.TAG_NAME, value="button")
                index = 0
                buttons[2].click()
                time.sleep(5)
                buttons = driver.find_elements(by=By.TAG_NAME, value="button")
                index = 0
                # for b in buttons:
                #     print(f'{b.text} = {index}')
                #     index += 1
                buttons[6].click()
            else:
                abort_application()

    except NoSuchElementException:
        continue

# next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
# next_button.click()