from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
url = "https://www.google.com/maps/place/Dhaba+Estd+1986,+Kondapur/@17.4581667,78.3729882,17z/data=!3m2!4b1!5s0x3bcb93d023e74295:0xcc0e445348391428!4m6!3m5!1s0x3bcb93d0208fd04d:0x7db249b386dc84f3!8m2!3d17.4581667!4d78.3729882!16s%2Fg%2F11c5s643p1"


def searchPlace():
    driver.get(url)
    
    sleep(2)

def allReviews():
    allreview = driver.find_element(By.CLASS_NAME, "wNNZR fontTitleSmall")
    allreview.click()
    sleep(2)


# search the place
searchPlace()

try:
    # click on all reviews
    element = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[2]/span[1]/span')
    print("Element is present")
    try:
        element.click()
        sleep(5)
        # Review page is loaded
    except:
        # exception and thus quit
        print("Not Loaded")
        driver.quit()
except:
    # exception and thus quit
    print("Element is not present")
    driver.quit()

# load the list of already loaded reviews 
reviews = driver.find_elements(By.CLASS_NAME,'jftiEf')
sleep(2)


# highlight the last div 
idx = 0
while True:

    # scroll the window to get more reviews
    for i in range(idx, len(reviews)):
        review = reviews[i]
        try:
            moreButton = review.find_element(By.CLASS_NAME,'w8nwRe')
            moreButton.click()
            sleep(2)
        except:
            print("")
        text_class = review.find_element(By.CLASS_NAME,'wiI7pd')
        text = text_class.text

        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", review, "border: 2px solid red;")
        sleep(1)
        print("\n\n------------------",i,"--------------\n\n",text)
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", review, "border: none;")
        sleep(1)
        driver.execute_script('arguments[0].scrollIntoView(true);', reviews[i])
        sleep(1)
    
    # get the list of reviews again
    idx = len(reviews)-1
    reviews = driver.find_elements(By.CLASS_NAME,'jftiEf')
    sleep(1)
    print("CHANGEEEEE ",idx,len(reviews))
    # check if the list is loaded
    if len(reviews) == 0:
        break

    print("----------------------------------------------------------------------------")



    
#     people = driver.find_elements(By.CLASS_NAME,'jftiEf')
   
    sleep(5)

 
#     print("people are ",len(people))
    sleep(1)