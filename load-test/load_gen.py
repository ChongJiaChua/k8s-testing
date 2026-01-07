import time
import urllib.request

URL = "http://guestbook-ui.test-app.svc.cluster.local"

print("Start") #log start

# while True:
#     try:
#         response = urllib.request.urlopen(URL)
#         print(f"Sent, Status Code: {response.getcode()}")
#     except Exception as e:
#         print(f"Error: {e}")
    
#     time.sleep(0.01)