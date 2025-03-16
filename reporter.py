import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# The following code is a simple implementation of the Page Transactions pattern
# Works on Python 3.11+
from guara.abstract_transaction import AbstractTransaction

# Load configuration
config = open("config.json", "r")
data = json.load(config)


# Concrete Transactions
class AcceptCookies(AbstractTransaction):
    def do(self, **kwargs):
        cookies = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]",
                )
            )
        )
        cookies.click()


class Login(AbstractTransaction):
    def do(self, username, password, **kwargs):
        username_field = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input",
                )
            )
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input",
                )
            )
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button",
                )
            )
        )
        login_button.click()


class SaveLoginInfo(AbstractTransaction):
    def do(self, **kwargs):
        save_button = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button",
                )
            )
        )
        save_button.click()


class ReportUser(AbstractTransaction):
    def do(self, **kwargs):
        more_button = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[1]/div/button",
                )
            )
        )
        more_button.click()

        report_button = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[3]",
                )
            )
        )
        report_button.click()

        report_acc_button = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]",
                )
            )
        )
        report_acc_button.click()

        second_option = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[2]/div/div[1]",
                )
            )
        )
        second_option.click()

        me_option = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/fieldset/div[1]/label",
                )
            )
        )
        me_option.click()

        submit_button = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[6]/button",
                )
            )
        )
        submit_button.click()

        close_button = WebDriverWait(self._driver, 100).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]",
                )
            )
        )
        close_button.click()


# Application Class (Orchestrator)
class Application:
    def __init__(self, driver):
        self._driver = driver

    def at(self, transaction_class, *args, **kwargs):
        transaction = transaction_class(self._driver)
        return transaction.do(*args, **kwargs)


# Main Script
if __name__ == "__main__":
    os.system("cls & title Instagram Reporter")

    # Set up Selenium WebDriver
    options = Options()
    options.page_load_strategy = "eager"
    options.headless = False
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=OFF")
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options)
    driver.get(
        f'https://www.instagram.com/accounts/login/?next=%2F{input("Username > ")}%2F&source=desktop_nav'
    )

    # Initialize Application
    app = Application(driver)

    # Perform actions using the Page Transactions pattern
    app.at(AcceptCookies)
    app.at(Login, data["username"], data["password"])
    app.at(SaveLoginInfo)

    # Report user in a loop
    while True:
        app.at(ReportUser)
