class Order:
    def __init__(self, id, user_id, items, total_price, status):
        self.id = id
        self.user_id = user_id
        self.items = items
        self.total_price = total_price
        self.status = status
