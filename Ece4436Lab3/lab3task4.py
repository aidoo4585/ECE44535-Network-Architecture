import pandas as pd
from matplotlib import pyplot as pyplot

# Reading data from csv files
TenPercentLoss = pd.read_csv('lab3task4_h1.csv')
OnePercentLoss = pd.read_csv('lab3task4_h3.csv')

# Adding to window size
def addWin(df):

    df['cwnd'] = 0;

    for i,row in df.iterrows():        
        try:
            df.at[i,'cwnd'] = int(row['Info'].split("Win=")[1].split(" ")[0])
        except:
            df.drop(i, inplace=True)
            continue
        
# Deleting Acks using row length (longer message if ACK)
def deleteAcks(df):

    for i,row in df.iterrows():        
        if(row['Length'] > 100):
            df.drop(i, inplace=True)


addWin(TenPercentLoss)
deleteAcks(TenPercentLoss)

addWin(OnePercentLoss)
deleteAcks(OnePercentLoss)

TenPercentLoss.plot('No.','cwnd',title="10%")
OnePercentLoss.plot('No.','cwnd',title="1%")

pyplot.show()

    
