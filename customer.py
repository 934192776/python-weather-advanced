class Customer:
    def __init__(self, id, first_name, last_name, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def description(self):
        return f"Customer #{self.id}: {self.first_name} {self.last_name}, {self.email}"