from selenium import webdriver as driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import os, requests
from colorama import init, Fore, Style
import json
init(convert=True)


######## INFORMATION###################################

class Task_Info(object):
    
    def __init__(self, location, billing_profile, task_scheduler):
        self.location = location
        self.billing_profile = billing_profile
        self.task_scheduler = task_scheduler


    def sign_up(self):

        input ('Press Enter to Start the Script...')
        #### EDIT THE BILLING PROFILE FOLDER PATH BELOW ####
        checkout_profile_path = ('C:\\Users\\Example\\Desktop\\Supreme Sign-Up Script\\billing profiles\\'+ self.billing_profile)
        final_checkout_profile_path = (checkout_profile_path + '.json')
        with open(final_checkout_profile_path) as data_file:
            active_profile = json.loads(data_file.read())

        global driver
        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = driver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.gmail.com')

        if self.task_scheduler == 'None':
            print ('Task Started...')
            pass
        else:
            time_setting = '%I:%M:%S'
            now = time.strftime(time_setting)
            timer_difference = datetime.strptime(self.task_scheduler, time_setting) - datetime.strptime(now, time_setting)
            print ('Starting Task in', + timer_difference.seconds, 'seconds...')
            time.sleep(timer_difference.seconds)
            print ('Task Started...')

        url = 'https://register.supremenewyork.com/'
        dict = {
            'Brooklyn':'//*[@id="step_1"]/div[4]/label[2]',
            'Manhattan':'//*[@id="step_1"]/div[4]/label[1]',
            'Los Angeles':'//*[@id="step_1"]/div[4]/label[3]'
            }

        states_dict = {
            'Alabama':'//*[@id="customer_state"]/option[2]',
            'Alaska':'//*[@id="customer_state"]/option[3]',
            'America Samoa':'//*[@id="customer_state"]/option[4]',
            'Arizona':'//*[@id="customer_state"]/option[5]',
            'Arkansas':'//*[@id="customer_state"]/option[6]',
            'California':'//*[@id="customer_state"]/option[7]',
            'Colorado':'//*[@id="customer_state"]/option[8]',
            'Connecticut':'//*[@id="customer_state"]/option[9]',
            'Delaware':'//*[@id="customer_state"]/option[10]',
            'District of Columbia':'//*[@id="customer_state"]/option[11]',
            'Federated States of Micronesia':'//*[@id="customer_state"]/option[12]',
            'Florida':'//*[@id="customer_state"]/option[13]',
            'Georgia':'//*[@id="customer_state"]/option[14]',
            'Guam':'//*[@id="customer_state"]/option[15]',
            'Hawaii':'//*[@id="customer_state"]/option[16]',
            'Idaho':'//*[@id="customer_state"]/option[17]',
            'Illinois':'//*[@id="customer_state"]/option[18]',
            'Indiana':'//*[@id="customer_state"]/option[19]',
            'Iowa':'//*[@id="customer_state"]/option[20]',
            'Kansas':'//*[@id="customer_state"]/option[21]',
            'Kentucky':'//*[@id="customer_state"]/option[22]',
            'Louisiana':'//*[@id="customer_state"]/option[23]',
            'Maine':'//*[@id="customer_state"]/option[24]',
            'Maryland':'//*[@id="customer_state"]/option[25]',
            'Massachusetts':'//*[@id="customer_state"]/option[26]',
            'Marshall Islands':'//*[@id="customer_state"]/option[27]',
            'Michigan':'//*[@id="customer_state"]/option[28]',
            'Minnesota':'//*[@id="customer_state"]/option[29]',
            'Mississippi':'//*[@id="customer_state"]/option[30]',
            'Missouri':'//*[@id="customer_state"]/option[31]',
            'Montana':'//*[@id="customer_state"]/option[32]',
            'Nebraska':'//*[@id="customer_state"]/option[33]',
            'Nevada':'//*[@id="customer_state"]/option[34]',
            'New Hampshire':'//*[@id="customer_state"]/option[35]',
            'New Jersey':'//*[@id="customer_state"]/option[36]',
            'New Mexico':'//*[@id="customer_state"]/option[37]',
            'New York':'//*[@id="customer_state"]/option[38]',
            'North Carolina':'//*[@id="customer_state"]/option[39]',
            'North Dakota':'//*[@id="customer_state"]/option[40]',
            'Northern Mariana Islands':'//*[@id="customer_state"]/option[41]',
            'Ohio':'//*[@id="customer_state"]/option[42]',
            'Oklahoma':'//*[@id="customer_state"]/option[43]',
            'Oregon':'//*[@id="customer_state"]/option[44]',
            'Palau':'//*[@id="customer_state"]/option[45]',
            'Pennsylvania':'//*[@id="customer_state"]/option[46]',
            'Puerto Rico':'//*[@id="customer_state"]/option[47]',
            'Rhode Island':'//*[@id="customer_state"]/option[48]',
            'South Carolina':'//*[@id="customer_state"]/option[49]',
            'South Dakota':'//*[@id="customer_state"]/option[50]',
            'Tennessee':'//*[@id="customer_state"]/option[51]',
            'Texas':'//*[@id="customer_state"]/option[52]',
            'Utah':'//*[@id="customer_state"]/option[53]',
            'Vermont':'//*[@id="customer_state"]/option[54]',
            'Virgin Island':'//*[@id="customer_state"]/option[55]',
            'Virginia':'//*[@id="customer_state"]/option[56]',
            'Washington':'//*[@id="customer_state"]/option[57]',
            'West Virginia':'//*[@id="customer_state"]/option[58]',
            'Wisconsin':'//*[@id="customer_state"]/option[59]',
            'Wyoming':'//*[@id="customer_state"]/option[60]'
            }
            
        credit_month = {
            '1':'//*[@id="credit_card_month"]/option[2]',
            '2':'//*[@id="credit_card_month"]/option[3]',
            '3':'//*[@id="credit_card_month"]/option[4]',
            '4':'//*[@id="credit_card_month"]/option[5]',
            '5':'//*[@id="credit_card_month"]/option[6]',
            '6':'//*[@id="credit_card_month"]/option[7]',
            '7':'//*[@id="credit_card_month"]/option[8]',
            '8':'//*[@id="credit_card_month"]/option[9]',
            '9':'//*[@id="credit_card_month"]/option[10]',
            '10':'//*[@id="credit_card_month"]/option[11]',
            '11':'//*[@id="credit_card_month"]/option[12]',
            '12':'//*[@id="credit_card_month"]/option[13]'
            }

        credit_year = {
            '2017':'//*[@id="credit_card_year"]/option[2]',
            '2018':'//*[@id="credit_card_year"]/option[3]',
            '2019':'//*[@id="credit_card_year"]/option[4]',
            '2020':'//*[@id="credit_card_year"]/option[5]',
            '2021':'//*[@id="credit_card_year"]/option[6]',
            '2022':'//*[@id="credit_card_year"]/option[7]',
            '2023':'//*[@id="credit_card_year"]/option[8]',
            '2024':'//*[@id="credit_card_year"]/option[9]',
            '2025':'//*[@id="credit_card_year"]/option[10]',
            '2026':'//*[@id="credit_card_year"]/option[11]',
            '2027':'//*[@id="credit_card_year"]/option[12]',
            '2028':'//*[@id="credit_card_year"]/option[13]'
            }

        driver.get(url)

        while True:
            try:
                driver.find_element_by_id("customer_name")
            except NoSuchElementException:
                driver.refresh()
                time.sleep(1)
            else:
                driver.execute_script("document.getElementById('customer_name').setAttribute('value', '" + active_profile['Name'] + "')")
                driver.execute_script("document.getElementById('customer_email').setAttribute('value', '" + active_profile['Email'] + "')")
                driver.execute_script("document.getElementById('customer_tel').setAttribute('value', '" + active_profile['Phone'] + "')")
                driver.find_element_by_xpath(dict[self.location]).click()
                driver.find_element_by_xpath('//*[@id="step_1_button"]').click()
                print (Fore.YELLOW + 'Filled out Page[1/2]...')
                break
            
        secondary_page = True
        while secondary_page:
            try:
                driver.execute_script("document.getElementById('customer_street').setAttribute('value', '" + active_profile['Billing Address'] + "')")
            except NoSuchElementException:
                time.sleep(1)
            else:
                driver.execute_script("document.getElementById('customer_zip').setAttribute('value', '" + active_profile['Zipcode'] + "')")
                driver.execute_script("document.getElementById('customer_city').setAttribute('value', '" + active_profile['City'] + "')")
                driver.find_element_by_xpath(states_dict[active_profile['State']]).click()
                driver.find_element_by_xpath('//*[@id="cn"]').send_keys(active_profile['Credit Card Number'])
                driver.find_element_by_xpath(credit_month[active_profile['Expiration Month']]).click()
                driver.find_element_by_xpath(credit_year[active_profile['Expiration Year']]).click()
                driver.find_element_by_xpath('//*[@id="credit_card_verification_value"]').send_keys(active_profile['Security Code'])
                print (Fore.YELLOW + 'Filled out Page[2/2]...')
                driver.find_element_by_css_selector('#submit_button').click()
                if 'problem' in driver.page_source:
                    print ('Error Submitting Details, Trying Again...')
                    pass
                else:
                    print (Fore.GREEN + 'Processing...')
                    secondary_page = False
                    break
                


