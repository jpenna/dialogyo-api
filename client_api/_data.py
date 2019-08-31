author1 = {
    'id': '123',
    'name': 'Grizzly Bear',
    'avatar': '#984321'
}

author2 = {
    'id': '90',
    'name': 'Mary Poppins',
    'avatar': '#782312'
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
    'groupId': '123',
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
    'groupId': '123',
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
