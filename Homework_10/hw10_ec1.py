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
    try:
        statement = '''
            ALTER TABLE 'Games' ADD Channels INTEGER;
        '''
        cur.execute(statement)
    except:
        pass
    
    conn.commit()
    conn.close()
    
def add_channel_for_round(network_name, round_name):
    conn = sqlite.connect('tengdann_big10.sqlite')
    cur = conn.cursor()
    
    statement = '''
        SELECT id FROM 'TVNetworks' WHERE name = ?
    '''
    cur.execute(statement, (network_name,))
    channel_id = cur.fetchone()[0]
    
    statement = '''
        SELECT id from 'Rounds' WHERE name = ?
    '''
    cur.execute(statement, (round_name,))
    round_id = cur.fetchone()[0]
    
    try:
        statement = '''
            UPDATE 'Games' SET Channels = ? WHERE round = ?
        '''
        cur.execute(statement,(channel_id, round_id))
        print('Update successful')
    except:
        print('Update failed')
        
    conn.commit()
    conn.close()
        
def check_teams_for_network(network_name):
    conn = sqlite.connect('tengdann_big10.sqlite')
    cur = conn.cursor()
    teams = []
    print('Teams who played on %s:' % (network_name))
    
    statement = '''
        SELECT t.name FROM Teams AS t
            JOIN Games AS g ON g.winner = t.id
            JOIN TVNetworks AS tv on g.Channels = tv.id WHERE tv.name = ?
    '''
    cur.execute(statement, (network_name,))
    _teams = cur.fetchall()
    for team in _teams:
        teams.append(team[0])
        
    statement = '''
        SELECT t.name FROM Teams AS t
            JOIN Games AS g ON g.loser = t.id
            JOIN TVNetworks AS tv on g.Channels = tv.id WHERE tv.name = ?
    '''
    cur.execute(statement, (network_name,))
    _teams = cur.fetchall()
    for team in _teams:
        teams.append(team[0])
    
    for team in sorted(teams):
        print(team)
        
    conn.commit()
    conn.close()
       

if __name__ == '__main__':
    create_and_edit_stuff()
    print('Created and edited stuff for EC1\n')
    add_channel_for_round('BTN', 'Quarterfinals')
    print()
    check_teams_for_network('BTN')