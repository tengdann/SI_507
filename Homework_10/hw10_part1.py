# 507 Homework 10 Part 1
import csv
import sqlite3 as sqlite
from sqlite3 import Error

#### Part 1 ####
print('\n*********** PART 1 ***********')

# Creates a database called yourlastnamefirstname_big10.sqlite
def create_tournament_db():
    # Your code goes here
    # Code below provided for your convenience to clear out the big10 database
    # This is simply to assist in testing your code.  Feel free to comment it
    # out if you would prefer
    
    try:
        conn = sqlite.connect('tengdann_big10.sqlite')
        cur = conn.cursor()
    except Error as e:
        print(e)
        return
    
    statement = '''
        DROP TABLE IF EXISTS 'Teams';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Games';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Rounds';
    '''
    cur.execute(statement)
    conn.commit()
    
    statement = '''
        CREATE TABLE 'Teams' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'seed' INTEGER UNIQUE NOT NULL,
            'name' TEXT UNIQUE NOT NULL,
            'confrecord' TEXT NOT NULL
        );
    '''
    cur.execute(statement)
    
    statement = '''
        CREATE TABLE 'Games' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'winner' INTEGER,
            'loser' INTEGER,
            'winnerscore' INTEGER,
            'loserscore' INTEGER,
            'round' INTEGER,
            'time' TEXT
        );
    '''
    
    cur.execute(statement)
    
    statement = '''
        CREATE TABLE 'Rounds' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'name' TEXT,
            'date' TEXT
        );
    '''
    cur.execute(statement)
    
    conn.commit()
    conn.close()

# Populates big10.sqlite database using csv files
def populate_tournament_db():

    # Connect to big10 database
    conn = sqlite.connect('tengdann_big10.sqlite')
    cur = conn.cursor()
    
    # Your code goes here
    # HINTS:
    # Column order in teams.csv file: Seed,Name,ConfRecord
    # Column order in games.csv file: Winner,Loser,WinnerScore,LoserScore,Round,Time
    # Column order in rounds.csv file: Name,Date

    with open("teams.csv") as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            statement = '''
                INSERT INTO 'Teams' (seed, name, confrecord) VALUES (?, ?, ?)
            '''
            cur.execute(statement, (row[0], row[1], row[2]))
        f.close()
    
    with open("games.csv") as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            statement = '''
                INSERT INTO 'Games' (winner, loser, winnerscore, loserscore, round, time) VALUES (?, ?, ?, ?, ?, ?)
            '''
            cur.execute(statement, (row[0], row[1], row[2], row[3], row[4], row[5]))
        f.close()
        
    with open("rounds.csv") as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            statement = '''
                INSERT INTO 'Rounds' (name, date) VALUES (?,?)
            '''
            cur.execute(statement, (row[0], row[1]))
        f.close()

    # Close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tournament_db()
    print("Created big10 Database")
    populate_tournament_db()
    print("Populated big10 Database")
