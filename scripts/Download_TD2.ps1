# Disable-UAC
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f

[string] $sourceUrl = "https://kwc5w69wa3.execute-api.us-east-1.amazonaws.com/production/msi-filename-redirect?hostname=app.staff.com&companyId=XldH-SQHXgAE9n0Q"
[string] $destPath = "C:/Users/IEUser/installer"

Write-Host "Downloading msi file to local file system"
Function Get-RedirectedUrl {
	Param (
		[Parameter(Mandatory=$true)]
		[String]$URL
	)
	$request = [System.Net.WebRequest]::Create($url)
	$request.AllowAutoRedirect=$false
	$response=$request.GetResponse()

	If ($response.StatusCode -eq "Found"){
		$response.GetResponseHeader("Location")
	}
}

$FileName = ([System.IO.Path]::GetFileName((Get-RedirectedUrl "$sourceUrl")))
$FileName -match "(?<Name>sfproc-\d.*.msi)"
Write-Host $Matches.Name
$TempFileName = $Matches.Name

If(!(test-path $destPath))
{
	New-Item -ItemType Directory -Force -Path $destPath
}

Invoke-WebRequest -uri $sourceUrl -Outfile "$destPath/$TempFileName" 

Write-Host "msi file download completed"
