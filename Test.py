import re
from playwright.sync_api import sync_playwright

def combined_automation_flow():
    print("Starting browser...")
    with sync_playwright() as p:
        # 1. Add a real User-Agent so the website doesn't block GitHub's bots
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # ==========================================
        # PART 1: Click the "Get started" button
        # ==========================================
        print("Navigating to Playwright website...")
        page.goto("https://www.1024terabox.com/wap/referral/4401884469720?abGroup=1&cardType=drainage", wait_until="load")
        
        try:
            print("Page title:", page.title())
            print("Looking for 'Get started' link...")
            
            # 2. Use Regex to ignore upper/lowercase differences (re.IGNORECASE)
            get_started_link = page.get_by_role("link", name=re.compile("get started", re.IGNORECASE)).first
            
            print("Clicking the link...")
            get_started_link.click(timeout=15000)
            
            print("✅ Part 1 Successful: Clicked 'Get started' and moved to the next page!")
                
        except Exception as e:
            print(f"❌ Failed during Part 1: {e}")


        # ==========================================
        # PART 2: Open Login Page and Enter Email
        # ==========================================
        print("\n--- Starting Login Flow Simulation ---")
        
        # NOTE: Replace this URL with your actual target login URL
        #page.goto("https://example.com/login", wait_until="load")

        try:
            # 1. Click the mail image/icon
            print("Looking for mail image to click...")
            mail_icon = page.locator('img[alt="email-icon"]')
            mail_icon.click(timeout=5000)
            
            # 2. Fill the email input field
            print("Looking for email input field...")
            email_input = page.locator('input[type="email"]')
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
