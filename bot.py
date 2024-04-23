"""
from selenium import webdriver as wd
import chromedriver
wd = wd.Chrome()
wd.implicitly_wait(10)
wd.get("https://www.ebay.fr/itm/265930375786?hash=item3deaaf826a:g:-2QAAOSwON5jRTi9&amdata=enc%3AAQAHAAAA4PdeVdpvgU2DMbUdCnMQVuYh62Laq8vwCE2viMwtuqEcJzyDw1qaFKARKwMeh6lGojIY2jeq4NEK3IR9mDSwpJWl5Zq%2B8mcAUqUYl1abNfwnPe1WrfB3iZmDZdmbXm0py%2Bk9UyaruqjP9vNkAaxKhnbI%2F02HwCbGKW9A8b3RnQSokfTlRmR1qW8n5cNyDUaBkF%2BAKWxJ02ia11URLjzIHnoBOf8dAF5%2Fx%2FvUua%2FKsmOxg1UgQB9lYnV7%2FQ7vlz2KOGuk2obOZtL5IFjwCuJ8bhOhLpOo4o5QpwCgabsXuCGg%7Ctkp%3ABFBMoPXTi_pg")



from selenium import webdriver as wd
import chromedriver_autoinstaller

import time

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = wd.Chrome()
driver.get("https://www.ebay.fr/itm/265930375786?hash=item3deaaf826a:g:-2QAAOSwON5jRTi9&amdata=enc%3AAQAHAAAA4PdeVdpvgU2DMbUdCnMQVuYh62Laq8vwCE2viMwtuqEcJzyDw1qaFKARKwMeh6lGojIY2jeq4NEK3IR9mDSwpJWl5Zq%2B8mcAUqUYl1abNfwnPe1WrfB3iZmDZdmbXm0py%2Bk9UyaruqjP9vNkAaxKhnbI%2F02HwCbGKW9A8b3RnQSokfTlRmR1qW8n5cNyDUaBkF%2BAKWxJ02ia11URLjzIHnoBOf8dAF5%2Fx%2FvUua%2FKsmOxg1UgQB9lYnV7%2FQ7vlz2KOGuk2obOZtL5IFjwCuJ8bhOhLpOo4o5QpwCgabsXuCGg%7Ctkp%3ABFBMoPXTi_pg")
add_to_cart = wd.find_element_by_xpath('//*[@id="isCartBtn_btn"]')
add_to_cart.click()
assert "Python" in driver.title
time.sleep(10)

import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
 # to use when 1st time on the machine and then leave comented
os.system("pip install  selenium ")
os.system("pip install  chromedriver_autoinstaller ")
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.headless = False
options.binary_location = ('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
driver = webdriver.Chrome(options=options)
driver.get("https://www.ebay.fr/itm/265930375786?hash=item3deaaf826a:g:-2QAAOSwON5jRTi9&amdata=enc%3AAQAHAAAA4PdeVdpvgU2DMbUdCnMQVuYh62Laq8vwCE2viMwtuqEcJzyDw1qaFKARKwMeh6lGojIY2jeq4NEK3IR9mDSwpJWl5Zq%2B8mcAUqUYl1abNfwnPe1WrfB3iZmDZdmbXm0py%2Bk9UyaruqjP9vNkAaxKhnbI%2F02HwCbGKW9A8b3RnQSokfTlRmR1qW8n5cNyDUaBkF%2BAKWxJ02ia11URLjzIHnoBOf8dAF5%2Fx%2FvUua%2FKsmOxg1UgQB9lYnV7%2FQ7vlz2KOGuk2obOZtL5IFjwCuJ8bhOhLpOo4o5QpwCgabsXuCGg%7Ctkp%3ABFBMoPXTi_pg")
add_to_cart = webdriver.find_element_by_xpath('//*[@id="isCartBtn_btn"]')
add_to_cart.click()
time.sleep(10)

import time
from unicodedata import name
from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\\44eme\\Documents\\In-ventory\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(1) # Let the user actually see something!
add_to_cart = driver.find_element(by=xpath_tokenizer, value='//*[@id="L2AGLb"]/div')
add_to_cart.click()
search_box = driver.find_element(by=xpath_tokenizer,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.ebay.fr/itm/265930375786?hash=item3deaaf826a:g:-2QAAOSwON5jRTi9&amdata=enc%3AAQAHAAAA4PdeVdpvgU2DMbUdCnMQVuYh62Laq8vwCE2viMwtuqEcJzyDw1qaFKARKwMeh6lGojIY2jeq4NEK3IR9mDSwpJWl5Zq%2B8mcAUqUYl1abNfwnPe1WrfB3iZmDZdmbXm0py%2Bk9UyaruqjP9vNkAaxKhnbI%2F02HwCbGKW9A8b3RnQSokfTlRmR1qW8n5cNyDUaBkF%2BAKWxJ02ia11URLjzIHnoBOf8dAF5%2Fx%2FvUua%2FKsmOxg1UgQB9lYnV7%2FQ7vlz2KOGuk2obOZtL5IFjwCuJ8bhOhLpOo4o5QpwCgabsXuCGg%7Ctkp%3ABFBMoPXTi_pg")
print(driver.title)
search_bar = driver.find_element(By.ID,"isCartBtn_btn")
search_bar.click()
#search_bar.clear()
#search_bar.send_keys("getting started with python")
#search_bar.send_keys(Keys.RETURN)
"""

