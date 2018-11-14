# 507 Homework 10 Part 2
import sqlite3 as sqlite

#### Part 2 ####
print('\n*********** PART 2 ***********')

# Params: game_id (ie. 1)
# Returns: A string formatted as follows with the game’s information:
# {Round Name}: ({Winner Seed}) {Winner} defeated ({Loser Seed}) {Loser}
# {Winner Score}-{Loser Score}
# Note: You must use only one SQL statement in this function.
def get_info_for_game(game_id):
    conn = sqlite.connect('tengdann_big10.sqlite')
    cur = conn.cursor()
    
    statement = '''
        SELECT r.name, g.winner, tw.name, g.loser, tl.name, g.winnerscore, g.loserscore FROM 'Games' AS g
            JOIN 'Teams' AS tw ON g.winner = tw.id
            JOIN 'Teams' AS tl ON g.loser = tl.id
            JOIN 'Rounds' AS r ON g.round = r.id
            WHERE g.id = ?
    '''
    cur.execute(statement, (game_id,))
    game = cur.fetchone()
    conn.close()
    
    return '%s: (%d) %s defeated (%d) %s %d - %d' % (game[0], game[1], game[2], game[3], game[4], game[5], game[6])

# Prints all of the round names a team won (sorted from lowest round id to
# highest round id) and the corresponding scores
# Params: team_name (ie. “Michigan”)
# Returns: a combined string like "Michigan won:\nFirst Round: 96-87\nSecond Round: 123-110"
# Note: You must use only one SQL statement in this function.
def print_winning_rounds_for_team(team_name):
    conn = sqlite.connect('tengdann_big10.sqlite')
    cur = conn.cursor()
    
    statement = '''
        SELECT r.name, g.winnerscore, g.loserscore FROM 'Games' AS g
            JOIN 'Rounds' as r ON g.round = r.id
            JOIN 'Teams' AS t ON g.winner = t.id WHERE t.name = ? ORDER BY g.round
    '''
    cur.execute(statement, (team_name,))
    string = '%s won:' % (team_name)
    wins = cur.fetchall()
    for win in wins:
        string += '\n%s: %d-%d' % (win[0], win[1], win[2])
    
    print(string)
    
    conn.close()
    return string

# Update the database to include the following Championship game information:
#   Round Name: “Championship”
#   Round Date: “03-04-18”
#   Winner: “Michigan”
#   Loser: “Purdue”
#   WinnerScore: 75
#   LoserScore: 66
#   Time: “4:30pm”
# Params: None
# Returns: Success string (detailed in spec)
# Note: You will need to update the ‘Games’ and ‘Rounds’ tables with the above
# data.  You are permitted to use multiple SQL statements in this function.
def add_championship_info():
    conn = sqlite.connect('tengdann_big10.sqlite')
    cur = conn.cursor()
    
    statement = '''
        DELETE FROM 'Rounds' WHERE name = 'Championship'
    '''
    cur.execute(statement)
    
    statement = '''
        DELETE FROM 'Games' WHERE winnerscore = 75 AND loserscore = 66 AND time = '4:30pm'
    '''
    cur.execute(statement)
    
    try:
        statement = '''
            INSERT INTO 'Rounds' (id, name, date) VALUES (5, 'Championship', '03-04-18')
        '''
        cur.execute(statement)
        
        statement = '''
            SELECT id FROM 'Teams' WHERE name = 'Michigan' OR name = 'Purdue'
        '''
        cur.execute(statement)
        team_ids = cur.fetchall()
        team_ids = (team_ids[0][0], team_ids[1][0])
        
        statement = '''
            SELECT id FROM 'Rounds' WHERE name = 'Championship'
        '''
        cur.execute(statement)
        round_id = cur.fetchone()
        
        inputs = (team_ids[0], team_ids[1], 75, 66, round_id[0], '4:30pm')        
        statement = '''
            INSERT INTO 'Games' (winner, loser, winnerscore, loserscore, round, time) VALUES (?, ?, ?, ?, ?, ?)
        '''
        cur.execute(statement, inputs)
        conn.commit()
        conn.close()
        return 'Added game'
    except:
        return 'Failed to add game'

# Update the date for the specified round and the times for each of the games
# in that round
# Params: round_id (ex. 1), date (ie. “03-05-18”), time (ie. “5:30pm”)
# Returns: Success string (detailed in spec)
# Note: All of these games will be updated to the same time.
# You may use multiple SQL statements in this function as well.
def update_schedule_for_round(round_id, date, time):
    conn = sqlite.connect('tengdann_big10.sqlite')
    cur = conn.cursor()
    
    try:
        statement = '''
            UPDATE 'Games' SET time = ? WHERE round = ?
        '''
        cur.execute(statement, (time, round_id))
        
        statement = '''
            UPDATE 'Rounds' SET date = ? WHERE id = ?
        '''
        cur.execute(statement, (date, round_id))
        conn.commit()
        conn.close()
        return 'Updated schedule'
    except:
        return 'Failed to update schedule'

if __name__ == "__main__":
    game_info = get_info_for_game(1)
    print(game_info)
    print("-"*15)

    print_winning_rounds_for_team("Michigan")
    print("-"*15)

    status = add_championship_info()
    print(status)
    print("-"*15)

    status2 = update_schedule_for_round(5,'03-05-18','12:00pm')
    print(status2)
    print("-"*15)
