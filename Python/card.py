from payment import Payment

class Card:
    id = int
    number = int
    cvv = int
    date = str

    def __init__(self, id, number, cvv, date) -> None:
        super.__init__(id)
        self.number = number
        self.cvv = cvv
        self.date = date