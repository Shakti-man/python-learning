def formate_name(f_name):
    new_string=""
    y=f_name.split()
    for letter in range(len(y)):
        new_string+=y[letter].capitalize()+" " 
    print(new_string)
name=input("type a sentence:\n")
formate_name(name)