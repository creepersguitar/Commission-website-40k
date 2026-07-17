class StudioAI:

    def __init__(self):
        self.current_projects = []
        self.available_hours = 20

    def evaluate_commission(self, commission):

        models = commission["models"]
        paint_level = commission["paint_level"]

        # Estimate difficulty
        if paint_level.lower() == "display":
            difficulty = "high"
        else:
            difficulty = "medium"

        # Estimate hours
        hours_per_model = 1

        if paint_level.lower() == "display":
            hours_per_model = 3

        hours = models * hours_per_model


        if hours > self.available_hours:
            return {
                "status": "declined",
                "reason": "Current workload too high",
                "estimated_time": f"{hours} hours",
                "difficulty": difficulty
            }


        return {
            "status": "accepted",
            "estimated_time": f"{hours} hours",
            "difficulty": difficulty
        }