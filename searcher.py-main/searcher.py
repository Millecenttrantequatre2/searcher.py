import os
from tqdm import tqdm
from colorama import init, Fore

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_files(search_term, database_folder, max_results=10):
    results = []
    results_found = 0
    file_count = sum(len(files) for _, _, files in os.walk(database_folder))

    with tqdm(total=file_count) as pbar:
        for root, _, files in os.walk(database_folder):
            for file in files:
                pbar.update(1)
                if file.endswith(('.txt', '.csv', '.sql')):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', errors='ignore') as f:
                        for line in f:
                            if search_term in line:
                                results.append(line.strip())
                                results_found += 1
                                if results_found >= max_results:
                                    return results
    return results

def save_results(results):
    save_choice = input(Fore.LIGHTBLUE_EX + "Voulez-vous enregistrer les résultats dans un fichier texte ? (Y/N): " + Fore.RESET)
    if save_choice.lower() == 'y':
        file_name = input(Fore.LIGHTBLUE_EX + "Entrez un nom pour le fichier de sauvegarde: " + Fore.RESET)
        with open(f"{file_name}.txt", "w") as file:
            for result in results:
                file.write(result + "\n")
        print(Fore.LIGHTBLUE_EX + f"Les résultats ont été enregistrés dans le fichier {file_name}.txt" + Fore.RESET)

def main():
    databases = {
        '1': r"",#chemins de la ou des db 
        '2': r"",#chemins de la ou des db 
        '3': r"",#chemins de la ou des db 
        '4': r"",#chemins de la ou des db 
        '5': r""#chemins de la ou des db 
    }

    db_choice = None
    while True:
        if not db_choice:
            clear_screen()
            print(Fore.LIGHTBLUE_EX + """
               /$$     /$$    /$$$$$$  /$$   /$$ 
             /$$$$   /$$$$   /$$__  $$| $$  | $$ 
            |_  $$  |_  $$  |__/  \ $$| $$  | $$ 
              | $$    | $$     /$$$$$/| $$$$$$$$ 
              | $$    | $$    |___  $$|_____  $$ by 1134 
              | $$    | $$   /$$  \ $$      | $$
             /$$$$$$ /$$$$$$|  $$$$$$/      | $$ 
            |______/|______/ \______/       |__/         
                                               """ + Fore.RESET)
            print(Fore.LIGHTBLUE_EX + "Choisissez la base de données à rechercher:" + Fore.RESET)
            for key in databases.keys():
                print( f"{Fore.LIGHTBLUE_EX}{key}: Database {key}{Fore.RESET}")
            db_choice_input = input(Fore.LIGHTBLUE_EX + "Entrez un numéro de base de données 'q' pour quitter: " + Fore.RESET)

            if db_choice_input.lower() == 'q':
                break
            if db_choice_input in databases:
                db_choice = db_choice_input

        database_folder = databases[db_choice]
        term = input(Fore.LIGHTBLUE_EX + "Que voulez-vous chercher ?=> " + Fore.RESET)
        if term.lower() == 'q':
            break

        results = search_files(term, database_folder)
        if results:
            print(Fore.LIGHTBLUE_EX + "Résultats trouvés :" + Fore.RESET)
            for result in results:
                print(result)
            save_results(results)
        else:
            print(Fore.LIGHTBLUE_EX + "Aucun résultat n'a été trouvé" + Fore.RESET)

        change_db = input(Fore.LIGHTBLUE_EX + "Voulez-vous changer de base de données ? (Y/N): " + Fore.RESET)
        if change_db.lower() == 'y':
            db_choice = None

if __name__ == "__main__":
    main()
