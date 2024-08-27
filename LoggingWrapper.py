import logging
import csv
from functools import wraps
from datetime import datetime

global_log_settings = {
    "save": False,
    "file_name": None,
    "logs": [] 
}

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_setting(save=False, file_name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global_log_settings['save'] = save
            global_log_settings['file_name'] = file_name
            return func(*args, **kwargs)
        return wrapper
    return decorator

def loggingwrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("""\n
        ###########################################
        ###########################################
        """)
        start_message = f"### Starting function: {func.__name__}"
        logging.info(start_message)
        print("""\n
        ###########################################
        ###########################################
              """)
        global_log_settings['logs'].append({'timestamp': datetime.now(), 'level': 'INFO', 'message': start_message})

        try:
            result = func(*args, **kwargs)
            print("""\n
            ###########################################
            ###########################################
            """)
            success_message = f"### Function {func.__name__} completed successfully."
            logging.info(success_message)
            print("""\n
            ###########################################
            ###########################################
            """)
            global_log_settings['logs'].append({'timestamp': datetime.now(), 'level': 'INFO', 'message': success_message})

            if global_log_settings['save']:
                save_logs_to_csv(global_log_settings['logs'], global_log_settings['file_name'])

            return result
        except Exception as e:
            print("""\n
            ###########################################
            ###########################################
            """)
            error_message = f"### Error in function {func.__name__}: {e}"
            logging.error(error_message)
            print("""\n
            ###########################################
            ###########################################
            """)
            global_log_settings['logs'].append({'timestamp': datetime.now(), 'level': 'ERROR', 'message': error_message})
            
            if global_log_settings['save']:
                save_logs_to_csv(global_log_settings['logs'], global_log_settings['file_name'])
            
            raise
    return wrapper

def save_logs_to_csv(logs, base_file_name):
    if base_file_name is None:
        base_file_name = "logs"

    file_name = f"{base_file_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(file_name, 'w', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        log_writer.writerow(['timestamp', 'level', 'message'])
        for log in logs:
            log_writer.writerow([log['timestamp'], log['level'], log['message']])
