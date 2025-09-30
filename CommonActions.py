from playwright.sync_api import sync_playwright
import pandas as pd


# function to wait a few seconds
def Wait(time, page):
    page.wait_for_timeout(time)

def SelectSession(page, option):
    # page.locator("select[name*='LegSess']").highlight()
    page.locator("select[name*='LegSess']").select_option(option)
    