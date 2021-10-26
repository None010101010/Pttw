from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pyfzf.pyfzf import FzfPrompt
from selenium import webdriver
import time
import web
#-------------------------------------------------------------------------------
import os
os.system("clear")
#-------------------------------------------------------------------------------
print("""
 ____  _   _            
|  _ \| |_| |___      __
| |_) | __| __\ \ /\ / /
|  __/| |_| |_ \ V  V / 
|_|    \__|\__| \_/\_/  
""")
#-------------------------------------------------------------------------------
serch = input("Serch web page : ")
add_p = 37 + len(serch) + 2
#-------------------------------------------------------------------------------
fzf = FzfPrompt()

year = fzf.prompt(range(1996, 2022))
year2 = str(year)
year3 = year2[2:6]
#-------------------------------------------------------------------------------
web.Web.file(serch, year3)
#-------------------------------------------------------------------------------
web0 = open("web.txt")
w0 = fzf.prompt(web0)
w1 = str(w0)
w2 = w1[2:add_p]
print(w2)

def web_archive():
    print(": " + serch)
    driver = webdriver.Firefox()
    driver.get(w2)
print(year3)
web_archive()
