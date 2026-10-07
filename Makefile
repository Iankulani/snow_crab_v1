# SNOW-CRAB-V1 Makefile

.PHONY: help install install-dev test clean run docker-build docker-run docker-stop lint format security

# Variables
PYTHON := python3
PIP := pip3
VENV := venv
DOCKER_IMAGE := snow-crab-v1
DOCKER_TAG := latest

# Help
help:
	@echo "SNOW-CRAB-V1 Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make install        Install production dependencies"
	@echo "  make install-dev    Install development dependencies"
	@echo "  make test           Run tests"
	@echo "  make test-coverage  Run tests with coverage"
	@echo "  make lint           Run linters"
	@echo "  make format         Format code"
	@echo "  make security       Run security checks"
	@echo "  make clean          Clean build artifacts"
	@echo "  make run            Run application"
	@echo "  make docker-build   Build Docker image"
	@echo "  make docker-run     Run Docker container"
	@echo "  make docker-stop    Stop Docker container"
	@echo "  make setup          Full setup (install + directories)"

# Installation
install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements-dev.txt

setup: install
	@mkdir -p .snow_crab_v1/{payloads,workspaces,scans,reports,phishing_templates,captured_credentials,ssh_keys,traffic_logs,graphics,web_templates,sessions,dos_logs,agents,c2_logs,network_monitor,deployments,domain_hosting,cracking,arp_logs,mac_logs,nat_logs,docker_scans,email_composer,pdf_reports}
	@mkdir -p snow_crab_reports/{graphics,pdf_reports}
	@mkdir -p logs
	@echo "Setup complete!"

# Testing
test:
	$(PYTHON) -m pytest test-commands.py -v

test-coverage:
	$(PYTHON) -m pytest test-commands.py -v --cov=. --cov-report=html --cov-report=term

test-requirements:
	$(PYTHON) requirements-check.py

# Code quality
lint:
	$(PYTHON) -m flake8 *.py
	$(PYTHON) -m pylint *.py --disable=all --enable=E

format:
	$(PYTHON) -m black *.py
	$(PYTHON) -m isort *.py

security:
	$(PYTHON) -m bandit -r . -f txt
	$(PYTHON) -m safety check -r requirements.txt

# Cleaning
clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .mypy_cache/
	rm -f *.db
	rm -f *.log

clean-all: clean
	rm -rf .snow_crab_v1/
	rm -rf snow_crab_reports/
	rm -rf logs/
	rm -rf venv/

# Running
run:
	$(PYTHON) snow_crab_v1.py

# Docker
docker-build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

docker-build-alpine:
	docker build -f Dockerfile.alpine -t $(DOCKER_IMAGE):alpine .

docker-run:
	docker run -it --rm --name snow-crab \
		--cap-add=NET_ADMIN \
		--cap-add=NET_RAW \
		-p 5000:5000 \
		-p 8080:8080 \
		$(DOCKER_IMAGE):$(DOCKER_TAG)

docker-stop:
	docker stop snow-crab || true
	docker rm snow-crab || true

docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down

# Full pipeline
ci: lint test security
	@echo "CI pipeline complete!"
