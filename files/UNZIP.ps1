$zipFile = Read-Host "Enter ZIP file name (with extension)"
$outputFolder = $PWD

Expand-Archive -Path "$PWD\$zipFile" -DestinationPath $outputFolder -Force
Write-Output "Unzip completed!"
