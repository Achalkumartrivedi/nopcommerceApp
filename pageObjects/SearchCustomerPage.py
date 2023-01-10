from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.customeLogger import LogGenclass

class SearchCustomer:
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstname_id = "SearchFirstName"
    txtLastname_id = "SearchLastName"
    btnSearch_id = "search-customers"

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRow_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_cpath = "//table[@id='customers-grid']//tbody/tr/td"

    logger = LogGenclass.loggenmethod()  # call loggenmethod of LEggenClass

    def __init__(self, driver):
       self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstname_id).clear()
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastname_id).clear()
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoofRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRow_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumn_cpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoofRows()+1):
            self.logger.info("***** POM > Start function - searchCustomerByEmail() *****")
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            if table == email:
              self.logger.info("***** POM > Element is found in table and stored in 'table' *****")
              print(table)
              emailid = table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text #second column
              self.logger.info("***** POM > Elememt is found in second column and store in 'emailid' *****")
              if emailid == email:
                 flag = True
                 self.logger.info("***** POM > Found email is equal to the entered ..Return 'True' Flag *****")
                 break
            else:
                flag = False
                self.logger.info("***** POM > Entered email is not found in table ..Return 'False' Flag *****")
        return flag

    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoofRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text #Third column
            if name == Name:
                flag = True
                break
        return flag
