# Time Doctor Evaluation Task
Find task details [here](/docs/task-description.md) 

## REQUIREMENTS

* [Vagrant](https://www.vagrantup.com/downloads.html) 

* [VirtualBox](https://www.virtualbox.org)

* [pydoit](https://pydoit.org/install.html)

* [chocolatey](https://chocolatey.org/install)



## Steps

* Install Virtual box
    * Download Windows 10 Virtual Box image from [Microsoft official site](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)
    * Import image into Virtual Box, VM created with name "__MSEdge - Win10__" 
    * Change Windows 10 Settings to [Turn off and disable UAC](https://winaero.com/blog/how-to-turn-off-and-disable-uac-in-windows-10/)
    
* Create Vagrant BaseBox
 
    
        # goto default directory
        $ cd VirtualBox\ VMs/
         
        # create base box from VM
        $ vagrant package --base 'MSEdge - Win10' --output Win10x64.box
         
        # add box
        $ vagrant box add ulhas/windows10 Win10x64.box
         
        # check vagrant boxes
        $ vagrant box list
  
    
* Create Vagrant file
        
        
        # goto project folder
        $ cd ~/time-doctor-test-automation
         
        # initializes to be a Vagrant environment
        $ vagrant init ulhas/windows10
         
* Edit [Vagrantfile](Vagrantfile)
         
        
        
* Create and execute [dodo.py](dodo.py) task file
    * Add [tasks](https://pydoit.org/tasks.html) to automate as per Evaluation task details
    * Execute doit 
    ```python
        python3 -m doit
    ```
     
## Reference
* https://softwaretester.info/create-windows-10-vagrant-base-box/
* https://softwaretester.info/create-windows-10-virtualbox-vm/
* https://digitaldrummerj.me/vagrant-overview/
* https://www.taniarascia.com/what-are-vagrant-and-virtualbox-and-how-do-i-use-them/
* https://www.virtualbox.org/manual/UserManual.html#vboxmanage-cmd-overview
* https://www.vagrantup.com/docs/provisioning/
* https://en.jeffprod.com/blog/2019/automating-tasks-in-a-virtualized-os/
* https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
 