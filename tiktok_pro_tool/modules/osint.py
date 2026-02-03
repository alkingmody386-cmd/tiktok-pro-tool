import json
import re

class TikTokOSINT:
    def __init__(self, session_manager):
        self.sm = session_manager

    def get_user_info(self, username):
        """Fetches basic user info from the TikTok web profile."""
        url = f"https://www.tiktok.com/@{username}"
        response = self.sm.request("GET", url)
        
        if response.status_code != 200:
            return {"error": f"Failed to fetch profile, status code: {response.status_code}"}

        # Extracting data from the __UNIVERSAL_DATA_FOR_REHYDRATION__ script tag
        try:
            pattern = r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>'
            match = re.search(pattern, response.text)
            if match:
                data = json.loads(match.group(1))
                user_data = data.get("__DEFAULT_SCOPE__", {}).get("webapp.user-detail", {}).get("userInfo", {})
                if user_data:
                    return {
                        "id": user_data.get("user", {}).get("id"),
                        "uniqueId": user_data.get("user", {}).get("uniqueId"),
                        "nickname": user_data.get("user", {}).get("nickname"),
                        "avatar": user_data.get("user", {}).get("avatarLarger"),
                        "signature": user_data.get("user", {}).get("signature"),
                        "verified": user_data.get("user", {}).get("verified"),
                        "followerCount": user_data.get("stats", {}).get("followerCount"),
                        "followingCount": user_data.get("stats", {}).get("followingCount"),
                        "heartCount": user_data.get("stats", {}).get("heartCount"),
                        "videoCount": user_data.get("stats", {}).get("videoCount"),
                        "diggCount": user_data.get("stats", {}).get("diggCount"),
                    }
            return {"error": "Could not find user data in page source."}
        except Exception as e:
            return {"error": f"Error parsing user data: {str(e)}"}

    def archive_search(self, target_url):
        """Generates archive search links for a given URL."""
        archives = {
            "Wayback Machine": f"https://web.archive.org/web/*/{target_url}",
            "Archive.is": f"https://archive.is/{target_url}",
            "Google Cache": f"https://www.google.com/search?q=cache:{target_url}"
        }
        return archives
