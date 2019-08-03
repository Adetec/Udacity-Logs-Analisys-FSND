#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'

queries = [
    {
        'question': 'What are the most popular three articles of all time',
        'query': '''select articles.title, count(*) as num
                    from articles, log where log.status = '200 OK'
                    and articles.slug = substring(log.path, 10)
                    group by articles.title
                    order by num desc
                    limit 3''',
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
test_query =  queries[0]['query']
print(question)
res = connect_db(test_query)
for r in res:
    print(r[0] + '-' + str(r[1]))