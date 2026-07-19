from playwright.sync_api import sync_playwright

def validate_google_search_button():
    print("Starting browser...")
    with sync_playwright() as p:
        # Launch a headless browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to Google...")
        page.goto("https://www.google.com", wait_until="domcontentloaded")
        
        try:
            # 1. Find the search box and type a letter to reveal the buttons
            print("Typing into search box to reveal buttons...")
            search_box = page.locator('textarea[name="q"], input[name="q"]').first
            search_box.fill("test")
            
            # 2. Wait a brief moment for Google's animation to complete
            page.wait_for_timeout(1000)
            
            # 3. Now validate the 'Google Search' button
            print("Validating 'Google Search' button...")
            # We use .first because Google sometimes has multiple hidden buttons
            search_button = page.locator('input[name="btnK"]').first
            
            # Wait for it to become visible
            search_button.wait_for(state="visible", timeout=5000)
            
            if search_button.is_visible():
                print("✅ Validation Successful: 'Google Search' button is present and visible.")
            else:
                print("❌ Validation Failed: Button is present but not visible.")
                
        except Exception as e:
            print(f"❌ Validation Failed: Could not find the search button. Error: {e}")
            
        # Close the browser
        browser.close()

if __name__ == "__main__":
    validate_google_search_button()
