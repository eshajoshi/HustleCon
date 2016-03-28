# Esha Joshi
# Emails list: 'emails.txt'
# Selenium Python

from sys import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def main():
   print argv

   if (len(argv) == 3):
      emailsFile = open(argv[1], "r")
      writeToFile = open(argv[2], "a")

      for email in emailsFile.readlines():
         incognitoBrowser = retrieveBrowser()
         submitEmail(incognitoBrowser, email)
         print email,
         writeToFile.write(email)
         #incognitoBrowser.close()
   else:
      print 'Command line args: <read_from_file>.txt <write_to_file>.txt'


# Opens Chrome igcognito window
def retrieveBrowser():
   chromeOptions = webdriver.ChromeOptions()
   chromeOptions.add_argument("-incognito")

   browser = webdriver.Chrome(chrome_options=chromeOptions)
   #browser.get('http://prelaunch.hustlecon.com/?ref=b91966323e')
   browser.get('http://ambassadors.thehustle.co/?ref=6f7a0e3a95')
   return browser

# Selects element by id, inputs email into text field, and simulates hitting ENTER
def submitEmail(browser, email):
   try:
      element = WebDriverWait(browser, 10).until(
         EC.presence_of_element_located((By.ID, "user_email"))
      )
      element.send_keys(email)
      #element.submit()
   finally:
      browser.quit()

if __name__ == "__main__":
   main()


