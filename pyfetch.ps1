$pythonExists = Get-Command python -ErrorAction SilentlyContinue
$debug = $false

if ($args -contains "-a") {
    $debug = $true
}

$debug && Write-Host "Checking Python installation..."

if (-not $pythonExists) {
    $debug && Write-Host "Python is not installed! Please install it and try again." -ForegroundColor Red
    exit 1
}

$debug && Write-Host "Creating Virtual Environment..."
python -m venv .venv

$debug && Write-Host "Activating VENV..."
& .venv\Scripts\Activate

if (Test-Path requirements.txt) {
    $debug && Write-Host "Installing dependencies..."
    pip install -r requirements.txt --quiet
} else {
    $debug && Write-Host "requirements.txt wasn't found!" -ForegroundColor Yellow
}

if (Test-Path pyfetch.py) {
    $debug && Write-Host "Running program..."
    python pyfetch.py
} else {
    $debug && Write-Host "pyfetch.py wasn't found!" -ForegroundColor Red
}

Start-Sleep -Seconds 3

$debug && Write-Host "Deactivating VENV..."
& .venv\Scripts\deactivate
