# Time Doctor Evaluation Task
Find task details [here](/docs/task-description.md) 

## REQUIREMENTS

* [Packer](https://packer.io/downloads.html) 

* [VirtualBox](https://www.virtualbox.org)

* [pydoit](https://pydoit.org/install.html)



## Steps

* Install Virtual box
    * Download Windows 10 Virtual Box image from [Microsoft official site](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)
    * Unzip file
    
    
* Edit [packer.json](packer.json) file
        
        
        # goto project folder
        $ cd ~/time-doctor-test-automation
         
        # Edit Packer jason and update source_path to path where VM image file unzipped 
        "source_path": "/Users/ulhas/Downloads/MSEdge-Win10/MSEdge-Win10.ovf",
         

* Execute [dodo.py](dodo.py) task file
    * Execute doit 
    ```python
        python3 -m doit
    ```
     
## Reference
* https://packer.io/docs/index.html
* https://github.com/StefanScherer/packer-windows
* https://github.com/dylanmei/packer-windows-templates/blob/master/windows_2012_r2/vbox-iso.json
*https://packer.io/docs/builders/virtualbox-ovf.html#http-directory-configuration
* https://www.virtualbox.org/manual/UserManual.html#vboxmanage-cmd-overview
* https://en.jeffprod.com/blog/2019/automating-tasks-in-a-virtualized-os/
* http://ramblings.narrabilis.com/node/374
* https://www.advancedinstaller.com/user-guide/msiexec.html
 
