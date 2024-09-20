BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'

def get_choice_version():
    """Demande à l'utilisateur de spécifier la version de l'image Docker."""
    image_version = input(f"{BLUE}Veuillez spécifier la version de l'image docker que vous souhaitez créer {BOLD}(exemple: 1.0.0): {RESET}")
    return image_version

def get_choice_api():
    """Demande à l'utilisateur de spécifier l'API à utiliser."""
    api_choice = input(f"{BLUE}Veuillez spécifier pour quelle API vous souhaitez créer l'image docker {BOLD}(client, bo):{RESET} ")

    if api_choice not in ['client', 'bo']:
        print(f"{RED}Choix invalide. Veuillez spécifier 'client' ou 'bo'.{RESET}")
        return get_choice_api()
    
    return 'api-nodejs-dp-client' if api_choice == 'client' else 'api-nodejs-dp-bo'

def recap_configuration(os_choice, image_version, api_choice):
    """Affiche un récapitulatif de la configuration choisie."""
    print(f"{BOLD}{GREEN}Configuration choisie:{RESET}")
    print(f"{BLUE} => OS: {os_choice}")
    print(f" => Version de l'image: {image_version}")
    print(f" => API: {api_choice}{RESET}")

    confirmation = input("Confirmez-vous la configuration choisie? (o/n): ")
    if confirmation == 'o':
        return
    else:
        return main()
