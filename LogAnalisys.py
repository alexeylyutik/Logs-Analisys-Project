#!/usr/bin/python3
# "Database code" for the DB Forum.

import psycopg2
    # Define function for print
def print_column(dbCursor, sql_query, column1, column2):
    dbCursor.execute(sql_query)
    data = []
    data.append([column1, column2])
    for (name, views) in dbCursor.fetchall():
        data.append([name, views])
    col_width = max(len(str(word))
        for row in data for word in row) + 2  
    for row in data:
        print "".join(str(word).ljust(col_width) for word in row)
def main():
    # Connect to Database and create cursor to query DB.
    dbConnection = psycopg2.connect("dbname=news")
    dbCursor = dbConnection.cursor()

    # 1. What are the most  popular three articles of all time?
    # Join articles and log tables
    sql_most_popular_articles = """
        select title, count(*) as views
            from articles join log
            on log.path like '%' || articles.slug
            group by articles.title
            order by views desc
            limit 3;
    """
    print("1. What are the most popular three articles of all time?")
    print_column(dbCursor, sql_most_popular_articles, 'Article:', 'Views:')

    # 2. Who are the most popular article authors of all time?
    # Join articles,log and authors tables
    sql_most_popular_authors = """
        select authors.name, count(*) as views
            from articles, authors, log
            where articles.author = authors.id
            and log.path like '%' || articles.slug
            group by authors.name order by views desc;
    """
    print("2. Who are the most popular article authors of all time?")
    print_column(dbCursor, sql_most_popular_authors, 'Author:', 'Views:')
    
    # 3. On which days did more than 1% of requests lead to errors?
    # Views that were attempted in each day
    views_table = """
        create view views_table as
            select date(time), count(*) as view_count
                from log
                group by date(time)
                order by date(time)
    """
    # Error occured in a particular day
    error_table = """
        create view error_table as
            select date(time), count(*) as error_count
                from log
                where status='404 NOT FOUND'
                group by date(time)
                order by date(time)
    """
    
    dbCursor.execute(views_table)
    dbCursor.execute(error_table)
    # Percent of errors that occurred in each day
    error_percent = """
        create view error_percent as
            select views_table.date,
                (100.0*error_table.error_count/views_table.view_count) as percent
                from error_table, views_table
                where error_table.date = views_table.date
    """
    dbCursor.execute(error_percent)
    more_than_one_percent = """
        select *
            from error_percent
            where percent > 1;
    """

    print("3. On which days did more than 1% of requests lead to errors?")
    print_column(dbCursor, more_than_one_percent, 'Date:', 'Errors Percentage:')
    
    # Close communication 
    dbCursor.close()
    dbConnection.close()

if __name__ == "__main__":
    main()

