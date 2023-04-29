from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys 
import requests
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re
import time


chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chromeOptions)

driver.get('https://vndb.org/v') #opens the target in a chrome instance
driver.set_window_position(0, 0)
driver.set_window_size(1400, 900)
time.sleep(1) #sec

# finds the number of results, slices just the first digits, then converts to an int
totalTitlesStr = driver.find_element(By.XPATH, '//*[@id="maincontent"]/form/div[1]/p[2]').text 
totalTitlesList = re.findall(r'\d+', (totalTitlesStr))
totalTitlesInt = int(totalTitlesList[0])   
resultsPerPageXPATH = driver.find_element(By.XPATH, '//*[@id="tableopts-results"]/div/a').text
resultsperpageInt = int(resultsPerPageXPATH)
# get the name and link for current title, we'll add 1 to the titlePos and use that to remake the string 
# into the next titles xpath, then we'll parse that then reiterate for all results
titlePos = 1 #first title starts at 1 not 0
#value tr[] marks title number
posXPATH = ('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[1]/a')
popularityXPATH = ('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[5]')
ratingXPATH = ('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[6]')
releaseDateXPATH = ('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[4]')
titleName = driver.find_element(By.XPATH, posXPATH).get_attribute("title") 
titleLink = driver.find_element(By.XPATH, posXPATH).get_attribute("href")
titlePopularity = driver.find_element(By.XPATH, popularityXPATH).text
titleRating = driver.find_element(By.XPATH, ratingXPATH).text
titleRelease = driver.find_element(By.XPATH, releaseDateXPATH).text
lastPageLink = driver.find_element(By.XPATH, '//*[@id="maincontent"]/form/div[2]/ul[1]/li[5]/a').get_attribute("href")
itemsList = [titlePos, titleName, titlePopularity, titleRating, titleRelease, titleLink]
pagecount = 0
f = open('items.txt', "w", encoding="utf-8") 
for item in itemsList:
    f.write(str(item)+",")
    if item == itemsList[-1]:
        f.write(str(item)+"\n")
            
f
urlNumber = 1   
updatedUrl = driver.current_url
if updatedUrl != lastPageLink:
    while updatedUrl != lastPageLink:
        if titlePos != resultsperpageInt:
        #concat the xpath for next title
            titlePos += 1 
            posXPATH = str('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[1]/a')
            posXPATH = ('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[1]/a')
            popularityXPATH = ('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[5]')
            ratingXPATH = ('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[6]')
            releaseDateXPATH = ('//*[@id="maincontent"]/form/div[3]/table/tbody/tr[' + str(titlePos) + ']/td[4]')
            titleName = driver.find_element(By.XPATH, posXPATH).get_attribute("title") 
            titleLink = driver.find_element(By.XPATH, posXPATH).get_attribute("href")
            titlePopularity = driver.find_element(By.XPATH, popularityXPATH).text
            titleRating = driver.find_element(By.XPATH, ratingXPATH).text
            titleRelease = driver.find_element(By.XPATH, releaseDateXPATH).text
            itemsList = [titlePos, titleName, titlePopularity, titleRating, titleRelease, titleLink]
            for item in itemsList:
                open('items.txt', "w", encoding="utf-8")
                f.write(str(item)+",")
                if item == itemsList[-1]:
                    f.write(str(item)+"\n")
            pagecount += 1 
            if pagecount == 50:
                pagecount = 0
             #sec to avoid hitting rate limit and getting ipbanned LOL
            
        #concat and check conditions for new url 
        urlNumber += 1 
        newTargetUrl = str('https://vndb.org/v?f=&p=' + str(urlNumber) + '&s=34w')
        driver.get(newTargetUrl) #doesnt open in new window thnk gawd
        updatedUrl = driver.current_url
        
        
        #navigate to next page after parsing all links on the page
#else:
#    break
f.close()

#def name_link_index():
    
