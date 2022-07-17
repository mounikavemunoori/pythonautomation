from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Tutorial_Locators(object):
    firstName='firstname'
    lastname='lastname'
    maleRadioButton = "//input[@value='Male']"
    femaleRadioButton = "//input[@value='Female']"
    submitButton = "submit"
    continents="[name='continents']"
    seleniumCommands = "selenium_commands",
    button='[name="submit"]'

class TestData(object):
    chrome_driver_path='/home/mvemunoori/Desktop/python_training/drivers/chromedriver'
    target_url='https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm'


class Test_Tutorials_point(object):
    def test_browser_open(self):
        driver= webdriver.Chrome("/home/mvemunoori/Desktop/python_training/drivers/chromedriver")
        driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
        print("\n"+driver.current_url)
        print("\n"+driver.page_source)
        assert "Selenium - Automation Practice Form" == driver.title
        assert "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm" == driver.current_url
        driver.quit()

    def create_dynamic_element(self, value):
        return "//input[@name='exp' and @value='"+ str(value) +"']"

    def test_enter_text(self):
        driver=webdriver.Chrome(TestData.chrome_driver_path)
        driver.get(TestData.target_url)
        driver.maximize_window()

        driver.find_element('name', Tutorial_Locators.firstName).clear()
        driver.find_element('name', Tutorial_Locators.firstName).send_keys('Mounika')

        driver.find_element('name', Tutorial_Locators.lastname).clear()
        driver.find_element('name', Tutorial_Locators.lastname).send_keys('Vemunoori')
    #
        driver.implicitly_wait(20)
        print("TEXT_____________________>", driver.find_element('name', Tutorial_Locators.firstName).get_attribute('value'))

        femaleRadioButton = driver.find_element(By.XPATH, Tutorial_Locators.femaleRadioButton)
        driver.execute_script("arguments[0].scrollIntoView();", femaleRadioButton)
        if femaleRadioButton.is_selected() != True:
            driver.execute_script("arguments[0].click();", femaleRadioButton)
        assert femaleRadioButton.is_selected() == True
        driver.quit()

    def test_take_screenshots(self):
        driver=webdriver.Chrome(TestData.chrome_driver_path)
        driver.get(TestData.target_url)
        driver.maximize_window()
        time.sleep(20)
        driver.get_screenshot_as_png()

    def test_years_of_exp(self):
        value=2
        driver=webdriver.Chrome(TestData.chrome_driver_path)
        driver.get(TestData.target_url)
        driver.maximize_window()
        time.sleep(5)
        yr_exp=self.create_dynamic_element(value)
        print(yr_exp)

        yr_exp_element=driver.find_element(By.XPATH, yr_exp)
        driver.execute_script("arguments[0].scrollIntoView();", yr_exp_element)
        driver.execute_script("arguments[0].click();", yr_exp_element)
        time.sleep(10)
        print(yr_exp_element.is_selected())


    def test_drop_down_menu(self):
        driver=webdriver.Chrome(TestData.chrome_driver_path)
        driver.get(TestData.target_url)
        driver.maximize_window()
        femaleRadioButton = driver.find_element(By.XPATH, Tutorial_Locators.femaleRadioButton)
        driver.execute_script("arguments[0].scrollIntoView();", femaleRadioButton)
        print("----->",femaleRadioButton.get_attribute('value'))
        print("--->", femaleRadioButton.get_property('class'))
        select_obj = Select(driver.find_element(By.CSS_SELECTOR, Tutorial_Locators.continents))
        print(dir(select_obj))
        select_obj.select_by_index(1)
        select_obj.select_by_visible_text('Asia')
        for ele in select_obj.options:
            print("element name-->", ele.text)

        print(select_obj)
        print("elements--->", Tutorial_Locators.continents+" "+"option")
        options_web=driver.find_elements(By.CSS_SELECTOR, Tutorial_Locators.continents+" "+"option")
        for opt in options_web:
            print(opt.text)

    def test_multiwindow(self):
        driver=webdriver.Chrome(TestData.chrome_driver_path)
        driver.get(TestData.target_url)
        driver.maximize_window()
        select_obj=Select(driver.find_element(By.NAME, Tutorial_Locators.seleniumCommands))
        select_obj.select_by_visible_text('Wait Commands')
        time.sleep(10)
        parentWindow=driver.current_window_handle
        driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, Tutorial_Locators.button))
        ale=Alert(driver)
        ale.accept()
        time.sleep(20)
        allwindows=driver.window_handles
        for window in allwindows:
            driver.switch_to.window(window)
            print(driver.current_url)
            if  "selenium_commands" in driver.current_url:
                print("yessss-->")
                driver.close()


    #     driver.switch_to.window(parentWindow)
    #     print(driver.current_url)
    #     driver.quit()

    def test_waits_in_selenium(self):
        driver=webdriver.Chrome(TestData.chrome_driver_path)
        driver.get(TestData.target_url)
        driver.maximize_window()
        select_obj = Select(driver.find_element(By.NAME, Tutorial_Locators.seleniumCommands))
        select_obj.select_by_visible_text('Wait Commands')
        time.sleep(10)
        parentWindow = driver.current_window_handle
        wait = WebDriverWait(driver, 100)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Tutorial_Locators.button)))
        driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, Tutorial_Locators.button))
        time.sleep(20)
        ale=Alert(driver)
        wait.until(EC.alert_is_present())
        ale.accept()

    # def test_move_to_element(self):
    #     print("move to element")
    #     driver = webdriver.Chrome(TestData.chrome_driver_path)
    #     driver.get(TestData.target_url)
    #     driver.maximize_window()
    #     driver.find_element('name', Tutorial_Locators.firstName).send_keys('mounika reddy')
    #     wait = WebDriverWait(driver, 300)
    #     act = ActionChains(driver)
    #     act.send_keys(Keys.TAB).perform()
    #     driver.find_element('name', Tutorial_Locators.lastname).send_keys('vemunoori')
    #     time.sleep(25)
    #     act.key_down(Keys.CONTROL).send_keys('a').perform()
    #     time.sleep(25)

    def test_mouse_operations(self):
        driver=webdriver.Chrome(TestData.chrome_driver_path)
        driver.get(TestData.target_url)
        driver.maximize_window()
        time.sleep(30)
        act=ActionChains(driver)
        act.click().perform()
        act.context_click().perform()
        act.drag_and_drop()


    def test_exceptions_code(self):
        from selenium.common.exceptions import *









