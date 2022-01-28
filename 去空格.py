import os
filenames=os.listdir("images/total2020")
for filename in filenames:
    os.rename("images/total2020/"+filename, "images/total2020/"+filename.replace(' ', ''))
# import os, sys
# import json
#
#
# def get_new_json(filepath, key, value):
#     key_ = key.split(".")
#     key_length = len(key_)
#     with open(filepath, 'r+') as f:
#         json_data = json.loads(f.read())
#         i = 0
#         a = json_data
#         while i < key_length:
#             if i + 1 == key_length:
#                 a[key_[i]] = value
#                 i = i + 1
#             else:
#                 a = a[key_[i]]
#                 i = i + 1
#     f.close()
#     return json_data
#
#
# def rewrite_json_file(filepath, json_data):
#     with open(filepath, 'w') as f:
#         json.dump(json_data, f)
#     f.close()
#
#
# if __name__ == '__main__':
#     key = "imagePath"
#
#     json_path = os.listdir("labelme/total2020")
#     for i in json_path:
#         value=i.split(".",-1)[0].replace(" ","")+".jpg"
#         m_json_data = get_new_json("labelme/total2020/"+i, key, value)
#         rewrite_json_file("labelme/total2020/"+i, m_json_data)