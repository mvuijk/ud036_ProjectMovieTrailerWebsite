'''
Created on Tue Nov 28 22:15:26 2017

@author: m.vuijk
'''
import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        '''
        Initialization of the instance variables
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''
        Used the instance variables as input.
        Open the URL in the browser as output.
        '''
        webbrowser.open(self.trailer_youtube_url)
