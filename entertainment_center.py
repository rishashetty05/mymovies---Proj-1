# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064


import newmedia
import fresh_tomatoes

avatar = newmedia.Movie("Avatar", "A marine in alien land",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# instance variables are being created by passing value through instance "avatar"

avengers2 = newmedia.Movie("Avengers2 ","A union of Superheroes with new villian", 
                          "http://t0.gstatic.com/images?q=tbn:ANd9GcRlGeugacRkKznDOtRhUCVt0AkrOTPbaaKwF9xgGZgNViyC_Xko",
                           "https://www.youtube.com/watch?v=tmeOjFno6Do")

few_good_men=newmedia.Movie("A Few Good Men","US marines charged with killing a fellow marine",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcSYAB38F7l03EtFMcKKFH4_TQcyBbbETDdreBvbVX30UQ0bsg8L",
                            "https://www.youtube.com/watch?v=ePo91pMcu94")

how2_train_your_dragon=newmedia.Movie("How to train your dragon","A viking boy trains a dragon",
                                      "http://www.gstatic.com/tv/thumb/movieposters/3625299/p3625299_p_v7_aa.jpg",
                                      "https://www.youtube.com/watch?v=oKiYuIsPxYk")

frozen=newmedia.Movie("Frozen","Princess saves a kingdon trapped in winter",
                      "http://vignette2.wikia.nocookie.net/disney/images/5/58/Frozen-movie-poster.jpg/revision/latest?cb=20131002122858",
                      "https://www.youtube.com/watch?v=2Jw-AeaU5WI")

kate_and_leopold=newmedia.Movie("Kate & Leopold","the love story of Kate and leopold both from different centuries ",
                                "http://www.gstatic.com/tv/thumb/dvdboxart/28882/p28882_d_v7_aa.jpg",
                                "https://www.youtube.com/watch?v=ajQbq9zuUNk")

movies = [avatar, avengers2, few_good_men, how2_train_your_dragon, frozen, kate_and_leopold] # list of movies
fresh_tomatoes.open_movies_page(movies)

kate_and_leopold.show_trailer()

