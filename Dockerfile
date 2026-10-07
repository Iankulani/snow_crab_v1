# SNOW-CRAB-V1 Dockerfile
FROM alpine:3.19

LABEL maintainer="Ian Carter Kulani"
LABEL description="SNOW-CRAB-V1 - Ultimate Cybersecurity Command & Control Platform"
LABEL version="1.0.0"

# Install system dependencies
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    python3-dev \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    rust \
    nmap \
    nmap-scripts \
    curl \
    wget \
    netcat-openbsd \
    bind-tools \
    traceroute \
    mtr \
    whois \
    openssh-client \
    openssh-keygen \
    tcpdump \
    tshark \
    hping3 \
    iputils \
    iproute2 \
    net-tools \
    bash \
    git \
    make \
    g++ \
    libxml2-dev \
    libxslt-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    linux-headers \
    libcap \
    libcap-dev \
    libpcap-dev \
    sqlite \
    sqlite-dev \
    && rm -rf /var/cache/apk/*

# Create app directory
WORKDIR /app

# Create virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create necessary directories
RUN mkdir -p /app/.snow_crab_v1/{payloads,workspaces,scans,reports,phishing_templates,captured_credentials,ssh_keys,traffic_logs,nikto_results,graphics,web_templates,sessions,spear_phishing,email_templates,dos_logs,agents,c2_logs,modules,network_monitor,keylog_exfil,deployments,domain_hosting,cracking,arp_logs,mac_logs,nat_logs,animation_cache,platform_logs,docker_scans,email_composer,pdf_reports,templates,custom_templates,threat_monitor,charts}

# Create non-root user for security
RUN addgroup -g 1000 snowcrab && \
    adduser -u 1000 -G snowcrab -s /bin/bash -D snowcrab && \
    chown -R snowcrab:snowcrab /app

# Set capabilities for network operations
RUN setcap cap_net_raw,cap_net_admin+eip /usr/bin/python3 2>/dev/null || true

# Expose ports
EXPOSE 5000 8080 4444 5555

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import socket; s=socket.socket(); s.connect(('localhost',5000)); s.close()" || exit 1

# Switch to non-root user
USER snowcrab

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV SNOW_CRAB_HOME=/app

# Default command
CMD ["python3", "snow_crab_v1.py"]
