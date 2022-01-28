# Daraz Scaper App 
- [Python](#)
- [Selenium](#)
- [Chromedriver](#)
- [Flask](#)

## Chromedriver:
ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. It is maintained by the Chromium team with help from WebDriver contributors. If you are unfamiliar with Selenium WebDriver, you should check out the [Selenium site](https://www.selenium.dev/).

### Sample test:
```
import time

from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()

```

## Get Start:
- Create new virtual enviroment and install dependencies
- Install requirements.txt using RUN : `pip3 install -r requirements.tx`
- And RUN `python app.py`
- Now your app is running on : [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## You can go with this [link](http://127.0.0.1:5000/) and open app like this
<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/Br0rGk6/Screenshot-from-2022-01-28-22-53-55.png" height="175px"/></a>
- In this URl means which link you want scraping from daraz websites.
- And file name is you csv file name.
  
#### Here is the Examples:
- `https://www.daraz.com.np/womens-shoes/`
- `https://www.daraz.com.np/smartphones/`
- `https://www.daraz.com.np/mens-sports/`

### Background Process:
- This app using selenium chromedrive so this app auto start your chrome browser.like this
<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/VBXLp6t/Screenshot-from-2022-01-28-22-58-38.png" height="175px"/></a>
- And scraping data from website and write into CSV format.
<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/HDDS93v/Screenshot-from-2022-01-28-22-52-10.png" height="175px"/></a>

## Result:
- Now you have clean csv format of scraped data from your link and download on your local.
<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/98k29wb/Screenshot-from-2022-01-28-22-54-23.png" height="175px"/></a>
  
  