from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import math


def euclidDistance(a,b):

    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2) + ((a[3] - b[3]) ** 2))


def main():

    topic_name = "pokec_user_data_stream" 
    k_groups = ["a", "b","c", "d", "e"]
    # List of centroids obtained by running KMeans on historical data
    centroids = [[ 17.06885379, 150.18104496,  39.91130012,  17.88511185]
                 [ 22.42164308, 181.86572316,  73.81014843,  22.39042891]
                 [ 24.60374415, 185.90119605,  93.33541342,  27.11410181]
                 [ 20.92698048, 172.24845006,  62.7836969,   21.21083215]
                 [ 20.24362774, 163.56431535,  52.43301719,  19.7061175 ]]

    k_consumer = KafkaConsumer(topic_name,
                               bootstrap_servers=["localhost:9092"],
                               auto_offset_reset="earliest",
                               value_deserializer=lambda x: json.loads(x.decode("utf-8")))

    m_client = MongoClient()

    for stream_data in k_consumer:

        lowest_distance = math.inf
        group = None
        new_entry = [stream_data.value["AGE"] , stream_data.value["Height"], stream_data.value["Weight"],stream_data.value["BMI"]]
        for (i,center) in enumerate(centroids):
            d = euclidDistance(center, new_entry)
            if d < lowest_distance:
                lowest_distance = d
                group = k_groups[i]

        #Push to mongo
        m_client.k_means.k_m_c.insert_one({"group" : group  })




if __name__ == "__main__":
    main()