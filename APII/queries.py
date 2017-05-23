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


def contacts_query():
    # On this page you should show the result of a query that returns the name of the school plus the name of contact person
    # at the school (from the mentors table) ordered by the name of the school
    # columns: schools.name, mentors.first_name, mentors.last_name
    result = config.connect("""SELECT schools.name, mentors.first_name, mentors.last_name
                        FROM mentors
                        RIGHT JOIN schools
                        ON mentors.id = schools.contact_person
                        ORDER BY schools.name ASC;""")
    return result


def applicants_query():
    # On this page you should show the result of a query that returns the first name and the code of the applicants plus
    # the creation_date of the application (joining with the applicants_mentors table) ordered by the creation_date in 
    # descending order BUT only for applications later than 2016-01-01
    # columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date
    result = config.connect("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                        FROM applicants
                        JOIN applicants_mentors
                        ON applicants.id = applicants_mentors.applicant_id
                        WHERE creation_date > '2016-01-01'
                        ORDER BY applicants_mentors.creation_date ASC;""")
    return result


def applicants_mentors_query():
    # On this page you should show the result of a query that returns the first name and the code of the applicants plus
    # the name of the assigned mentor (joining through the applicants_mentors table) ordered by the applicants id column
    # Show all the applicants, even if they have no assigned mentor in the database!
    # In this case use the string 'None' instead of the mentor name
    # columns: applicants.first_name, applicants.application_code, mentor_first_name, mentor_last_name
    result = config.connect("""SELECT applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name
                        FROM ((applicants
                        LEFT JOIN applicants_mentors
                        ON applicants.id = applicants_mentors.applicant_id)
                        LEFT JOIN mentors
                        ON mentors.id = applicants_mentors.mentor_id)
                        ORDER BY applicants.id ASC;""")
    return result
