from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import random
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/cadastrar")
fake = Faker('pt_BR')



for i in range(5):

    campo_nome = driver.find_element(By.NAME, "nome_cliente")
    campo_cargo = driver.find_element(By.NAME, "cargo_cliente")
    campo_email = driver.find_element(By.NAME, "email_cliente")
    campo_cpf = driver.find_element(By.NAME, "cpf_cliente")
    campo_salario = driver.find_element(By.NAME, "salario_cliente")
    campo_submit= driver.find_element(By.NAME, "btn_cadastrar")

    nome = fake.name()
    cargo = fake.job()
    email = fake.email()
    cpf = fake.cpf().replace(".", "").replace("-", "")
    salario = round(random.uniform(1300,20000),2)

    campo_nome.send_keys(nome)
    campo_cargo.send_keys(cargo)
    campo_email.send_keys(email)
    campo_cpf.send_keys(cpf)
    campo_salario.send_keys(str(salario))

    campo_submit.click()

    time.sleep(1)

driver.quit()