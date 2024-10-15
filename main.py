from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import tkinter as tk
import time

usr=""
p=""

def main():
    

    serv=Service(executable_path="resources/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=serv)

    # x="n"

    # while x !="y":
    #     usr=input("Enter your instagram username: ")
    #     p=input("Enter your instagram password: ")
    #     x=input("Are you sure? (y/n): ")

    accept()
    login(driver)

    time.sleep(7)

    driver.get("https://www.instagram.com/"+usr)

    followers_list=get_list(driver, "followers")
    driver.get("https://www.instagram.com/"+usr)
    following_list=get_list(driver, "following")

    print("\n\nAccounts that do not follow "+usr+" back")

    x=len(following_list)
    for i in range(x):
        if following_list[i] not in followers_list:
            print(following_list[i])
        else:
            continue
    
    driver.quit()




def login(driver):
    driver.get("https://www.instagram.com")

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


    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "a[href*='"+usr+"/"+str+"']"))
    )

    f1=driver.find_element(By.CSS_SELECTOR, "a[href*='" +usr +"/"+str+"']")

    f1.click()

    time.sleep(2)
    size=int(f1.text.split(" ")[0])

    ff=get_list_ver1(str,driver)
    # ff=get_list_ver2(str,driver,size)

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
    x=10
    while True:
        if len(ff)==size:
            return(ff)
        else:
            scroll(driver)
            # print("scroll down")
            ff2=driver.find_elements(By.CSS_SELECTOR, "span._ap3a")
            if len(ff2)>=len(ff):
                ff=ff2


def accept():
    root =tk.Tk()
    root.title("Login Details")

    tk.Label(root, text="Email/Username: ").grid(row=0,column=0)
    m_entry=tk.Entry(root,width=30)
    m_entry.grid(row=0,column=1)

    tk.Label(root, text="Password: ").grid(row=1, column=0)
    pwd_entry=tk.Entry(root, width=30, show="*")
    pwd_entry.grid(row=1, column=1)

    def assign():
        email = m_entry.get()
        pwd=pwd_entry.get()
        global usr,p
        usr=email
        p=pwd
        root.destroy()

    tk.Button(root, text="Submit", command=assign).grid(row=3, column=1)
    root.mainloop()

if __name__=="__main__":
    main()