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
            # Give the page a brief moment to render
            page.wait_for_timeout(1000)
            
            # Find the link by searching for an <a> tag containing the text "Get started"
            print("Looking for 'Get started' link...")
            get_started_link = page.locator('a:has-text("Get started")').first
            
            # Wait for it to be visible on the screen
            get_started_link.wait_for(state="visible", timeout=10000)
            
            # Validate it
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
