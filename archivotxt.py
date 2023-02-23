with open('alumnos2.txt', 'a') as file: # r - read | w - write | a - append
    # content = file.read().splitlines()
    # print(content)
    # file.seek(0) # Regresa el cursor del buffer a la primera posición
    # content2 = file.read().splitlines()
    # print(f"content 2 {content2}")
    # alumnos = file.readlines()
    # print(alumnos)
    file.write('Hello World')
    file.write('New Hello World')
