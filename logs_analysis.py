#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'

queries = [
    {
        'question': 'What are the most popular three articles of all time',
        'query': '',
    },
    {
        'question': 'Who are the most popular article authors of all time',
        'query': '',
    },
    {
        'question': 'On which days did more than 1% of requests lead to errors',
        'query': '',
    }
]

# Database connection functionality:
def connect_db(q):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(q)
    result = c.fetchall()
    db.close()
    return result

question = queries[0]['question']
test_guery =  queries[0]['query']
print(question)
print(query)