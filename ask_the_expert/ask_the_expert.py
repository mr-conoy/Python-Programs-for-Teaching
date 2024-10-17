from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('ask_the_expert/capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city

def write_to_file(country_name, city_name):
    with open('ask_the_expert/capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.withdraw()
the_world = {}

read_from_file()

while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country:')
    query_country = query_country.capitalize()

    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + ' is ' + result)
    else:
        new_city = simpledialog.askstring('Teach me', 'I don\'t know! ' + 'What is the capital city of ' + query_country + '?')
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)

    ask_again = messagebox.askyesno('Continue?', 'Do you want to ask another question?')
    if not ask_again:
        break

root.mainloop()