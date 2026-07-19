from playwright.sync_api import sync_playwright

def validate_google_search_button():
    print("Starting browser...")
    with sync_playwright() as p:
        # Launch a headless browser (runs in the background)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to Google...")
        page.goto("https://www.google.com")
        
        # Google's "Google Search" button usually has the name 'btnK'
        # We wait for it to appear on the page
        try:
            search_button = page.wait_for_selector('input[name="btnK"]', timeout=5000)
            
            # Validate if the button is visible
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
