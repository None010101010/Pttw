from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pyfzf.pyfzf import FzfPrompt
#-------------------------------------------------------------------------------
from tqdm import tqdm
import random
#-------------------------------------------------------------------------------
import os
os.system("clear")
os.system("rm web.txt")
os.system("touch web.txt")
#-------------------------------------------------------------------------------
class Web:
    def file(page, year):
        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)

        driver.get("https://web.archive.org/web/" + year +"0000000000*/" + page)
        time.sleep(1)

        elems = driver.find_elements_by_tag_name('a')
        for i in tqdm(range(100), colour = "green"):
                        sleep(random.uniform(0.01, 0.01))
        for elem in elems:
            href = elem.get_attribute("href")
            
            if href is not None:
                f = open("web.txt", "a")
                f.write(href + "\n")
                #print(f)
                f.close()
