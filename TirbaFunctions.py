from playwright.sync_api import sync_playwright
import pandas as pd
import CommonActions

def RunBillComparison(page, BillNum):
    
    # Get page values
    OnPageBillNum = page.locator("span[text='" + BillNum + "']")
    print(BillNum)

    # Validate the Text on the page is the same as in the file
    if((BillNum == OnPageBillNum) and (1 + 1 == 2)): # If its the same, report back 'Same'
        print("Same")
    else: # Otherwise write in the file
        print("Not Same")

    
    # Basic Method
    print(BillNum)
