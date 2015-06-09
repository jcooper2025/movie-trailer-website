# The open_movies_page() function from fresh_tomatoes will create the web page
# with a static list of movies generated here.
# All the code in the fresh_tomatoes module was provided by Udacity. Thanks!

import media
import fresh_tomatoes

# creating and initializing the movie objects to be displayed.

space_odyssey = media.Movie("2001: a space odyssey", "An epic drama of adventure and exploration",
                        "http://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg",
                        "https://www.youtube.com/watch?v=Z2UWOeBcsJI")

STTMP = media.Movie("Star Trek: The Motion Picture", "The Human Adventure is Just Beginning",
                     "http://upload.wikimedia.org/wikipedia/en/d/df/Star_Trek_The_Motion_Picture_poster.png",
                     "https://www.youtube.com/watch?v=h5vK8hCVrFg")

buckaroo = media.Movie("Buckaroo Banzai", "Feel good story of the year!",
                             "http://upload.wikimedia.org/wikipedia/en/b/ba/Adventures_of_buckaroo_banzai.jpg",
                             "https://www.youtube.com/watch?v=RdanCNK4ayo")

apollo13 = media.Movie("Apollo 13", "Houston we have a problem",
                          "http://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
                          "https://www.youtube.com/watch?v=nEl0NsYn1fU")

incredibles = media.Movie("The Incredibles", "Save the Day",
                            "http://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                            "https://www.youtube.com/watch?v=eZbzbC9285I")

hunger_games = media.Movie("Hunger Games", "Atlas Shrugged for today's youth",
                           "http://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

# the open_movies_page() function of fresh_tomatoes takes in a list of movie objects.
movie_list = [space_odyssey, incredibles, hunger_games, STTMP, buckaroo, apollo13]

fresh_tomatoes.open_movies_page(movie_list)
