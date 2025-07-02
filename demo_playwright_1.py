from playwright.async_api import async_playwright
import asyncio

async def scrape_text():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        url = "https://playwright.dev/docs/intro#installing-playwright"
        await page.goto(url)

        await page.wait_for_timeout(50000)

   # Wait for the <main> tag to load
        await page.wait_for_selector("#__docusaurus_skipToContent_fallback > div > div > main > div > div > div.col.docItemCol_VOVn > div > article")

        # Extract text from the <main> element
        content = await page.inner_text("#__docusaurus_skipToContent_fallback > div > div > main > div > div > div.col.docItemCol_VOVn > div > article")

        # Write to a text file
        with open("webscraping_test.txt", "w", encoding="utf-8") as f:
            f.write(content)

        print("Scraped content written to webscraping_test.txt")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_text())
