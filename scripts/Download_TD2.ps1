# Invoke-WebRequest https://s3.amazonaws.com/sfproc-downloads/3.0.52/windows/bitrock/timedoctor2-setup-3.0.52-windows.exe -OutFile C:/Users/IEUser/timedoctor2-setup-3.0.52-windows.exe

[string] $isoFile = "timedoctor2-setup-3.0.52-windows.exe"
[string] $sourceUrl = "https://s3.amazonaws.com/sfproc-downloads/3.0.52/windows/bitrock/timedoctor2-setup-3.0.52-windows.exe"
[string] $destPath = "C:/Users/IEUser/$isoFile"

Write-Host "Copying Exe file to local file system"
Invoke-WebRequest -Uri $sourceUrl -OutFile $destPath

Write-Host "Exe file downloaded"

# Disable-UAC
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f