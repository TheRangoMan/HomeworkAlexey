import json

try:
    with open(r'C:\Users\Alexey\Desktop\Python 2.0\HomeworkAlexey\homework2.py') as file_object:
        
        for line in file_object:
            print(line)      
        json.dumps(object, ensure_ascii=False)    
except FileNotFoundError:
    print("No such file exists!")
except IOError:
    print("Cannot read / write file maybe disk is corrupted")
except Exception as e:
    print("Something wrong!", repr(e))
finally:
    print('YES')
    

 