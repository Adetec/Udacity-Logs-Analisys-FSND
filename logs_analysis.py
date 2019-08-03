#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'

queries = [
    {
        'quest': 'What are the most popular three articles of all time',
        'query': '''select articles.title, count(*) as num
                    from articles, log where log.status = '200 OK'
                    and articles.slug = substring(log.path, 10)
                    group by articles.title
                    order by num desc
                    limit 3''',
        'end': ' views'
    },
    {
        'quest': 'Who are the most popular article authors of all time',
        'query': '''select authors.name, count(*) as num
                    from authors, articles, log
                    where log.status = '200 OK'
                    and articles.slug = substring(log.path, 10)
                    and articles.author = authors.id
                    group by authors.name
                    order by num desc''',
        'end': ' views'
    },
    {
        'quest': 'On which days did more than 1% of requests lead to errors',
        'query': '''select date, round(((fail * 1.0/ total) * 100), 2) from (
                    select cast(time as date) date, count(*) as total,
                    sum(case status when '404 NOT FOUND'
                    then 1 else 0 END) as fail from log
                    group by date) as notfail
                    where ((fail * 1.0/ total) * 1.0) * 100 > 1''',
        'end': '% errors'
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


def generate_log(query, end):
    question = query['question']
    query = query['query']
    result = connect_db(query)
    print(question + '?')
    for r in result:
        print(str(r[0]) + ', with ' + str(r[1]) + end)


if __name__ == '__main__':
    for query in queries:
        generate_log(query, query['end'])
