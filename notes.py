from atproto import Client

USERNAME = "jobaeyaert.com"
APP_PASSWORD = "6z62-c2pg-zxqb-t6z4"

client = Client()

try:
    # Attempt login
    client.login(USERNAME, APP_PASSWORD)
    
    # Check if session was created
    if hasattr(client, "session") and client.session:
        print(f"✅ Login successful! Session Token: {client.session.access_jwt}")
    else:
        print("❌ Login failed: Session object not created.")
        
except Exception as e:
    print(f"❌ Login failed: {e}")
