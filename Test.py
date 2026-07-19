
from playwright.sync_api import sync_playwright

def validate_get_started_button():
    print("Starting browser...")
    with sync_playwright() as p:
        # Launch a headless browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to Playwright website...")
        page.goto("https://www.1024terabox.com/wap/referral/4401884469720?abGroup=1&cardType=drainage", wait_until="domcontentloaded")
        
        try:
            # 1. Find the "Get started" link by its exact text
            print("Looking for 'Get started' link...")
            get_started_link = page.get_by_role("link", name="Get Started")
            
            # 2. Wait for it to be visible on the screen
            get_started_link.wait_for(state="visible", timeout=10000)
            
            # 3. Validate it
            if get_started_link.is_visible():
                print("✅ Validation Successful: 'Get started' link is present and visible.")
            else:
                print("❌ Validation Failed: Link is present but not visible.")
                
        except Exception as e:
            print(f"❌ Validation Failed: Could not find the link. Error: {e}")
            
        # Close the browser
        browser.close()

if __name__ == "__main__":
    validate_get_started_button()
