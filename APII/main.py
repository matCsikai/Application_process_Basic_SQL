import psycopg2
import queries
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
# Root root [/]:
# It shows a list of links which are pointing to specific roots. See the roots below.
def homepage():
    return render_template("homepage.html")


@app.route("/mentors")
# Mentors and schools page [/mentors]
# On this page you should show the result of a query that returns the name of the mentors plus the name and country of
# the school (joining with the schools table) ordered by the mentors id column (columns: mentors.first_name,
# mentors.last_name, schools.name, schools.country).
def mentors_schools_page():
    mentors_schools = queries.mentors_schools_query()
    return render_template("mentors-schools.html", mentors_schools=mentors_schools)


@app.route("/all-school")
# All school page [/all-school]
# On this page you should show the result of a query that returns the name of the mentors plus the name and country of
# the school (joining with the schools table) ordered by the mentors id column.
# BUT include all the schools, even if there's no mentor yet!
# columns: mentors.first_name, mentors.last_name, schools.name, schools.country
def all_school_page():
    all_school = queries.all_schools_query()
    return render_template("all_school.html", all_school=all_school)


@app.route("/mentors-by-country")
# Contacts page [/mentors-by-country]
# On this page you should show the result of a query that returns the number of the mentors per country ordered by the
# name of the countries
# columns: country, count
def mentors_by_country_page():
    mentors_by_country = queries.mentors_by_country_query()
    return render_template("mentors_by_country.html", mentors_by_country=mentors_by_country)


@app.route("/contacts")
# Contacts page [/contacts]
# On this page you should show the result of a query that returns the name of the school plus the name of contact person
# at the school (from the mentors table) ordered by the name of the school
# columns: schools.name, mentors.first_name, mentors.last_name
def contacts_page():
    contacts = queries.contacts_query()
    return render_template("contacts.html", contacts=contacts)


@app.route("/applicants")
# Applicants page [/applicants]
# On this page you should show the result of a query that returns the first name and the code of the applicants plus the
# creation_date of the application (joining with the applicants_mentors table) ordered by the creation_date in
# descending order BUT only for applications later than 2016-01-01
# columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date
def applicants_page():
    applicants = queries.applicants_query()
    return render_template("applicants.html", applicants=applicants)


@app.route("/applicants-and-mentors")
# Applicants and mentors page [/applicants-and-mentors]
# On this page you should show the result of a query that returns the first name and the code of the applicants plus the
# name of the assigned mentor (joining through the applicants_mentors table) ordered by the applicants id column
# Show all the applicants, even if they have no assigned mentor in the database!
# In this case use the string 'None' instead of the mentor name
# columns: applicants.first_name, applicants.application_code, mentor_first_name, mentor_last_name
def applicants_mentors_page():
    applicants_mentors = queries.applicants_mentors_query()
    return render_template("applicants_mentors.html", applicants_mentors=applicants_mentors)


if __name__ == '__main__':
    app.run(debug=True)
