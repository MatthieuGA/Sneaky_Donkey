import re
import time
from playwright.async_api import Page, expect
from playwright.async_api import async_playwright 
import asyncio
async def main_buy_playin(product_name,prenom,nom,mail,password,adresse,codepostal,ville,tel):
    async with async_playwright() as p:
        #init
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.play-in.com/")
        """
        print(page.get_by_role('button').all())     .nth(13)    """
        time.sleep(1.5)
        await page.get_by_role('button').nth(13).click()
        #time.sleep(300)
        #await page.click('button:text("Ajouter au panier")') 
        await page.get_by_role('link', name=product_name).nth(1).click()
        await page.get_by_role('button', name="Précommander").click()
        #signin
        await page.goto("https://www.play-in.com/user/signin.php")
        await page.get_by_role('textbox').nth(1).fill(mail)
        await page.get_by_role('textbox').nth(2).fill(password)
        await page.get_by_role('button', name="Me connecter").click()
        #cart
        await page.goto("https://www.play-in.com/order/address.php")
        await page.get_by_label("En validant votre commande, vous acceptez l'intégralité de nos conditions générales de vente").check() 
        await page.get_by_role('button', name="suivante").click()
        await page.get_by_role("radio").nth(0).check()
        await page.get_by_role('link',name="KER BIKE").click()
        await page.get_by_role('button', name="Valider votre choix").click()
        await page.get_by_role("radio").nth(1).check()
        time.sleep(300)
        #await page.goto("https://www.play-in.com/order/cart.php")
        #await page.get_by_role('button').click()

        #En validant votre commande, vous acceptez l'intégralité de nos conditions générales de vente
#config
file_option = open("config.txt", "r")
nom = file_option.readline()[5:]
prenom = file_option.readline()[8:]
mail = file_option.readline()[6:]
passwordinvescollect = file_option.readline()[23:]
adresse = file_option.readline()[9:]
codepostal = file_option.readline()[12:]
ville = file_option.readline()[7:]
tel = file_option.readline()[5:]
passwordplayin = file_option.readline()[16:]
nom ="Univers"
#run
asyncio.run(main_buy_playin(nom,prenom,nom,mail,passwordplayin,adresse,codepostal,ville,tel))