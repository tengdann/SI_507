'''
SI 507 F18 homework 9: Basic SQL statements
'''

import sqlite3 as sqlite

conn = sqlite.connect('Northwind_small.sqlite')
cur = conn.cursor()

#----- Q1. Show all rows from the Region table 
print('-'*20 + "Question 1" + '-'*20)
def question1():
    cur.execute('SELECT * FROM Region')
    rows = cur.fetchall()
    return rows
    
q1 = question1()
print()
for row in q1:
    print(str(row[0]).ljust(20, '.') + row[1])
print()

#----- Q2. How many customers are there? 
print('-'*20 + "Question 2" + '-'*20)
def question2():
    cur.execute('SELECT count(*) FROM Customer')
    cust = cur.fetchone()
    return cust

cust = question2()
print('\nThere are', cust[0], 'customers on file.\n')

#----- Q3. How many orders have been made? 
print('-'*20 + "Question 3" + '-'*20)
def question3():
    cur.execute('SELECT count(*) FROM [Order]')
    order = cur.fetchone()
    return order

order = question3()    
print('\nThere are', order[0], 'orders on file.\n')

#----- Q4. Show the first five rows from the Product table 
print('-'*20 + "Question 4" + '-'*20)
def question4():
    cur.execute('SELECT * FROM Product')
    prod = cur.fetchmany(5)
    return prod
    
prod = question4()
print()
for r in prod:
    print('{:<2}{:<30}{:<5}{:<5}{:<20}{:<8}{:<5}{:<5}{:<5}{:<5}'.format(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))
print()

#----- Q5. Show the names of the five cheapest products 
print('-'*20 + "Question 5" + '-'*20)
def question5():
    cur.execute('SELECT * FROM Product ORDER BY UnitPrice')
    cheap = cur.fetchmany(5)
    return cheap
    
cheap = question5()
print()
for row in cheap:
    print(row[1])
print()

#----- Q6. Show the names and number of units in stock of all products that have more than 100 units in stock  
print('-'*20 + "Question 6" + '-'*20)
def question6():
    cur.execute('SELECT * FROM Product WHERE UnitsInStock > 100 ORDER BY UnitsInStock DESC')
    stock = cur.fetchall()
    return stock
    
stock = question6()
print()
for row in stock:
    print('{:.<47}{}'.format(row[1], row[6]))
print()

#----- Q7. Show all column names in the Order table 
print('-'*20 + "Question 7" + '-'*20)
def question7():
    cur.execute('SELECT * FROM [Order]')
    names = list((map(lambda x: x[0], cur.description),))
    return names
    
names = question7()
print()
for name in names[0]:
    print(name)
print()

#----- Q8. Show the names of all customers who lives in USA and have a fax number on record.
print('-'*20 + "Question 8" + '-'*20)
def question8():
    cur.execute('SELECT ContactName FROM Customer WHERE Country = \'USA\' AND Fax <> \'\'')
    cust = cur.fetchall()
    return cust

cust = question8()
print()
for row in cust:
    print(row[0])
print()

#----- Q9. Show the names of all the products, if any, that requires a reorder. 
# (If the units in stock of a product is lower than its reorder level but there's no units of the product currently on order, the product requires a reorder) 
print('-'*20 + "Question 9" + '-'*20)
def question9():
    cur.execute('SELECT ProductName FROM Product WHERE UnitsInStock < ReorderLevel AND UnitsOnOrder = 0')
    reord = cur.fetchall()
    return reord

reord = question9()
print()
print(reord[0][0])
print()

#----- Q10. Show ids of all the orders that ship to France where postal code starts with "44"
print('-'*20 + "Question 10" + '-'*20)
def question10():
    cur.execute('SELECT Id FROM [Order] WHERE ShipCountry = \'France\' AND ShipPostalCode LIKE \'44%\'')
    ids = cur.fetchall()
    return ids
    
ids = question10()
print()
for id in ids:
    print(id[0])
print()


