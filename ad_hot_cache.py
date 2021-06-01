import json
from producer import main
import pandas as pd
from kafka import KafkaConsumer

# Hot-Cache
# A dict containing keys as smocking-attribute names & values as IDs
smocking_type_user = {}

def main():

    print(" Starting data injest from kafka...")

    topic_name = "pokec_user_data_stream"  
    k_consumer_a = KafkaConsumer(topic_name,
                                 bootstrap_servers=["localhost:9092"],
                                 auto_offset_reset="earliest",
                                 value_deserializer=lambda x: json.loads(x.decode("utf-8")))


    for streaming_data in k_consumer_a:
        
        _id = streaming_data.value["user_id"]   
        _smockingStatus = streaming_data.value["SmokingStatus"]
            
        if _smockingStatus in smocking_type_user:
            smocking_type_user[_smockingStatus].append(_id)
        else:
            smocking_type_user[_smockingStatus] = [_id]


    # Print food_user hot cache
    print(smocking_type_user)

if __name__ == "__main__":
    main()