from Helpers.loadDataHelper import loadDataHelper

loadData = loadDataHelper()

loadData.saveDataset(
    function = loadData.load_fantasyAccumulativePts,
    fileName = 'fantasyRanking.csv')
