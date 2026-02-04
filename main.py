import sys
import argparse
import json
import os
from tiktok_pro_tool.core.session import SessionManager
from tiktok_pro_tool.modules.osint import TikTokOSINT
from tiktok_pro_tool.modules.scraper import TikTokScraper
from tiktok_pro_tool.modules.reporter import TikTokReporter

def interactive_mode():
    sm = SessionManager()
    osint = TikTokOSINT(sm)
    scraper = TikTokScraper(sm)
    reporter = TikTokReporter(sm)

    while True:
        print("\n--- TikTok Pro Tool Interactive Mode ---")
        print("1. OSINT (User Info)")
        print("2. Scrape (Video, Hashtag, Trend, Music)")
        print("3. Report (Mass Reporting)")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter TikTok username (without @): ")
            print(f"[*] Gathering info for @{username}...")
            info = osint.get_user_info(username)
            print(json.dumps(info, indent=4))
            archives = osint.archive_search(f"https://www.tiktok.com/@{username}")
            print("\n[*] Archive Search Links:")
            for name, link in archives.items():
                print(f" - {name}: {link}")

        elif choice == "2":
            print("\n--- Scrape Options ---")
            print("1. Download Video")
            print("2. Scrape Hashtag Metadata")
            print("3. Scrape Trending Metadata")
            print("4. Scrape Music Metadata")
            scrape_choice = input("Select an option: ")
            
            if scrape_choice == "1":
                url = input("Enter video URL: ")
                res = scraper.download_video(url)
                print(res)
            elif scrape_choice == "2":
                hashtag = input("Enter hashtag: ")
                count = int(input("Enter count (default 10): ") or 10)
                res = scraper.get_hashtag_metadata(hashtag, count)
                print(json.dumps(res, indent=4))
            elif scrape_choice == "3":
                count = int(input("Enter count (default 10): ") or 10)
                res = scraper.get_trend_metadata(count)
                print(json.dumps(res, indent=4))
            elif scrape_choice == "4":
                music_id = input("Enter music ID: ")
                count = int(input("Enter count (default 10): ") or 10)
                res = scraper.get_music_metadata(music_id, count)
                print(json.dumps(res, indent=4))

        elif choice == "3":
            target_id = input("Enter target ID (User or Video): ")
            count = int(input("Enter report count: "))
            print(f"[*] Sending {count} report(s) for target {target_id}...")
            res = reporter.mass_report(target_id, count=count)
            print(json.dumps(res, indent=4))

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    parser = argparse.ArgumentParser(description="TikTok Pro Tool - Unified TikTok Intelligence & Automation")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # OSINT Command
    osint_parser = subparsers.add_parser("osint", help="Gather intelligence on a user")
    osint_parser.add_argument("username", help="TikTok username (without @)")

    # Scraper Command
    scraper_parser = subparsers.add_parser("scrape", help="Scrape data from TikTok")
    scraper_parser.add_argument("--video", help="URL of the video to download")
    scraper_parser.add_argument("--hashtag", help="Hashtag to scrape metadata from")
    scraper_parser.add_argument("--trend", action="store_true", help="Scrape trending video metadata")
    scraper_parser.add_argument("--music", help="Music ID to scrape metadata from")
    scraper_parser.add_argument("--count", type=int, default=10, help="Number of items to scrape")
    scraper_parser.add_argument("--output", default="downloads", help="Output directory")

    # Reporter Command
    reporter_parser = subparsers.add_parser("report", help="Report a user or video")
    reporter_parser.add_argument("target_id", help="ID of the target user or video")
    reporter_parser.add_argument("--count", type=int, default=1, help="Number of reports to send")

    # Interactive Command
    subparsers.add_parser("interactive", help="Start interactive mode")

    args = parser.parse_args()

    if args.command == "interactive" or not args.command:
        interactive_mode()
        return

    sm = SessionManager()
    
    if args.command == "osint":
        osint = TikTokOSINT(sm)
        info = osint.get_user_info(args.username)
        print(json.dumps(info, indent=4))
        archives = osint.archive_search(f"https://www.tiktok.com/@{args.username}")
        for name, link in archives.items():
            print(f" - {name}: {link}")

    elif args.command == "scrape":
        scraper = TikTokScraper(sm)
        if args.video:
            res = scraper.download_video(args.video, args.output)
            print(res)
        elif args.hashtag:
            res = scraper.get_hashtag_metadata(args.hashtag, args.count)
            print(json.dumps(res, indent=4))
        elif args.trend:
            res = scraper.get_trend_metadata(args.count)
            print(json.dumps(res, indent=4))
        elif args.music:
            res = scraper.get_music_metadata(args.music, args.count)
            print(json.dumps(res, indent=4))

    elif args.command == "report":
        reporter = TikTokReporter(sm)
        res = reporter.mass_report(args.target_id, count=args.count)
        print(json.dumps(res, indent=4))

if __name__ == "__main__":
    main()
