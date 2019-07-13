friends = {'name': 'Friends', 'genre': 'sitcom', 'no_of_seasons': 10}
# friends['no_of_seasons']
friends['no_of_episodes'] = 236  # adding a key in our dictionary
# friends[14] -- adds a a new key
# del friends[14] -- deletes key
creators = ['David Crane', 'Marta Kauffman']  # list of creators
friends['creators'] = creators  # adding the creators to the dictionary

seinfeld = {'name': 'Seinfeld', 'creators': [
    'Larry David', 'Jerry Seinfeld'], 'genre': 'sitcom', 'no_of_seasons': 10, 'no_of_episodes': 180}
tv_shows = [friends, seinfeld]
tv_shows  # testing
jerry = tv_shows[1]['creators'][1]
jerry  # test
