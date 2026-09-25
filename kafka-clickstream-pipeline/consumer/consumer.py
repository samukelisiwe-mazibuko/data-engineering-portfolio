import json

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "clickstream",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Waiting for clickstream events...")

for message in consumer:
    event = message.value
    print("Received:", event)