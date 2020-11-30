from selenium import webdriver
import time

try: 
    # link without Error http://suninjuly.github.io/registration1.html
    link = "http://suninjuly.github.io/registration2.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("div.first_block>div.form-group.first_class>input") #xpath //div[1]/div[1]/input
    input1.send_keys("Vadym")
    input2 = browser.find_element_by_css_selector("div.first_block>div.form-group.second_class>input") #xpath //div[1]/div[2]/input
    input2.send_keys("2")
    input3 = browser.find_element_by_css_selector("div.first_block>div.form-group.third_class>input") #xpath  //div[1]/div[3]/input
    input3.send_keys("3")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    #########