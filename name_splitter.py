def name_splitter(full_name):
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]
    return (first_name, last_name)
print("Name Splitter: ", name_splitter("John Doe"))