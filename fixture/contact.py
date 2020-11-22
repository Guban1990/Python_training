from model.group import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home(self):
        # return to home page
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.add_new_contact_page()
        # fill contact firm
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_home()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # open for editing
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact
        self.fill_contact_form(contact)
        # submit update
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.return_to_home()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def add_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.add_new_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_home()
        contacts = []
        for element in wd.find_elements_by_xpath(".//tr[@name='entry']"):
            # element in wd.find_elements_by_name("entry"):
            # element in wd.find_elements_by_css_selector("td.center"):
            lastname = element.find_element_by_xpath(".//td[2]").text
            firstname = element.find_element_by_xpath(".//td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts
