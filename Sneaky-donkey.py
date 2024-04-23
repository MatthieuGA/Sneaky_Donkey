# webdriver
from ast import expr_context
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


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
import ctypes #screensize
from datetime import datetime # timeand stuff



# def
def open_url():
    try:
        global stored_url
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  
        driver = webdriver.Chrome('./chromedriver', options=options)
        driver.set_window_position(user32.GetSystemMetrics(0)/2,0)
        driver.set_window_size(user32.GetSystemMetrics(0)/2,user32.GetSystemMetrics(1))
        driver.get(url_main.get())
        print("Igot here")
        #time left
        temp_restant = driver.find_element(By.ID,"vi-cdown_timeLeft")
        print(temp_restant.get_attribute('innerHTML'))
        time_left.config(text=temp_restant.get_attribute('innerHTML') )
        # minimum bid
        bid = driver.find_element(By.ID,"MaxBidId")
        minbid = driver.find_element(By.CLASS_NAME,'bidAmt')
        #bid.clear()
        minbid = minbid.get_attribute('innerHTML')
        minbid = minbid[10:]
        minbid = minbid[:-18]
        print(minbid)
        min_bid_display.config(text=minbid)
        #bid.send_keys(minbid)
        #root.update_idletasks()
        stored_url = url_main.get()
        print("storedurl",stored_url)
        time.sleep(0.1)
        try :
            click1 = driver.find_element(By.XPATH,'//*[@id="gh-ug"]/a')
            click1.click()
        except:
            messagebox.showinfo(title="NONO LE PETIT ROBOT", message="Remplissez le captcha")
        enter_mail = driver.find_element(By.ID,'userid')
        enter_mail.clear()
        enter_mail.send_keys(mail.get())#-----MAIL

        continue_email =driver.find_element(By.ID,'signin-continue-btn')
        continue_email.click()
        time.sleep(0.5)
        enter_password = driver.find_element(By.ID,'pass')
        enter_password.clear()
        enter_password.send_keys(password.get())#-----PASSWORD
        time.sleep(0.1)
        continue_password =driver.find_element(By.ID,'sgnBt')
        continue_password.click()
        enter_bid = driver.find_element(By.ID,'MaxBidId')
        enter_bid.clear()
        enter_bid.send_keys("20,00")
        messagebox.showinfo(title="Fait", message="Valeur trouvé")
        
    except:
        messagebox.showinfo(title="Oops", message="Il y a eut une erreur, vérifier que vous avez correctement entré l'url")
    #time.sleep(10)
    #click1 = driver.find_element(By.ID,"bidBtn_btn")
    #click1.click()

def open_url_key(event):
    try:
        global stored_url
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  
        driver = webdriver.Chrome('./chromedriver', options=options)
        driver.set_window_position(user32.GetSystemMetrics(0)/2,0)
        driver.set_window_size(user32.GetSystemMetrics(0)/2,user32.GetSystemMetrics(1))
        driver.get(url_main.get())
        print("Igothere")
        #time left
        temp_restant = driver.find_element(By.ID,"vi-cdown_timeLeft")
        print(temp_restant.get_attribute('innerHTML'))
        time_left.config(text=temp_restant.get_attribute('innerHTML') )
        # minimum bid
        bid = driver.find_element(By.ID,"MaxBidId")
        minbid = driver.find_element(By.CLASS_NAME,'bidAmt')
        #bid.clear()
        minbid = minbid.get_attribute('innerHTML')
        minbid = minbid[10:]
        minbid = minbid[:-18]
        print(minbid)
        min_bid_display.config(text=minbid)
        #bid.send_keys(minbid)
        #root.update_idletasks()
        stored_url = url_main.get()
        print("storedurl",stored_url)
        time.sleep(0.1)
        try :
            click1 = driver.find_element(By.XPATH,'//*[@id="gh-ug"]/a')
            click1.click()
        except:
            messagebox.showinfo(title="NONO LE PETIT ROBOT", message="Remplissez le captcha")
        """enter_mail = driver.find_element(By.ID,'userid')
        enter_mail.clear()
        enter_mail.send_keys(mail.get())#-----MAIL

        continue_email =driver.find_element(By.ID,'signin-continue-btn')
        continue_email.click()
        time.sleep(0.5)
        enter_password = driver.find_element(By.ID,'pass')
        enter_password.clear()
        enter_password.send_keys(password.get())#-----PASSWORD
        time.sleep(0.1)
        continue_password =driver.find_element(By.ID,'sgnBt')
        continue_password.click()
        enter_bid = driver.find_element(By.ID,'MaxBidId')
        enter_bid.clear()
        enter_bid.send_keys("20,00")"""
        messagebox.showinfo(title="Fait", message="Valeur trouvé")
        
    except:
        messagebox.showinfo(title="Oops", message="Il y a eut une erreur, vérifier que vous avez correctement entré l'url")
    #time.sleep(10)
    #click1 = driver.find_element(By.ID,"bidBtn_btn")
    #click1.click()
