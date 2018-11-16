import sqlite3 as sqlite
import csv

def create_and_edit_stuff():
    conn = sqlite.connect('tengdann_big10.sqlite')
    cur = conn.cursor()
    
    statement = '''
        DROP TABLE IF EXISTS 'TVNetworks';
    '''
    cur.execute(statement)
    
    statement = '''
        CREATE TABLE 'TVNetworks' (
            'id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'name' TEXT UNIQUE NOT NULL,
            'channel' INTEGER UNIQUE
        );
    '''
    cur.execute(statement)
    
    with open('tvnetworks.csv') as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            statement = '''
                INSERT INTO 'TVNetworks' (name, channel) VALUES (?, ?);
            '''
            cur.execute(statement, (row[0], row[1]))
    
    statement = '''
        ALTER TABLE 'Games' ADD Channels INTEGER;
    '''
    cur.execute(statement)
    
    conn.commit()
    conn.close()
    
def add_channel_for_round(network_name, round_name):
    pass
    
    
if __name__ == '__main__':
    create_and_edit_stuff()
    print('Created and edited stuff for EC1')