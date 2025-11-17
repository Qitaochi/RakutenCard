from get_chrome_driver import GetChromeDriver
from selenium import webdriver


def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)


get_driver = GetChromeDriver()
get_driver.install()
driver = driver_init()
driver.get("https://www.example.com")
print(driver.title)
print(driver.current_url)
driver.quit()
