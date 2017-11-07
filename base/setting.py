import os
import configobj

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

BASE_DIR = os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))
)

config = configobj.ConfigObj(os.path.join(BASE_DIR, 'base/config.ini'), encoding='utf-8')

# desired_caps config
DESIRED_CAPS = config['desired_caps']

# mail config
MAIL_HOST = config['mail']['email_host']
MAIL_PORT = config['mail']['email_port']
MAIL_HOST_USER = config['mail']['email_host_user']
MAIL_HOST_PASSWORD = config['mail']['email_host_password']
MAIL_TO = config['mail']['email_to']
MAIL_HEADER = config['mail']['email_header']

# other config
IMAGE_IP = config['other']['image_ip']
LOG_LEVEL = config['other']['log']
CASE_LEVEL = int(config['other']['case_level'])

if __name__ == '__main__':
    # port = config['mail']['email_port']
    print(BASE_DIR)



