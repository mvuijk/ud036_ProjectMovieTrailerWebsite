#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:39:31 2017

@author: m.vuijk
"""

import media
import fresh_tomatoes

# Create instance for movie Toy Story
toy_story = media.Movie("Toy Story",
                        "Toy Story is een Amerikaanse animatiefilm uit 1995."
                        " Het was de eerste volledig computergeanimeerde film."
                        "De film werd geregisseerd door John Lasseter,"
                        " die ook Een luizenleven regisseerde.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://youtu.be/4KPTXpQehio")

# Create instance for movie Toy Story 2
toy_story2 = media.Movie("Toy Story 2",
                         "Toy Story 2 is een Amerikaanse animatiefilm uit"
                         " 1999. De productie is het eerste vervolg op de"
                         " animatiefilm Toy Story van Pixar. Net als de vorige"
                         " werd ook deze film geheel met de computer"
                         " getekend.",
                         "https://vignette.wikia.nocookie.net/pixar/images/4/"
                         "40/Movie_poster_toy_story_2.jpg/revision/"
                         "latest?cb=20071011042752",
                         "https://youtu.be/62AfUwqMSuY")

# Create instance for movie Toy Story 3
toy_story3 = media.Movie("Toy Story 3",
                         "Toy Story 3 is een Amerikaanse animatiefilm van"
                         " Pixar Animation Studios die in juni 2010 in"
                         " wereldpremière ging op het Nantucket Film Festival."
                         " De productie is het vervolg op Toy Story 2 en"
                         " eveneens geheel met de computer geanimeerd.",
                         "https://fanart.tv/fanart/movies/10193/movieposter/"
                         "toy-story-3-5223ed474123d.jpg",
                         "https://youtu.be/jTz2k8X58lw")

# Create instance for movie Binnenstebuiten
binnenstebuiten = media.Movie("Binnenstebuiten",
                              "Animatiefilm van Pete Docter (Up) waarin we"
                              " worden meegenomen in het brein van een"
                              "11-jarig jongetje en kennismaken met zijn vijf"
                              "emoties",
                              "http://www.film1.nl/images/portrait/"
                              "original/112973.jpg",
                              "https://youtu.be/-eZoI1fTvc4")

# Create instance for movie Dummie de Mummie
dummie_de_mummie = media.Movie("Dummie de Mummie",
                               "Stel je voor. Je heet Goos Guts, je bent"
                               " doodnormaal en je woont in het saaiste dorp"
                               " van de wereld. Op een dag loop je de tuin"
                               " in en je ontdekt ineens een levende mummie."
                               " Wat doe je dan? In het geval van Goos en zijn"
                               " vader Klaas loopt hun idee om net te doen"
                               " alsof Dummie hun Egyptische neefje is uit op"
                               " een heel stoer avontuur. Dummie moet"
                               " natuurlijk mee naar school, maar mag nooit"
                               " zijn magische scarabee kwijtraken.",
                               "http://filmpjekijken.com/Content/upload/"
                               "posterprimeur-dummie-de-mummie-poster.jpg",
                               "https://youtu.be/GvZtIXRNV3E")

# Create instance for movie Dummie de Mummie 2
dummie_de_mummie2 = media.Movie("Dummie de Mummie 2 - de Sfinx van Shakaba",
                                "Wanneer Dummie beseft dat hij nooit groot zal"
                                " worden en dus ook geen koning, wil hij in"
                                " ieder geval net zo beroemd worden als zijn"
                                " farao-vader. Vol zelfvertrouwen doet hij mee"
                                " aan een bijzondere wedstrijd. Ondertussen"
                                " heeft zijn beste vriend Goos een ander plan."
                                " Ergens op aarde bevindt zich een"
                                " geheimzinnig beeldje – de sfinx van"
                                " Shakaba. Misschien kan dat machtige beeldje"
                                " Dummie helpen?! Goos moet en zal het"
                                " vinden. Maar… waar is het?"
                                " Toch niet op de bodem van de zee?",
                                "http://filmpjekijken.com/Content/upload/"
                                "dummiesfinxposter.jpg",
                                "https://youtu.be/dF71UgM_xgk")

# Create a list with the created movie instances
movies = [toy_story, toy_story2, toy_story3, binnenstebuiten,
          dummie_de_mummie, dummie_de_mummie2]

# Call to open the movie trailer website
fresh_tomatoes.open_movies_page(movies)
