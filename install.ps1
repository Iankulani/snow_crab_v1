# SNOW-CRAB-V1 Installation Script for Windows PowerShell
# Usage: .\install.ps1
# Or with execution policy bypass: powershell -ExecutionPolicy Bypass -File install.ps1

#Requires -Version 5.1

param(
    [switch]$SkipDependencies,
    [switch]$SkipVenv,
    [switch]$Force
)

# Set error action
$ErrorActionPreference = "Stop"

# Colors
function Write-Color {
    param(
        [string]$Text,
        [string]$Color = "White"
    )
    Write-Host $Text -ForegroundColor $Color
}

function Write-Banner {
    Write-Color @"
╔══════════════════════════════════════════════════════════════════════════════╗
║        ❄️ SNOW-CRAB-V1 Installation Script v1.0.0                          ║
║        Ultimate Cybersecurity Command & Control Platform                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
"@ -Color Cyan
}

function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Test-Python {
    try {
        $pythonVersion = python --version 2>&1
        if ($pythonVersion -match "Python (\d+\.\d+)") {
            $version = [Version]$matches[1]
            if ($version -ge [Version]"3.7") {
                Write-Color "[+] Python $version found" -Color Green
                return $true
            } else {
                Write-Color "[X] Python $version found, but 3.7+ required" -Color Red
                return $false
            }
        }
    } catch {
        Write-Color "[X] Python not found" -Color Red
        return $false
    }
    return $false
}

function Install-Python {
    Write-Color "[*] Python not found. Installing..." -Color Blue
    
    # Try winget
    try {
        winget install Python.Python.3.11 --accept-package-agreements --accept-source-agreements
        Write-Color "[+] Python installed via winget" -Color Green
        return $true
    } catch {
        Write-Color "[!] Winget not available, trying direct download..." -Color Yellow
    }
    
    # Direct download
    $pythonUrl = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
    $pythonInstaller = "$env:TEMP\python-installer.exe"
    
    Write-Color "[*] Downloading Python installer..." -Color Blue
    Invoke-WebRequest -Uri $pythonUrl -OutFile $pythonInstaller
    
    Write-Color "[*] Installing Python..." -Color Blue
    Start-Process -FilePath $pythonInstaller -Args "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    
    Remove-Item $pythonInstaller -Force
    
    # Refresh PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
    
    return (Test-Python)
}

function Install-SystemDependencies {
    Write-Color "[*] Installing system dependencies..." -Color Blue
    
    $dependencies = @(
        @{Name="nmap"; Url="https://nmap.org/dist/nmap-7.94-setup.exe"; Args="/S"},
        @{Name="curl"; Url="https://curl.se/windows/dl-8.4.0_1/curl-8.4.0_1-win64-mingw.zip"; IsZip=$true},
        @{Name="wget"; Url="https://eternallybored.org/misc/wget/1.21.4/64/wget.exe"; IsExe=$true}
    )
    
    # Check if Chocolatey is installed
    try {
        choco --version | Out-Null
        Write-Color "[+] Chocolatey found, using it for installations" -Color Green
        
        $packages = @("nmap", "curl", "wget", "netcat", "openssh")
        foreach ($pkg in $packages) {
            try {
                choco install $pkg -y --no-progress 2>$null
                Write-Color "  [+] $pkg installed" -Color Green
            } catch {
                Write-Color "  [!] Failed to install $pkg" -Color Yellow
            }
        }
    } catch {
        Write-Color "[!] Chocolatey not found, skipping system tools installation" -Color Yellow
        Write-Color "    Install Chocolatey from https://chocolatey.org for better support" -Color Yellow
    }
}

function New-VirtualEnvironment {
    Write-Color "[*] Creating virtual environment..." -Color Blue
    
    if ((Test-Path "venv") -and $Force) {
        Write-Color "[*] Removing existing virtual environment..." -Color Yellow
        Remove-Item -Recurse -Force "venv"
    }
    
    if (-not (Test-Path "venv")) {
        python -m venv venv
        if ($LASTEXITCODE -ne 0) {
            throw "Failed to create virtual environment"
        }
    }
    
    Write-Color "[+] Virtual environment ready" -Color Green
}

