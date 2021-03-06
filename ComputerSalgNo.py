import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import winsound

print("This program comes with ABSOLUTELY NO WARRANTY; for details check included license. This is free software, and you are welcome to redistribute it under certain conditions; check license for conditions.")

item = 'https://www.computersalg.no/i/8031925/sony-playstation-5-blu-ray-825gb-disk-edition?utm_source=prisjaktNo&utm_medium=prisjaktNoLINK&utm_campaign=prisjaktNo' # Variable for the item wanted
options = Options()
options.add_argument("user-data-dir=C:\\Users\\ps5\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(item)
while True:
    try:
        # Code with possible error - error being that there's no add to cart button
        driver.find_element_by_xpath('//*[@id="pecr-cookie-banner-wrapper"]/div/div[1]/div/div[2]/button[1]').click() # checks for anything interupting the the atb such as "accept cookies or manage cookies" and gets rid of it to stop interuptions
        driver.find_element_by_xpath('//*[@id="button--add-to-basket"]').click() # Looks for the 'add to cart button' using xpath
    except:
        driver.get(item) # If the atc button cannot be found, refresh until it is found
    else:
        time.sleep(1)
        driver.get('https://www.computersalg.no/checkout/basket?viewsource=') # Goes to checkout page after adding to cart
        break
winsound.Beep(899, 5000) # Makes a beep sound for 5 seconds to notify the user that the item is in stock and at checkout page
