from playwright.sync_api import sync_playwright

def combined_automation_flow():
    print("Starting browser...")
    with sync_playwright() as p:
        # Added a standard desktop viewport so the website loads the desktop layout
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        # ==========================================
        # PART 1: Click the "Get started" button
        # ==========================================
        print("Navigating to Playwright website...")
        page.goto("https://www.1024terabox.com/wap/referral/4401884469720?abGroup=1&cardType=drainage", wait_until="domcontentloaded")
        
        try:
            print("Looking for 'Get started' link...")
            get_started_link = page.locator('a:has-text("Get started")').first
            
            # Playwright's .click() automatically waits for the element to be visible and clickable!
            print("Clicking the link...")
            get_started_link.click(timeout=20000)
            
            print("✅ Part 1 Successful: Clicked 'Get started' and moved to the next page!")
                
        except Exception as e:
            print(f"❌ Failed during Part 1: {e}")


        # ==========================================
        # PART 2: Open Login Page and Enter Email
        # ==========================================
        print("\n--- Starting Login Flow Simulation ---")
        
        # NOTE: Replace this URL with your actual target login URL
       # page.goto("https://example.com/login", wait_until="domcontentloaded")

        try:
            # 1. Click the mail image/icon
            print("Looking for mail image to click...")
            mail_icon = page.locator('img[alt="email-icon"]')
            # Click automatically waits up to 5 seconds (default) or specified timeout
            mail_icon.click(timeout=5000)
            
            # 2. Fill the email input field
            print("Looking for email input field...")
            email_input = page.locator('input[type="email"]')
            # Fill also automatically waits for the input to be ready
            email_input.fill("hussain.17eee.rymec@gmail.com")
            
            # 3. Click the "Continue" button
            print("Looking for 'Continue' button...")
            continue_button = page.locator('button:has-text("Continue")')
            continue_button.click(timeout=5000)
            
            print("✅ Login flow actions completed successfully.")
            
        except Exception as e:
            print(f"❌ Login flow failed. Error: {e}")
            print("NOTE: Part 2 will fail here until you replace the placeholders with real ones.")
            
        browser.close()

if __name__ == "__main__":
    combined_automation_flow()
