import webbrowser

class Movie():
    """This is the movie object to be used in fresh_tomatoes to create a web
    page of movies trailer. The constructor accepts 4 strings for the movie title,
    the movie storyline, a url for the poster image, and a url for the movie trailer.
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
