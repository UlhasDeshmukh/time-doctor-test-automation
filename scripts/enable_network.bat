@echo off
net session >NUL 2>&1 || powershell Start-Process '%0' -Verb RunAs&& exit /b|| exit /b
netsh interface set interface Ethernet enable