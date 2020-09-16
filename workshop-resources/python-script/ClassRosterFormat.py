#Script to reformat a class roster into output format
#9/26/2019

import pandas as pd
import sys

def parser(filePath):
    df = pd.read_csv(filePath)

    dfdrop = df.drop([0, 1, 2, 3, 4, 5, 6])

    dffiltered = dfdrop.iloc[1:, 1:3]
    names = dffiltered['Unnamed: 2']

    splitname1 = dffiltered['Class List'].str.split(", ", n=1,expand=True)
    splitname1.columns = ['a', 'b']

    h = splitname1['b'].str.split(" ", expand=True)
    h.columns = ['c','d']
    h = h.drop(['d'], axis=1)
    h.head()

    splitname1 = splitname1.drop(['b'], axis=1)
    final = pd.concat([splitname1, h], axis=1)
    final = pd.concat([final, names], axis=1)
    final.columns = ['First', 'Last', 'User']
    final

    email = final['User'] + "@calpoly.edu"
    final = pd.concat([final, email], axis=1)
    final.columns = ['First', 'Last', 'User', 'Email']

    username = final['User'] + "_CalPoly"
    final = pd.concat([final, username], axis=1)

    final.columns = ['First Name', 'Last Name', 'User', 'Email', 'Username']
    final['Role'] = "Publisher"
    final['User Type'] = "Creator"
    final = final.drop('User', axis=1)
    final = final.reset_index()
    final = final.drop(['index'], axis=1)

    final.to_csv(filePath[:-4] + "_output.csv") 
    
def main():
    parser(sys.argv[1])
    
main()
