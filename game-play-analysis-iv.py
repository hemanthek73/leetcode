import pandas as pd
import datetime as dt
def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df=activity.sort_values(by=['player_id','event_date'])
    df['first']=df.groupby('player_id')['event_date'].transform('min')
    df['diff']=(df['event_date']-df['first']).dt.days
    frac=df[df['diff']==1].drop_duplicates().shape[0]/df['player_id'].drop_duplicates().shape[0]
    return pd.DataFrame({'fraction':[round(frac,2)]})
    