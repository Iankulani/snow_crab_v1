#!/bin/bash
# SNOW-CRAB-V1 Installation Script for Linux/macOS
# Usage: chmod +x install.sh && ./install.sh

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Banner
print_banner() {
    echo -e "${BLUE}"
    echo "╔══════════════════════════════════════════════════════════════════════════════╗"
    echo "║        ❄️ SNOW-CRAB-V1 Installation Script v1.0.0                          ║"
    echo "║        Ultimate Cybersecurity Command & Control Platform                    ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Check if running as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo -e "${YELLOW}⚠️  Not running as root. Some features may not work.${NC}"
        echo -e "${YELLOW}   Consider running with sudo for full functionality.${NC}"
    fi
}

# Detect OS
detect_os() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$ID
        VER=$VERSION_ID
    elif [ -f /etc/debian_version ]; then
        OS="debian"
    elif [ -f /etc/redhat-release ]; then
        OS="rhel"
    elif [ "$(uname)" == "Darwin" ]; then
        OS="macos"
    else
        OS="unknown"
    fi
    echo -e "${GREEN}✅ Detected OS: $OS${NC}"
}

# Install system dependencies
install_deps() {
    echo -e "\n${BLUE}📦 Installing system dependencies...${NC}"
    
    case $OS in
        ubuntu|debian|kali|parrot)
            apt-get update -qq
            apt-get install -y -qq \
                python3 \
                python3-pip \
                python3-venv \
                python3-dev \
                build-essential \
                libssl-dev \
                libffi-dev \
                libxml2-dev \
                libxslt1-dev \
                libjpeg-dev \
                zlib1g-dev \
                libfreetype6-dev \
                nmap \
                curl \
                wget \
                netcat-openbsd \
                dnsutils \
                traceroute \
                mtr-tiny \
                whois \
                openssh-client \
                tcpdump \
                hping3 \
                iputils-ping \
                net-tools \
                sqlite3 \
                libsqlite3-dev \
                git \
                make \
                gcc \
                g++ \
                2>/dev/null || true
            ;;
        fedora|rhel|centos|rocky|almalinux)
            dnf install -y -q \
                python3 \
                python3-pip \
                python3-devel \
                gcc \
                gcc-c++ \
                make \
                openssl-devel \
                libffi-devel \
                libxml2-devel \
                libxslt-devel \
                libjpeg-turbo-devel \
                zlib-devel \
                freetype-devel \
                nmap \
                curl \
                wget \
                nmap-ncat \
                bind-utils \
                traceroute \
                mtr \
                whois \
                openssh-clients \
                tcpdump \
                hping3 \
                iputils \
                net-tools \
                sqlite \
                sqlite-devel \
                git \
                2>/dev/null || true
            ;;
        arch|manjaro)
            pacman -Sy --noconfirm --needed \
                python \
                python-pip \
                base-devel \
                openssl \
                libffi \
                libxml2 \
                libxslt \
                libjpeg-turbo \
                zlib \
                freetype2 \
                nmap \
                curl \
                wget \
                gnu-netcat \
                bind \
                traceroute \
                mtr \
                whois \
                openssh \
                tcpdump \
                hping \
                iputils \
                net-tools \
                sqlite \
                git \
                2>/dev/null || true
            ;;
        alpine)
            apk add --no-cache \
                python3 \
                py3-pip \
                python3-dev \
                build-base \
                openssl-dev \
                libffi-dev \
                libxml2-dev \
                libxslt-dev \
                jpeg-dev \
                zlib-dev \
                freetype-dev \
                nmap \
                curl \
                wget \
                netcat-openbsd \
                bind-tools \
                traceroute \
                mtr \
                whois \
                openssh-client \
                tcpdump \
                iputils \
                net-tools \
                sqlite \
                git \
                2>/dev/null || true
            ;;
        macos)
            # Check for Homebrew
            if ! command -v brew &> /dev/null; then
                echo -e "${BLUE}Installing Homebrew...${NC}"
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            
            brew install \
                python3 \
                nmap \
                curl \
                wget \
                netcat \
                bind \
                traceroute \
                mtr \
                whois \
                openssh \
                tcpdump \
                hping \
                sqlite \
                git \
                2>/dev/null || true
            ;;
        *)
            echo -e "${RED}❌ Unsupported OS: $OS${NC}"
            echo -e "${YELLOW}Please install dependencies manually.${NC}"
            ;;
    esac
    
    echo -e "${GREEN}✅ System dependencies installed${NC}"
}

# Create Python virtual environment
setup_venv() {
    echo -e "\n${BLUE}🐍 Setting up Python virtual environment...${NC}"
    
    if [ ! -d "venv" ]; then
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    
    pip install --upgrade pip setuptools wheel -q
    
    echo -e "${GREEN}✅ Virtual environment ready${NC}"
}

# Install Python dependencies
install_python_deps() {
    echo -e "\n${BLUE}📦 Installing Python dependencies...${NC}"
    
    source venv/bin/activate
    
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt -q
    else
        echo -e "${YELLOW}⚠️ requirements.txt not found. Installing core packages...${NC}"
        pip install -q \
            colorama \
            requests \
            psutil \
            paramiko \
            scapy \
            dnspython \
            whois \
            flask \
            flask-socketio \
            flask-cors \
            reportlab \
            matplotlib \
            numpy \
            qrcode \
            pillow \
            beautifulsoup4 \
            tabulate \
            termcolor \
            pynput
    fi
    
    echo -e "${GREEN}✅ Python dependencies installed${NC}"
}

