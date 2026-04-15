import time
from garminconnect import Garmin
from credentials import email, password

def vibe_check_login():
    print("📶 Make sure your Hotspot is connected...")
    print("⏳ Waiting 30 seconds to look 'Human' (Garmin's new 2026 requirement)...")
    
    # This delay helps bypass the Cloudflare 'instant-bot' detection
    time.sleep(30)
    
    try:
        print("🔑 Attempting side-door login...")
        # We tell the library to use the 'Garth' engine specifically
        api = Garmin(email, password)
        api.login()
        
        print("✅ SUCCESS! We are in.")
        print(f"👋 Hello, {api.display_name}")
        return api
        
    except Exception as e:
        print(f"❌ Result: {e}")
        return None

if __name__ == "__main__":
    vibe_check_login()