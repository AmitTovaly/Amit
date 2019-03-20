#This method open google.com with selenium and serch for claroty then Print to console the results number and Make sure that claroty.com is the first result's link and then  Go to https://www.claroty.com/careers and Print console number of carriers 



from selenium import webdriver

__author___ = 'Amit_Tovaly'

def test_setup():
    try: # This function open Chrome with selenium to google.com serch for claroty and print the result number 
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

    try: #comment this function check if claroty is the first
        y = driver.find_element_by_class_name("iUh30")
        print(y.text)
        if y.text == "https://www.claroty.com/":
            print("Claroty.com is the first")
        else:
            print("Claroty.com is not the first")
    except:
        print("Problem")

    try: #comment this function go to claroty.com/careers and print the number of careers
        clickme=driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[2]/div/div/div[1]/a[1]/div/cite/span')
        #print(clickme.text)
        if clickme.text != "https://www.claroty.com/careers":
            driver.close() #if claroty.com/careers not in the second line open with another browser 
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
        print("the numbers of careers : " + str(number))  #print the number of careers
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


















