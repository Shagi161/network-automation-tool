 # Network Automation Tool (Python)

A simple network monitoring and automation tool that checks device availability and generates a status report.

## Features
- Reads a list of devices from a CSV file
- Performs reachability checks (ping)
- Generates a timestamped report (CSV + TXT summary)

## Tech Stack
- Python 3
- Works on Linux/macOS/Windows

## How to Run
1. Install Python 3
2. Install requirements:
   ```bash

   
Yes, just three backticks.

So it becomes:


   pip install -r requirements.txt
   

   ## Example Output
   ![Demo](docs/demo.png)


Console:
```text
GoogleDNS (8.8.8.8) -> UP
CloudflareDNS (1.1.1.1) -> UP
Localhost (127.0.0.1) -> UP

