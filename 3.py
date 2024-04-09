def replace_character_at_position(s, position, character):
    position -= 1

    modified_string = s[:position] + character + s[position + 1:]

    return modified_string


input_string = input().strip()
position, character = input().split()
position = int(position)

output_string = replace_character_at_position(input_string, position, character)

print(output_string)