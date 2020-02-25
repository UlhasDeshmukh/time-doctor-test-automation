cd C:\Users\IEUser\installer
for /r %%i in (*.msi) do SET var1= %%i 
msiexec /i %var1% /qn
