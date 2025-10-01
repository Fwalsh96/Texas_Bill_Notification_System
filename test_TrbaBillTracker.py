from playwright.sync_api import sync_playwright
import pandas as pd
import CommonActions
import TirbaFunctions

def test_TrbaBillTracker():
    with sync_playwright() as p:

        # Variables
        fileName = "BillFolder\\BillFile.xlsx"
        df = pd.read_excel(fileName)
        columnNames = df.columns.tolist()
        billList = []

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

        # Search the First Bill in the list
        print(billList[0])
        TirbaFunctions.SearchFirstBill(page, "89(R) - 2025", billList[0])

        # Wait a few seconds
        CommonActions.Wait(5000, page)

        # Compare First Bill
        TirbaFunctions.RunBillComparison(page, billList[0])

        # Loop through the rest of the bills
        page.locator("input[name='NextBill']").fill(billList[1])

        # Wait a few seconds
        CommonActions.Wait(5000, page)

        # Close the Browser Out
        browser.close()
