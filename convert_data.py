import pandas as pd
import json
import os

file_path = 'd:/المكتب/قاعدة بيانات القسم/student_neutration/data.xlsx'
json_path = 'd:/المكتب/قاعدة بيانات القسم/student_neutration/data.json'

try:
    df = pd.read_excel(file_path)
    # Convert all columns to string to avoid serialization issues and ensuring searching works as expected
    df = df.astype(str)
    
    # Save to JSON
    df.to_json(json_path, orient='records', force_ascii=False)
    
    with open('d:/المكتب/قاعدة بيانات القسم/student_neutration/columns.txt', 'w', encoding='utf-8') as f:
        f.write("Columns: " + str(df.columns.tolist()) + "\n")
        f.write("First Record: " + str(df.iloc[0].to_dict()) + "\n")
    
    print("Conversion successful. Output written to columns.txt")
except Exception as e:
    print(f"Error: {e}")
