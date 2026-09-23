import random
import time
from datetime import datetime

pages = [
    "/",
    "/products",
    "/about",
    "/contact",
    "/login"
]

print("Clickstream producer started")

while True:
    event = {
        "user_id": random.randint(1, 100),
        "page": random.choice(pages),
        "timestamp": datetime.now().isoformat()
    }

    print(event)

    time.sleep(2)