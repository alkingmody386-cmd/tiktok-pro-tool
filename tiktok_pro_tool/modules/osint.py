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
            # Fixed the syntax error by removing incorrect backslashes
            pattern = r'"user":(\{.*?\}),"stats":(\{.*?\})'
            match = re.search(pattern, response.text)
            if match:
                user_data = json.loads(match.group(1))
                stats_data = json.loads(match.group(2))
                
                return {
                    "id": user_data.get("id"),
                    "uniqueId": user_data.get("uniqueId"),
                    "nickname": user_data.get("nickname"),
                    "avatar": user_data.get("avatarLarger"),
                    "signature": user_data.get("signature"),
                    "verified": user_data.get("verified"),
                    "followerCount": stats_data.get("followerCount"),
                    "followingCount": stats_data.get("followingCount"),
                    "heartCount": stats_data.get("heartCount"),
                    "videoCount": stats_data.get("videoCount"),
                    "diggCount": stats_data.get("diggCount"),
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
