from doit.action import CmdAction
import requests
import json
import datetime


# def task_create_company():

#     def create_com():
#         url = "https://api2.timedoctor.com:443/api/1.0/register/signup"
#         ts = str(datetime.datetime.now().timestamp()).split(".")[0]
#         company_name = "qa-automation-ulhas-" + ts + "@timedocrtor.dev"
#         email = "xyz-" + ts + "@getnada.com"
#         payload = {
#             "name": company_name,
#             "email": email,
#             "password": "xyz@123",
#             "company": "qa-automation-ulhas",
#             "trackingMode": "",
#             "timezone": "",
#             "referrer": "",
#             "pricingPlan": "",
#             "splitTest": [
#                 {
#                     "name": "",
#                     "value": ""
#                 }
#             ]
#         }
#
#         headers = {
#           'Content-Type': 'application/json'
#         }
#
#         r = requests.post(url=url, data=json.dumps(payload), headers=headers)
#         print(payload)
#         print(r.text.encode('utf8'))
#
#     return {
#         'actions': [create_com],
#         'verbosity': 2,
#     }
#
#
# def task_download_installer():
#
#     def download_file(targets):
#         local_filename = targets[0].split('/')[-1]
#         # NOTE the stream=True parameter below
#         with requests.get(targets[0], stream=True) as r:
#             r.raise_for_status()
#             with open(local_filename, 'wb') as f:
#                 for chunk in r.iter_content(chunk_size=8192):
#                     if chunk:  # filter out keep-alive new chunks
#                         f.write(chunk)
#
#         return local_filename
#
#     return {
#         'actions': [download_file],
#         'targets': ['https://s3.amazonaws.com/sfproc-downloads/3.0.52/windows/bitrock/timedoctor2-setup-3.0.52-windows.exe'],
#         'verbosity': 2,
#     }


def task_vagrant_up():

    def create_cmd_string():
        return "vagrant up"

    return {
        'actions': [CmdAction(create_cmd_string)],
        'verbosity': 2,
        }


def task_start_calculator():

    def create_cmd_string():
        return "VBoxManage guestcontrol 'Windows_Vagrant' run --exe 'C:\\Windows\\System32\\calc.exe' " \
               "--timeout 3000 --username IEUser --password Passw0rd! --putenv 'DISPLAY=:0' --wait-stdout"

    return {
        'actions': [CmdAction(create_cmd_string)],
        'verbosity': 2,
        }


def task_start_browser():

    def create_cmd_string():
        return "VBoxManage guestcontrol 'Windows_Vagrant'" \
               " start --exe 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'" \
               " --username IEUser --password Passw0rd! " \
               " -- --new-window youtube.com"

    return {
        'actions': [CmdAction(create_cmd_string)],
        'verbosity': 2,
        }


def task_vagrant_halt():

    def create_cmd_string():
        return "vagrant suspend"

    return {
        'actions': [CmdAction(create_cmd_string)],
        'verbosity': 2,
        }
