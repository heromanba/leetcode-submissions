import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium['is_eligible'] = False
    
    def _f(win):
        win_df = stadium.loc[win.index]
        shifted_df = win_df.shift(1)
        is_eligible = ((win_df.iloc[1:, win_df.columns.get_loc('id')] - shifted_df.iloc[1:, shifted_df.columns.get_loc('id')]) == 1).all()
        is_eligible &= (win_df['people'] >= 100).all()
        if is_eligible:
            stadium.loc[win.index, 'is_eligible'] = True
        return is_eligible
    stadium['id'].rolling(3).apply(_f)
            
    return stadium[stadium['is_eligible']].drop(columns=['is_eligible'])
