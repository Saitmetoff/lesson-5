def format_string(input_string):
    formatted_string = "-".join(input_string.lower().split())
    return formatted_string

sample_input = input("Enter: ")

output = format_string(sample_input)
print(output)