import logging
import threading
import time



# webdriver
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#tkinter
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import tkinter as tkin
from tkinter import ttk
from tkinter import filedialog as fd
from functools import partial
import sys
from PIL import ImageTk
import time


# threading 
import logging
import threading

#other stuff
def prog2():
    global temp_restant
    temp_restant = 10
    while 0==0:
        temp_restant -=1
        time.sleep(1)
        print(temp_restant)
    
def prog1():
# def
    def open_url():
        global temp_restant
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url_main.get())
        temp_restant = driver.find_element(By.ID,"vi-cdown_timeLeft")
        print(temp_restant)
        click1 = driver.find_element(By.ID,"isCartBtn_btn")
        click1.click()

    def toggle_fullscreen(event):
        root.state = not root.state  # Just toggling the boolean
        #fenetre.columnconfigure(2,weight = 2)
        #fenetre.rowconfigure(6,weight = 2)
        root.attributes("-fullscreen", root.state)
        print("start")
        


    def end_fullscreen(event):
        root.state = False
        #fenetre.columnconfigure(2, weight =1)
        #fenetre.rowconfigure(6, weight =1)
        root.attributes("-fullscreen", False)
        print("start")
        x.start()

    def toggle_fullscreen_touch():
        root.state = not root.state  # Just toggling the boolean
        root.columnconfigure(2,minsize= 2000)
        root.rowconfigure(6, minsize= 2000)
        root.attributes("-fullscreen", root.state)


    def end_fullscreen_touch():
        root.state = False
        root.columnconfigure(2,minsize=  1)
        root.rowconfigure(6, minsize= 1)
        root.attributes("-fullscreen", False)  
    #tkinter prog main
    # - basics
    root = tk.Tk()
    root.title("Sneaky donkey")
    root.geometry("960x570")
    root.configure(background = "aquamarine3")
    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Escape>", end_fullscreen)
    # btn1
    entry1_main = StringVar() 
    entry1_main.set("Url")
    url_main = Entry(root, textvariable=entry1_main)
    url_main.grid(row = 0, column = 0)
    #search 1

    search1_btn = tk.Button(root, text="Chercher", command=open_url)
    search1_btn.grid(row = 0, column = 1)
    #display time left 
    time_left = Label(root, text="1",font=("Bahnshrift", 20), background= "aquamarine3", foreground= "white")
    time_left.grid(row = 2, column = 0)
    root.mainloop()

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")


    x = threading.Thread(target=prog2)
    x.start()
    y = threading.Thread(target=prog1)
    

    prog1()



