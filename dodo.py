from doit.action import CmdAction
import requests
import json
import datetime


def task_create_company():

    def create_com():
        url = "https://api2.timedoctor.com:443/api/1.0/register/signup"
        ts = str(datetime.datetime.now().timestamp()).split(".")[0]
        company_name = "qa-automation-ulhas-" + ts + "@timedocrtor.dev"
        email = "xyz-" + ts + "@getnada.com"
        payload = {
            "name": company_name,
            "email": email,
            "password": "xyz@123",
            "company": "qa-automation-ulhas",
            "trackingMode": "",
            "timezone": "",
            "referrer": "",
            "pricingPlan": "",
            "splitTest": [
                {
                    "name": "",
                    "value": ""
                }
            ]
        }

        headers = {
          'Content-Type': 'application/json'
        }

        r = requests.post(url=url, data=json.dumps(payload), headers=headers)
        print(payload)
        print(r.text.encode('utf8'))

    return {
        'actions': [create_com],
        'verbosity': 2,
    }

# This is taken care by packer

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

# Build 'virtualbox-ovf' errored: Output directory exists: output-virtualbox-ovf
#
# Use the force flag to delete it prior to building.


def task_packer_build():
    def build_packer_json():
        return "packer build -only virtualbox-ovf packer.json"

    return {
        'actions': [CmdAction(build_packer_json)],
        'verbosity': 2,
    }


def task_import_vm():

    def create_cmd_string():
        return "VBoxManage import output-virtualbox-ovf/windows_10.ovf"

    return {
        'actions': [CmdAction(create_cmd_string)],
        'verbosity': 2,
        }


def task_start_vm():

    def start_vm():
        return "vboxmanage startvm 'windows_10'"

    return {
        'actions': [CmdAction(start_vm)],
        'verbosity': 2,
        }


def task_install_time_doctor():

    def install_time_doctor():
        return "vboxmanage guestcontrol 'windows_10' run --exe 'C:\\Windows\\System32\\cmd.exe' " \
               "--username IEUser --password Passw0rd! " \
               "-- cmd.exe /c 'C:/Users/IEUser/timedoctor2-setup-3.0.52-windows.exe --mode unattended'"

    return {
        'actions': [CmdAction(install_time_doctor)],
        'verbosity': 2,
    }


def task_start_calculator():

    def create_cmd_string():
        return "VBoxManage guestcontrol 'windows_10' run --exe 'C:\\Windows\\System32\\calc.exe' " \
               "--timeout 3000 --username IEUser --password Passw0rd! --putenv 'DISPLAY=:0' --wait-stdout"

    return {
        'actions': [CmdAction(create_cmd_string)],
        'verbosity': 2,
        }


def task_start_browser():

    def create_cmd_string():
        return "VBoxManage guestcontrol 'windows_10'" \
               " start --exe 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'" \
               " --username IEUser --password Passw0rd! " \
               " -- --new-window youtube.com"

    return {
        'actions': [CmdAction(create_cmd_string)],
        'verbosity': 2,
        }
