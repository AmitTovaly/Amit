from selenium import webdriver

__author___ = 'Amit_Tovaly'

def test_setup():
    try: #comment
        driver= webdriver.Chrome(executable_path="C:/Users/Udi/PycharmProjects/caltory/SeleniumScripts/chromedriver.exe")
        driver.set_page_load_timeout(30)
        driver.maximize_window()
        driver.get("http://www.google.com")
        query = driver.find_element_by_name("q")
        query.send_keys("Claroty")
        query.submit()
        x = driver.find_element_by_id("resultStats")
        print(x.text)
    except:
        print("Problem")

    try: #comment
        y = driver.find_element_by_class_name("iUh30")
        print(y.text)
        if y.text == "https://www.claroty.com/":
            print("Claroty.com is the first")
        else:
            print("Claroty.com is not the first")
    except:
        print("Problem")

    try: #comment
        clickme=driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[2]/div/div/div[1]/a[1]/div/cite/span')
        #print(clickme.text)
        if clickme.text != "https://www.claroty.com/careers":
            driver.close()
            driver = webdriver.Chrome(
                executable_path="C:/Users/Udi/PycharmProjects/caltory/SeleniumScripts/chromedriver.exe")
            driver.set_page_load_timeout(30)
            driver.maximize_window()
            driver.get("https://www.claroty.com/careers")
        else:
            clickme.click()
        z = driver.find_elements_by_tag_name("h1")
        counter = len(z)
        number = 0
        for i in range(0, counter):
            #print(str(i) +" "+ z[i].text)
            if z[i].text != "" and z[i].text != "Working At Claroty":
                number = number + 1
        print("the numbers of careers : " + str(number))
        print("Test Completed")
        driver.close()
    except:
        print("Problem")
        print("Test Wasn't Completed")
        driver.close()

def main():
    test_setup()

if __name__ == '__main__':
    main()


















