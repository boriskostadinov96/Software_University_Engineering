def loading_bar(some_number: int):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    loaded_percent = some_number // 10
    return f"{some_number}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."


number = int(input())
print(loading_bar(number))


# solution 2 (stupid one but working)
# def loading_bar(num):
#     if num == 0:
#         print('0% [..........]\nStill loading...')
#
#     elif num == 10:
#         print('10% [%.........]\nStill loading...')
#
#     elif num == 20:
#         print('20% [%%........]\nStill loading...')
#
#     elif num == 30:
#         print('30% [%%%.......]\nStill loading...')
#
#     elif num == 40:
#         print('40% [%%%%......]\nStill loading...')
#
#     elif num == 50:
#         print('50% [%%%%%.....]\nStill loading...')
#
#     elif num == 60:
#         print('60% [%%%%%%....]\nStill loading...')
#
#     elif num == 70:
#         print('70% [%%%%%%%...]\nStill loading...')
#
#     elif num == 80:
#         print('80% [%%%%%%%%..]\nStill loading...')
#
#     elif num == 90:
#         print('90% [%%%%%%%%%.]\nStill loading...')
#
#     elif num == 100:
#         print('100% Complete!\n[%%%%%%%%%%]')
#
#
# num = int(input())
# loading_bar(num)
