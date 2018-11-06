import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

# input = ('Western Europe',)
# cur.execute('SELECT CompanyName FROM Customer WHERE Region = ?', input)
# print('Companies in Western Europe')
# print('---------------------------')
# for row in cur:
    # print(row[0])
    
# print()

# cur.execute('SELECT ProductName FROM Product WHERE Discontinued = 1')
# print('Discontinued Products')
# print('---------------------')
# for row in cur:
    # print(row[0])
    
# print()

# cur.execute('SELECT LastName, Firstname FROM Employee WHERE ReportsTo = 2 ORDER BY LastName')
# print('Employees Reporting to Andrew Fuller')
# print('------------------------------------')
# for row in cur:
    # print(row[0] + ',', row[1])
    
# print()

# input = ('USA',)
# cur.execute('SELECT OrderDate, ShippedDate FROM [Order] WHERE ShipCountry = ?', input)
# print('Order and Ship Dates for USA-bound Orders')
# print('-----------------------------------------')
# for row in cur:
    # print(row[0], row[1])

input = ('2014-04-__',)
cur.execute('SELECT Id FROM [Order] WHERE ShippedDate LIKE ?', input)
for row in cur:
    print(row[0])
    
print('---------------------')
cur.execute('SELECT Companyname FROM Customer WHERE Region IN ("Northern Europe","Eastern Europe","Western Europe", "Scandinavia", "British Isles")')
for row in cur:
    print(row[0])
    
print('---------------------')
cur.execute('''SELECT ShipAddress, ShipCity, ShipCountry, ShipPostalCode 
FROM [Order] 
WHERE EmployeeId = 4 AND ShipRegion IN ("Northern Europe","Eastern Europe","Western Europe", "Scandinavia", "British Isles")''')
for row in cur:
    print(row[0] + ',', row[1] + ',', row[2] + ',', row[3])


conn.close()