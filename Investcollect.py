import re
import time
from playwright.async_api import Page, expect
from playwright.async_api import async_playwright 
import asyncio
async def main_buy_investcollect(product_name,prenom,nom,mail,password,adresse,codepostal,ville,tel):
    async with async_playwright() as p:
        #init
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        #await page.goto("https://investcollect.com/pre-commande-tcg/16379--22-09-2023-display-one-piece-kingdoms-of-intrigue-op04-24-boosters-scelle-anglais.html")
        await page.goto("https://investcollect.com/")
        #await page.click('button:text("Ajouter au panier")') 
        await page.get_by_role('link', name=product_name).nth(1).click()
        await page.click('button:text("Ajouter au panier")') 
        await page.get_by_role('link', name="Commander").click()
        await page.goto("https://investcollect.com/commande")
        #phase 1
        await page.get_by_label("M", exact= True).check()
        await page.get_by_role('textbox').nth(0).fill(prenom)
        await page.get_by_role('textbox').nth(1).fill(nom)
        await page.get_by_role('textbox').nth(2).fill(mail)
        await page.get_by_role('textbox').nth(3).fill(password)

        await page.get_by_label("J'accepte les termes et conditions et la politique de confidentialité.").check()
        await page.get_by_role('button').nth(1).click()
        #phase 2
        await page.get_by_role('textbox').nth(4).fill(adresse)
        await page.get_by_role('textbox').nth(6).fill(codepostal)
        await page.get_by_role('textbox').nth(7).fill(ville)
        await page.get_by_role('textbox').nth(8).fill(tel)
        await page.get_by_role('button').nth(1).click()
        #phase 3
        await page.get_by_role('radio').nth(2).check()
        await page.get_by_role('button').nth(1).click()
        #phase 4 
        await page.get_by_role('radio').nth(3).check()

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
nom ="22-09"
#run
asyncio.run(main_buy_investcollect(nom,prenom,nom,mail,passwordinvescollect,adresse,codepostal,ville,tel))