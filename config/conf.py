import os 


class Conf:
    path: str = ("/home/cagri/Desktop/code/python/assoicate_cloud_engineer" \
                 "/pubsub/config/pubsub-my-project-633da0ae8ee2.json") 
    
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