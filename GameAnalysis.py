import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import os

def div0(x,y):
    try:
        return round(x/y,2)
    except ZeroDivisionError:
        return 0

today          = datetime.today()
today_formated = today.strftime("%Y-%m-%d")

postave_path   = os.path.join(os.path.dirname(__file__),f'{today_formated}')
analize_path   = os.path.join(os.path.dirname(__file__),f'{today_formated}')

seznam_postav  = os.listdir(postave_path)
#print(seznam_postav)

os.makedirs(analize_path, exist_ok=True)
seznam_analiz  = os.listdir(analize_path)
#print(seznam_analiz)
for file in seznam_postav:
    if file not in seznam_analiz:
        
        df = pd.read_excel(postave_path+'/'+file).drop(columns='Unnamed: 0')
        #print(df)
        #NaN napolnimo z 0
        result_df = df.fillna(0)
        df= result_df[df['Pos'] != 'G']
        df = df.reset_index(drop=True)
        
        #Dodamo skalkulirane metrike
        
        df['FPC'] = div0(df['foulPG'] , df['yC']+df['dRC'])
        df['FPC'].replace(np.inf, 0, inplace=True)
        
        df['TPC'] = div0(df['TacklesPG'] , df['yC']+df['dRC'])
        df['TPC'].replace(np.inf, 0, inplace=True)
        
        df['FTPC'] = df['TPC']+df['TPC']
        
        #df['FPC_div_FPG'] = div0(df['FPC'] , df['foulPG'])
        
        df['TouchesPC'] = div0(df['TouchesPG'] , df['yC']+df['dRC'])
        df['TouchesPC'].replace(np.inf, 0, inplace=True)
        
        df['PassesPC'] = div0(df['PassesPG'] , df['yC']+df['dRC'])
        df['PassesPC'].replace(np.inf, 0, inplace=True)
        
        df['PTPC'] = df['TouchesPC'] + df['PassesPC']
        
        df['TouchPerTacklePG'] = div0(df['TouchesPC'], df['TacklesPG'])
        df['TouchPerTacklePG'].replace(np.inf, 0, inplace=True)
        
        #naredimo norme
        #max_cpg = df['CardPG'].max()
        #df['CardPG_norm'] = df['CardPG'].apply(lambda x: x / max_cpg)

        max_ftpc = df['FTPC'].max()
        df['FTPC_norm'] = df['FTPC'].apply(lambda x: 0 if x == 0 else 1 -  x / max_ftpc) #Manjsa vrednost je boljsa, razen ce je vrednost 0 je rezultat 0

        df['tacklesWP'] = df['tacklesWP'].str.rstrip(' %').astype(float)
        df['TacklesWP_norm'] = df['tacklesWP'].apply(lambda x: 0 if x == 0 else  1 - x / 100) #Manjsa vrednost je boljsa, razen ce je vrednost 0 je rezultat 0

        df['mPG_norm'] = df['mPG'].apply(lambda x: x / 90)

        df['Starter_norm'] = df['Starter'].apply(lambda x: 1 if x == 'XI' else 0)
        
        max_ptpc = df['PTPC'].max()
        df['PTPC_norm'] = df['PTPC'].apply(lambda x: 0 if x == 0 else 1 - div0(x, max_ptpc)) #Manjsa vrednost je boljsa, razen ce je vrednost 0 je rezultat 0
        
        max_tpt = df['TouchPerTacklePG'].max()
        df['TPT_norm'] = df['TouchPerTacklePG'].apply(lambda x: 0 if x == 0 else 1 -  x / max_tpt)
        
        # dolocimo ponder
        #cpg_ponder = 0.10
        tpt_ponder = 0.30  #Touch per tackle per Game
        ftpc_ponder = 0.20 #Foul and Tackle per Card
        ptpc_ponder = 0.20 #Pass and Touch per Card
        twp_ponder = 0.10  #Tackle win percentage
        mpg_ponder = 0.10  #Minutes per game
        pos_ponder = 0.10  #Starter or Bench (1 or 0)

        ponder_sum = ftpc_ponder+twp_ponder+mpg_ponder+pos_ponder+ptpc_ponder+tpt_ponder
        
        #skalkuliramo koncni order
        df['Points'] = (
        #df['CardPG_norm'] * cpg_ponder +
        df['FTPC_norm'] * ftpc_ponder +
        df['TacklesWP_norm'] * twp_ponder +
        #df['FPC'] * fpc_ponder + 
        df['mPG_norm'] * mpg_ponder + 
        df['Starter_norm'] * pos_ponder +
        df['PTPC_norm'] * ptpc_ponder  +
        df['TPT_norm'] * tpt_ponder  
        )
        
        df_ordered = df.sort_values(by=['Points'], ascending=False)
        df_ordered

        df_ordered.reset_index(drop=True, inplace=True)
        out = df_ordered.head(10)

        #print(sorted_df)
        out.to_excel(f'{analize_path}/{file}')
        
        #Vizualizacija
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Points', y='Player', hue='Pos', data=out, palette='Set1')
        plt.xlabel('Points')
        plt.ylabel('Player')
        plt.title('Points by Player and Position')
        plt.legend(title='Position')
        plt.tight_layout()
        plt.savefig(f'{analize_path}/{file[:-5]}.png')
