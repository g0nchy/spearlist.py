import itertools

PROMPTS = {
    "nombre": "Ingresa el nombre: ",
    "apellido": "Ingresa el apellido: ",
    "apodo": "Ingresa el apodo: ",
    "nick": "Ingresa el nick: ",
    "año_de_nacimiento": "Ingresa el año de nacimiento (yyyy): ",
    "mes_de_nacimiento": "Ingresa el mes de nacimiento (mm): ",
    "dia_de_nacimiento": "Ingresa el día de nacimiento (dd): ",
    "equipo_deportivo": "Ingresa el equipo deportivo: ",
    "banda_musical": "Ingresa la banda musical: ",
    "mascota": "Ingresa el nombre de la mascota: ",
    "nombre_familiar": "Ingresa el nombre familiar: ",
    "nombre_pareja": "Ingresa el nombre de la pareja: ",
    "año_aniversario_pareja": "Ingresa el año de aniversario de pareja (yyyy): ",
    "mes_aniversario_pareja": "Ingresa el mes de aniversario de pareja (mm): ",
    "día_aniversario_pareja": "Ingresa el día de aniversario de pareja (dd): ",
    "contraseña_antigua": "Ingresa la contraseña antigua: ",
    "palabra_clave":"Ingresa la palabra clave: "
}

BOOLEAN_PROMPTS = {
    "lowercase": "¿Quiéres añadir todas las palabras en minúsculas a la wordlist? (S/N): ",
    "uppercase": "¿Quiéres añadir todas las palabras en mayúsculas a la wordlist? (S/N): ",
    "casing": "¿Quiéres añadir tan solo el primer caractér en mayúscula y el resto en minúscula a la wordlist? (S/N): ",
    "leet": "¿Quiéres añadir leet speak (cambiar las i por 1, las e por 3, etc) a la wordlist? (S/N): ",
    "reverse": "¿Quiéres añadir las palabras revertidas a la wordlist? (S/N): ",
}

def get_user_input(prompt):
    return input(prompt).strip().replace(" ", "")

def create_wordlist():
    victim_info = {}
    for key, prompt in PROMPTS.items():
        victim_info[key] = get_user_input(prompt)
    return victim_info

def get_booleans():
    choices = {}
    for key, prompt in BOOLEAN_PROMPTS.items():
        choices[key] = get_user_input(prompt).lower() == "s"
    return choices

def modify_wordlist(victim_info, choices):
    keyword_wordlist = []
    for key, value in victim_info.items():
        keyword_wordlist.append(value)

        if choices["lowercase"]:
            keyword_wordlist.append(value.lower())

        if choices["uppercase"]:
            keyword_wordlist.append(value.upper())

        if choices["casing"]:
            keyword_wordlist.append(value.capitalize())

        if key in ["año_de_nacimiento", "año_aniversario_pareja"]:
            year_abbr = value[-2:]
            keyword_wordlist.append(year_abbr)

        if choices["leet"]:
            leet_replace = str.maketrans("aeiots", "431075")
            leet_word = value.translate(leet_replace)
            keyword_wordlist.append(leet_word)

        if choices["reverse"]:
            keyword_wordlist.append(value[::-1])

    return keyword_wordlist

def generate_combined_wordlist(keyword_wordlist):
    combined_wordlist = []
    for r in range(1, 4):
        for combination in itertools.combinations(keyword_wordlist, r):
            combined_wordlist.append("".join(combination))
    return combined_wordlist

def save_wordlist(filename, wordlist):
    try:
        with open(filename, "w") as file:
            file.write("\n".join(wordlist))
        print(f"Wordlist saved as {filename}")
    except IOError as e:
        print(f"Error: Unable to save wordlist. {e}")

def main():
    print("#########################################################")
    print("# Wordlist Generation - Spear Social Engineering Attack #")
    print("#########################################################")
    print()

    victim_info = create_wordlist()
    print()
    choices = get_booleans()
    print()
    keyword_wordlist = modify_wordlist(victim_info, choices)
    combined_wordlist = generate_combined_wordlist(keyword_wordlist)

    filename = f"wordlist-{victim_info['nombre']}-{victim_info['apellido']}.txt"
    print()
    save_wordlist(filename, combined_wordlist)
    print()

if __name__ == "__main__":
    main()
