#!/usr/bin/env python
"""
Project: Movie Trailer Website
Author:  Rohan Kumar
Date:    Sep 8, 2017

---

MIT License

Copyright (c) 2017 Rohan Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from fresh_tomatoes import open_movies_page
from media import Movie


def main():
    """
    Generate and serve a simple movie trailer website containing some of my
    favorite movies.
    :return: None
    """
    rocky = Movie('Rocky',
                  'https://i.imgur.com/xrJTWjZ.jpg',
                  'https://www.youtube.com/watch?v=3VUblDwa648')

    lethal_weapon = Movie('Lethal Weapon',
                          'https://i.imgur.com/ZIN7nQ2.jpg',
                          'https://www.youtube.com/watch?v=bKeW-MGu-qQ')

    apollo_13 = Movie('Apollo 13',
                      'https://i.imgur.com/7ZaAFsK.jpg',
                      'https://www.youtube.com/watch?v=KtEIMC58sZo')

    la_confidential = Movie('L.A. Confidential',
                            'https://i.imgur.com/4DHMZnZ.jpg',
                            'https://www.youtube.com/watch?v=6sOXrY5yV4g')

    inglourious_basterds = Movie('Inglourious Basterds',
                                 'https://i.imgur.com/Kzg3Ujp.jpg',
                                 'https://www.youtube.com/watch?v=KnrRy6kSFF0')

    moonrise_kingdom = Movie('Moonrise Kingdom',
                             'http://i.imgur.com/ALm2Ciu.jpg',
                             'https://www.youtube.com/watch?v=7N8wkVA4_8s')

    movies = [rocky, lethal_weapon, apollo_13, la_confidential,
              inglourious_basterds, moonrise_kingdom]

    open_movies_page(movies)


if __name__ == '__main__':
    main()
