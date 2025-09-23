from playwright.sync_api import sync_playwright
import pandas as pd

def test_TrbaBillTracker():
    with sync_playwright() as p:

        # Variables
        fileName = "C:\\Users\\Brack\\Documents\\TRBA Automation\\BillFolder\\BillFile.XLSX"
        df = pd.read_excel(fileName)
        columnNames = df.columns.tolist()
        billList = []
        # rowNames = df

        # Create a list of the bill numbers
        for index, row in df.iterrows():
            firstItem = row.iloc[0]
            billList.append(firstItem)

        # Printing the List for debugging sake
        for x in billList:
            print(x)

        # Opens the browser and a new page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Goes to the Texas Lege site
        page.goto("https://capitol.texas.gov/")

        # Assert that we are on the correct page
        assert "TLO" in page.title()

        # Wait a few seconds
        Wait(3000)

        # Search the first bill
        page.locator("input[name='txtBill']").highlight()
        page.locator("input[name='txtBill']").type(billList[0])

        # Wait a few seconds
        Wait(3000)

        # Click the submit button
        page.locator("input[name='btnSubmit']").click()
        
        # Wait a few seconds
        Wait(5000)

        # Close the Browser Out
        browser.close()

# function to wait a few seconds
def Wait(time, page):
    page.wait_for_timeout(time)

    