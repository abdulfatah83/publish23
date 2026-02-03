import json

json_path = 'd:/المكتب/قاعدة بيانات القسم/student_neutration/data.json'
js_path = 'd:/المكتب/قاعدة بيانات القسم/student_neutration/data.js'

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    js_content = f"window.studentData = {json.dumps(data, ensure_ascii=False)};"
    
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print(f"Successfully converted data.json to data.js")
except Exception as e:
    print(f"Error: {e}")
