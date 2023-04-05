import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # navigate to the login page
        await page.goto('https://lng-tgk-aime-gw.am-all.net/common_auth/login?site_id=maimaidxex&redirect_url=https://maimaidx-eng.com/maimai-mobile/&back_url=https://maimai.sega.com/')

        # wait for the login page to load
        await page.wait_for_selector('span[class="c-button--openid--segaId"]')

        # click the SEGA ID button
        await page.click('span[class="c-button--openid--segaId"]')

        # wait for the SEGA ID form to load
        await page.wait_for_selector('input[type="text"][id="sid"]')

        # fill in login credentials
        await page.fill('input[type="text"][id="sid"]', 'pugking4')
        await page.fill('input[type="password"][id="password"]', 'Cocothe4th00')

        # click the login button
        await page.click('input[type="submit"][class="c-button--login"]')
        print('Waiting for record image to load... ')
        # wait for the page to load after login
        await page.wait_for_selector('a[class="d_ib col4 p_4"][href="https://maimaidx-eng.com/maimai-mobile/record/"]')
        print('Record image loaded. ')
        # click the record menu
        await page.click('a[class="d_ib col4 p_4"][href="https://maimaidx-eng.com/maimai-mobile/record/"]')
        print('Waiting for sub-record music image to load... ')
        # wait for the sub-record music menu to appear
        await page.wait_for_selector('img[src="https://maimaidx-eng.com/maimai-mobile/img/menu_sub_record_music.png?ver=1.30"]')

        # click the sub-record music menu
        await page.click('img[src="https://maimaidx-eng.com/maimai-mobile/img/menu_sub_record_music.png?ver=1.30"]')

        # wait for the master music button to appear
        await page.wait_for_selector('img[src="https://maimaidx-eng.com/maimai-mobile/img/btn_music_master.png"]')

        # click the master music button
        await page.click('img[src="https://maimaidx-eng.com/maimai-mobile/img/btn_music_master.png"]')

        # wait for the page to load after clicking the button
        await page.wait_for_selector('div[class="f_10"]')

        # get all information on the page
        page_content = await page.content()

        # print the page content
        print(page)

        # close the browser
        await browser.close()

asyncio.run(main())
