# PowerShell Script: build-server.ps1

# Store the original location
$originalLocation = Get-Location

# Change to src-python directory
Set-Location -Path "./src-python"

# Specify the Conda environment name
$condaEnvName = "tensorflow-fastapi"

# Path to Miniconda installation
# Replace with the actual path if Miniconda is installed elsewhere
$condaPath = "C:\Users\YannPro\miniconda3"

# Activate the Conda environment
$activateScript = Join-Path -Path $condaPath -ChildPath "Scripts\Activate.bat"
Write-Host  $activateScript
if (!(Test-Path $activateScript)) {
    Write-Host "Error: Could not find Activate.ps1 at $condaPath. Ensure Miniconda is installed." -ForegroundColor Red
    exit 1
}

Write-Host "Activating Conda environment: $condaEnvName" -ForegroundColor Green
& $activateScript $condaEnvName

# Check if activation was successful
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: Failed to activate Conda environment $condaEnvName." -ForegroundColor Red
    exit 1
}

# Path to Miniconda and the environment
$condaEnvPath = "C:\Users\YannPro\miniconda3\envs\tensorflow-fastapi"
$scriptsPath = Join-Path -Path $condaEnvPath -ChildPath "Scripts"

# Append the environment's Scripts folder to PATH
$env:PATH += ";$scriptsPath"

# Run PyInstaller with the provided .spec file
$specFilePath = "server.spec"  # Adjust path if needed
$distPath = "../src-tauri/bin/"   # Adjust path if needed

Write-Host "Running PyInstaller..." -ForegroundColor Green
pyinstaller --clean --noconfirm $specFilePath --distpath $distPath

# Check if PyInstaller executed successfully
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error: PyInstaller failed to package the server." -ForegroundColor Red
    exit 1
}

Write-Host "Build completed successfully. Server is in $distPath." -ForegroundColor Green