function Install-PythonDependencies {
    Write-Color "[*] Installing Python dependencies..." -Color Blue
    
    # Activate virtual environment
    & ".\venv\Scripts\Activate.ps1"
    
    # Upgrade pip
    python -m pip install --upgrade pip setuptools wheel --quiet
    
    if (Test-Path "requirements.txt") {
        pip install -r requirements.txt --quiet
    } else {
        Write-Color "[!] requirements.txt not found, installing core packages..." -Color Yellow
        
        $corePackages = @(
            "colorama",
            "requests",
            "psutil",
            "paramiko",
            "scapy",
            "dnspython",
            "whois",
            "flask",
            "flask-socketio",
            "flask-cors",
            "reportlab",
            "matplotlib",
            "numpy",
            "qrcode",
            "pillow",
            "beautifulsoup4",
            "tabulate",
            "termcolor"
        )
        
        pip install $corePackages --quiet
    }
    
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to install Python dependencies"
    }
    
    Write-Color "[+] Python dependencies installed" -Color Green
}

function New-DirectoryStructure {
    Write-Color "[*] Creating directory structure..." -Color Blue
    
    $directories = @(
        ".snow_crab_v1",
        ".snow_crab_v1\payloads",
        ".snow_crab_v1\workspaces",
        ".snow_crab_v1\scans",
        ".snow_crab_v1\reports",
        ".snow_crab_v1\phishing_templates",
        ".snow_crab_v1\captured_credentials",
        ".snow_crab_v1\ssh_keys",
        ".snow_crab_v1\traffic_logs",
        ".snow_crab_v1\graphics",
        ".snow_crab_v1\web_templates",
        ".snow_crab_v1\sessions",
        ".snow_crab_v1\spear_phishing",
        ".snow_crab_v1\email_templates",
        ".snow_crab_v1\dos_logs",
        ".snow_crab_v1\agents",
        ".snow_crab_v1\c2_logs",
        ".snow_crab_v1\modules",
        ".snow_crab_v1\network_monitor",
        ".snow_crab_v1\keylog_exfil",
        ".snow_crab_v1\deployments",
        ".snow_crab_v1\domain_hosting",
        ".snow_crab_v1\cracking",
        ".snow_crab_v1\arp_logs",
        ".snow_crab_v1\mac_logs",
        ".snow_crab_v1\nat_logs",
        ".snow_crab_v1\animation_cache",
        ".snow_crab_v1\platform_logs",
        ".snow_crab_v1\docker_scans",
        ".snow_crab_v1\email_composer",
        ".snow_crab_v1\pdf_reports",
        ".snow_crab_v1\templates",
        ".snow_crab_v1\custom_templates",
        ".snow_crab_v1\threat_monitor",
        ".snow_crab_v1\charts",
        "snow_crab_reports",
        "snow_crab_reports\graphics",
        "snow_crab_reports\pdf_reports",
        "snow_crab_reports\charts",
        "logs"
    )
    
    foreach ($dir in $directories) {
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }
    
    Write-Color "[+] Directory structure created" -Color Green
}