def put_in_table():
    tree.insert('', 'end', text=stored_url, values=(name_main.get(),time_left.cget("text"),min_bid_display.cget("text")))
    ronde_complet= partial(ronde,stored_url,timefinder(time_left.cget("text")))
    thread = threading.Thread(daemon=True,target=ronde_complet)
    thread.start()
def timefinder(value):
    time2wait = 86400
    """Transform str de timeleft en int pour prochaine ronde"""
    if value[1] == "j" or value[2] =="j" :
        print(value,"est en jour")
        if time2wait> 86400:
            time2wait = 86400
    elif value[1] == "h" or value[2] =="h":
        print(value,"est en heure")
        if time2wait> 3600:
            time2wait = 3600
    elif value[2] =="m":
        print(value,"est en minute (+10)")
        if time2wait> int(value[0])*500:
            time2wait = int(value[0])*500
    elif value[1] == "m":
        print(value,"est en minute (-10)")
        if time2wait> int(value[0])*20:
            time2wait = int(value[0])*20
    elif value[-1] == "s" or value[-2] == "s":
        print(value,"est en seconde")
        time2wait = 10
    return time2wait
def buy(link,dabid):
    print("IT WORK FUTURE ME! IT WOOORKED")
    driver = webdriver.Chrome('./chromedriver')
    driver.get(link)
    temp_restant_secondleft = driver.find_element(By.ID,"vi-cdown_timeLeft")
    print(temp_restant_secondleft.get_attribute('innerHTML'))
    # minimum bid
    bid = driver.find_element(By.ID,"MaxBidId")
    minbid = driver.find_element(By.CLASS_NAME,'bidAmt')
    bid.clear()
    minbid = minbid.get_attribute('innerHTML')
    minbid = minbid[10:]
    minbid = minbid[:-18]
    print(minbid)
    min_bid_display.config(text=minbid)
    #bid.send_keys(minbid)
    #root.update_idletasks()
    stored_url = url_main.get()
    print("storedurl",stored_url)
    time.sleep(0.1)
    click1 = driver.find_element(By.XPATH,'//*[@id="gh-ug"]/a')
    click1.click()
    enter_mail = driver.find_element(By.ID,'userid')
    enter_mail.clear()
    enter_mail.send_keys(mail.get())#-----MAIL
    continue_email =driver.find_element(By.ID,'signin-continue-btn')
    continue_email.click()
    time.sleep(0.5)
    enter_password = driver.find_element(By.ID,'pass')
    enter_password.clear()
    enter_password.send_keys(password.get())#-----PASSWORD
    time.sleep(0.1)
    continue_password =driver.find_element(By.ID,'sgnBt')
    continue_password.click()
    time.sleep(0.1)
    enter_bid = driver.find_element(By.ID,'MaxBidId')
    enter_bid.clear()
    enter_bid.send_keys(dabid)
    decade = int(driver.find_element(By.ID,"vi-cdown_timeLeft").get_attribute('innerHTML')[0])
    while decade != 1:
        decade = int(driver.find_element(By.ID,"vi-cdown_timeLeft").get_attribute('innerHTML')[0])
        print(decade)
        time.sleep(0.4)
    try :
        fake =driver.find_element(By.XPATH,'//*[@id="bidBtn_btn"]')
        fake.click()
    except :
        pass
    time.sleep(1)
    bid_end =driver.find_element(By.ID,"confirm_button")
    bid_end.click()	
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")	
    print(datetime.now().strftime("%H:%M:%S"))



def delete():
   # Get selected item to Delete
   selected_item = tree.selection()[0]
   tree.delete(selected_item)
def edit():
   # Get selected item to Edit
   selected_item = tree.selection()[0]
   tree.item(selected_item, text= tree.item(selected_item)["text"], values=(val_name_edit.get(), tree.item(selected_item)["values"][1],val_price_edit.get()))
