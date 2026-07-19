from playwright.sync_api import sync_playwright

def combined_automation_flow():
    print("Starting browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # ==========================================
        # PART 1: Click the "Get started" button
        # ==========================================
        print("Navigating to Playwright website...")
        page.goto("https://www.1024terabox.com/wap/referral/4401884469720?abGroup=1&cardType=drainage", wait_until="domcontentloaded")
        
        try:
            page.wait_for_timeout(1000)
            print("Looking for 'Get started' link...")
            get_started_link = page.locator('a:has-text("Get Started")').first
            get_started_link.wait_for(state="visible", timeout=30000)
            
            if get_started_link.is_visible():
                print("✅ Validation Successful: 'Get started' link found. Clicking it now...")
                # Click the button to proceed
                get_started_link.click()
                page.wait_for_timeout(2000) # Wait for the next page to load
            else:
                print("❌ Validation Failed: Link is present but not visible.")
                
        except Exception as e:
            print(f"❌ Failed during Part 1: {e}")


        # ==========================================
        # PART 2: Open Login Page and Enter Email
        # ==========================================
        print("\n--- Starting Login Flow Simulation ---")
        
        # NOTE: Replace this URL with your actual target login URL
        page.goto("https://www.1024terabox.com/wap/referral/4401884469720?abGroup=1&cardType=drainage", wait_until="domcontentloaded")

        try:
            # 1. Click the mail image/icon
            # NOTE: Replace 'img[alt="email-icon"]' with the actual CSS selector of the image
            print("Looking for mail image to click...")
            mail_icon = page.locator('img[alt="email-icon"]')
            mail_icon.wait_for(state="visible", timeout=5000)
            mail_icon.click()
            
            # 2. Wait for the email input field to appear
            # NOTE: Replace 'input[type="email"]' with the actual CSS selector of the input box
            print("Looking for email input field...")
            email_input = page.locator('input[type="email"]')
            email_input.wait_for(state="visible", timeout=5000)
            
            # 3. Enter the email address
            print("Entering email address...")
            email_input.fill("hussain.17eee.rymec@gmail.com")
            
            # 4. Click the "Continue" button
            # NOTE: Replace the text "Continue" if the button says something else
            print("Looking for 'Continue' button...")
            continue_button = page.locator('button:has-text("Continue")')
            continue_button.click()
            
            print("✅ Login flow actions completed successfully.")
            
        except Exception as e:
            print(f"❌ Login flow failed. Error: {e}")
            print("NOTE: Part 2 will fail here until you replace the placeholder selectors with real ones from your target website.")
            
        browser.close()

if __name__ == "__main__":
    combined_automation_flow()
