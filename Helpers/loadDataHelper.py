import pandas as pd
import os
from pathlib import Path

ROOT_PATH = os.path.dirname(__file__)
DATASETS_PATH = 'datasets'

class loadDataHelper():
    
    def __init__(self):
       pass 
    
    #Load data from pro-football
    def load_fantasyAccumulativePts(self, parms):
        url = "https://www.pro-football-reference.com/years/2022/fantasy.htm"
        html = pd.read_html(url, header = 1)
        df = html[0]
        raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
        raw = raw.fillna(0)
        playerStats = raw.drop(['Rk'], axis=1)
        return playerStats
    
    #save dataset
    def saveDataset(self, function, fileName, parms=''):
        df = function(parms)
        path = os.path.join(DATASETS_PATH, fileName)
        
        df.to_csv(path, index=False)  
        
        
    