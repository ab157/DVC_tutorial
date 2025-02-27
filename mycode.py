import pandas as pd
import os

data = {
    "name": ["Alex","John","Joe"],
    "age": [25,30,22],
    "city": ["kol", "mum", "blr"]
}

df = pd.DataFrame(data)

new_row_loc = {"name":"peter","age":32,"city":"hyd"}
df.loc[len(df.index)] = new_row_loc


data_dir="data"
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,"sample_data.csv")

df.to_csv(file_path,index=False)
print(f"csv file saved to {file_path}")