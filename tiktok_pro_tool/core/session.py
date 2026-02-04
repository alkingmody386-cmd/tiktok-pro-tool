import requests
import random
import json
import os

class SessionManager:
    def __init__(self, proxies=None, cookies_file="cookies.json"):
        self.session = requests.Session()
        self.proxies = proxies or []
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        ]
        self.cookies_file = cookies_file
        self.load_cookies()
        self.update_headers()

    def update_headers(self):
        self.session.headers.update({
            "User-Agent": random.choice(self.user_agents),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://www.tiktok.com",
            "Referer": "https://www.tiktok.com/"
        })

    def get_proxy(self):
        if self.proxies:
            proxy = random.choice(self.proxies)
            return {"http": proxy, "https": proxy}
        return None

    def load_cookies(self):
        if os.path.exists(self.cookies_file):
            with open(self.cookies_file, "r") as f:
                try:
                    cookies = json.load(f)
                    self.session.cookies.update(cookies)
                except json.JSONDecodeError:
                    print("Warning: Could not decode cookies file. Starting with no cookies.")

    def save_cookies(self):
        with open(self.cookies_file, "w") as f:
            json.dump(self.session.cookies.get_dict(), f)

    def request(self, method, url, **kwargs):
        proxy = self.get_proxy()
        if proxy:
            kwargs["proxies"] = proxy
        response = self.session.request(method, url, **kwargs)
        self.save_cookies() # Save cookies after each request
        return response
