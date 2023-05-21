import os

name = "DBDConfigurations"
version = "0.2.0"
print(f"{name} v{version} (by Neinndall)")

# Menú de inicio
input("Welcome to my new tool, this tool will be used for a simple function, change settings of the 'GameUserSettings' file, without you having to go to that file yourself, I hope you like it.\n\nPress ENTER to start!")
os.system("cls")

# Ruta del archivo
default_path = r"C:\Users\{}\AppData\Local\DeadByDaylight\Saved\Config\WindowsClient"
print("Default Path:", default_path)
username = input("Enter your username: ")
file_path = default_path.format(username)
print()

# Verificación de la ruta del archivo
while not os.path.exists(file_path):
    print("The file path you entered does not exist")
    file_path = input("Introduce path of the file: ")
    print()

# Archivo
default_file = "GameUserSettings.ini"
file = input("Default File: {}\nEnter the name of the file to edit: ".format(default_file))
print()

# Verificación del archivo
while not os.path.exists(os.path.join(file_path, file)):
    print("The file you entered does not exist")
    file = input("Enter the name of the file to edit: ")
    print()

# Ruta completa
full_path = os.path.join(file_path, file)
print("This is your full path:", full_path)
print()

# Cadena de búsqueda
search = input("Enter what you want to search for editing: ")
print()
print("Search results:")
print("-------------------------")
with open(full_path, "r") as file_content:
    for line in file_content:
        if search.lower() in line.lower():
            print(line, end="")
print("-------------------------")
print()

# Reemplazo de valor
value_replace = input("Enter the value to replace: ")
print()

new_value = input("Enter the new value: ")
print()

# Verificación del valor
with open(full_path, "r") as file_content:
    if value_replace not in file_content.read():
        print("The value does not exist in the file")
        value_replace = input("Enter the value to replace: ")
        print()

# Ejecución
with open(full_path, "r") as file_content:
    file_data = file_content.read()
    file_data = file_data.replace(value_replace, new_value)
with open(full_path, "w") as file_content:
    file_content.write(file_data)
print("The value has been replaced successfully. Finished!")
input("Press ENTER to exit!")
