from doit.action import CmdAction
import requests
import json
import datetime
import time

vm_name = 'windows_10'
td_email = ''
td_password = "xyz@123"


def task_create_company():

    def create_com():
        url = "https://api2.timedoctor.com:443/api/1.0/register/signup"
        ts = str(datetime.datetime.now().timestamp()).split(".")[0]
        company_name = "qa-automation-ulhas-" + ts + "@timedocrtor.dev"
        td_email = "xyz-" + ts + "@getnada.com"
        payload = {
            "name": company_name,
            "email": td_email,
            "password": td_password,
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


# # Build 'virtualbox-ovf' errored: Output directory exists: output-virtualbox-ovf
# #
# # Use the force flag to delete it prior to building.
#
#
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
        cmd_string = "vboxmanage startvm '{0}'".format(vm_name)
        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(start_vm), wait_for_min],
        'verbosity': 2,
        }


def task_copy_files():

    def copy_lock_file():
        cmd_string = "vboxmanage guestcontrol '{0}' copyto ./scripts/lock.bat 'C:\\Users\\IEUser' " \
             " --username IEUser --password Passw0rd! ".format(vm_name)
        return cmd_string

    def copy_enable_nw_file():
        cmd_string = "vboxmanage guestcontrol '{0}' copyto ./scripts/enable_network.bat 'C:\\Users\\IEUser' " \
             " --username IEUser --password Passw0rd! ".format(vm_name)
        return cmd_string

    def copy_disable_nw_file():
        cmd_string = "vboxmanage guestcontrol '{0}' copyto ./scripts/disable_network.bat 'C:\\Users\\IEUser' " \
             " --username IEUser --password Passw0rd! ".format(vm_name)
        return cmd_string

    return {
          'actions': [CmdAction(copy_lock_file), CmdAction(copy_enable_nw_file), CmdAction(copy_disable_nw_file)],
          'verbosity': 2,
    }


def task_install_time_doctor():

    def install_time_doctor():
        cmd_string = "vboxmanage guestcontrol '{0}' run --exe 'C:\\Windows\\System32\\cmd.exe' " \
               "--username IEUser --password Passw0rd! " \
               "-- cmd.exe /c 'C:/Users/IEUser/timedoctor2-setup-3.0.52-windows.exe --mode unattended'".format(vm_name)
        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(install_time_doctor), wait_for_min],
        'verbosity': 2,
    }

# Here we might need to login to TimeDoctor to capture user activities


def task_open_browser_and_navigate_to_verge():

    def create_cmd_string():
        cmd_string = "VBoxManage guestcontrol '{0}'" \
               " start --exe 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'" \
               " --username IEUser --password Passw0rd! " \
               " -- --new-window theverge.com".format(vm_name)

        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(create_cmd_string), wait_for_min],
        'verbosity': 2,
        }


def task_pause_vm():

    def pause_vm():
        cmd_string = "vboxmanage controlvm '{0}' pause".format(vm_name)
        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(pause_vm), wait_for_min],
        'verbosity': 2,
        }


def task_resume_vm_and_wait():

    def resume_vm():
        cmd_string = "vboxmanage controlvm '{0}' resume".format(vm_name)
        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(resume_vm), wait_for_min],
        'verbosity': 2,
        }


def task_open_browser_and_navigate_to_facebook():

    def create_cmd_string():
        cmd_string = "VBoxManage guestcontrol '{0}'" \
               " start --exe 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'" \
               " --username IEUser --password Passw0rd! " \
               " -- --new-window fb.com".format(vm_name)
        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(create_cmd_string), wait_for_min],
        'verbosity': 2,
        }


def task_start_calculator():

    def create_cmd_string():
        cmd_string = "VBoxManage guestcontrol '{0}' run --exe 'C:\\Windows\\System32\\calc.exe' " \
               "--timeout 3000 --username IEUser --password Passw0rd! --putenv 'DISPLAY=:0' " \
                     "--wait-stdout".format(vm_name)
        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(create_cmd_string), wait_for_min],
        'verbosity': 2,
        }


def task_lock_screen():

    def create_cmd_string():
        cmd_string = "vboxmanage guestcontrol '{0}' run --exe 'C:\\Windows\\System32\\cmd.exe' " \
               "--username IEUser --password Passw0rd! " \
               "-- cmd.exe /c 'C:\\Users\\IEUser\\lock.bat'".format(vm_name)
        return cmd_string

    def wait_for_sec():

        time.sleep(5)
    return {
        'actions': [CmdAction(create_cmd_string), wait_for_sec],
        'verbosity': 2,
    }


def task_unlock_screen():

    def enter_password():
        return "VBoxManage controlvm '{0}' keyboardputstring 'Passw0rd!'".format(vm_name)

    def press_enter():
        return "VBoxManage controlvm '{0}' keyboardputscancode 1c 9c".format(vm_name)

    def wait_for_sec():

        time.sleep(5)

    return {
        'actions': [CmdAction(press_enter), wait_for_sec, CmdAction(enter_password),
                    wait_for_sec, CmdAction(press_enter)],
        'verbosity': 2,
    }


def task_wait_and_pause_vm():

    def pause_vm():
        cmd_string = "vboxmanage controlvm '{0}' pause".format(vm_name)
        return cmd_string

    def wait_for_3m():

        time.sleep(180)

    def resume_vm():
        cmd_string = "vboxmanage controlvm '{0}' resume".format(vm_name)
        return cmd_string

    def wait_for_sec():

        time.sleep(10)

    return {
        'actions': [wait_for_3m, CmdAction(pause_vm), wait_for_sec, CmdAction(resume_vm)],
        'verbosity': 2,
    }


def task_disable_network_and_wait():
    def create_cmd_string():
        cmd_string = "vboxmanage guestcontrol '{0}' run --exe 'C:\\Windows\\System32\\cmd.exe' " \
                   "--username IEUser --password Passw0rd! " \
                   "-- cmd.exe /c 'C:\\Users\\IEUser\\disable_network.bat'".format(vm_name)
        return cmd_string

    def wait_for_2m():

        time.sleep(120)

    return {
            'actions': [CmdAction(create_cmd_string), wait_for_2m],
            'verbosity': 2,
    }


def task_enable_network():
    def create_cmd_string():
        cmd_string = "vboxmanage guestcontrol '{0}' run --exe 'C:\\Windows\\System32\\cmd.exe' " \
                   "--username IEUser --password Passw0rd! " \
                   "-- cmd.exe /c 'C:\\Users\\IEUser\\enable_network.bat'".format(vm_name)
        return cmd_string

    return {
            'actions': [CmdAction(create_cmd_string)],
            'verbosity': 2,
    }

# TODO: Uninstall the MSI
# TODO: Check via API if the tracking data was successfully uploaded
#  https://api2.timedoctor.com/#!/activity/getActivityTimeuse
