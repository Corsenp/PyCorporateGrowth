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

def main():
    '''
    Main function
    '''
    driver = init_driver()

    url = "https://www.google.fr"
    open_url(driver, url)
    print("Corporate Growth")

main()
