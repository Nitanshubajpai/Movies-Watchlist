class Movie:
    def __init__(self, name, genre, rating, watched):
        self.name = name
        self.genre = genre
        self.rating = rating
        self.watched = watched
    def __repr__(self):
        return "<Movie: {}\nGenre: {}\nRating: {}\nWatched: {}>\n".format(self.name, self.genre, self.rating, self.watched)