# Create directory structure
create_directories() {
    echo -e "\n${BLUE}📁 Creating directory structure...${NC}"
    
    mkdir -p .snow_crab_v1/{payloads,workspaces,scans,reports,phishing_templates,captured_credentials,ssh_keys,traffic_logs,nikto_results,graphics,web_templates,sessions,spear_phishing,email_templates,dos_logs,agents,c2_logs,modules,network_monitor,keylog_exfil,deployments,domain_hosting,cracking,arp_logs,mac_logs,nat_logs,animation_cache,platform_logs,docker_scans,email_composer,pdf_reports,templates,custom_templates,threat_monitor,charts}
    mkdir -p snow_crab_reports/{graphics,pdf_reports,charts}
    mkdir -p logs
    
    echo -e "${GREEN}✅ Directory structure created${NC}"
}

# Set up configuration
setup_config() {
    echo -e "\n${BLUE}⚙️ Setting up configuration...${NC}"
    
    if [ ! -f ".snow_crab_v1/config.json" ]; then
        cat > .snow_crab_v1/config.json << 'EOF'
{
    "version": "1.0.0",
    "auto_start": false,
    "auto_block_enabled": false,
    "auto_block_threshold": 5,
    "scan_timeout": 30,
    "report_format": "both",
    "generate_graphics": true,
    "animations": {
        "enabled": true,
        "startup": "matrix_rain",
        "loading": "spinner",
        "success": "pulse",
        "error": "glitch",
        "duration": 2.0
    },
    "web": {
        "enabled": true,
        "port": 5000,
        "host": "0.0.0.0",
        "require_auth": true
    }
}
EOF
    fi
    
    echo -e "${GREEN}✅ Configuration created${NC}"
}

# Create launcher script
create_launcher() {
    echo -e "\n${BLUE}🚀 Creating launcher script...${NC}"
    
    cat > snow-crab << 'EOF'
#!/bin/bash
# SNOW-CRAB-V1 Launcher

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Check for main script
if [ -f "snow_crab_v1.py" ]; then
    python3 snow_crab_v1.py "$@"
elif [ -f "snow_crab.py" ]; then
    python3 snow_crab.py "$@"
else
    echo "❌ Main script not found!"
    exit 1
fi
EOF
    
    chmod +x snow-crab
    
    # Also create a symlink in /usr/local/bin if root
    if [ "$EUID" -eq 0 ]; then
        ln -sf "$(pwd)/snow-crab" /usr/local/bin/snow-crab
        echo -e "${GREEN}✅ Installed to /usr/local/bin/snow-crab${NC}"
    fi
    
    echo -e "${GREEN}✅ Launcher created${NC}"
}

# Verify installation
verify_installation() {
    echo -e "\n${BLUE}🔍 Verifying installation...${NC}"
    
    source venv/bin/activate
    
    # Check Python packages
    python3 -c "import colorama; print('  ✅ colorama')" 2>/dev/null || echo "  ❌ colorama"
    python3 -c "import requests; print('  ✅ requests')" 2>/dev/null || echo "  ❌ requests"
    python3 -c "import psutil; print('  ✅ psutil')" 2>/dev/null || echo "  ❌ psutil"
    python3 -c "import paramiko; print('  ✅ paramiko')" 2>/dev/null || echo "  ❌ paramiko"
    python3 -c "import scapy; print('  ✅ scapy')" 2>/dev/null || echo "  ❌ scapy"
    python3 -c "import flask; print('  ✅ flask')" 2>/dev/null || echo "  ❌ flask"
    python3 -c "import reportlab; print('  ✅ reportlab')" 2>/dev/null || echo "  ❌ reportlab"
    python3 -c "import matplotlib; print('  ✅ matplotlib')" 2>/dev/null || echo "  ❌ matplotlib"
    
    # Check system tools
    command -v nmap &>/dev/null && echo "  ✅ nmap" || echo "  ❌ nmap"
    command -v curl &>/dev/null && echo "  ✅ curl" || echo "  ❌ curl"
    command -v nc &>/dev/null && echo "  ✅ netcat" || echo "  ❌ netcat"
    command -v dig &>/dev/null && echo "  ✅ dig" || echo "  ❌ dig"
    command -v traceroute &>/dev/null && echo "  ✅ traceroute" || echo "  ❌ traceroute"
    command -v ssh &>/dev/null && echo "  ✅ ssh" || echo "  ❌ ssh"
    
    echo -e "\n${GREEN}✅ Installation verified${NC}"
}

# Print completion message
print_completion() {
    echo -e "\n${GREEN}╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                    ✅ SNOW-CRAB-V1 Installation Complete!                    ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo -e ""
    echo -e "${CYAN}To start SNOW-CRAB-V1:${NC}"
    echo -e "  ${BOLD}./snow-crab${NC}"
    echo -e ""
    echo -e "${CYAN}Or activate the virtual environment first:${NC}"
    echo -e "  ${BOLD}source venv/bin/activate${NC}"
    echo -e "  ${BOLD}python3 snow_crab_v1.py${NC}"
    echo -e ""
    echo -e "${CYAN}Documentation:${NC}"
    echo -e "  ${BOLD}https://github.com/your-repo/snow-crab-v1${NC}"
    echo -e ""
    echo -e "${YELLOW}⚠️  Remember: Only use on systems you own or have permission to test!${NC}"
    echo -e ""
}

# Main installation
main() {
    print_banner
    check_root
    detect_os
    install_deps
    setup_venv
    install_python_deps
    create_directories
    setup_config
    create_launcher
    verify_installation
    print_completion
}

# Run main
main "$@"
