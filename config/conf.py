import os 


class Conf:
    path: str = ("/YOUR/PATH/TO/KEY.json") 
    
    def conf() -> dict:
        json_key: str = Conf.path
        project_id = "pubsub-my-project"
        topic_name = "my-pubsub-topic"
        
        conf_info = {
            "json_key": json_key,
            "project_id": project_id,
            "topic_name": topic_name
        }
        
        return conf_info
