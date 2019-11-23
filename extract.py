import json
from parse import search
import csv

#--------------------------------------------------

member_list = []                                        # Liste aller am Tippspiel teilnehmenden User
user_list = []                                          # Liste aller User, die einen Beitrag im Thread posteten
tip_dict = {}                                           # Dict für die abgegebenen Tipps

matches = []                                            # 9 zu tippende Spiele
post_dict = json.load(open('forumposts.json','r'))      # Dict, dass alle Posts im Thread enthält

#--------------------------------------------------

def read_memberlist():
    with open('member_list.txt','r') as member_file:
        for line in member_file.read().split("\n"):
            if line == '' or line[0] == '#': continue
            member_list.append(line)
            tip_dict[line] = [None]*9

def extract_matches():
    for line in post_dict['posts'][0]['content']:
        if search('{} Uhr {} - {}', line): matches.append(line)

def extract_tips(post):
    if post['user'] not in member_list: return
    tmp_tips = [None]*9

    if post['user'] not in user_list: user_list.append(post['user'])

    for line in post['content']:
        if line == "\u2022\u00a0\u00a0\u00a0\u00a0\u00a0\u2022\u00a0\u00a0\u00a0\u00a0\u00a0\u2022\r": break
        for i in range(0,9):
            tip = search(matches[i] + ' {:d}{}{:d}',line)
            if tip:
                tmp_tips[i] = tip
    if tmp_tips != [None]*9:
        if tip_dict[post['user']] == [None]*9:
            tip_dict[post['user']] = tmp_tips
        else: print(post['user'] + ' hat bereits getippt')
    
def convert_to_csv():
    csv_text = [[] for _ in range(10)]
    for user in member_list:
        csv_text[0] += [user,None]
        for i in range(1,10):
            if tip_dict[user][i-1] == None: csv_text[i] += [None,None]
            else: csv_text[i] += [tip_dict[user][i-1][0], tip_dict[user][i-1][2]]
    with open('tips.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_text)

def nichttipper():
    print('Nichttipper: ' + ', '.join(set(member_list) - set(user_list)))
    print('Haben im Thread gepostet, aber nicht getippt: ' + ', '.join(set(user_list) - set(tip_dict.keys())))

#--------------------------------------------------

read_memberlist() 
extract_matches()
for post in post_dict['posts']:
    if post != post_dict['posts'][0]:
        extract_tips(post)
convert_to_csv()
nichttipper()
