author1 = {
    'id': '123',
    'name': 'Grizzly Bear',
    'avatar': '#984321'
}

reply1 = {
    'id': '1',
    'body': 'You are completely wrong',
    'author': author1,
    'dyoId': '1',
}

reply2 = {
    'id': '2',
    'body': 'I am definetelly right',
    'author': author1,
    'dyoId': '2'
}

dyo1 = {
    'id': '1',
    'headline': 'A title',
    'body': 'My content',
    'tags': ['content', 'first'],
    'privacy': [],
    'author': author1,
    'repliesCount': 2,
    'repliesList': [reply1, reply2],
    'dyosCount': 1,
    'dyosList': [],
}

dyo2 = {
    'id': '2',
    'headline': 'A title',
    'body': 'My content',
    'tags': ['content', 'first'],
    'privacy': ['*'],
    'author': author1,
    'repliesCount': 2,
    'repliesList': [reply2],
    'dyosCount': 1,
    'dyosList': [dyo1],
}
