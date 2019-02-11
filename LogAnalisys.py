#!/usr/bin/python3
# "Database code" for the DB Forum.

import psycopg2


def main():
    # Connect to Database & create cursor to query DB.
    dbConnection = psycopg2.connect("dbname=news")
    dbCursor = dbConnection.cursor()

    # 1. What are the most  popular three articles of all time?
    # Join articles and log tables
    # count based on articles.slug being a substring of log.path
    sqlMostPopularArticles = """
        select title, count(*) as views
            from articles join log
            on log.path like '%' || articles.slug
            group by articles.title
            order by views desc
            limit 3;
    """
    dbCursor.execute(sqlMostPopularArticles)
    print("1. What are the most popular three articles of all time?")
    for (title, views) in dbCursor.fetchall():
        print("   {} - {} views".format(title, views))

    print("")

    # 2. Who are the most popular article authors of all time?
    # Join articles,log and authors tables
    # count appearance of authors.name
    # when author id's match and website was visited
    sqlMostPopularAuthors = """
        select authors.name, count(*) as views
            from articles, authors, log
            where articles.author = authors.id
            and log.path like '%' || articles.slug
            group by authors.name order by views desc;
    """
    dbCursor.execute(sqlMostPopularAuthors)
    print("2. Who are the most popular article authors of all time?")
    for (name, views) in dbCursor.fetchall():
        print("   {} - {} views".format(name, views))

    print("")

    # Create a view for all the times an error occured in a particular day
    errorsTable = """
        create view errorsTable as
            select date(time), count(*) as errorCount
                from log
                where status='404 NOT FOUND'
                group by date(time)
                order by date(time)
    """
    # Create a view for all the views that were attempted in each day
    viewsTable = """
        create view viewsTable as
            select date(time), count(*) as viewCount
                from log
                group by date(time)
                order by date(time)
    """
    dbCursor.execute(errorsTable)
    dbCursor.execute(viewsTable)

    # Create a table of the percentage of errors that occurred in each day
    errorPercent = """
        create view errorPercent as
            select viewsTable.date,
                (100.0*errorsTable.errorCount/viewsTable.viewCount) as percent
                from errorsTable, viewsTable
                where errorsTable.date = viewsTable.date
    """
    dbCursor.execute(errorPercent)

    moreThanOnePercent = """
        select *
            from errorPercent
            where percent > 1;
    """

    # 3. On which days did more than 1% of requests lead to errors?
    print("3. On which days did more than 1% of requests lead to errors?")
    dbCursor.execute(moreThanOnePercent)
    for (date, percent) in dbCursor.fetchall():
        print("   {} - {}% errors".format(date, percent))

    print("")


if __name__ == "__main__":
    main()
