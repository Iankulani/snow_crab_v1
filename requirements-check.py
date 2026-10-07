#!/usr/bin/env python3
"""
SNOW-CRAB-V1 Requirements Checker
Verifies all dependencies and tools are properly installed
"""

import os
import sys
import shutil
import subprocess
import importlib
from typing import Dict, List, Tuple

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def print_header():
    """Print header"""
    print(f"""
{Colors.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.CYAN}         ❄️ SNOW-CRAB-V1 Requirements Checker v1.0.0                        {Colors.BLUE}║
║{Colors.CYAN}         Verify all dependencies and tools                                {Colors.BLUE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")


def check_python_version() -> Tuple[bool, str]:
    """Check Python version"""
    version = sys.version_info
    if version >= (3, 7):
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    return False, f"Python {version.major}.{version.minor}.{version.micro} (need 3.7+)"


def check_system_tool(name: str) -> Tuple[bool, str]:
    """Check if a system tool is available"""
    path = shutil.which(name)
    if path:
        try:
            result = subprocess.run(
                [name, '--version'],
                capture_output=True,
                text=True,
                timeout=5
            )
            version = result.stdout.split('\n')[0] or result.stderr.split('\n')[0]
            return True, version[:50] if version else path
        except:
            return True, path
    return False, "Not found"


def check_python_package(name: str, import_name: str = None) -> Tuple[bool, str]:
    """Check if a Python package is installed"""
    import_name = import_name or name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'Unknown')
        return True, str(version)
    except ImportError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)


def check_directory(path: str) -> Tuple[bool, str]:
    """Check if a directory exists"""
    if os.path.isdir(path):
        return True, path
    return False, "Not found"


def run_checks() -> Dict[str, List]:
    """Run all checks"""
    results = {
        'passed': [],
        'failed': [],
        'warnings': []
    }
    
    # Python version
    success, msg = check_python_version()
    if success:
        results['passed'].append(('Python Version', msg))
    else:
        results['failed'].append(('Python Version', msg))
    
    # System tools
    system_tools = [
        ('ping', 'Network ping utility'),
        ('nmap', 'Network mapper'),
        ('curl', 'HTTP client'),
        ('wget', 'File downloader'),
        ('nc', 'Netcat'),
        ('dig', 'DNS lookup'),
        ('traceroute', 'Network tracer'),
        ('ssh', 'SSH client'),
        ('tcpdump', 'Packet capture'),
    ]
    
    for tool, desc in system_tools:
        success, msg = check_system_tool(tool)
        if success:
            results['passed'].append((f'System: {tool}', msg))
        else:
            results['warnings'].append((f'System: {tool}', desc))
    
    # Python packages
    python_packages = [
        ('colorama', 'colorama'),
        ('requests', 'requests'),
        ('psutil', 'psutil'),
        ('paramiko', 'paramiko'),
        ('scapy', 'scapy'),
        ('dnspython', 'dns'),
        ('whois', 'whois'),
        ('flask', 'flask'),
        ('flask-socketio', 'flask_socketio'),
        ('flask-cors', 'flask_cors'),
        ('reportlab', 'reportlab'),
        ('matplotlib', 'matplotlib'),
        ('numpy', 'numpy'),
        ('qrcode', 'qrcode'),
        ('Pillow', 'PIL'),
        ('beautifulsoup4', 'bs4'),
        ('tabulate', 'tabulate'),
        ('termcolor', 'termcolor'),
    ]
    
    for pkg, import_name in python_packages:
        success, msg = check_python_package(pkg, import_name)
        if success:
            results['passed'].append((f'Python: {pkg}', msg))
        else:
            results['failed'].append((f'Python: {pkg}', msg))
    
    # Optional packages
    optional_packages = [
        ('discord.py', 'discord'),
        ('telethon', 'telethon'),
        ('slack-sdk', 'slack_sdk'),
        ('selenium', 'selenium'),
        ('pynput', 'pynput'),
        ('shodan', 'shodan'),
    ]
    
    for pkg, import_name in optional_packages:
        success, msg = check_python_package(pkg, import_name)
        if success:
            results['passed'].append((f'Optional: {pkg}', msg))
        else:
            results['warnings'].append((f'Optional: {pkg}', msg))
    
    # Directories
    directories = [
        '.snow_crab_v1',
        'snow_crab_reports',
        'logs',
    ]
    
    for directory in directories:
        success, msg = check_directory(directory)
        if success:
            results['passed'].append((f'Directory: {directory}', msg))
        else:
            results['warnings'].append((f'Directory: {directory}', 'Not created yet'))
    
    return results


def print_results(results: Dict[str, List]):
    """Print check results"""
    print(f"\n{Colors.BOLD}Check Results:{Colors.RESET}\n")
    
    # Passed
    if results['passed']:
        print(f"{Colors.GREEN}✅ Passed ({len(results['passed'])}):{Colors.RESET}")
        for name, msg in results['passed']:
            print(f"   {Colors.GREEN}✓{Colors.RESET} {name}: {msg}")
        print()
    
    # Warnings
    if results['warnings']:
        print(f"{Colors.YELLOW}⚠️  Warnings ({len(results['warnings'])}):{Colors.RESET}")
        for name, msg in results['warnings']:
            print(f"   {Colors.YELLOW}!{Colors.RESET} {name}: {msg}")
        print()
    
    # Failed
    if results['failed']:
        print(f"{Colors.RED}❌ Failed ({len(results['failed'])}):{Colors.RESET}")
        for name, msg in results['failed']:
            print(f"   {Colors.RED}✗{Colors.RESET} {name}: {msg}")
        print()


def print_summary(results: Dict[str, List]):
    """Print summary"""
    total = len(results['passed']) + len(results['failed']) + len(results['warnings'])
    passed = len(results['passed'])
    failed = len(results['failed'])
    warnings = len(results['warnings'])
    
    print(f"{Colors.BOLD}Summary:{Colors.RESET}")
    print(f"   Total checks: {total}")
    print(f"   {Colors.GREEN}Passed: {passed}{Colors.RESET}")
    print(f"   {Colors.YELLOW}Warnings: {warnings}{Colors.RESET}")
    print(f"   {Colors.RED}Failed: {failed}{Colors.RESET}")
    
    if failed == 0:
        print(f"\n{Colors.GREEN}✅ All critical requirements met!{Colors.RESET}")
        print(f"{Colors.CYAN}   You can run SNOW-CRAB-V1 with: python snow_crab_v1.py{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}❌ Some requirements are missing!{Colors.RESET}")
        print(f"{Colors.CYAN}   Install missing packages with:{Colors.RESET}")
        print(f"   pip install -r requirements.txt")
    
    if warnings > 0:
        print(f"\n{Colors.YELLOW}⚠️  Some optional features may not work without warnings.{Colors.RESET}")


def print_recommendations(results: Dict[str, List]):
    """Print recommendations"""
    print(f"\n{Colors.BOLD}Recommendations:{Colors.RESET}\n")
    
    # Check for missing system tools
    missing_tools = [name.split(': ')[1] for name, _ in results['warnings'] 
                    if name.startswith('System:')]
    
    if missing_tools:
        print(f"{Colors.CYAN}Install missing system tools:{Colors.RESET}")
        print(f"   Ubuntu/Debian: sudo apt install {' '.join(missing_tools)}")
        print(f"   Fedora/RHEL: sudo dnf install {' '.join(missing_tools)}")
        print(f"   macOS: brew install {' '.join(missing_tools)}")
        print()
    
    # Check for missing Python packages
    missing_packages = [name.split(': ')[1] for name, _ in results['failed'] 
                       if name.startswith('Python:')]
    
    if missing_packages:
        print(f"{Colors.CYAN}Install missing Python packages:{Colors.RESET}")
        print(f"   pip install {' '.join(missing_packages)}")
        print()


def main():
    """Main entry point"""
    print_header()
    
    print(f"{Colors.CYAN}Running dependency checks...{Colors.RESET}\n")
    
    results = run_checks()
    print_results(results)
    print_summary(results)
    print_recommendations(results)
    
    # Return exit code
    return 0 if len(results['failed']) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
