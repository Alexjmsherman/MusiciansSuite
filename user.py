class User:
    def __init__(self):
        self.name = None
        self.total = 0

    def update_total(self):
        self.total += 1
        return self.total
