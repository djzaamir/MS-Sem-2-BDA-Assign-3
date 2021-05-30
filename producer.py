import json
import pandas as pd 
from kafka import KafkaProducer
import threading


def producer(topic_name, file_a_uri):

    # Loading data 
    df_pokec_a = pd.read_csv(file_a_uri)


    k_producer_a = KafkaProducer(bootstrap_servers=["localhost:9092"],
                               value_serializer=lambda x: json.dumps(x).encode("utf-8")                              )

     # Start Streaming data to apache-kafka
    for data_tuple in df_pokec_a.itertuples():

        obj_to_stream = {}
        for col_i in range(df_pokec_a.columns.shape[0]):
            obj_to_stream[df_pokec_a.columns[col_i]] = data_tuple[col_i]
        
        k_producer_a.send(topic=topic_name,value=obj_to_stream)

        break


def main():

    topic_name = "pokec_user_data_stream" 

    file_a_uri = "/home/djzaamir/Desktop/Pokec_Cleaned_Data/pokec_chunk_a.csv"
    file_b_uri = "/home/djzaamir/Desktop/Pokec_Cleaned_Data/pokec_chunk_b.csv"
    file_c_uri = "/home/djzaamir/Desktop/Pokec_Cleaned_Data/pokec_chunk_c.csv"
    


    t1 = threading.Thread(target=producer, args=(topic_name, file_a_uri))
    t1.start()
    
    t1.join()

if __name__ == "__main__":
    main()