import sys
import argparse
import json
from tiktok_pro_tool.core.session import SessionManager
from tiktok_pro_tool.modules.osint import TikTokOSINT
from tiktok_pro_tool.modules.scraper import TikTokScraper
from tiktok_pro_tool.modules.reporter import TikTokReporter

def main():
    parser = argparse.ArgumentParser(description="TikTok Pro Tool - Unified TikTok Intelligence & Automation")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # OSINT Command
    osint_parser = subparsers.add_parser("osint", help="Gather intelligence on a user")
    osint_parser.add_argument("username", help="TikTok username (without @)")

    # Scraper Command
    scraper_parser = subparsers.add_parser("scrape", help="Scrape data from TikTok")
    scraper_parser.add_argument("--video", help="URL of the video to download")
    scraper_parser.add_argument("--output", default="downloads", help="Output directory")

    # Reporter Command
    reporter_parser = subparsers.add_parser("report", help="Report a user or video")
    reporter_parser.add_argument("target_id", help="ID of the target user or video")
    reporter_parser.add_argument("--count", type=int, default=1, help="Number of reports to send")

    args = parser.parse_args()

    sm = SessionManager()
    
    if args.command == "osint":
        osint = TikTokOSINT(sm)
        print(f"[*] Gathering info for @{args.username}...")
        info = osint.get_user_info(args.username)
        print(json.dumps(info, indent=4))
        
        print("\n[*] Archive Search Links:")
        archives = osint.archive_search(f"https://www.tiktok.com/@{args.username}")
        for name, link in archives.items():
            print(f" - {name}: {link}")

    elif args.command == "scrape":
        scraper = TikTokScraper(sm)
        if args.video:
            print(f"[*] Downloading video: {args.video}...")
            res = scraper.download_video(args.video, args.output)
            print(res)
        else:
            print("[!] Please provide a video URL with --video")

    elif args.command == "report":
        reporter = TikTokReporter(sm)
        print(f"[*] Sending {args.count} report(s) for target {args.target_id}...")
        res = reporter.mass_report(args.target_id, count=args.count)
        print(json.dumps(res, indent=4))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
