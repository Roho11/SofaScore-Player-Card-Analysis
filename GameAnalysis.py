#!pip install pandas
#!pip install openpyxl
import pandas as pd
from datetime import datetime
import os

def div0(x,y):

    try:
        return round(x/y,2)
    except ZeroDivisionError:
       return 0

today          = datetime.today()
today_formated = today.strftime("%Y-%m-%d")

#postave_path   = f'/Users/Roho11/Desktop/pyscripts/GamesInPlay/2023-08-20'
postave_path   = f'/Users/Roho11/Desktop/pyscripts/GamesInPlay/{today_formated}'
analize_path   = f'/Users/Roho11/Desktop/pyscripts/CardAnalysis/{today_formated}'

seznam_postav  = os.listdir(postave_path)
#print(seznam_postav)

os.makedirs(analize_path, exist_ok=True)
seznam_analiz  = os.listdir(analize_path)
#print(seznam_analiz)
for file in seznam_postav:
    if file not in seznam_analiz:
        
        df = pd.read_excel(postave_path+'/'+file).drop(columns='Unnamed: 0')
        print(df)
        #samo XI, NaN napolnimo z 0
        result_df = df[df['Starter'] == 'XI'].fillna(0)
        result_df = result_df.reset_index(drop=True)
        #mPG zaenkrat se ne uporabljamo
        
        #samo igralci, ki imajo povprecno nad 70mPG
        #result_df = result_df[result_df['mPG'] >= 70.0]
        
        #izberemo median cpg, ker je bolj odporna proti ekstremnim vrednostnim
        cpg_median = result_df['CardPG'].median()
        foul_median = result_df['foulPG'].median()
        tackle_median = result_df['TacklesPG'].median()
        #print(f'Card per game median: {cpg_median}')
        result_df = result_df[result_df['CardPG'] >= cpg_median]
        #median FoulPG
        #print(f'Foul per game median: {foul_median}')
        result_df = result_df[result_df['foulPG'] >= foul_median]
        #median tacklesPG
        #print(f'Tackle per game median: {tackle_median}')
        result_df = result_df[result_df['TacklesPG'] >= tackle_median]
        #cardPfoul
        #result_df['CPF'] = result_df['foulPG'] / result_df['CardPG']
        result_df['CPF'] = div0(result_df['foulPG'], result_df['CardPG'])
        #order
        sorted_df = result_df.sort_values(by=['CPF'], ascending=[True])
        sorted_df.reset_index(drop=True, inplace=True)
        out = sorted_df.head(9)

        
        #print(sorted_df)
        out.to_excel(f'{analize_path}/{file}')