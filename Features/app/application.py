from pages.base_page import Page
from pages.sign_in_page import Page
from pages.verify_page import Page

# place all pages you will be using above as well as in the class Application
class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
    
    def __init__(self, driver):
        self.sign_in_page.Page(driver)

    def __init__(self, driver):
        self.verify_page.page(driver)

#steps

# create am app, features, and page folder
# in app folder create application.py file
#