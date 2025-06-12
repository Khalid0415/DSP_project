import pandas as pd
import multiprocessing

def read_csv(data_frame):
    df = pd.read_csv(data_frame)
    return df.groupby(by=['brand'])['price'].agg(['mean','min','max']).reset_index()

if __name__ == '__main__':
    df_pool = multiprocessing.Pool(processes=2)
    df1 = df_pool.apply_async(read_csv,args=('lap1.csv',))
    df2 = df_pool.apply_async(read_csv,args=('lap2.csv',))
    
    df_pool.close()
    df_pool.join()
    
    new_df = pd.concat([df1.get(),df2.get()],axis=0,ignore_index=True)
    print(new_df)