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