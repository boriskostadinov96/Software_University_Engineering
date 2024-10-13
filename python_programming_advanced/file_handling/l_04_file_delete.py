import os

path = os.path.join("just_created.txt")

try:
    os.remove(path)
except FileNotFoundError:
    print('File already deleted!')

# 1.1
#
# if os.path.exists(path):
#     os.remove(path)
# else:
#     print("File is already deleted")