# TikTok Pro Tool

A unified professional framework for TikTok intelligence, data extraction, and automation. This tool integrates multiple open-source resources into a single, modular Python platform.

## Features

- **Intelligence (OSINT):** Extract detailed profile information including follower counts, verification status, and signatures.
- **Archive Search:** Automatically generate archive links for TikTok profiles across multiple platforms.
- **Data Extraction:** Modular scraper for video and metadata collection.
- **Automation:** Framework for reporting and account checking.
- **Modular Design:** Easily extendable core with separate modules for different functionalities.

## Installation

1. Clone the repository or download the files.
2. Install dependencies:
   ```bash
   pip install requests
   ```

## Usage

### OSINT Module
Gather intelligence on a specific user:
```bash
python3 main.py osint <username>
```

### Scraper Module
Download a video:
```bash
python3 main.py scrape --video <video_url>
```

### Reporter Module
Send reports for a target ID:
```bash
python3 main.py report <target_id> --count <number>
```

## Project Structure

- `main.py`: CLI entry point.
- `tiktok_pro_tool/core/`: Core engine (Session management, Proxy handling).
- `tiktok_pro_tool/modules/`: Functional modules (OSINT, Scraper, Reporter).

## Disclaimer
This tool is for educational and research purposes only. Users are responsible for complying with TikTok's Terms of Service and local laws.
