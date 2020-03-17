from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"./chromedriver")


driver.get("http://demos.rsamanez.com/questionnaire-survey/login")
user = driver.find_element_by_id("email")
user.send_keys("rsamanez@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("12345678")
password.send_keys(Keys.ENTER)
#time.sleep(3)
create_questionnaire = driver.find_element_by_link_text("Create New Questionnaire")
create_questionnaire.click()
title = driver.find_element_by_id("title")
purpose = driver.find_element_by_id("purpose")
title.send_keys("Cuestionario Personal")
purpose.send_keys("este es un cuestionario para validar una automatizacion")
purpose.send_keys(Keys.ENTER)
add_new_question = driver.find_element_by_link_text("Add new Question")
add_new_question.click()

question = driver.find_element_by_id("question")
question.send_keys("Cual es tu color favorito")
answer1 = driver.find_element_by_id("answer1")
answer1.send_keys("Verde")
answer2 = driver.find_element_by_id("answer2")
answer2.send_keys("Amarillo")
answer3 = driver.find_element_by_id("answer3")
answer3.send_keys("Azul")
answer4 = driver.find_element_by_id("answer4")
answer4.send_keys("Rojo")
answer1.send_keys(Keys.ENTER)

add_new_question = driver.find_element_by_link_text("Add new Question")
add_new_question.click()

question = driver.find_element_by_id("question")
question.send_keys("Cual es tu nombre favorito")
answer1 = driver.find_element_by_id("answer1")
answer1.send_keys("Armando")
answer2 = driver.find_element_by_id("answer2")
answer2.send_keys("Juan")
answer3 = driver.find_element_by_id("answer3")
answer3.send_keys("Pedro")
answer4 = driver.find_element_by_id("answer4")
answer4.send_keys("Raul")
answer1.send_keys(Keys.ENTER)

add_new_question = driver.find_element_by_link_text("Add new Question")
add_new_question.click()

question = driver.find_element_by_id("question")
question.send_keys("En que ranfo de edar estas?")
answer1 = driver.find_element_by_id("answer1")
answer1.send_keys("45 - Mas")
answer2 = driver.find_element_by_id("answer2")
answer2.send_keys("35 - 44")
answer3 = driver.find_element_by_id("answer3")
answer3.send_keys("25 - 34")
answer4 = driver.find_element_by_id("answer4")
answer4.send_keys("15 - 24")
answer1.send_keys(Keys.ENTER)

add_new_question = driver.find_element_by_link_text("Take Survey")
add_new_question.click()

formElement = driver.find_element_by_tag_name("form")

allFormChildElements = formElement.find_elements(by_xpath("*"))
for item in allFormChildElements:
    if item.get_tag_name() =="input":
        if item.get_attribute("radio"):
            item.click()
    time.sleep(3)