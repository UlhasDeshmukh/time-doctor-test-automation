# Evaluation task

The main goal is to automate testing of TimeDoctor 2 desktop application (silent) Windows 10.
The test should be repeatable. You must also emulate keyboard and mouse actions throughout
the test. To register test companies, you must use: qa-automation-${your name}-
${timestamp}@timedocrtor.dev

The test should be compatible with local VirtualBox VM and remote execution (preferable AWS
or Google Cloud, but we can also consider using Azure)

Steps:

● Create a new silent company   https://api2.timedoctor.com/#!/auth/registerSignup

● Download the application installer from https://2.timedoctor.com/new/downloads

● Install the MSI file

● Simulate user activity on the computer

    ○ Open a browser and navigate to https://www.theverge.com and wait 1 minute
    ○ Put OS into sleep mode and wait 1 minute
    ○ Resume from the sleep mode and wait 1 minute
    ○ Open a new tab and navigate to https://facebook.com wait 1 minute
    ○ Open Calculator app and wait 1 minute
    ○ Lock and unlock the screen multiple times (100 would be enough) if this can
    happen fast
    ○ Wait 3 minutes and pause the VM
    ○ Disable network connection ( api2.timedoctor.com should not be accessible) wait
    for 2 minutes
    ○ Restore network connection

● Uninstall the MSI

● Check via API if the tracking data was successfully uploaded
https://api2.timedoctor.com/#!/activity/getActivityTimeuse