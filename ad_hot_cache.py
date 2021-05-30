import json
from producer import main
import pandas as pd
from kafka import KafkaConsumer

# Hot-Cache
# A dict containing keys as food names & values as IDs
food_user = {}

def main():

    print(" Starting data injest from kafka...")

    topic_name = "pokec_user_data_stream"  
    k_consumer_a = KafkaConsumer(topic_name,
                                 bootstrap_servers=["localhost:9092"],
                                 auto_offset_reset="earliest",
                                 value_deserializer=lambda x: json.loads(x.decode("utf-8")))


    for streaming_data in k_consumer_a:
        print(food_user)
        _id = streaming_data.value["user_id"]
        for f in streaming_data.value["I_most_enjoy_good_food"].split():
            
            if f in food_user:
                food_user[f].append(_id)
            else:
                food_user[f] = [_id]


    # Print food_user hot cache
    print(food_user)

if __name__ == "__main__":
    main()