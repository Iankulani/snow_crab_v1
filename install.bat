@echo off
REM SNOW-CRAB-V1 Installation Script for Windows
REM Usage: install.bat

setlocal EnableDelayedExpansion

REM Colors (using ANSI escape codes)
set "GREEN=[92m"
set "RED=[91m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "CYAN=[96m"
set "BOLD=[1m"
set "NC=[0m"

REM Banner
echo %BLUE%
echo ================================================================================
echo         SNOW-CRAB-V1 Installation Script v1.0.0
echo         Ultimate Cybersecurity Command & Control Platform
echo ================================================================================
echo %NC%

REM Check for admin privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%[!] Not running as Administrator. Some features may not work.%NC%
    echo %YELLOW%    Consider running as Administrator for full functionality.%NC%
    echo.
)

REM Check Python installation
echo %BLUE%[*] Checking Python installation...%NC%
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo %RED%[X] Python not found!%NC%
    echo %YELLOW%    Please install Python 3.7+ from https://python.org%NC%
    echo %YELLOW%    Make sure to check "Add Python to PATH" during installation.%NC%
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo %GREEN%[+] Python %PYTHON_VERSION% found%NC%

REM Check pip
echo %BLUE%[*] Checking pip...%NC%
python -m pip --version >nul 2>&1
if %errorLevel% neq 0 (
    echo %YELLOW%[!] pip not found. Installing...%NC%
    python -m ensurepip --upgrade
)

REM Upgrade pip
echo %BLUE%[*] Upgrading pip...%NC%
python -m pip install --upgrade pip setuptools wheel --quiet

REM Create virtual environment
echo %BLUE%[*] Creating virtual environment...%NC%
if not exist "venv" (
    python -m venv venv
    if %errorLevel% neq 0 (
        echo %RED%[X] Failed to create virtual environment%NC%
        pause
        exit /b 1
    )
)
echo %GREEN%[+] Virtual environment created%NC%

REM Activate virtual environment
echo %BLUE%[*] Activating virtual environment...%NC%
call venv\Scripts\activate.bat

REM Install Python dependencies
echo %BLUE%[*] Installing Python dependencies...%NC%
if exist "requirements.txt" (
    pip install -r requirements.txt --quiet
) else (
    echo %YELLOW%[!] requirements.txt not found. Installing core packages...%NC%
    pip install --quiet ^
        colorama ^
        requests ^
        psutil ^
        paramiko ^
        scapy ^
        dnspython ^
        whois ^
        flask ^
        flask-socketio ^
        flask-cors ^
        reportlab ^
        matplotlib ^
        numpy ^
        qrcode ^
        pillow ^
        beautifulsoup4 ^
        tabulate ^
        termcolor
)

if %errorLevel% neq 0 (
    echo %RED%[X] Failed to install Python dependencies%NC%
    pause
    exit /b 1
)
echo %GREEN%[+] Python dependencies installed%NC%

