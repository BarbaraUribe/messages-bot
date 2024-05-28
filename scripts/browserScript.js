import puppeteer from "puppeteer";

export const sendMessages = async () => {
  const searchElement =
    "#side > div:first-of-type > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div:first-of-type > p";
  const writeElement =
    "#main > footer > div:first-of-type > div > span:nth-of-type(2) > div > div:nth-of-type(2) > div:first-of-type > div:nth-of-type(2) > div:first-of-type > p";
  const resultsElement = "#pane-side > div:first-of-type > div > div";
  const firstResultElement =
    "#pane-side > div:first-of-type > div > div > div:first-of-type";
  const browser = await puppeteer.launch({ headless: false });
  try {
    const page = await browser.newPage("https://web.whatsapp.com/");
    await page.goto("https://web.whatsapp.com/");
    // Set screen size
    // await page.setViewport({width: 1080, height: 1024});
    await page.waitForSelector(searchElement);
    await page.click(searchElement);
    await page.type(searchElement, "89958403");
    await new Promise((resolve) => setTimeout(resolve, 2000));
    await page.waitForSelector(resultsElement);
    await page.click(firstResultElement);
    await page.waitForSelector(writeElement);
    await page.type(writeElement, "Holi");
    // await page.click('button[aria-label="Enviar"]');
  } catch (e) {
    console.log(e);
  }
  await browser.close();
};
