BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'
RED = '\033[91m'

def get_user_os():
    """Demande à l'utilisateur de spécifier l'OS."""
    os_choice = input(f"{BLUE}Veuillez spécifier pour quel architecture vous souhaitez créer l'image docker {BOLD}(mac, ubuntu, windows):{RESET} ")
    
    if os_choice not in ['mac', 'ubuntu', 'windows']:
        print(f"{RED}Choix invalide. Veuillez spécifier 'mac', 'ubuntu', ou 'windows'.{RESET}")
        return get_user_os()  # Redemander en cas de choix invalide
    return os_choice
