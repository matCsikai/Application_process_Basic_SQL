import psycopg2
import config



def mentors_schools_query():
    # a query that returns the name of the mentors plus the name and country of
    # the school (joining with the schools table) ordered by the mentors id column (columns: mentors.first_name,
    # mentors.last_name, schools.name, schools.country).
    result = config.connect("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                        FROM mentors
                        INNER JOIN schools
                        ON mentors.city = schools.city
                        ORDER BY mentors.id ASC;""")
    return result


def all_schools_query():
    # a query that returns the name of the mentors plus the name and country of the school
    # (joining with the schools table) ordered by the mentors id column.
    # BUT include all the schools, even if there's no mentor yet!
    # columns: mentors.first_name, mentors.last_name, schools.name, schools.country
    result = config.connect("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                        FROM mentors
                        RIGHT JOIN schools
                        ON mentors.city = schools.city
                        ORDER BY mentors.id ASC;""")
    return result


def mentors_by_country_query():
    # On this page you should show the result of a query that returns the number of the mentors per country ordered by
    # the name of the countries
    # columns: country, count 
    result = config.connect("""SELECT schools.country, count(mentors.id)
                        FROM mentors
                        JOIN schools
                        ON mentors.city = schools.city
                        GROUP BY country
                        ORDER BY schools.country ASC;""")
    return result


