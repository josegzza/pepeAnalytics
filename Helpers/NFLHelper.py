#Dictionary NFL Tweets
tweetsHASHTAG = {
    'MIN' : '#Skol',
    'NYG' : '#TogetherBlue',
    'KAN' : '#ChiefsKingdom',
    'IND' : '#ForTheShoe',
    'DET' : '#OnePride',
    'BUF' : '#BillsMafia',
    'LVR' : '#RaiderNation',
    'ATL' : '#DirtyBirds',
    'CIN' : '#RuleTheJungle',
    'LAR' : '#RamsHouse',
    'CLE' : '#Browns',
    'TEN' : '#Titans',
    'JAX' : '#DUUUVAL',
    'HOU' : '#WeAreTexans',
    'WAS' : '#HTTC',
    'NOR' : '#Saints',
    'BAL' : '#RavensFlock',
    'PHI' : '#FlyEaglesFly',
    'DEN' : '#BroncosCountry',
    'CAR' : '#KeepPounding',
    'GNB' : '#GoPackGo',
    'TAM' : '#GoBucs',
    'LAC' : '#BoltUp',
    'MIA' : '#FinsUp',
    'SEA' : '#Seahawks',
    'ARI' : '#BirdCityFootball',
    'CHI' : '#DaBears',
    'SFO' : '#FTTB',
    'PIT' : '#HereWeGo',
    'NYJ' : '#TakeFlight',
    'DAL' : '#DallasCowboys',
    'NWE' : '#ForeverNE'
}

class NFLHelper():

    def __init__(self):
        pass

    def getHashtag(self, team):
        return tweetsHASHTAG[team]

