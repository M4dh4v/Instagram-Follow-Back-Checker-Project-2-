from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
from accounts import username,password


usr=username
p=password

def main():
    serv=Service(executable_path="resources/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=serv)

    login(driver)

    time.sleep(5)

    driver.get("https://www.instagram.com/"+usr)

    time.sleep(2)

    followers_list=get_list(driver, "followers")
    driver.get("https://www.instagram.com/"+usr)
    time.sleep(3)
    following_list=get_list(driver, "following")

    print("\n\nAccounts that do not follow "+usr+" back")

    x=max(len(following_list), len(followers_list))
    for i in range(x):
        if following_list[i] not in followers_list:
            print(following_list[i])
        else:
            continue
    
    driver.quit()




def login(driver):
    driver.get("https://www.instagram.com")

    time.sleep(2)
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.NAME, "username"))
    )

    login_usr = driver.find_element(By.NAME, "username")
    login_usr.clear()
    login_usr.send_keys(usr)

    passw = driver.find_element(By.NAME, "password")
    passw.clear()
    passw.send_keys(p + Keys.ENTER)



def get_list(driver, str):

    f1=driver.find_element(By.CSS_SELECTOR, "a[href*='" +usr +"/"+str+"']")

    f1.click()

    time.sleep(2)
    size=int(f1.text.split(" ")[0])

    #ff=get_list_ver1(str,driver)
    ff=get_list_ver2(str,driver,size)

    """
    I have no idea why get_list_ver2 fails but it does sometimes, i tried an acc
    which has 276 followers but it counts only to 275
    Its probably some instagram thingee

    If  you know why, please reach out to me and explain 
    through instagram -> kbs.madhav

    If get_list_ver2 dosent work, comment it out and remove '#' from  get_list_ver1

    """

    ffl=[x.text for x in ff]
    return ffl



def scroll(driver):
    liElement = driver.find_element(By.XPATH, "//div[@style='display: flex; flex-direction: column; padding-bottom: 0px; padding-top: 0px; position: relative;']")
    driver.execute_script("arguments[0].scrollIntoView(false);", liElement)

def get_list_ver1(str, driver):
    while True:
        time.sleep(3)
        print("\n\n\nScroll down the "+str+" dialog box")
        confirm=input("Did u reach end of the list (y/n) : ")
        if confirm=="y":
            ff=driver.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")
            break

    return ff



def get_list_ver2(str,driver,size):
    ff=driver.find_elements(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")
    while True:
        if len(ff)==size:
            return(ff)
        else:
            scroll(driver)
            # print("scroll down")
            time.sleep(1)
            ff2=driver.find_elements(By.CSS_SELECTOR, "span._ap3a")
            if len(ff2)>=len(ff):
                ff=ff2




if __name__=="__main__":
    main()