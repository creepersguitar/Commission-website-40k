class StudioAI:

    def __init__(self):
        self.current_projects = []
        self.available_hours = 20  # change later

    def evaluate_commission(self, commission):
        difficulty = commission["difficulty"]
        hours = commission["hours"]

        if hours > self.available_hours:
            return {
                "status": "declined",
                "reason": "Current workload too high"
            }

        return {
            "status": "accepted",
            "estimated_time": f"{hours} hours",
            "difficulty": difficulty
        }