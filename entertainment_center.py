import fresh_tomatoes
import media  

toy_story = media.Movie("Toy Story",
	                    "A story of a boy and his toythat come to life.",
	                    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	                    "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
	                 "A marine on a alien planet.",
	                 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	                 "https://www.youtube.com/watch?v=-9ceBgWV8io")
#avatar.show_trailer()
baahubali2 = media.Movie("Baahubali 2 - The Conclusion",
	                     "Answer: Why Kattapa killed Baahubali?",
	                     "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
	                     "https://www.youtube.com/watch?v=G62HrubdD6o")
baahubali1 = media.Movie("Baahubali: The Beginning",
                         "Question: Why Kattapa killed Baahubali?",
	                     "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
	                     "https://www.youtube.com/watch?v=VdafjyFK3ko")
thegreatwall = media.Movie("The Great Wall",
	                       "Saving the wall.",
	                       "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Great_Wall_%28film%29.png",
	                       "https://www.youtube.com/watch?v=6SKI9rgqFck")
themummy = media.Movie("The Mummy",
	                   "Rise of The Mummy.",
	                   "https://upload.wikimedia.org/wikipedia/en/a/a2/The_Mummy_%282017%29.jpg",
	                   "https://www.youtube.com/watch?v=GzorZUuZqEI")
movies = [toy_story, avatar, baahubali1, baahubali2, thegreatwall, themummy]
fresh_tomatoes.open_movies_page(movies)	                        