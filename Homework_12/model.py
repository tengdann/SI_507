
import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
entries_admin = []
counter = -1
next_id = 0

def init():
    global entries, counter, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        counter = int(entries[-1]['MAX_ID'])
        next_id = counter + 1
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, counter, next_id
    next_id = counter + 1
    now = datetime.now()
    # time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    counter += 1
    entries.insert(0, entry) ## add to front of list
    
    try:
        entries[-1]['MAX_ID'] = str(next_id)
    except:
        entries.insert({'MAX_ID': str(next_id)})
    
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
        
def delete_entry(id):
    global entries
    for entry in entries:
        try:
            if entry['id'] == id:
                entries.remove(entry)
                break
        except:
            pass