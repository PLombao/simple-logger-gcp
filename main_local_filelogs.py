#################### Configure logging ##################
import json
import os
import logging.config
#########################################################

GCP_LOGGING = True

if __name__ == "__main__":
   #################### Configure logging ##################

    # LOCAL LOG
    with open('config/logging.json', 'r') as json_config:
        json_data = json.load(json_config)
        os.makedirs(os.path.dirname(json_data['handlers']['file']['filename']), exist_ok=True)
        logging.config.dictConfig(json_data)
  
