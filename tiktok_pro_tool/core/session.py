import requests
import random

class SessionManager:
    def __init__(self, proxies=None):
        self.session = requests.Session()
        self.proxies = proxies or []
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        ]
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

    def request(self, method, url, **kwargs):
        proxy = self.get_proxy()
        if proxy:
            kwargs['proxies'] = proxy
        return self.session.request(method, url, **kwargs)
