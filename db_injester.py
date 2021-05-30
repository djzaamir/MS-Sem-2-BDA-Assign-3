import kafka
from pymongo import MongoClient
from kafka import KafkaConsumer
import pprint








def main():

    k_consumer = KafkaConsumer()
    mongo_client = MongoClient()

    db = mongo_client["yolo_db"]

    r = db.users.insert_one({
        "name" : "Aik tha cheeta",
        "age" : 27
    })

    
    for doc in db.users.find():
        pprint.pprint(doc)

if __name__ == "__main__":
    main()