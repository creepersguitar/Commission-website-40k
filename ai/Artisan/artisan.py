class ArtisanAI:

    def __init__(self):
        self.name = "The Artisan"
        self.role = "Painting Specialist"

    def analyse_project(self, commission):

        army = commission["army"]
        paint_level = commission["paint_level"]

        recommendations = []

        if paint_level.lower() == "display":
            recommendations.append(
                "Use advanced techniques such as edge highlighting, glazing and detailed basing."
            )
        else:
            recommendations.append(
                "Focus on clean basecoats, shading and efficient techniques."
            )

        return {
            "army": army,
            "recommendations": recommendations
        }