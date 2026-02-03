import time

class TikTokReporter:
    def __init__(self, session_manager):
        self.sm = session_manager

    def report_user(self, user_id, reason=101):
        """
        Sends a report for a user.
        Reasons (common):
        101: Inappropriate Content
        102: Spam
        103: Harassment
        """
        # This is a template for the report API call
        # Real reporting requires a logged-in session and valid CSRF tokens
        url = "https://www.tiktok.com/api/report/user/"
        payload = {
            "target_id": user_id,
            "reason": reason,
            "type": "user"
        }
        
        # response = self.sm.request("POST", url, json=payload)
        # return response.json()
        
        return {"status": "simulated", "message": f"Report sent for user {user_id} with reason {reason}"}

    def mass_report(self, target_id, count=5, delay=1):
        """Simulates mass reporting."""
        results = []
        for i in range(count):
            res = self.report_user(target_id)
            results.append(res)
            time.sleep(delay)
        return results
