@echo off
set /p zipFile=Enter ZIP file name (with extension): 
set outputFolder=%CD%

powershell -Command "Expand-Archive -Path '%CD%\\%zipFile%' -DestinationPath '%outputFolder%' -Force"
echo Unzip completed!
pause