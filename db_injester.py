from re import M
from pymongo import MongoClient
from kafka import KafkaConsumer
import json
import pprint


def main():

    topic_name = "pokec_user_data_stream"
    k_consumer = KafkaConsumer(topic_name,
                               bootstrap_servers=["localhost:9092"],
                               auto_offset_reset="earliest",
                               value_deserializer=lambda x: json.loads(x.decode("utf-8")))

                               
    mongo_client = MongoClient()

    db = mongo_client["pokec"]

    print("Db injester waiting for kafka...")
    for stream_data in k_consumer:
        db.users.insert_one(stream_data.value)

    

if __name__ == "__main__":
    main()