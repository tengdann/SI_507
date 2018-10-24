import json
# 507 Homework 7 Part 2

count = 0
#### Your Part 2 solution goes here ####
cache_file = open('directory_dict.json', 'r')
cache_contents = cache_file.read()
DIRECT_DICTION = json.loads(cache_contents)
cache_file.close()

for email in DIRECT_DICTION:
    if DIRECT_DICTION[email]['Title'] == 'PhD student':
        count += 1


#### Your answer output (change the value in the variable, count)####
print('The number of PhD students: ', count)