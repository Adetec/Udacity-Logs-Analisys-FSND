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
        'query': '''select authors.name, count(*) as num
                    from authors, articles, log
                    where log.status = '200 OK'
                    and articles.slug = substring(log.path, 10)
                    and articles.author = authors.id
                    group by authors.name
                    order by num desc''',
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


def generate_log(query):
    question = query['question']
    query =  query['query']
    result = connect_db(query)
    print(question)
    for r in result:
        print('"' + r[0] + '" - ' + str(r[1]) + ' views')


if __name__ == '__main__':
    for query in queries:
        if not query['query'] == '':
            generate_log(query)
        else:
            print('No answer yet')
