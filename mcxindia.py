from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
class IMARC:
    def __init__(self):
        options = Options()
#         options.add_argument("headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(" https://www.mcxindia.com/market-data/spot-market-price/")
        Archive_button = self.driver.find_element("xpath",'//*[@id="form1"]/div[3]/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]').click()
        self.driver.implicitly_wait(2)

    def send_data(self):
        Select_button = self.driver.find_element("xpath",'//*[@id="ctl00_cph_InnerContainerRight_C004_ddlSymbols_Arrow"]').click()
        Select_gold = self.driver.find_element("xpath",'//*[@id="ctl00_cph_InnerContainerRight_C004_ddlSymbols_DropDown"]/div/ul/li[18]').click()
        Select_session = self.driver.find_element("xpath",'//*[@id="cph_InnerContainerRight_C004_ddlSession"]/option[3]').click()
        click_start=self.driver.find_element("xpath",'//*[@id="txtFromDate"]')
        time.sleep(2)

    def send_start_date(self): 
        start_date="01/11/2023"
        find_from_text = self.driver.find_element("xpath",'//*[@id="txtFromDate"]')
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", find_from_text)
        text_box = self.driver.find_element(By.ID,"txtFromDate")
        text_box.send_keys(start_date)
        click_date = self.driver.find_element("xpath","/html/body/div[3]/div/div[2]/div/table/tbody/tr[1]/td[4]/a").click()
        time.sleep(2)

    def send_end_date(self):
        click_on=self.driver.find_element("xpath",'//*[@id="txtToDate"]')
        end_date="24/1/2024"
        find_from_text = self.driver.find_element("xpath",'//*[@id="txtToDate"]')
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", find_from_text)
        text_box = self.driver.find_element(By.ID,"txtToDate")
        text_box.send_keys(end_date)
        click_date = self.driver.find_element("xpath","/html/body/div[3]/div/div[2]/div/table/tbody/tr[4]/td[4]/a").click()
        time.sleep(2)
        show_button=self.driver.find_element("xpath",'//*[@id="btnShowArchive"]').click()

    def get_table_Data(self):
        click_button_csv=self.driver.find_element('xpath','//*[@id="cph_InnerContainerRight_C004_lnkExportToExcel"]').click()
    
obj=IMARC()
obj.send_data()
obj.send_start_date()
obj.send_end_date()
obj.get_table_Data()

    
def Excel_read():
    global data_Fram
    table=pd.read_csv("c:/Users/SpotMarket_20240627132159.xls")
    data_Fram=pd.DataFrame(table)
    time.sleep(2)

def Total_rows_data():
    total_rows = data_Fram.shape[0]
    print("Total number of rows : ",total_rows)
    time.sleep(2)
        
def Highest_price():
    max_price_date = data_Fram.loc[data_Fram['Price(Rs.)'].idxmax(), 'Date']
    print("Date with highest Spot Price: ", max_price_date)
    time.sleep(2)
        
def new_excel():
    output_file = 'Final.xlsx'
    with pd.ExcelWriter(output_file) as writer:
        data_Fram.to_excel(writer, sheet_name='Raw Data', index=False)
    
Excel_read()
Total_rows_data()
Highest_price()
new_excel()
