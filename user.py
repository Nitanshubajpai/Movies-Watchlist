from movie import Movie
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<user {}>".format(self.name)

    def add_movie(self):
        name=input("Enter the name of movie: ")
        genre = input("Enter the genre of movie: ")
        rating = int(input("Enter the rating of movie, out of 5: "))
        movie = Movie(name , genre, rating, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        for movie in self.movies:
            if movie.name == name:
                self.movies.remove(movie)

    def movie_status(self, name):
        for movie in self.movies:
            if movie.name==name:
                movie.watched=True
                print(movie.watched)

    def watched_movies(self):
        watched_movie_list = list(filter(lambda x: x.watched, self.movies))
        print(watched_movie_list)

    def save_to_file(self):
        with open(self.name, 'w') as f:
            f.write("{} \n".format(self.name))
            for m in self.movies:
                f.write("-> name: {}, genre: {}, rating: {}, watched: {}.\n".format(m.name, m.genre, m.rating, m.watched))
    def view_saved_file(self):
        with open(self.name, 'r') as f:
            content=f.read()
            print(content)



