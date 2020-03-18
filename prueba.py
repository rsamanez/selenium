# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from random import seed
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSurvey1():
  surveys = [
    '2-second-cool-title',
    '7-demo-test',
    '1-cool-title',
    '3-new-record-using-relationships',
    '4-animales-que-te-gustan',
    '5-muy-buena-relacion-laboral-con-los-companeros-de-trabajo',
    '6-cool-title'
  ]
  def setup_method(self):
    self.driver = webdriver.Chrome(executable_path=r"./chromedriver")
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_survey1(self):
    # Test name: survey1
    # Step # | name | target | value | comment
    # 1 | open | http://demos.rsamanez.com/questionnaire-survey/surveys/2-second-cool-title |  |

    survey = randint(0,6)
    self.driver.get("http://demos.rsamanez.com/questionnaire-survey/surveys/" + self.surveys[survey])
    # 2 | setWindowSize | 1470x830 |  |
    self.driver.set_window_size(1470, 830)
    item1 = randint(1, 4)
    item2 = randint(1, 4)
    item3 = randint(1, 4)
    item4 = randint(1, 4)

    # 3 | click | css=.card:nth-child(2) label:nth-child(1) > .list-group-item |  |
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) label:nth-child(" + str(item1) + ") > .list-group-item").click()
    # 4 | click | css=.card:nth-child(3) label:nth-child(2) > .list-group-item |  |
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) label:nth-child(" + str(item2) + ") > .list-group-item").click()
    # 5 | click | css=.card:nth-child(4) label:nth-child(3) > .list-group-item |  |
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(4) label:nth-child(" + str(item3) + ") > .list-group-item").click()
    # 6 | click | css=.card:nth-child(5) label:nth-child(4) > .list-group-item |  |
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(5) label:nth-child(" + str(item4) + ") > .list-group-item").click()
    # 4 | click | id=name |  |
    self.driver.find_element(By.ID, "name").click()
    # 5 | type | id=name | Selenium Tester |
    self.driver.find_element(By.ID, "name").send_keys("Selenium Tester")
    # 6 | click | id=email |  |
    self.driver.find_element(By.ID, "email").click()
    # 7 | type | id=email | selenium@test.com |
    self.driver.find_element(By.ID, "email").send_keys("selenium@test.com")
    # 8 | click | css=.btn |  |
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()


seed(datetime.now())
my_delay = randint(0,60)
print( str(my_delay) + "\n")
if my_delay < 56 :
  time.sleep(my_delay)
  test1 = TestSurvey1()
  test1.setup_method()
  test1.test_survey1()
  time.sleep(1)
  test1.teardown_method()
