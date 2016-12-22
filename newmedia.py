import webbrowser

class Movie():
           """ This class provides a  way to store move related information"""
           # there is always a predefined class variable for every class called __doc__
           VALID_RATINGS = ["G", "PG", "PG-13", "R"]
            # googles style guide dictates that we used uppercase while defining a list inside class.
           # we just defined a class variable
           def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
                      # this is a constructor and when a class is called constructor fucntion is the one that runs to create space of instance "self" which is later replaced by whatever instance name we create.
                      #self is not a keyword, it is a convention that is used by most Python programmers. Using the word self will make your code more readable to other programmers
                      self.title = movie_title      # if self is not included here instance variable will not be created for instance such as "avatar" because then, storyline will be considered a local variable accessible only inside this class and not outside. hence storyline will not be an attribute available for this class
                      self.storyline =movie_storyline 
                      self.poster_image_url = poster_image
                      self.trailer_youtube_url = trailer_youtube
           def show_trailer(self):
                   webbrowser.open(self.trailer_youtube_url) # a function defined inside a class and is associated with the instance is called instance method (function)
