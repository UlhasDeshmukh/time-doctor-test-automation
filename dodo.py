from doit.action import CmdAction
import requests
import json
import datetime
import time

vm_name = 'windows_10'
td_email = ''
td_password = "xyz@123"
td_companyid = ''
td_user = ''
td_token = ''


def task_create_company():

    def create_com():
        global td_companyid, td_user, td_token

        url = "https://api2.timedoctor.com:443/api/1.0/register/signup"
        ts = str(datetime.datetime.now().timestamp()).split(".")[0]
        company_name = "qa-automation-ulhas-" + ts + "@timedocrtor.dev"
        td_email = "xyz-" + ts + "@getnada.com"
        payload = {
            "name": company_name,
            "email": td_email,
            "password": td_password,
            "company": "qa-automation-ulhas",
            "trackingMode": "silent",
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

        output = json.loads(r.text)
        print(r.text.encode('utf8'))
        print(payload)

        td_companyid = output['data']['companyId']
        td_user = output['data']['userId']
        td_token = output['data']['token']

        print(td_token)
        print(td_companyid)
        print(td_user)

        with open('./scripts/Download_TD2.ps1', 'w') as file:  # Use file to refer to the file object
            file.write("# Disable-UAC\n")
            file.write('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" '
                       '/v EnableLUA /t REG_DWORD /d 0 /f\n\n')
            file.write('[string] $sourceUrl = "https://kwc5w69wa3.execute-api.us-east-1.amazonaws.com/production'
                       '/msi-filename-redirect?hostname=app.staff.com&companyId={0}"\n'.format(td_companyid))
            file.write('[string] $destPath = "C:/Users/IEUser/installer"\n\n')
            file.write('If(!(test-path $destPath))\n')
            file.write('{\n\tNew-Item -ItemType Directory -Force -Path $destPath\n}\n\n')
            file.write('Write-Host "Copying Exe file to local file system"\n')
            file.write('Invoke-WebRequest -Uri $sourceUrl -OutFile $destPath\n\n')
            file.write('Write-Host "msi file downloaded"\n')

    return {
        'actions': [create_com],
        'verbosity': 2,
    }


# # Build 'virtualbox-ovf' errored: Output directory exists: output-virtualbox-ovf
# #
# # Use the force flag to delete it prior to building.
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

    def copy_install_td_file():
        cmd_string = "vboxmanage guestcontrol '{0}' copyto ./scripts/install_td.bat 'C:\\Users\\IEUser\\installer' " \
             " --username IEUser --password Passw0rd! ".format(vm_name)
        return cmd_string

    def copy_uninstall_td_file():
        cmd_string = "vboxmanage guestcontrol '{0}' copyto ./scripts/uninstall_td.bat 'C:\\Users\\IEUser\\installer' " \
             " --username IEUser --password Passw0rd! ".format(vm_name)
        return cmd_string

    return {
          'actions': [CmdAction(copy_lock_file), CmdAction(copy_enable_nw_file), CmdAction(copy_disable_nw_file),
                      CmdAction(copy_install_td_file), CmdAction(copy_uninstall_td_file)],
          'verbosity': 2,
    }


def task_install_time_doctor():

    def install_time_doctor():
        cmd_string = "vboxmanage guestcontrol '{0}' run --exe 'C:\\Windows\\System32\\cmd.exe' " \
               "--username IEUser --password Passw0rd! " \
               "-- cmd.exe /c 'C:\\Users\\IEUser\\installer\\install_td.bat'".format(vm_name)
        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(install_time_doctor), wait_for_min],
        'verbosity': 2,
    }


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

def task_uninstall_time_doctor():

    def install_time_doctor():
        cmd_string = "vboxmanage guestcontrol '{0}' run --exe 'C:\\Windows\\System32\\cmd.exe' " \
               "--username IEUser --password Passw0rd! " \
               "-- cmd.exe /c 'C:\\Users\\IEUser\\installer\\uninstall_td.bat'".format(vm_name)
        return cmd_string

    def wait_for_min():
        time.sleep(60)

    return {
        'actions': [CmdAction(install_time_doctor), wait_for_min],
        'verbosity': 2,
    }


def task_verify_tracking_data_uploaded():

    def verify_tracking_data_uploaded():
        global td_companyid
        url = "https://api2.timedoctor.com:443/api/1.0/activity/timeuse"

        params = {
            'company': td_companyid,
            'user': td_user,
            'token': td_token,
        }

        r = requests.get(url=url, params=params)
        print(r.text.encode('utf8'))

    return {
        'actions': [verify_tracking_data_uploaded],
        'verbosity': 2,
    }
