import pandas as pd
import json
import os
import sys

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, 'data.xlsx')
JSON_PATH = os.path.join(BASE_DIR, 'data.json')
JS_PATH = os.path.join(BASE_DIR, 'data.js')

def build_data():
    print("Starting data build process...")
    
    if not os.path.exists(EXCEL_PATH):
        print(f"Error: {EXCEL_PATH} not found.")
        sys.exit(1)

    try:
        # Step 1: Excel to JSON
        print(f"Reading {EXCEL_PATH}...")
        df = pd.read_excel(EXCEL_PATH)
        
        # Ensure all data is string to prevent type issues in JS
        df = df.astype(str)
        
        # Write JSON (for debug/backup)
        print(f"Writing {JSON_PATH}...")
        df.to_json(JSON_PATH, orient='records', force_ascii=False, indent=2)
        
        # Step 2: JSON data to JS variable
        # We read back from the dataframe (or could read from JSON)
        data_list = df.to_dict(orient='records')
        
        js_content = f"window.studentData = {json.dumps(data_list, ensure_ascii=False)};"
        
        print(f"Writing {JS_PATH}...")
        with open(JS_PATH, 'w', encoding='utf-8') as f:
            f.write(js_content)
            
        print("Build successful! data.js has been updated.")
        
    except Exception as e:
        print(f"Error during build: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_data()
