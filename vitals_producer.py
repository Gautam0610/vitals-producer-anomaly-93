import os
import time
import random
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

# Environment variables
output_topic = os.environ.get('OUTPUT_TOPIC')
kafka_bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
sasl_username = os.environ.get('SASL_USERNAME')
sasl_password = os.environ.get('SASL_PASSWORD')
interval_ms = int(os.environ.get('INTERVAL_MS', 1000))  # Default to 1000ms if not set

# SASL configuration
sasl_mechanism = 'PLAIN'
security_protocol = 'SASL_SSL'

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_servers,
    sasl_plain_username=sasl_username,
    sasl_plain_password=sasl_password,
    security_protocol=security_protocol,
    sasl_mechanism=sasl_mechanism,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_vitals():
    body_temp = round(random.uniform(36.5, 37.5), 1)  # Normal body temp
    heart_rate = random.randint(60, 100)  # Normal heart rate
    systolic = random.randint(110, 140)  # Normal systolic pressure
    diastolic = random.randint(70, 90)  # Normal diastolic pressure
    breaths_per_minute = random.randint(12, 20)  # Normal breaths per minute
    oxygen_saturation = random.randint(95, 100)  # Normal oxygen saturation
    blood_glucose = random.randint(70, 140)  # Normal blood glucose

    # Introduce anomaly
    if random.random() < 0.05:  # 5% chance of anomaly
        heart_rate = random.randint(150, 220)  # Extremely high heart rate
        breaths_per_minute = random.randint(30, 50)  # Extremely high breaths per minute

    return {
        'body_temp': body_temp,
        'heart_rate': heart_rate,
        'systolic': systolic,
        'diastolic': diastolic,
        'breaths_per_minute': breaths_per_minute,
        'oxygen_saturation': oxygen_saturation,
        'blood_glucose': blood_glucose
    }

if __name__ == '__main__':
    try:
        while True:
            vitals = generate_vitals()
            print(f"Sending vitals: {vitals}")
            producer.send(output_topic, vitals)
            time.sleep(interval_ms / 1000)

    except KafkaError as e:
        print(f"Kafka error: {e}")
    except KeyboardInterrupt:
        print("Stopping the producer.")
    finally:
        producer.close()
