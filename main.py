import pandas as pd
import json
import datetime 
import os
from google.cloud import pubsub_v1
import time 
from LoggingWrapper import *
log_setting(save=False, file_name=None)
from config.conf import Conf

@loggingwrapper
def initialize_pubsub():
    conf_info = Conf.conf()

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = conf_info["json_key"]
    project_id = conf_info["project_id"]
    topic_name = conf_info["topic_name"]

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    return topic_path, publisher

@loggingwrapper
def read_data_and_publish():
    df = pd.read_csv("MOCK_DATA.csv")
    df.info()
    
    topic_path, publisher = initialize_pubsub()
    
    for index, row in df.iterrows():
        row_data = row.to_dict()
        row_data["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        
        publish_message(row_data, topic_path, publisher)
        print(f"Published row {index}")
        time.sleep(5)
        
@loggingwrapper
def publish_message(data, topic_path, publisher):
    message_data = json.dumps(data).encode("utf-8")

    future = publisher.publish(topic_path, data=message_data)
    print(f"Published message ID: {future.result()}")

if __name__ == "__main__":
    read_data_and_publish()
