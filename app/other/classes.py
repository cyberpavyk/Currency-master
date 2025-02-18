
from patchright.async_api import async_playwright


from config import PROXY

import asyncio

class GetData(): 
   

    #Usd-rub garantex
    @staticmethod
    async def grantex_usd_rub():

        URL = "https://garantex.org/"
        GAR_LOC_USD_RUB = 'span.form_price_usdt_ask'

        async with async_playwright() as p:

            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(URL)
            try:
                act_price = await page.locator(GAR_LOC_USD_RUB).inner_text()
            except Exception as e:
                act_price = None
                print(f'error appeared {e}')

            
            return act_price
        
    #Usd-rub investing
    @staticmethod
    async def investing_usd_rub():

        USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        URL = "https://ru.investing.com/currencies/usd-rub"
        INV_LOC_PRCICE = 'div[data-test="instrument-header-details"] div[data-test="instrument-price-last"]'
        INV_LOC_PERC = 'div[data-test="instrument-header-details"] span[data-test="instrument-price-change-percent"]'
        INV_LOC_CHANGE = 'div[data-test="instrument-header-details"] span[data-test="instrument-price-change"]'
        
        async with async_playwright() as p:
            async with await p.chromium.launch(
                channel='chrome',
                headless=True
            ) as br:
                
                context = await br.new_context(user_agent=USER_AGENT)
                page = await context.new_page()
                await page.goto(URL, wait_until='domcontentloaded')
            
            
                try:
                    act_price = await page.locator(INV_LOC_PRCICE).inner_text()
                    percent = await page.locator(INV_LOC_PERC).inner_text()
                    change = await page.locator(INV_LOC_CHANGE).inner_text()

                except Exception as e:

                    print(f"Error occurred: {e}")
                    act_price, percent, change = None
                    
                    
                    
                return {"price":act_price, "percent": percent, "change": change}


    """
    
    central bank part
    
    """
    #Usd-rub central bank
    @staticmethod 
    async def central_bank_usd_rub():

        USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        URL = "https://www.cbr.ru/currency_base/daily/"
        CB_USD_RUB_LOC = 'table.data tbody tr:has(td:has-text("USD"))'

        async with async_playwright() as p:
            async with await p.chromium.launch(
                channel='chrome',
                headless = True
            ) as br:
                
                context = await br.new_context(user_agent=USER_AGENT)
                page = await context.new_page()
                await page.goto(URL)


                try:
                    act_price = await page.locator(CB_USD_RUB_LOC).inner_text()
                except Exception as e:
                    act_price = None
                    print(f'smth wrong with {e}')
                    return act_price
                    
                

               
                return act_price.split()[-1]
          

        

    "CNY"
    @staticmethod
    async def central_bank_cny_rub():
    
    
        URL = "https://www.cbr.ru/currency_base/daily/"
        CB_CNY_RUB_LOC = 'table.data tbody tr:has(td:has-text("CNY"))'
    
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(URL)


            try:
                act_price = await page.locator(CB_CNY_RUB_LOC).inner_text()
            except Exception as e:
                act_price = None
                print(f'smth wrong with {e}')
                return act_price
            

           
            return act_price.split()[-1]

    "eur"
    @staticmethod
    async def central_bank_eur_rub():

        URL = "https://www.cbr.ru/currency_base/daily/"
        CB_EUR_RUB_LOC = 'table.data tbody tr:has(td:has-text("EUR"))'

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(URL)


            try:
                act_price = await page.locator(CB_EUR_RUB_LOC).inner_text()
            except Exception as e:
                act_price = None
                print(f'smth wrong with {e}')
                return act_price

            
            return act_price.split()[-1]


    """
    
    
    XE part 
    
    
    """
    @staticmethod
    async def xe_usd_rub():

        USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        URL = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=RUB"
        XE_USD_RUB_LOC = '//p[contains(@class, "sc-294d8168-1 hVDvqw")]'

        async with async_playwright() as p:
            async with await p.chromium.launch(
                channel='chrome',
                headless = True
            ) as br:
                
                context = await br.new_context(user_agent=USER_AGENT, proxy=PROXY)
                page = await context.new_page()
                await page.goto(URL, wait_until='domcontentloaded')

                try:
                    await page.wait_for_selector(XE_USD_RUB_LOC)
                    act_price = await page.locator(XE_USD_RUB_LOC).inner_text()
                except Exception as e:

                    act_price = None
                    print(f'error found {e}')
                    return act_price

                    
                return act_price.split()[0]


    @staticmethod
    async def xe_usd_cny():

        USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        URL = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CNY"
        XE_USD_CNY_LOC = '//p[contains(@class, "sc-294d8168-1 hVDvqw")]'

        
        async with async_playwright() as p:
            async with await p.chromium.launch(
                channel='chrome',
                headless = True
            ) as br:
            
            
                context = await br.new_context(user_agent=USER_AGENT, proxy=PROXY)
                                              
                page = await context.new_page()
                await page.goto(URL, wait_until='domcontentloaded')

                try:

                    await page.wait_for_selector(XE_USD_CNY_LOC)
                    act_price = await page.locator(XE_USD_CNY_LOC).inner_text()
                except Exception as e:
                    act_price = None
                    print(f'error found {e}')
                    return act_price

                   
                return act_price.split()[0]

                
            

    @staticmethod
    async def xe_eur_usd():

        USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        URL = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=USD"
        XE_USD_EUR_LOC = '//p[contains(@class, "sc-294d8168-1 hVDvqw")]'
        async with async_playwright() as p:
            async with await p.chromium.launch(
                channel='chrome',
                headless = True,
                proxy=PROXY
            ) as br:
                
                context = await br.new_context(user_agent=USER_AGENT)
                
                page = await context.new_page()
                await page.goto(URL, wait_until='domcontentloaded')

                try:
                    await page.wait_for_selector(XE_USD_EUR_LOC)
                    act_price = await page.locator(XE_USD_EUR_LOC).inner_text()
                except Exception as e:
                    act_price = None
                    print(f'error found {e}')
                    return act_price

                return act_price.split()[0]
                

    @staticmethod
    async def xe_eur_rub():

        USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        URL = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=RUB"
        XE_RUB_EUR_LOC = '//p[contains(@class, "sc-294d8168-1 hVDvqw")]'

        async with async_playwright() as p:
            async with await p.chromium.launch(
                channel='chrome',
                headless = True,
                proxy=PROXY
            ) as br:
            
                context = await br.new_context(user_agent=USER_AGENT)
                
                page = await context.new_page()
                await page.goto(URL, wait_until='domcontentloaded')

                try:
                    await page.wait_for_selector(XE_RUB_EUR_LOC)
                    act_price = await page.locator(XE_RUB_EUR_LOC).inner_text()
                except Exception as e:
                    act_price = None
                    print(f'error found {e}')
                    return act_price

                return act_price.split()[0] 
                
        
        
      

    async def __call__(self):
        
        tasks = [
            self.grantex_usd_rub(),
            self.investing_usd_rub(),
            self.central_bank_usd_rub(),
            self.xe_usd_cny(),
            self.xe_eur_usd(),
            self.xe_usd_rub(),
            self.central_bank_cny_rub( ),
            self.central_bank_eur_rub(),
            self.xe_eur_rub()
        ]
        results = await asyncio.gather(*tasks)
        
        answ = {
            "garantex": results[0],
            "investing": results[1],
            "centralb": results[2],
            "xe_cny": results[3],
            "xe_eur": results[4],
            "xe_usd": results[5],
            "centralb_cny": results[6],
            "centralb_eur": results[7],
            "xe_e_r": results[8]
        }
        return answ
