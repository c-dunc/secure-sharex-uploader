import sys
sys.path.append('./src')  

import config
import logging

class Vulnerabilities:
    COMMON_SECRETS = ['secret', 'key', 'mySecret']
    COMMON_PATHS = ['i', 'ss', 'file', 'files', 'upload']
    COMMON_ENDPOINTS = ['upload.php', 'up.php', 'sharex.php', 'file.php', 'files.php', 'fileupload.php', 'image.php']
    COMMON_FIELD_NAMES = ['secret', 'key', 'apiKey', 'apikey', 'token', 'api_key']
    COMMON_FORM_NAMES = ['sharex', 'file', 'files', 'image']
    CURRENT_CONFIG =  {k: v for k, v in vars(config).items() if not k.startswith('__')}

def check_vulnerable(): 
    POS_VULN = []
    vulnerable = True
    for attr_name, value in vars(Vulnerabilities).items():
        if not attr_name.startswith('__') and attr_name != 'CURRENT_CONFIG':
            POS_VULN.extend(value)

    for key, value in Vulnerabilities.CURRENT_CONFIG.items():
        if value in POS_VULN:
            print(f"ShareX config is easily guessable, please update your config before using this tool.\n\t\t\t`{key} : {value}` ")
            vulnerable = True
        else:
            vulnerable = False
