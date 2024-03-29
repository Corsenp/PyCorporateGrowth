import sys
from selenium import webdriver
import matplotlib.pyplot as plt
import numpy as np
import time

def create_graph_profit(data):
    '''
    Create Graph Profit
    '''
    try:
        if data["date"] and data["name"] and data["profit"]:
            plt.subplot(2,1,2)
            plt.title("Profit of {} over time".format(data["name"]))
            plt.plot(data["date"], data["profit"])
            plt.grid(True)
            plt.xlabel("Date")
            plt.ylabel("Profit in %")
        else:
            sys.exit(1)
    except:
        print("Error while creating the profit graph")
        sys.exit(1)

def create_graph_revenue_growth(data):
    '''
    Create Graph Revenue Growth
    '''
    try:
        if data["date"] and data["revenue growth"] and data["name"]:
            plt.subplot(2,1,1)
            plt.title("Revenue Growth rate of : {}".format(data["name"]))
            plt.plot(data["date"][1:],data["revenue growth"])
            plt.grid(True)
            plt.xlabel("Date")
            plt.ylabel("Revenue Growth in %")
        else:
            sys.exit(1)
    except:
        print("Error while creating the revenue growth graph")
        sys.exit(1)

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
    '''
    Computing growth from @year_one to @year_two
    '''
    try:
        growth = (year_two - year_one) / year_one
        growth = growth * 100

    except:
        print("Error while computing growth")
        sys.exit(1)
    return(growth)

def compute_profit_margin(income, revenue):
    '''
    Computing profit margin with @income and @revenue
    '''
    try:
        profit = (income / revenue) * 100

    except:
        print("Error while computing profit margin")
        sys.exit(1)
    return profit

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
        "profit": [],
        "name": None
    }
    return data

def ask_for_tick():
    '''
    Ask the user to enter a corporation tick
    '''
    tick = input("Please enter the tick (Example : F):\n")

    return tick

def get_income(driver, data):
    '''
    Scrapping website with @driver and filling @data with the income
    '''
    try:
        i = 2
        while i < 7:
            income = driver.find_element_by_xpath("""//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/\
                       div[1]/div[2]/div[11]/div[1]/div[{}]""".format(i)).text
            income = income.replace(',', '')
            data["income"].append(int(income))
            i += 1
    except:
        pass

def get_date(driver, data):
    '''
    Scrapping website with @driver and filling @data with date
    '''
    try:
        i = 2
        while i < 7:
            date = driver.find_element_by_xpath("""//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/\
                        div[1]/div[1]/div/div[{}]""".format(i)).text
            data["date"].append(date)
            i += 1
    
    except:
        pass

def parse_revenue_data(data):
    '''
    Parsing list revenue of @data and filling revenu growth
    '''
    try:
        i = len(data["revenue"]) - 1
        while i > 0:
            growth = compute_growth(data["revenue"][i], data["revenue"][i - 1])
            growth = round(growth, 2)
            data["revenue growth"].append(float(growth))
            i -= 1

    except:
        print("error while parsing revenue data")
        sys.exit(1)

def parse_profit_data(data):
    '''
    Parsing list income and revenue of @data and filling profit
    '''
    try:
        i = len(data["revenue"]) - 1

        while i > -1:
            profit = compute_profit_margin(data["income"][i], data["revenue"][i])
            profit = round(profit, 2)
            data["profit"].append(float(profit))
            i -= 1
    except:
        print("Error while parsing profit")
        sys.exit(1)

def get_revenue(driver, data):
    '''
    Scrapping website with @driver and filling @data with revenue
    '''
    try:
        i = 2
        while i < 7:
            revenue = driver.find_element_by_xpath("""//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[{}]""".format(i)).text
            revenue = revenue.replace(',', '')
            data["revenue"].append(int(revenue))
            i += 1
    except:
        pass

def get_company_name(driver, data):
    '''
    Scrapping website with @driver and filling @data with name
    '''
    try:
        company_name = driver.find_element_by_xpath("""//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1""").text
        data["name"] = company_name
    except:
        print("No company name was found")

def fill_dictionnary(driver, data):
    '''
    Scrape all data needed with @driver and filling @data with it
    '''
    try:
        get_company_name(driver, data)
        get_revenue(driver, data)
        get_date(driver, data)
        get_income(driver, data)
        parse_revenue_data(data)
        parse_profit_data(data)
        data["date"].reverse()
    
    except:
        print("Error while filling data")
        sys.exit(1)

def setting_up_graphs(data):
    '''
    Setting up the graphs with @data before displaying it
    '''
    try:
        create_graph_revenue_growth(data)
        create_graph_profit(data)
        plt.tight_layout()
        plt.show()
    
    except:
        print("Error while creating graphs")
        sys.exit(1)

def main():
    '''
    Main function
    '''
    tick = ask_for_tick()
    driver = init_driver()
    url = 'https://finance.yahoo.com/quote/' + tick + '/financials?p=' + tick
    driver = open_url(driver, url)
    data = init_dictionnary()
    fill_dictionnary(driver, data)
    setting_up_graphs(data)
    driver.quit()

main()
