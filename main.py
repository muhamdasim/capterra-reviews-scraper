from selenium import webdriver
import  time
driver = webdriver.Chrome()

print("Loading Website......")
driver.get('https://www.capterra.com/p/76390/Infusionsoft/')
driver.maximize_window()
time.sleep(10)
print("Website Loaded")