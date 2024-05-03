import os
from pystyle import Colorate, Colors
from tqdm import tqdm

os.system('cls')

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
                        lines = f.readlines()
                        for index, line in enumerate(lines):
                            if results_found >= max_results:
                              break
                        if search_term in line:
                                result_str = f'{line.strip()}'
                                results.append(result_str)
                                results_found += 1
                                if results_found >= max_results:
                                    break
    return results

def main():
    database_folder = r"----------------" #replace "---------" par ton chemins de la DATABASE, par exemple d:\database
    print(Colorate.Horizontal(Colors.red_to_green,"""
       /$$     /$$    /$$$$$$  /$$   /$$ 
     /$$$$   /$$$$   /$$__  $$| $$  | $$ 
    |_  $$  |_  $$  |__/  \ $$| $$  | $$ 
      | $$    | $$     /$$$$$/| $$$$$$$$ 
      | $$    | $$    |___  $$|_____  $$ by 1134 
      | $$    | $$   /$$  \ $$      | $$
     /$$$$$$ /$$$$$$|  $$$$$$/      | $$ 
    |______/|______/ \______/       |__/         
                                       """))
    term = input(Colorate.Horizontal(Colors.red_to_green, "Que veux-tu chercher ? ?=> "))

    while term.lower() != 'q':
        results = search_files(term, database_folder)
        if results:
            print(Colorate.Horizontal(Colors.white_to_blue, "Résultats trouvés :"))
            for result in results:
                print(result)
        else:
            print(Colorate.Horizontal(Colors.white_to_blue, "Aucun résultat n'a été trouvé."))

            
if __name__ == "__main__":
    main()
