# Disable-UAC
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f

[string] $sourceUrl = "https://kwc5w69wa3.execute-api.us-east-1.amazonaws.com/production/msi-filename-redirect?hostname=app.staff.com&companyId=XlVFRsuBAgAEU-yp"
[string] $destPath = "C:/Users/IEUser/installer"

If(!(test-path $destPath))
{
	New-Item -ItemType Directory -Force -Path $destPath
}

Write-Host "Copying Exe file to local file system"
Invoke-WebRequest -Uri $sourceUrl -OutFile $destPath

Write-Host "msi file downloaded"
