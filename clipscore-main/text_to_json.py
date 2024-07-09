import json  
  
# 输入和输出文件的名称  
input_filename = 'C:\\Users\\87161\\Desktop\\clipscore-main\\image -Caption-Florence 2.txt'  
output_filename = 'candidates3.json'  
  
# 初始化一个空列表，用于存储JSON对象  
json_data = {}  
  
# 打开文本文件并逐行读取  
with open(input_filename, 'r') as file:  
    num=1
    for line in file:  
        # person = {  
        #     num:line
        # }  
            # 将字典添加到json_data列表中  
        json_data[f"{num}"] = line 
        num=num+1
  
# 将列表转换为JSON格式，并写入到输出文件中  
with open(output_filename, 'w') as file:  
    json.dump(json_data, file,indent=2)  
  
print(f'数据已从"{input_filename}"读取并转换为JSON格式，保存到"{output_filename}"中。')