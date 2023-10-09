import sqlite3
import os

def connectDB(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor

def createDB(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_id INTEGER PRIMARY KEY,
        company_name TEXT,
        job_name TEXT,
        posted_date DATE,
        job_type TEXT,
        position_count INTEGER
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_applicants (
        applicant_id INTEGER PRIMARY KEY,
        job_id INTEGER,
        applicant_name TEXT,
        application_date DATE,
        FOREIGN KEY (job_id) REFERENCES jobs(job_id)
    )""")

def insertDB(cursor, job_id, company_name, job_name, posted_date, job_type, position_count):
    cursor.execute(
        "INSERT INTO jobs "
        "(job_id, company_name, job_name, posted_date, job_type, position_count) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (job_id, company_name, job_name, posted_date, job_type, position_count),
    )

def insertApplicantsDB(cursor, applicant_id, job_id, applicant_name, application_date):
    cursor.execute(
        "INSERT INTO job_applicants "
        "(applicant_id, job_id, applicant_name, application_date) "
        "VALUES (?, ?, ?, ?)",
        (applicant_id, job_id, applicant_name, application_date),
    )

def readDB(cursor):
    cursor.execute("SELECT * FROM jobs")
    return cursor.fetchall()

def updateDB(cursor, job_id, new_posted_date):
    cursor.execute(
        "UPDATE jobs SET posted_date = ? WHERE job_id = ?", (new_posted_date, job_id)
    )

def deleteDB(cursor, job_id):
    cursor.execute("DELETE FROM jobs WHERE job_id = ?", (job_id,))

def complexQuery(cursor):
    cursor.execute("""
    SELECT company_name, COUNT(job_id) as job_count
    FROM jobs
    GROUP BY company_name
    ORDER BY job_count DESC
    """)
    return cursor.fetchall()


def main():
    database_name = "jobsDB.db"
    if os.path.exists(database_name):
        os.remove(database_name)

    conn, cursor = connectDB(database_name)

    # Create tables
    createDB(cursor)

    # Insert data into 'jobs' table
    insertDB(
        cursor, 55176, "Amazon", "Backend Developer", "2023-09-28", "experienced", 500
    )
    insertDB(
        cursor,
        55177,  # 修正此处的job_id
        "Amazon",
        "Associate Software Developer",
        "2023-09-27",
        "new grads",
        400
    )
    insertDB(
        cursor, 87356, "LinkedIn", "Fullstack Developer", "2023-09-27", "new grads", 300
    )
    insertDB(cursor, 99345, "Google", "Technology Analyst", "2023-09-26", "intern", 200)
    insertDB(
        cursor, 70001, "Apple", "Software Engineer", "2023-09-25", "new grads", 100
    )
    insertDB(
        cursor,
        80002,
        "Oracle",
        "Associate Software Developer",
        "2023-09-24",
        "experienced",
        250
    )
    insertDB(
        cursor,
        90102,
        "Veeva System",
        "Associate Software Developer",
        "2023-09-24",
        "new grads",
        350
    )

    # Insert data into 'job_applicants' table
    insertApplicantsDB(cursor, 1, 55176, "John Doe", "2023-09-28")
    insertApplicantsDB(cursor, 2, 55177, "Jane Smith", "2023-09-27")
    insertApplicantsDB(cursor, 3, 87356, "Alice White", "2023-09-29")
    insertApplicantsDB(cursor, 4, 99345, "Bob Green", "2023-09-26")
    insertApplicantsDB(cursor, 5, 70001, "Charlie Brown", "2023-09-25")
    insertApplicantsDB(cursor, 6, 80002, "David Black", "2023-09-24")
    insertApplicantsDB(cursor, 7, 90102, "Eva Blue", "2023-09-23")

    # Sample query: complexQuery
    print(complexQuery(cursor))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
