key = [int(x) for x in input().split()]
line = input()

while line != "find":
    decrypted_message = []

    for i in range(len(line)):
        decrypted_char = chr(ord(line[i]) - key[i % len(key)])
        decrypted_message.append(decrypted_char)

    decrypted_message = ''.join(decrypted_message)

    treasure_type_start = decrypted_message.find('&') + 1
    treasure_type_end = decrypted_message.find('&', treasure_type_start)
    treasure_type = decrypted_message[treasure_type_start:treasure_type_end]

    coordinates_start = decrypted_message.find('<') + 1
    coordinates_end = decrypted_message.find('>')
    coordinates = decrypted_message[coordinates_start:coordinates_end]

    print(f"Found {treasure_type} at {coordinates}")

    line = input()
