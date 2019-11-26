import sys
from selenium import webdriver

def open_url(driver, url):
    '''
    Open a Specific @url with Selenium @driver
    '''
    try:
        driver.get(url)
    except:
        print("ERROR")
        driver.quit()

def init_driver():
    '''
    Initiate the Selenium Web Driver
    '''
    try:
        driver = webdriver.Chrome(executable_path=".//chromedriver")
        return driver
    except:
        print("chromedriver not found, please place it on the root of the project's folder")
        sys.exit(1)

def ask_for_tick():
    tick = input("Please enter the tick (Example : APPL):\n")

    return tick

def main():
    '''
    Main function
    '''
    driver = init_driver()

    
    
    tick = ask_for_tick()
    url = "https://finance.yahoo.com/quote/" + tick
    open_url(driver, url)
    print("Tick : %s" % tick)

main()
