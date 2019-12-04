import sys
from selenium import webdriver
import time

def open_url(driver, url):
    '''
    Open a Specific @url with Selenium @driver
    '''
    try:
        driver.get(url)
    except:
        print("driver.quit()")
        driver.quit()
    return driver

def compute_growth(year_one, year_two):
    growth = (year_two - year_one) / year_one
    growth = growth * 100
    return(growth)

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

def init_dictionnary():
    '''
    Initializing the data dictionnary
    '''
    data = {
        "revenue": [],
        "income": [],
        "date": [],
        "revenue growth": [],
        "name": None
    }
    return data

def ask_for_tick():
    tick = input("Please enter the tick (Example : F):\n")

    return tick

def get_income(driver, data):
    try:
        i = 2
        while i < 7:
            income = driver.find_element_by_xpath("""//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/\
                       div[1]/div[2]/div[11]/div[1]/div[{}]""".format(i)).text
            data["income"].append(income.replace(',', ''))
            i += 1
    except:
        print("no more income to scrap")

def get_date(driver, data):
    try:
        i = 2
        while i < 7:
            date = driver.find_element_by_xpath("""//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/\
                        div[1]/div[1]/div/div[{}]""".format(i)).text
            data["date"].append(date)
            i += 1
    
    except:
        print("No more date to scrap, end at", i)

def parse_revenue_data(data):
    try:
        i = len(data["revenue"]) - 1
        while i > 0:
            growth = compute_growth(int(data["revenue"][i]), int(data["revenue"][i - 1]))
            growth = round(growth, 2)
            data["revenue growth"].append(float(growth))
            i -= 1

    except:
        print("error while parsing revenue data")
        sys.exit(1)

def get_revenue(driver, data):
    try:
        i = 2
        while i < 7:
            revenue = driver.find_element_by_xpath("""//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[{}]""".format(i)).text
            data["revenue"].append(revenue.replace(',', ''))
            i += 1
    except:
        print("no more revenue to scrap, end at", i)

def get_company_name(driver, data):
    try:
        company_name = driver.find_element_by_xpath("""//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1""").text
        data["name"] = company_name
    except:
        print("No company name was found")

def main():
    '''
    Main function
    '''
    tick = ask_for_tick()
    driver = init_driver()
    url = 'https://finance.yahoo.com/quote/' + tick + '/financials?p=' + tick
    driver = open_url(driver, url)
    data = init_dictionnary()
    get_company_name(driver, data)
    get_revenue(driver, data)
    get_date(driver, data)
    get_income(driver, data)
    parse_revenue_data(data)
    driver.quit()
    print(data)
    print("Tick : %s" % tick)

main()