def ronde(excluded,default):
    """le premier argt = url a ne pas vérif"""
    while 0==0 :
        time2wait= 86400
        for child in tree.get_children():
            if tree.item(child)["text"] not in excluded :
                driver = webdriver.Chrome('./chromedriver')
                driver.set_window_position(user32.GetSystemMetrics(0)/2,0)
                driver.get(tree.item(child)["text"])

                #time left
                temp_restant_update = driver.find_element(By.ID,"vi-cdown_timeLeft")
                tree.item(child, values =(tree.item(child)["values"][0], temp_restant_update.get_attribute('innerHTML'),tree.item(child)["values"][2]))
                driver.close()
                print("ronde de",tree.item(child)["values"])

                #print(tree.item(child)["values"][1])
                if tree.item(child)["values"][1][1] == "j" or tree.item(child)["values"][1][2] =="j" :
                    print(tree.item(child)["values"][1],"est en jour")
                    if time2wait> 86400:
                        time2wait = 86400
                elif tree.item(child)["values"][1][1] == "h" or tree.item(child)["values"][1][2] =="h":
                    print(tree.item(child)["values"][1],"est en heure")
                    if time2wait> 3600:
                        time2wait = 3600
                elif tree.item(child)["values"][1][2] =="m":
                    print(tree.item(child)["values"][1],"est en minute (+10)")
                    if time2wait> int(tree.item(child)["values"][1][0])*500:
                        time2wait = int(tree.item(child)["values"][1][0])*500
                elif tree.item(child)["values"][1][1] == "m":
                    print(tree.item(child)["values"][1],"est en minute (-10)")
                    if time2wait> int(tree.item(child)["values"][1][0])*20:
                        time2wait = int(tree.item(child)["values"][1][0])*20
                elif tree.item(child)["values"][1][-1] == "s" or tree.item(child)["values"][1][-2] == "s":
                    print(tree.item(child)["values"][1],"est en seconde")

                    time2wait = 10
                    if time2wait < 50:
                        buy(tree.item(child)["text"],tree.item(child)["values"][2])
                        tree.delete(child)
            else:
                print("déja vu",tree.item(child)["values"][0])
                excluded = ""
                time2wait = default

            
        print(time2wait)
        print(datetime.now().strftime("%H:%M:%S"))
        time.sleep(time2wait)

    

def link_tree(event):
	input_id = tree.selection()

	input_item = tree.item(input_id,"text")	
	print(input_item)
	#for opening the link in browser
	import webbrowser
	url ='{}'.format(input_item)
	print(url)
	webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(url)
	#webbrowser.open('{}'.format(input_item))
    #do whatever you want



def toggle_fullscreen(event):
    root.state = not root.state  # Just toggling the boolean
    #fenetre.columnconfigure(2,weight = 2)
    #fenetre.rowconfigure(6,weight = 2)
    root.attributes("-fullscreen", root.state)


def end_fullscreen(event):
    root.state = False
    #fenetre.columnconfigure(2, weight =1)
    #fenetre.rowconfigure(6, weight =1)
    root.attributes("-fullscreen", False)

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

def clear_text():
   url_main.delete(0, END)
#tkinter prog main
# - basics
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")	
print(datetime.now().strftime("%H:%M:%S"))


def quit_me():
    print('quit')


    root.quit()
    root.destroy()


user32 = ctypes.windll.user32
screensizewidth = user32.GetSystemMetrics(0)/2
screensizeheigth =user32.GetSystemMetrics(1)
windowsize = str(int(screensizewidth))+"x"+str(screensizeheigth)
root = tk.Tk()
root.title("sneaky donkey")
root.geometry(windowsize+"+0+0")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", quit_me)# kill when closed
root.configure(background = "Gold")
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)
#root.bind("<Return>", open_url_key)
root.iconbitmap('Icone.ico')

file_option = open("option.txt", "r")
mail = file_option.readline()[6:]
password = file_option.readline()[10:]

# btn1
entry1_main = StringVar() 
#entry1_main.set("Url")
entry1_main.set("url")
url_main = Entry(root, textvariable=entry1_main, bg='lightslategray',font=("Bahnshrift", 15))
url_main.grid(row = 0, column = 0,padx=10,pady=10)

#clear entry
clear_entry = tk.Button(root,text="Effacer", command=clear_text, font=("Bahnshrift", 18),bg='lightslategray')
clear_entry.grid(row = 0, column = 2,padx=10,pady=10)
#search 1

