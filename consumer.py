import json
from producer import main
import pandas as pd
from kafka import KafkaConsumer












def main():

    print(" Starting data injest from kafka...")

    topic_name = "pokec_user_data_stream"  
    k_consumer_a = KafkaConsumer(topic_name,
                                 bootstrap_servers=["localhost:9092"],
                                 auto_offset_reset="earliest",
                                 value_deserializer=lambda x: json.loads(x.decode("utf-8")))


    for streaming_data in k_consumer_a:

        print(streaming_data.value["AGE"])


if __name__ == "__main__":
    main()