function New-Launcher {
    Write-Color "[*] Creating launcher script..." -Color Blue
    
    $launcherContent = @"
@echo off
REM SNOW-CRAB-V1 Launcher for Windows

cd /d "%~dp0"

REM Activate virtual environment
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

REM Check for main script
if exist "snow_crab_v1.py" (
    python snow_crab_v1.py %*
) else if exist "snow_crab.py" (
    python snow_crab.py %*
) else (
    echo Main script not found!
    exit /b 1
)
"@
    
    $launcherContent | Out-File -FilePath "snow-crab.bat" -Encoding ASCII
    
    # Create PowerShell launcher
    $psLauncherContent = @"
# SNOW-CRAB-V1 PowerShell Launcher
Set-Location -Path `$PSScriptRoot

if (Test-Path "venv\Scripts\Activate.ps1") {
    & ".\venv\Scripts\Activate.ps1"
}

if (Test-Path "snow_crab_v1.py") {
    python snow_crab_v1.py @args
} elseif (Test-Path "snow_crab.py") {
    python snow_crab.py @args
} else {
    Write-Host "Main script not found!" -ForegroundColor Red
    exit 1
}
"@
    
    $psLauncherContent | Out-File -FilePath "snow-crab.ps1" -Encoding UTF8
    
    Write-Color "[+] Launcher created" -Color Green
}

function New-DesktopShortcut {
    Write-Color "[*] Creating desktop shortcut..." -Color Blue
    
    $desktopPath = [Environment]::GetFolderPath("Desktop")
    $shortcutPath = Join-Path $desktopPath "SNOW-CRAB-V1.lnk"
    
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($shortcutPath)
    $Shortcut.TargetPath = Join-Path (Get-Location) "snow-crab.bat"
    $Shortcut.WorkingDirectory = Get-Location
    $Shortcut.Description = "SNOW-CRAB-V1 Cybersecurity Platform"
    $Shortcut.IconLocation = "shell32.dll,77"
    $Shortcut.Save()
    
    Write-Color "[+] Desktop shortcut created" -Color Green
}

function Test-Installation {
    Write-Color "[*] Verifying installation..." -Color Blue
    
    # Activate venv
    & ".\venv\Scripts\Activate.ps1"
    
    $packages = @(
        "colorama",
        "requests",
        "psutil",
        "paramiko",
        "flask",
        "reportlab",
        "matplotlib"
    )
    
    foreach ($pkg in $packages) {
        try {
            python -c "import $pkg" 2>$null
            Write-Color "  [+] $pkg" -Color Green
        } catch {
            Write-Color "  [X] $pkg" -Color Red
        }
    }
    
    Write-Color "[+] Installation verified" -Color Green
}

function Write-Completion {
    Write-Color @"

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ✅ SNOW-CRAB-V1 Installation Complete!                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

"@ -Color Green
    
    Write-Color "To start SNOW-CRAB-V1:" -Color Cyan
    Write-Color "  .\snow-crab.bat" -Color White
    Write-Color "  # Or"
    Write-Color "  .\snow-crab.ps1" -Color White
    Write-Color ""
    Write-Color "Or activate the virtual environment first:" -Color Cyan
    Write-Color "  .\venv\Scripts\Activate.ps1" -Color White
    Write-Color "  python snow_crab_v1.py" -Color White
    Write-Color ""
    Write-Color "Or double-click the desktop shortcut" -Color Cyan
    Write-Color ""
    Write-Color "⚠️  Remember: Only use on systems you own or have permission to test!" -Color Yellow
    Write-Color ""
}

# Main installation
function Main {
    Write-Banner
    
    # Check admin
    if (-not (Test-Administrator)) {
        Write-Color "[!] Not running as Administrator. Some features may not work." -Color Yellow
        Write-Color "    Consider running as Administrator for full functionality." -Color Yellow
        Write-Color ""
    }
    
    # Check/Install Python
    if (-not (Test-Python)) {
        if (-not (Install-Python)) {
            Write-Color "[X] Failed to install Python. Please install manually." -Color Red
            Read-Host "Press Enter to exit"
            exit 1
        }
    }
    
    # Install system dependencies
    if (-not $SkipDependencies) {
        Install-SystemDependencies
    }
    
    # Create virtual environment
    if (-not $SkipVenv) {
        New-VirtualEnvironment
    }
    
    # Install Python dependencies
    Install-PythonDependencies
    
    # Create directory structure
    New-DirectoryStructure
    
    # Create launcher
    New-Launcher
    
    # Create desktop shortcut
    New-DesktopShortcut
    
    # Verify installation
    Test-Installation
    
    # Completion message
    Write-Completion
    
    Read-Host "Press Enter to exit"
}

# Run main
Main
