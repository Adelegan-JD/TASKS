names = input('Please enter three names and separate them by commas: ').strip(',').title().split()
unique_names = set(names)
dict_names = {name: len(name.strip(',')) for name in unique_names}
print(dict_names)

