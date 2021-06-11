import os
import os.path as osp

def find_in_dir(dir, filename):
    return osp.exists(osp.join(dir, filename))


mail_credentials_name = 'mail_credentials.json'
current_dir = os.getcwd()
config_dir = osp.expanduser('~/.config/hermes/')

if find_in_dir(current_dir, mail_credentials_name):
    mail_credentials = osp.join(current_dir, mail_credentials_name)
elif find_in_dir(config_dir, mail_credentials_name):
    mail_credentials = osp.join(current_dir, mail_credentials_name)
else:
    mail_credentials = ''


    