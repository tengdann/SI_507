import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

def firstExercise():
    cur.execute('SELECT o.Id, o.ShippedDate, s.CompanyName, s.Phone FROM [Order] AS o JOIN Shipper AS s ON o.ShipVia = s.Id')
    first = cur.fetchall()
    print('{:^10}{:^15}{:^20}{:^15}'.format('Order ID', 'Shipped Date', 'Company Name', 'Phone'))
    for order in first:
        if order[1] is not None:
            print('{:^10}{:^15}{:^20}{:^15}'.format(order[0], order[1], order[2], order[3]))
        else:
            print('{:^10}{:^15}{:^20}{:^15}'.format(order[0], 'Not yet shipped', order[2], order[3]))
            
def secondExercise():
    cur.execute('SELECT o.Id, o.Freight FROM [Order] AS o JOIN Shipper AS s ON o.ShipVia = s.Id WHERE s.CompanyName = \'United Package\' AND o.Freight > 100')
    second = cur.fetchall()
    print('{:^10}{:^15}'.format('Order ID', 'Ship Weight'))
    for order in second:
        print('{:^10}{:^15}'.format(order[0], order[1]))

def thirdExercise():
    cur.execute('SELECT c.CompanyName, o.Id FROM [Order] AS o JOIN Customer as c ON o.CustomerId = c.Id WHERE o.OrderDate LIKE \'2012-10%\'')
    third = cur.fetchall()
    print('{:^30}{:^10}'.format('Company Name', 'Order ID'))
    for order in third:
        print('{:^30}{:^10}'.format(order[0], order[1]))

def fourthExercise():
    cur.execute('SELECT e.LastName, e.FirstName, r.LastName, r.FirstName FROM Employee AS e JOIN Employee AS r ON e.ReportsTo = r.Id WHERE r.Title LIKE \'%Vice President%\'')
    fourth = cur.fetchall()
    print('{:^30}{:^30}'.format('Employee', 'Report To'))
    print('{:^15}{:^15}{:^15}{:^15}'.format('Last Name', 'First Name', 'Last Name', 'First Name'))
    for order in fourth:
        print('{:^15}{:^15}{:^15}{:^15}'.format(order[0], order[1], order[2], order[3]))

def init_db():
    conn = sqlite3.connect('teachingassignments.sqlite')
    cur = conn.cursor()

    # Drop tables
    statement = '''
        DROP TABLE IF EXISTS 'Instructors';
    '''
    cur.execute(statement)
    statement = '''
        DROP TABLE IF EXISTS 'Classes';
    '''
    cur.execute(statement)

    conn.commit()

    statement = '''
        CREATE TABLE 'Instructors' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'LastName' TEXT NOT NULL,
            'FirstName' TEXT NOT NULL,
            'Uniqname' TEXT NOT NULL,
            'Office' TEXT
        );
    '''
    cur.execute(statement)
    statement = '''
        CREATE TABLE 'Classes' (
                'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'CourseDept' TEXT NOT NULL,
                'CourseNum' TEXT NOT NULL,
                'TeacherId' INTEGER
        );
    '''
    cur.execute(statement)
    conn.commit()
    conn.close()

def airport_init_db():
    conn = sqlite3.connect()
    cur = conn.connect('airports.sqlite')
    
    # Drop tables
    statement = '''
        DROP TABLE IF EXISTS 'Airports';
    '''
    cur.execute(statement)
    
    statement = '''
        DROP TABLE IF EXISTS 'Cities';
    '''
    cur.execute(statement)
    
    statement = '''
        DROP TABLE IF EXISTS 'States';
    '''
    cur.execute(statement)
    
    statement = '''
        DROP TABLE IF EXISTS 'Countries';
    '''
    cur.execute(statement)
    conn.commit()
    
    statement = '''
        CREAT TABLE 'Airports' (
            'airportId' INTEGER PRIMARY KEY AUTOINCREMENT,
            'iata' TEXT NOT NULL,
            'airportName' TEXT NOT NULL,
            'lat' DECIMAL,
            'long' DECIMAL,
            'cityId' INTEGER,
            'traffic' INTEGER
        );
    '''
    cur.execute(statement)
    
    statement = '''
        CREAT TABLE 'Cities' (
            'cityId' INTEGER PRIMARY KEY AUTOINCREMENT,
            'cityName' TEXT NOT NULL,
            'stateId' INTEGER,
            'countryId' INTEGER
        );
    '''
    cur.execute(statement)
    
    statement = '''
        CREAT TABLE 'States' (
            'stateId' INTEGER PRIMARY KEY AUTOINCREMENT,
            'stateName' TEXT NOT NULL,
            'stateAbbr' TEXT NOT NULL,
            'countryId' INTEGER
        );
    '''
    cur.execute(statement)
    
    statement = '''
        CREAT TABLE 'Countries' (
            'countryId' INTEGER PRIMARY KEY,
            'countryName' TEXT NOT NULL
        );
    '''
    cur.execute(statement)
    
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    # firstExercise()
    # secondExercise()
    # thirdExercise()
    # fourthExercise()
    if len(sys.argv) > 1 and sys.argv[1] == '--init':
        print('Deleting db and starting over from scratch.')
        airport_init_db()
    else:
        print('Leaving the DB alone.')

conn.close()