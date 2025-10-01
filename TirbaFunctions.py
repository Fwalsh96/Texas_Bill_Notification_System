from playwright.sync_api import sync_playwright
import pandas as pd
import CommonActions

def SearchFirstBill(page, session, firstBill):
        
    # Wait a few seconds
    CommonActions.Wait(3000, page)

    # Select the Legislative Session
    CommonActions.SelectSession(page, session)

    # Select the Bill Number
    page.locator("input[value='rbBillNumber']").click()

    # Search the first bill
    page.locator("input[name='txtBill']").type(firstBill)

    # Wait a few seconds
    CommonActions.Wait(3000, page)

    # Click the submit button
    page.locator("input[name='btnSubmit']").click()


def RunBillComparison(page, BillNum):
    
    # Get page values
    OnPageBillNum = page.locator("span[id='usrBillInfoTabs_lblBill']").inner_text()

    print("On Page Bill Num: " + OnPageBillNum)

    # Validate the Text on the page is the same as in the file
    if(BillNum == OnPageBillNum): # If its the same, report back 'Same'
        print("Same")
    else: # Otherwise write in the file
        print("Not Same")

    # Basic Method
    print(BillNum)
