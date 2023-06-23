from bs4 import BeautifulSoup
import requests
from playwright.async_api import async_playwright
import asyncio
import time

async def scrape(depart_city, dest_city, depart_date, return_date, adults, _class, direct_pref):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        
        await page.goto(f'https://www.skyscanner.com.au/transport/flights/{depart_city}/{dest_city}/?adultsv2={adults}&cabinclass={_class}&preferdirects={direct_pref}')
        await page.wait_for_selector('wait')


asyncio.run(scrape('SYD', 'DE', '2021-10-01', '2021-10-02', 4, 'economy', False))