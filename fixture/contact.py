from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # init edit contact
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # update contact
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.name)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("email", contact.email)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wait = WebDriverWait(wd, 0.5)
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wait.until((ec.text_to_be_present_in_element
                    ((By.CLASS_NAME, "msgbox"), "Record successful deleted")))
        self.open_home_page()
        self.contact_cache = None

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        wd.find_element(By.NAME, "new_group").click()
        wd.find_element(By.XPATH, "//option[@value='[none]']").click()
        # submit contact creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php")):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements(By.NAME, "searchstring")) == 1:
            wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                id = int(element.find_element(By.TAG_NAME, "input").get_attribute("value"))
                lastname = element.find_element(By.XPATH, "./td[2]").text
                name = element.find_element(By.XPATH, "./td[3]").text
                self.contact_cache.append(Contact(id=id, name=name, lastname=lastname))
        return list(self.contact_cache)
