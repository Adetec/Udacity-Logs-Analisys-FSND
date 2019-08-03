#!/usr/bin/env python3

# Import psql adapter and os module
import psycopg2
import os

# Declare needed variables
# Store the database name
DBNAME = 'news'
# Store questions and their queries statement
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


# Log generation functionality
def generate_log(query, end):
    question = query['quest'] + '?'
    query = query['query']
    result = connect_db(query)
    # Generate and print logs
    output = '\r\r' + question + '\r'
    print(question)

    for r in result:
        answer = '\t' + '- ' + str(r[0]) + ', with ' + str(r[1]) + end
        print(answer)
        output += answer + '\r'
    return output


if __name__ == '__main__':
    content = ''
    output_file = open('output.txt', 'w')

    # Loop through queries list to generate logs
    for query in queries:
        content += generate_log(query, query['end'])

    output_file.write(content)
    output_file.close()
