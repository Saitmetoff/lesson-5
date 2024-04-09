def print_full_name(first, last):
    msg = f"Hello {first} {last}! You just delved into python."
    return msg
first = input("Enter: ")
last = input("Enter: ")

output_msg = print_full_name(first, last)
print(output_msg)