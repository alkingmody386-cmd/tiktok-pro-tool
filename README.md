# TikTok Pro Tool

A unified and user-friendly Python framework for advanced TikTok intelligence, data extraction, and automation. This tool consolidates various open-source functionalities into a single, modular platform, designed for researchers, analysts, and developers.

## Features

### 🕵️ OSINT (Open Source Intelligence)
- **User Profile Information:** Extract detailed public profile data, including unique ID, nickname, avatar, biography, verification status, follower/following counts, and total likes/videos.
- **Archive Search Integration:** Generate direct links to archived versions of TikTok profiles across major web archives (Wayback Machine, Archive.is, Google Cache) for historical analysis.

### 📊 Data Extraction & Scraping
- **Video Downloader:** Download TikTok videos (with watermark) directly from their URLs. The tool attempts to find the direct video URL from the page source.
- **Hashtag Metadata:** (Simulated) Collect metadata for videos associated with a specific hashtag.
- **Trending Video Metadata:** (Simulated) Gather metadata for currently trending TikTok videos.
- **Music Metadata:** (Simulated) Retrieve metadata for videos utilizing a particular music ID.

### 🚨 Reporting & Automation
- **Mass Reporting (Simulated):** A framework for simulating mass reporting of users or videos. This module is designed for ethical research and understanding of reporting mechanisms.

### ⚙️ Core & Utilities
- **Session Management:** Handles HTTP sessions, user-agent rotation, and persistent cookie management for more robust interactions with TikTok's web interface.
- **Proxy Support:** Integrates proxy rotation for enhanced anonymity and to mitigate rate-limiting during extensive data collection.
- **Interactive CLI:** A user-friendly command-line interface with an interactive mode for easy navigation and execution of various functions.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/alkingmody386-cmd/tiktok-pro-tool.git
    cd tiktok-pro-tool
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

## Usage

The TikTok Pro Tool can be used in two primary modes: **Command-Line Interface (CLI)** for direct commands or an **Interactive Mode** for a guided experience.

### Interactive Mode (Recommended for ease of use)

To start the interactive menu:

```bash
python3 main.py interactive
```

Follow the on-screen prompts to choose between OSINT, Scraper, and Reporter functionalities.

### Command-Line Interface (CLI)

#### OSINT Module
Gather intelligence on a specific user:

```bash
python3 main.py osint <username>
```

Example:
```bash
python3 main.py osint tiktok
```

#### Scraper Module

- **Download a video:**
  ```bash
  python3 main.py scrape --video <video_url> [--output <directory>]
  ```
  Example:
  ```bash
  python3 main.py scrape --video https://www.tiktok.com/@tiktok/video/7106594312292453675 --output my_downloads
  ```

- **Scrape hashtag metadata (simulated):**
  ```bash
  python3 main.py scrape --hashtag <hashtag_name> [--count <number>] [--output <directory>]
  ```
  Example:
  ```bash
  python3 main.py scrape --hashtag datascience --count 50
  ```

- **Scrape trending video metadata (simulated):**
  ```bash
  python3 main.py scrape --trend [--count <number>] [--output <directory>]
  ```
  Example:
  ```bash
  python3 main.py scrape --trend --count 20
  ```

- **Scrape music metadata (simulated):**
  ```bash
  python3 main.py scrape --music <music_id> [--count <number>] [--output <directory>]
  ```
  Example:
  ```bash
  python3 main.py scrape --music 7011536772089924869 --count 30
  ```

#### Reporter Module
Send reports for a target ID (user or video) - *simulated for ethical reasons*:

```bash
python3 main.py report <target_id> [--count <number>]
```

Example:
```bash
python3 main.py report 1234567890 --count 5
```

## Project Structure

```
tiktok-pro-tool/
├── core/
│   └── session.py        # Handles HTTP sessions, cookies, user-agents, and proxies.
├── modules/
│   ├── osint.py          # OSINT functionalities like user info and archive search.
│   ├── scraper.py        # Data extraction for videos, hashtags, trends, and music.
│   └── reporter.py       # Reporting functionalities.
└── main.py               # Main entry point for CLI and interactive modes.
└── README.md             # Project documentation.
```

## Disclaimer

This tool is developed for **educational and research purposes only**. Users are solely responsible for ensuring their actions comply with TikTok's Terms of Service, privacy policies, and all applicable local, national, and international laws. The developers of this tool do not endorse or condone any misuse or unethical practices. Use responsibly and ethically.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details. (Note: A `LICENSE` file is not included in this initial commit but is recommended for open-source projects.)
