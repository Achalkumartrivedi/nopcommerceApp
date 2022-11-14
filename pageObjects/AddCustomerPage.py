from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


class AddCustomer:
    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"

    #Add New Cutomer form fields
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath = "//input[@id='FirstName']"
    txtLastname_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chk_Istax_cssSelector = "#IsTaxExempt" #checkmarked

    lst_Newsletter = "//div[@class='input-group-append']//div[@role='listbox']"
    lst1_yourstorename_xpath ="//li[@id='b5e52cdf-a81e-4832-9ab6-8e6854c00bee']"

    txt_CustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']" #it is listbox ,not dropdown
    lst_Registered_xpath = "//span[normalize-space()='Registered']"
    lst_Administrator_xpath = "//li[normalize-space()='Administrators']"
    lst_ForumMode_xpath = "//li[normalize - space() = 'Forum Moderators']"
    lst_Guest_xpath = "//li[normalize-space()='Guests']"
    lst_Vendors_xpath = "//li[contains(text(),'Vendors')]"

    drp_ManagerVendor_xpath = "//select[@id='VendorId']"
    chk_Active_cssSelector = "#Active"
    txtarea_Admincontent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnCustomersSubMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
            self.driver.find_element(By.XPATH, self.txtPassword_xpath).clear()
            self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtFirstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFirstname_xpath).send_keys(firstname)

    def setLastame(self, lastname):
        self.driver.find_element(By.XPATH, self.txtLastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLastname_xpath).send_keys(lastname)

    def clickOnGender(self,gender):
        if gender == 'Male':
           self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()

    def clickOnFemaleGender(self):
        self.driver.find_element(By.ID, self.rdFemaleGender_id).click()

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyname(self,company):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(company)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH,self.txt_CustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH,self.lst_Registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.lst_Administrator_xpath)
        elif role == 'Guests':
            # Here user can be Registered or Geust, only one
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lst_Guest_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Registered_xpath)
        elif role == 'vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lst_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lst_Guest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVender(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drp_ManagerVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdmincomment(self,comment):
        self.driver.find_element(By.XPATH,self.txtarea_Admincontent_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtarea_Admincontent_xpath).send_keys(comment)

    def clickOnSavebtn(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()