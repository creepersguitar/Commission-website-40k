class CustomerAI:

    def __init__(self):
        self.name = "The Herald"
        self.role = "Customer Representative"

    def process(self):
        commission = {
            "customer": input("Customer name: "),
            "army": input("Army/Faction: "),
            "models": int(input("Models required: ")),
            "paint_level": input("Paint level (Tabletop/Display): "),
            "deadline": input("Deadline: ")
        }

        return commission
    
    def summarise(self, commission):
        return (
            f"{commission['customer']} wants "
            f"{commission['models']} {commission['army']} models "
            f"painted to {commission['paint_level']} standard."
        )