def billing_profile_creation():
        print ('Billing Profile Creator')
        print (Fore.WHITE + '-------------------------------------------------------------')
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input ("Enter your address: ")
        phone = input ("Enter your phone number: ")
        zipcode = input("Enter you zipcode: ")
        city = input ("Enter your city: ")
        state = input("Enter your state: ")
        country = input("Enter your country: ")
        credit_card_number = input("Enter your card number: ")
        expiration_month = input("Enter card expiration month: ")
        expiration_year = input("Enter card expiration year: ")
        cvv = input("Enter CVV/Security Code: ")
        billing_profile = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Billing Address": address,
            "City": city,
            "Zipcode": zipcode,
            "State": state,
            "Country": country,
            "Credit Card Number": credit_card_number,
            "Expiration Month": expiration_month,
            "Expiration Year": expiration_year,
            "Security Code": cvv
            }
        ##### EDIT THE BILLING PROFILE FOLDER PATH HERE AS WELL ####
        save_path = 'C://Users//Head Chef Alin//Desktop//Supreme Sign-Up Script//billing profiles'
        print ('')
        file_name = input('Enter file name: ')
        completeName = os.path.join(save_path, file_name+'.json')
        with open(completeName, 'w') as f:     
            json.dump(billing_profile, f)
            print (Fore.GREEN + '')
            print ("Added "+ file_name +" to saved billing profiles!")
            f.close()        




def main_menu():
    print (Fore.WHITE + 'Welcome to BA3 Supreme Sign-Up Script V1.0')
    print ('Created By Washed Dev Alin')
    print ('-------------------------------------------------------------')
    print (Fore.WHITE + 'Main Menu')
    print ('Choose one of the following:')
    print ('-------------------------------------------------------------')
    start_up_truth = True
    while start_up_truth:
        print (Fore.WHITE + '>>>  Billing Profile Creation  <<< [1]')
        print ('>>>  Task Creator/Scheduler  <<< [2]')
        print ('>>>  Quit/Exit/Escape  <<< [3]')
        print ('-------------------------------------------------------------')
        decider = input('Choose an option: ')
        print (Fore.WHITE + '-------------------------------------------------------------')
        if decider == '1':
            billing_profile_creation()
        if decider == '2':
            raw_location = input('Enter Location: ')
            raw_billing_profile = input('Enter Billing Profile: ')
            raw_task_scheduler = input('Enter Scheduled Timer: ')
            task = Task_Info(raw_location, raw_billing_profile, raw_task_scheduler)
            task.sign_up()
        if decider == '3':
            print ('Thank you for using BA3 Supreme Sign-Up Script!')
            time.sleep(2)
            quit()

main_menu()



