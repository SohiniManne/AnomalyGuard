from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
TOPIC = 'user_engagement'

def generate_event():
    return {
        'user_id': random.randint(1, 1000),
        'event_type': random.choice(['click', 'view', 'like', 'share']),
        'feature1': random.random(),
        'feature2': random.random(),
        'timestamp': time.time()
    }

if __name__ == "__main__":
    for _ in range(10):  # Generate 10 example events
        event = generate_event()
        producer.send(TOPIC, event)
        print(f"Produced: {event}")
        time.sleep(1)
