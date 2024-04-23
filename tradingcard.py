import re
import time
from playwright.async_api import Page, expect
from playwright.async_api import async_playwright 
import asyncio
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 10000  # Set Duration To 10000 ms == 10 second
#winsound.Beep(frequency, duration)
async def main_buy_tradingcard(product_name,prenom,nom,mail,password,adresse,codepostal,ville,tel,paypal,mailtradin):
    async with async_playwright() as p:
        #init
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        #page_two = await context.new_page() 
        await page.goto("https://tradingcardsxxx.fr/collections/pokemon")
        #await page_two.goto("https://tradingcardsxxx.fr/collections/pokemon")
        #await page.click('button:text("Ajouter au panier")') 
        await page.get_by_title(product_name).click()
        await page.get_by_role('button', name="Ajouter au panier").click()
        await page.get_by_label("termes et conditions").check() 
        await page.get_by_role('button', name="Paiement").click()
        #signin
        await page.get_by_role('textbox').nth(1).fill(mailtradin)
        await page.get_by_role('textbox').nth(2).fill(password)
        time.sleep(0.8)
        await page.get_by_role('button', name="Connexion").click()
        winsound.Beep(frequency, duration)
        #cart   
        #await page.get_by_role('button', name="Continuer vers l'expédition").click()
        #await page.get_by_role('radio').nth(1).check()
        #await page.get_by_role('button').nth(0).click()
        #time.sleep(1)
        #await page.get_by_role("radio", name="PayPal PayPal").check()
        #await page.get_by_role("button", name="Vérifier la commande").click()
        #time.sleep(2)
        #await page.get_by_role("button").click()
        #daframe = page.frame_locator('iFrame')
        #iframe paypal
        daotherframe = page.frame_locator('iFrame').nth(1)
        #page.wait_for_event('popup'),
        #print(await page.frame.content())
        """async def handle_page(page):
            await page.wait_for_load_state()
            print(await page.title(), "is active")
        context.on("page", handle_page)"""
        async with page.expect_popup() as popup_info:
            await daotherframe.get_by_label("").click()
        popup = await popup_info.value
        await popup.wait_for_load_state()
        #print(await popup.title())
        #print(page.url)
        #paypalpopup
        await popup.get_by_role('textbox').fill(mail)
        await popup.get_by_role('button', name="Suivant").click()
        time.sleep(0.4)
        await popup.get_by_role('textbox').fill(paypal)
        await popup.get_by_role('button', name="Connexion").click()
        time.sleep(1)
        await popup.get_by_role('radio').nth(1).check()
        winsound.Beep(frequency, duration)
        #id = jsx-iframe-69dc45df4b
        #id2 = jsx-iframe-5c1c67cc8a
        #await page.get_by_role('textbox').fill("0789789834346565")       
        #await page.get_by_label("paypal").click()
        time.sleep(100.5)


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
passwordtradingcard = file_option.readline()[16:]
paypalpassword = file_option.readline()[16:]
mailtradin = file_option.readline()[12:]
nom ="[Limite 1] Pokémon - Coffret Collection Classeur EV03.5 : Écarlate et Violet - 151"
#run
print(paypalpassword)
asyncio.run(main_buy_tradingcard(nom,prenom,nom,mail,passwordtradingcard,adresse,codepostal,ville,tel,paypalpassword,mailtradin))