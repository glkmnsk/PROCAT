from hire import Name, Driver

print('*' *25)
name = Name.import_from_file('name.src')
[print(el) for el in name]

print('*' *25)
driver = Driver.import_from_file('driver.src')
[print(el) for el in driver]