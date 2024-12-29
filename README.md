# Vulnerable Container with Exploitation Guide

## Overview

This repository demonstrates a vulnerable container built with intentional security flaws. The project showcases the exploitation of these vulnerabilities as part of an educational exercise. Please note that this is intended only for educational purposes, and any misuse of the information provided here is strictly prohibited.

## Vulnerability Details

The primary vulnerability in this container arises from the use of outdated and misconfigured dependencies, specifically:

- **Outdated OpenSSH Version**: The container installs OpenSSH 7.0p1, which has known security vulnerabilities that can be exploited.
- **Mismatched OpenSSL Libraries**: The project intentionally uses mismatched OpenSSL libraries and headers, causing further security weaknesses.
- **Excessive Privileges**: The container is configured to run services with unnecessary privileges, increasing the attack surface.
- **Weak Cryptographic Practices**: The project uses the outdated cryptography library version 2.2.2, which lacks modern security features and exposes the system to cryptographic attacks.

## Resources Used to Exploit the Vulnerability

- **OpenSSH 7.0p1**: Downloaded from OpenBSD.
- **Paramiko and PySNMP Libraries**: Used to interact with SSH and SNMP services.
- **Custom Exploit Scripts**: Included in the exploits directory to demonstrate the exploitation process.

## Part A: Explanation of Vulnerabilities

### OpenSSH 7.0p1

This version is outdated and includes vulnerabilities such as improper session handling and key management flaws. These allow attackers to compromise SSH sessions and gain unauthorized access.

### SNMP Misconfiguration

The Simple Network Management Protocol (SNMP) is misconfigured, exposing sensitive data to unauthorized users. Attackers can use SNMP enumeration to extract valuable information about the system.

## Part B: Steps to Build, Deploy, and Exploit

### Prerequisites

- Docker installed on your machine.
- Basic understanding of SSH, SNMP, and cryptographic operations.
- Python environment with pip installed.

### 1. Build the Vulnerable Container

Clone the repository:

```sh
git clone https://github.com/Ali-Taherii/Vulnerable_Container.git
cd vulnerable-container
```

Build the container image:

```sh
docker build -t vulnerable-container:latest .
```

### 2. Deploy the Container

Run the container:

```sh
docker run -d --name vulnerable-container -p 2222:22 -p 161:161/udp vulnerable-container:latest
```

- Port 2222 maps to the container's SSH port.
- Port 161 maps to the SNMP service.

Verify that the container is running:

```sh
docker ps
```

### 3. Exploit the Vulnerabilities

#### Exploit 1: Weak OpenSSH Configuration (SSH Enumeration)

Use the `ssh_enum.py` script to enumerate SSH users:

```sh
python3 ssh_enum.py [target_ip] --port p --username | --userList --outputFile
```

Analyze the results to identify valid usernames or misconfigurations.

#### Exploit 2: SNMP Enumeration

Use the `snmp_enum.py` script to extract information from the SNMP service:

```sh
python3 snmp_enum.py [target_ip] --community public
```

Review the output for sensitive data, such as process details or network configurations.

## Important Notes

- **Educational Use Only**: This repository is intended solely for learning and should not be used for malicious purposes.
- **Update Regularly**: Avoid using outdated libraries in production environments to mitigate vulnerabilities.
- **Principle of Least Privilege**: Configure services with minimal required permissions to reduce attack surfaces.
- **Multi-Architecture Support**: This container is built to support multiple architectures, ensuring compatibility across different systems.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

OpenBSD for OpenSSH.