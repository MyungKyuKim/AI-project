import os
import pandas as pd

def merge_csv(data_path, common):
    csv_list = [file for file in os.listdir(data_path) if file.endswith('.csv')]
    if not csv_list:
        return None
    
    merged_file = pd.read_csv(os.path.join(data_path, csv_list[0]))

    for i in csv_list[1:]:
        df = pd.read_csv(os.path.join(data_path, i))
        merged_file = pd.concat([merged_file, df], ignore_index=True)
        d = merged_file.drop_duplicates()
    return d

folder = "./result/"
same = 'title'

result_df = merge_csv(folder, same)

result_df.to_csv("./indexing_faiss/merged_crawling_data.csv", index=False)


