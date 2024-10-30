def format_name(f_name, l_name):
    first = f_name
    last = l_name
    first_name = first.capitalize()
    last_name = last.title()
    return f"{first_name} {last_name}"

#print(format_name("zEoN", "oJUOKO"))

fullname = format_name("zEoN", "oJUOKO")
print(fullname)
   