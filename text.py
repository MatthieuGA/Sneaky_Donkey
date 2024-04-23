

import re
import time
from playwright.async_api import Page, expect
from playwright.async_api import async_playwright 
import asyncio
async def main_buy_tradingcard():
    async with async_playwright() as p:
        #init
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://tradingcardsxxx.fr/checkouts/cn/c1-e2d3e55d9a3508dd04da0fca1f8b2c95/information#checkout-main")
        await page.get_by_role('textbox').nth(1).fill("howtolook@gmail.com")
        time.sleep(0.5)
        await page.get_by_role('textbox').nth(2).fill("MlPnN!")
        time.sleep(1)
        await page.get_by_role('button', name="Connexion").click()
        
        daframe = page.frame_locator("jsx-iframe-69dc45df4b")
        await daframe.get_by_label("PayPal").click()
        time.sleep(200)



#config

#run
asyncio.run(main_buy_tradingcard())