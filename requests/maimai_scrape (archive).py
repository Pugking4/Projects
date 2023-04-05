import json
import asyncio
from bs4 import BeautifulSoup
import re
from playwright.async_api import async_playwright

def get_score_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    difficulty = soup.select_one('.music_master_score_back img')
    level = soup.select_one('.music_lv_block').text.strip()
    title = soup.select_one('.music_name_block').text.strip()
    score = soup.select_one('.music_score_block:nth-of-type(1)').text.strip()
    deluxe_score_block = soup.select_one('.music_score_block:nth-of-type(2)')
    deluxe_score = deluxe_score_block.text.strip() if deluxe_score_block else 'N/A'

    return {
        'difficulty': difficulty,
        'level': level,
        'title': title,
        'score': score,
        'deluxe_score': deluxe_score
    }



async def scrape(difficulty):
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
        await page.wait_for_selector(f'button[value="{difficulty}"]')

        # click the master music button
        await page.click(f'button[value="{difficulty}"]')

        # wait for the page to load after clicking the button
        await page.wait_for_selector('div[class="w_450 m_15 p_r f_0"]')
        await page.wait_for_load_state('load')

        # Inject and execute the script
        script = """
            void(function(d){if(['maimaidx-eng.com','maimaidx.jp'].indexOf(d.location.host)>=0){var s=d.createElement('script');s.src='https://myjian.github.io/mai-tools/scripts/all-in-one.js?t='+Math.floor(Date.now()/60000);d.body.append(s);}})(document)
        """
        await page.evaluate(script)

        await page.wait_for_load_state('load')

        # parse the HTML content
        wrapper = await page.query_selector('div.wrapper.main_wrapper.t_c')
        div_elements = await wrapper.query_selector_all('div[class="w_450 m_15 p_r f_0"]')
        #print("div_elements:", div_elements)
        results = []
        for count, div in enumerate(div_elements):
            # get the HTML content of the div element
            div_content = await div.inner_html()
            results.append(div_content)
            

        for test in results:
            with open(f'output_{difficulty}.txt', 'a', encoding='utf-8') as f:
                f.write(test)
                f.write('|')

        #Print a message to indicate that the program has finished executing and the output has been saved
        print("Program finished. Output saved to 'output.json'.")

asyncio.run(scrape(3))
