filepath = input().split("\\")
filename_and_extension = filepath[-1]
filename, extension = filename_and_extension.split(".")

print(f"File name: {filename}")
print(f"File extension: {extension}")

# solution 2
# text = input().split("\\")
#
# for word in text:
#     if '.' in word:
#         file_name = word.split('.')[0]
#         file_extension = word.split('.')[1]
#
#         print(f"File name: {file_name}")
#         print(f"File extension: {file_extension}")
