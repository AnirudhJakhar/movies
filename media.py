import webbrowser

class Movie() :
    def __init__(self, movie_title, movie_storyline, 
    	          movie_poster, movie_trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)