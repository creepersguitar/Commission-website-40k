class CustomerAI:

    def __init__(self):
        self.name = "The Herald"

    def process(self):
        commission = {
            "customer": input("Customer name: "),
            "army": input("Army/Faction: "),
            "models": input("Models required: "),
            "paint_level": input("Paint level (Tabletop/Display): "),
            "deadline": input("Deadline: ")
        }

        return commission