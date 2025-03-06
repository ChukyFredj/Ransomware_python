# Python Ransomware Simulation

**EDUCATIONAL PURPOSE ONLY**: This project is developed strictly for educational and research purposes to understand ransomware mechanics and improve cybersecurity defenses. Using this code for malicious purposes is illegal and unethical.

## Description

This Python-based ransomware simulation demonstrates the technical concepts behind ransomware attacks using a client-server architecture. It's designed to help security professionals, students, and researchers understand how ransomware works in order to develop better protection mechanisms.

## Disclaimer

This software is provided for educational purposes only. The author and contributors are not responsible for any misuse or damage caused by this program. By using this software, you agree:

- To use it only in controlled environments with proper authorization
- Not to use it against systems without explicit permission
- To comply with all applicable laws and regulations

## Features

- Client-side file encryption and decryption
- Server-based key management
- Secure communication between client and server
- Sandboxed environment for testing

## Project Structure

- `client.py`: Contains encryption and decryption functions
  - `encrypt(path)`: Encrypts files at the specified path
  - `decrypt(path)`: Decrypts files at the specified path
- `server.py`: Manages key storage and authentication

## Requirements

- Python 3.8+
- Required packages:
  - cryptography
  - requests
  - [other dependencies as needed]

## Installation

```bash
# Clone repository
git clone [repository-url]

# Navigate to project directory
cd  Ransomware_python

# Install dependencies
pip install -r requirements.txt
```

## Usage

For educational testing only, in a controlled environment:

### Running the Server

```bash
# Start the key management server
python server.py
```

### Running the Client

```bash
# Run client in simulation mode
python client.py
```

## Safety Precautions

- NEVER run this code on production systems
- Always use in an isolated virtual environment
- Test only on dedicated files in a controlled directory
- Keep backups of any test files
- The server and client should only be run on the same machine or a secure local network

## How It Works

1. The client component identifies target files
2. It contacts the server to establish an encryption session
3. Files are encrypted using a secure algorithm
4. Decryption requires authentication with the server
5. All operations are logged for educational analysis

## License

[Specify license]

## Contributing

Contributions for educational purposes are welcome. Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