search1_btn = tk.Button(root, text="Chercher", command=open_url, bg='lightslategray',font=("Bahnshrift", 18))
search1_btn.grid(row = 0, column = 1,padx=10,pady=10)
#display time left 
time_left = Label(root, text= "temps restant",font=("Bahnshrift", 20), background= "Gold", foreground= "Black")
time_left.grid(row = 2, column = 0,padx=10,pady=10)

#display min bid
min_bid_display = Label(root, text= "enchère",font=("Bahnshrift", 20), background= "Gold", foreground= "Black")
min_bid_display.grid(row = 3, column = 0,padx=10,pady=10)

#entry name
entry2_main = StringVar() 
entry2_main.set("Nom")
name_main = Entry(root, textvariable=entry2_main, bg='lightslategray',font=("Bahnshrift", 15))
name_main.grid(row = 2, column = 1,padx=10,pady=10)
#interger in table
place_table = tk.Button(root, text="Placer", command=put_in_table, bg='lightslategray',font=("Bahnshrift", 18))
place_table.grid(row = 3, column = 1,padx=10,pady=10)
#delete btn
del_btn = tk.Button(root, text="Supprimer", command=delete, bg='lightslategray',font=("Bahnshrift", 18))
del_btn.grid(row = 5, column = 0,padx=10,pady=10)
# edit btn
edit_btn = tk.Button(root, text="Editer", command=edit, bg='lightslategray',font=("Bahnshrift", 18))
edit_btn.grid(row = 5, column = 1)
#EDIT 3 entry
entry3_main = StringVar() 
entry3_main.set("Nom")
val_name_edit = Entry(root, textvariable=entry3_main, bg='lightslategray',font=("Bahnshrift", 15))
val_name_edit.grid(row = 5, column = 2,padx=5,pady=10)
"""entry4_main = StringVar() 
entry4_main.set("Temps")
val_time_edit = Entry(root, textvariable=entry4_main, bg='lightslategray',font=("Bahnshrift", 15))
val_time_edit.grid(row = 6, column = 1,padx=10,pady=10)"""
entry5_main = StringVar() 
entry5_main.set("Prix")
val_price_edit = Entry(root, textvariable=entry5_main, bg='lightslategray',font=("Bahnshrift", 15))
val_price_edit.grid(row = 6, column = 2,padx=5,pady=10)
#mail password
entry6_main = StringVar() 
entry6_main.set(mail)
mail = Entry(root, textvariable=entry6_main, bg='lightslategray',font=("Bahnshrift", 15))
mail.grid(row = 7, column = 0,padx=5,pady=10)
entry7_main = StringVar() 
entry7_main.set(password)
password = Entry(root, textvariable=entry7_main, bg='lightslategray',font=("Bahnshrift", 15))
password.grid(row = 7, column = 1,padx=5,pady=10)
#tree---------
style = ttk.Style()
style.theme_use('clam')

tree = ttk.Treeview(root, column=("c1", "c2","c3"), show='headings', height=8)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Objet")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Temps")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Montant")
tree.bind("<Double-1>", link_tree)#open url
tree.grid(row = 4, column = 0, columnspan=4,padx=10,pady=10)



#test
#tree.insert('', 'end', text="https://www.ebay.fr/itm/175443349467?hash=item28d93d0fdb%3Ag%3AuH8AAOSw1btgN-KL&amdata=enc%3AAQAHAAAAoFa1y2ibz07jAmH6vb3jdh7bCZBzhvTphTsJsZmTW8jgpNWoArupPuvWtk82G6ySOTAD7%2B17Ke61DCLMz7mqmP%2BTiXgiqRDa8ks4WlYpNlS7JD1jM6Sk8%2FdL1LaV7u8Fkh21ghIbWX9IslGqBD4X9uWlXxUn24r3nz6JJC%2BmeLo8Qmyv2RbWt0OvP9w3jTRBv2Nq23Jg7plr7Q6ZuI7Ev4M%3D%7Ctkp%3ABk9SR5LTnIz-YA&LH_Auction=1", values=("Mordor","10s","23,00"))

#Thread "ronde"
ronde_complet= partial(ronde,"",86400)
thread = threading.Thread(daemon=True,target=ronde_complet)
thread.start()
#THE END
root.mainloop()
print("THERE")
sys.exit()
exit()
quit()