class Movie:
    def __init__(self, uuid: str | None, year: int, title: str, studios: str, producer: str, winner: bool):
        self.uuid = uuid
        self.year = year
        self.title = title
        self.studios = studios
        self.producer = producer
        self.winner = winner