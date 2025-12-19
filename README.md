# vitals-producer-anomaly-93

This project generates and pushes random vitals data to a Kafka topic. It includes anomaly injection for heart rate and breaths per minute.

## Usage

1.  Clone the repository:
   ```bash
   git clone https://github.com/Gautam0610/vitals-producer-anomaly-93.git
   cd vitals-producer-anomaly-93
   ```
2.  Create a `.env` file with the following variables:
   ```
   OUTPUT_TOPIC=<your_kafka_topic>
   KAFKA_BOOTSTRAP_SERVERS=<your_kafka_brokers>
   SASL_USERNAME=<your_sasl_username>
   SASL_PASSWORD=<your_sasl_password>
   INTERVAL_MS=1000
   ```
3.  Build the Docker image:
   ```bash
   docker build -t vitals-producer .
   ```
4.  Run the Docker container:
   ```bash
   docker run --env-file .env vitals-producer
   ```