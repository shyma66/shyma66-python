def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = input("Write something!\n-> ")
character_count = count_characters(input_string)
print("Number of characters:", character_count)