REM Create directory structure
echo %BLUE%[*] Creating directory structure...%NC%
if not exist ".snow_crab_v1" mkdir ".snow_crab_v1"
if not exist ".snow_crab_v1\payloads" mkdir ".snow_crab_v1\payloads"
if not exist ".snow_crab_v1\workspaces" mkdir ".snow_crab_v1\workspaces"
if not exist ".snow_crab_v1\scans" mkdir ".snow_crab_v1\scans"
if not exist ".snow_crab_v1\reports" mkdir ".snow_crab_v1\reports"
if not exist ".snow_crab_v1\phishing_templates" mkdir ".snow_crab_v1\phishing_templates"
if not exist ".snow_crab_v1\captured_credentials" mkdir ".snow_crab_v1\captured_credentials"
if not exist ".snow_crab_v1\ssh_keys" mkdir ".snow_crab_v1\ssh_keys"
if not exist ".snow_crab_v1\traffic_logs" mkdir ".snow_crab_v1\traffic_logs"
if not exist ".snow_crab_v1\graphics" mkdir ".snow_crab_v1\graphics"
if not exist ".snow_crab_v1\web_templates" mkdir ".snow_crab_v1\web_templates"
if not exist ".snow_crab_v1\sessions" mkdir ".snow_crab_v1\sessions"
if not exist ".snow_crab_v1\dos_logs" mkdir ".snow_crab_v1\dos_logs"
if not exist ".snow_crab_v1\agents" mkdir ".snow_crab_v1\agents"
if not exist ".snow_crab_v1\c2_logs" mkdir ".snow_crab_v1\c2_logs"
if not exist ".snow_crab_v1\network_monitor" mkdir ".snow_crab_v1\network_monitor"
if not exist ".snow_crab_v1\deployments" mkdir ".snow_crab_v1\deployments"
if not exist ".snow_crab_v1\domain_hosting" mkdir ".snow_crab_v1\domain_hosting"
if not exist ".snow_crab_v1\cracking" mkdir ".snow_crab_v1\cracking"
if not exist ".snow_crab_v1\arp_logs" mkdir ".snow_crab_v1\arp_logs"
if not exist ".snow_crab_v1\mac_logs" mkdir ".snow_crab_v1\mac_logs"
if not exist ".snow_crab_v1\nat_logs" mkdir ".snow_crab_v1\nat_logs"
if not exist ".snow_crab_v1\docker_scans" mkdir ".snow_crab_v1\docker_scans"
if not exist ".snow_crab_v1\email_composer" mkdir ".snow_crab_v1\email_composer"
if not exist ".snow_crab_v1\pdf_reports" mkdir ".snow_crab_v1\pdf_reports"
if not exist "snow_crab_reports" mkdir "snow_crab_reports"
if not exist "snow_crab_reports\graphics" mkdir "snow_crab_reports\graphics"
if not exist "snow_crab_reports\pdf_reports" mkdir "snow_crab_reports\pdf_reports"
if not exist "logs" mkdir "logs"
echo %GREEN%[+] Directory structure created%NC%

REM Create launcher script
echo %BLUE%[*] Creating launcher script...%NC%
(
echo @echo off
echo REM SNOW-CRAB-V1 Launcher for Windows
echo.
echo cd /d "%%~dp0"
echo.
echo REM Activate virtual environment
echo if exist "venv\Scripts\activate.bat" (
echo     call venv\Scripts\activate.bat
echo ^)
echo.
echo REM Check for main script
echo if exist "snow_crab_v1.py" (
echo     python snow_crab_v1.py %%*
echo ^) else if exist "snow_crab.py" (
echo     python snow_crab.py %%*
echo ^) else (
echo     echo Main script not found!
echo     exit /b 1
echo ^)
) > snow-crab.bat

echo %GREEN%[+] Launcher created%NC%

REM Create desktop shortcut
echo %BLUE%[*] Creating desktop shortcut...%NC%
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\SNOW-CRAB-V1.lnk'); $Shortcut.TargetPath = '%~dp0snow-crab.bat'; $Shortcut.WorkingDirectory = '%~dp0'; $Shortcut.Description = 'SNOW-CRAB-V1 Cybersecurity Platform'; $Shortcut.Save()" 2>nul
echo %GREEN%[+] Desktop shortcut created%NC%

REM Verify installation
echo %BLUE%[*] Verifying installation...%NC%
python -c "import colorama; print('  [+] colorama')" 2>nul || echo "  [X] colorama"
python -c "import requests; print('  [+] requests')" 2>nul || echo "  [X] requests"
python -c "import psutil; print('  [+] psutil')" 2>nul || echo "  [X] psutil"
python -c "import paramiko; print('  [+] paramiko')" 2>nul || echo "  [X] paramiko"
python -c "import flask; print('  [+] flask')" 2>nul || echo "  [X] flask"

REM Completion message
echo.
echo %GREEN%================================================================================%NC%
echo %GREEN%                    SNOW-CRAB-V1 Installation Complete!%NC%
echo %GREEN%================================================================================%NC%
echo.
echo %CYAN%To start SNOW-CRAB-V1:%NC%
echo   %BOLD%snow-crab.bat%NC%
echo.
echo   Or double-click the desktop shortcut
echo.
echo %CYAN%Or activate the virtual environment first:%NC%
echo   %BOLD%venv\Scripts\activate.bat%NC%
echo   %BOLD%python snow_crab_v1.py%NC%
echo.
echo %YELLOW%[!] Remember: Only use on systems you own or have permission to test!%NC%
echo.

pause
endlocal
