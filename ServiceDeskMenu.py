import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

def get_menu_choice():
    def print_menu():       # Your menu is right here :)
        print(30 * "-", "DD Service Desk automation MENU", 30 * "-")
        print("1. Login to Prosus OKTA ")
        print("2. Login to PayU  OKTA ")
        print("3. Check the weather ")
        print("4. Check Covid stats")        
        print("5. Exit from the script ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            int_choice = 1
            ADMaccount = input('Enter your Prosus Okta username:  ')
            time.sleep(4)
            password = input('Enter your Prosus Okta adm password ')


            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get('https://okta.prosus.com/')
        
            ###login to Prosus OKTA
            searchButton = driver.find_element_by_xpath('//*[@id="okta-signin-username"]')
            searchButton.send_keys(ADMaccount)
            passW = driver.find_element_by_xpath('//*[@id="okta-signin-password"]').send_keys(password)
            clicklogin = driver.find_element_by_xpath('//*[@id="okta-signin-submit"]').click()

            time.sleep(3)

            last= input("Do you still want to use Prosus OKTA? Y/N")

            if last=="Yes":
                print("Okay nice")

            else:
                driver.close()
                print(get_menu_choice())

            ##loop = False
        elif choice == '2':
            int_choice = 2
            ADMaccount = input('Enter your PayU Okta username:  ')
            time.sleep(4)
            password = input('Enter your PayU Okta adm password ')


            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get('https://payu.okta-emea.com/')
        
            ###login to Payu OKTA
            searchButton = driver.find_element_by_xpath('//*[@id="okta-signin-username"]')
            searchButton.send_keys(ADMaccount)
            passW = driver.find_element_by_xpath('//*[@id="okta-signin-password"]').send_keys(password)
            clicklogin = driver.find_element_by_xpath('//*[@id="okta-signin-submit"]').click()

            time.sleep(3)

            last= input("Do you still want to use PayU OKTA? Y/N")

            if last=="Yes":
                print("Okay nice")

            else:
                driver.close()
                print(get_menu_choice())

            ##loop = False
        elif choice == '3':
             int_choice = 3
             
             driver = webdriver.Chrome()
             driver.maximize_window()
             driver.get('https://www.google.com/')
        
            ###login to OKTA
             inputElems = driver.find_elements_by_css_selector('input[name=q]')
             for inputElems in inputElems:

                 inputElems.send_keys('weather')
                 inputElems.send_keys(Keys.ENTER)


             time.sleep(10)
             driver.close()
             print(get_menu_choice())



            ##loop = False
        elif choice == '4':
            int_choice = 4
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get('https://coronavirus.westerncape.gov.za/covid-19-dashboard')        
            time.sleep(30)
            driver.close()
            print(get_menu_choice())
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            loop = False  # This will make the while loop to end
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]


print(get_menu_choice())

exit()

## if you are erading this code then you should now realise the challange is on and that you might not win.GOODLUCK!
