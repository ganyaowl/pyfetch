param (
    [switch]$a
)

function Log {
    param ([string]$Message, [string]$Color = "White")
    if ($a) { Write-Host $Message -ForegroundColor $Color }
}

$pythonExists = Get-Command python -ErrorAction SilentlyContinue

if (-not $pythonExists) {
    Write-Host "Python is not installed! Please install Python and try again." -ForegroundColor Red
    exit 1
}

Log "Creating virtual environment..."
python -m venv .venv

Log "Activating virtual environment..."
.venv\Scripts\Activate

if (Test-Path "requirements.txt") {
    Log "Installing dependencies..."
    pip install -r requirements.txt --quiet
} else {
    Log "requirements.txt not found!" "Yellow"
}

if (Test-Path "pyfetch.py") {
    Log "Running pyfetch.py..."
    python pyfetch.py
} else {
    Log "pyfetch.py not found!" "Red"
}

Start-Sleep -Seconds 5

Log "Deactivating virtual environment..."
deactivate
