import pandas as pd
import multiprocessing

def read_csv(df):
    df['price(JD)'] = df['price'] / 117
    df['Storge Type'] = ['SSD,HD' if s>0 and h>0 else
                        'SSD' if s>0 else
                        'HD' if h>0 else
                        'nothing'
                        for s,h in zip(df['ssd(GB)'],df["Hard Disk(GB)"])]
    return df

if __name__ == '__main__':
    lap_df = pd.read_csv('laptop.csv',chunksize=200)
    df_pool = multiprocessing.Pool(processes=6)
    chunks = []
    
    for data in lap_df:
        AddCol_pool = df_pool.apply_async(read_csv,args=(data,))
        chunks.append(AddCol_pool.get())
        
    df_pool.close()
    df_pool.join()
    
    new_df = pd.concat(chunks,axis=0,ignore_index=True)
    print(new_df)