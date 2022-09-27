import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import emoji

from Helpers.loadDataHelper import loadDataHelper
from Helpers.NFLHelper import NFLHelper
from Helpers.TweetHelper import TweetHelper

#get stats per position
def getStatsPerPosition(data, i):
    pos = teamData[i-1:i]['FantPos'].to_string(index=False).replace(" ", "")
    stats = ""
    if pos == 'WR' or pos == 'TE':
        recTgt = teamData[i-1:i]['Tgt'].to_string(index=False).replace(" ", "")
        recRec = teamData[i-1:i]['Rec'].to_string(index=False).replace(" ", "")
        recYds = teamData[i-1:i]['Yds.2'].to_string(index=False).replace(" ", "")
        recTD = teamData[i-1:i]['TD.2'].to_string(index=False).replace(" ", "")
        stats += "Rec: Tgt/"+recTgt+" Rec/"+recRec+" Yds/"+recYds+" TD/"+recTD
    elif pos == 'RB': 
        rushAtt = teamData[i-1:i]['Att.1'].to_string(index=False).replace(" ", "")
        rushYds = teamData[i-1:i]['Yds.1'].to_string(index=False).replace(" ", "")
        rushYA = teamData[i-1:i]['Y/A'].to_string(index=False).replace(" ", "")
        rushTD = teamData[i-1:i]['TD.1'].to_string(index=False).replace(" ", "")
        stats += "Rush: Att/"+rushAtt+" Yds/"+rushYds+" Y/A/"+rushYA+" TD/"+rushTD
    elif pos == 'QB':
        passCmp = teamData[i-1:i]['Cmp'].to_string(index=False).replace(" ", "")
        passAtt = teamData[i-1:i]['Att'].to_string(index=False).replace(" ", "")
        passYds = teamData[i-1:i]['Yds'].to_string(index=False).replace(" ", "")
        passTD = teamData[i-1:i]['TD'].to_string(index=False).replace(" ", "")
        stats += "Pass: Cmp/"+passCmp+" Att/"+passAtt+" Yds/"+passYds+" TD/"+passTD
    return stats


#generate tweet string
def generateString(nfl, teamData):
    tweet = ''
    team = teamData[:1]['Tm'].to_string(index=False).replace(" ", "")
    tweet = nfl.getHashtag(team) + " líderes fantasy " + emoji.emojize(":crown:") + '\n'
    #per player
    for i in range(1, 4):
        player = teamData[i-1:i]['Player'].to_string(index=False).replace(" ", "")
        ppr = teamData[i-1:i]['PPR'].to_string(index=False).replace(" ", "")
        tweet +=  u'\u2694' + " " +player + " "+getStatsPerPosition(teamData, i) + " PPR: "+ ppr
        tweet += '\n'
    tweet+= '\n'
    return tweet 
    

if __name__ == "__main__":
    #Helpers
    loadData = loadDataHelper()
    nfl = NFLHelper()
    tweet = TweetHelper()

    # loadData.saveDataset(
    #     function = loadData.load_fantasyAccumulativePts,
    #     fileName = 'fantasyRanking.csv')
    rankingFantasy = loadData.getcsv('fantasyRanking.csv')
    #NFL data
    
    rankingFantasy['PPR'] = pd.to_numeric(rankingFantasy['PPR'], downcast='float')
    #Top 3 players per Team
    top3perTeam = rankingFantasy.groupby('Tm').apply(lambda x : x.sort_values(by = 'PPR', ascending = False).head(3)).reset_index(drop = True)
    
    #iterate by team
    teams = rankingFantasy['Tm'].unique()
    for team in teams:
        teamData = top3perTeam[top3perTeam['Tm'] == team]
        teamData = teamData.sort_values(by=['PPR'], ascending=False)

        tweet = generateString(nfl, teamData)
        #Testing
        loadData.saveTxt(tweet, 'rankingFantasy.txt', 'a')
        # tweet.tweetIt(tweet)



