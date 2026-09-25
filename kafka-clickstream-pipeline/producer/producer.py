import random
import time
from datetime import datetime
import json

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

pages = [
    "/",
    "/products",
    "/about",
    "/contact",
    "/login"
]

print("Sending events to Kafka...")
while True:
    event = {
        "user_id": random.randint(1, 100),
        "page": random.choice(pages),
        "timestamp": datetime.now().isoformat()
    }

    producer.send("clickstream", event)

    print("Sent:", event)

    time.sleep(2)