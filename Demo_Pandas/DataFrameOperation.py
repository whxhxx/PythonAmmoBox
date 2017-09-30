import pandas as pd

df = pd.read_csv('C:\Users\dell\PycharmProjects\PythonAmmoBox\data\dataFrameDataModel.csv',index_col=0)

# filter all values in a dataframe
def filterAll(df):
    df1 = df[df > 12.2]
    print df1

def remove_first_line(df):
    df_out = df[1:]


if __name__ == '__main__':
    # df = pd.read_csv('C:\Users\dell\PycharmProjects\PythonAmmoBox\data\dataFrameDataModel.csv',index_col=0)
    print df
    df.to_csv()
    # filterAll(df)

