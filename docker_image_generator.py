import subprocess
import os

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BLUE = '\033[94m'
BOLD = '\033[1m'

def get_user_os():
    """Demande à l'utilisateur de spécifier l'OS."""
    os_choice = input(f"{BLUE}Veuillez spécifier pour quel architecture vous souhaitez créer l'image docker {BOLD}(mac, ubuntu, windows):{RESET} ")
    
    if os_choice not in ['mac', 'ubuntu', 'windows']:
        print(f"{RED}Choix invalide. Veuillez spécifier 'mac', 'ubuntu', ou 'windows'.{RESET}")
        return get_user_os()  # Redemander en cas de choix invalide
    return os_choice

def get_choice_version():
    """Demande à l'utilisateur de spécifier la version de l'image docker qui sera créée."""
    image_version = input(f"{BLUE}Veuillez spécifier la version de l'image docker que vous souhaitez créer {BOLD}(exemple: 1.0.0): {RESET}")
    return image_version

def get_choice_api():
    """Demande à l'utilisateur de spécifier l'API à utiliser."""
    api_choice = input(f"{BLUE}Veuillez spécifier pour quelle API vous souhaitez créer l'image docker {BOLD}(client, bo):{RESET} ")

    if api_choice not in ['client', 'bo']:
        print(f"{RED}Choix invalide. Veuillez spécifier 'client' ou 'bo'.{RESET}")
        return get_choice_api()
    
    if api_choice == 'client':
        api_choice = 'api-nodejs-dp-client'
    else:
        api_choice = 'api-nodejs-dp-bo'

    return api_choice

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

def execute_command_for_os(os_choice, image_version, api_choice):

    """Exécute une commande spécifique en fonction de l'OS choisi."""
    if os_choice == 'mac':
        platform = 'linux/arm64'
        format_image_version = image_version.replace('.', '-')


        docker_build_command = "docker buildx build --platform " + platform +  " -t " + api_choice + ":" + image_version + " -f ./Dockerfile-prod ./ --load"
        docker_save_command = "docker save -o " + api_choice + "-" + format_image_version + ".tar " + api_choice + ":" + image_version
        zip_command = "zip " + api_choice + "-" + format_image_version + ".zip " + api_choice + "-" + format_image_version + ".tar"

        try:
            print(f"{GREEN}Création de l'image docker pour macOS version {image_version}...{RESET}")
            
            subprocess.run(docker_build_command, shell=True)
            working_directory = os.getcwd()
            os.chdir(working_directory + "/docker-image/mac-arm64")
            subprocess.run(docker_save_command, shell=True)
            subprocess.run(zip_command, shell=True)

            print(f"{GREEN}L'image docker pour macOS a été créée avec succès dans le dossier docker-image/mac-arm64{RESET}")

        except Exception as e:
            print(f"{RED}Une erreur s'est produite lors de la création de l'image docker pour macOS: {e}{RESET}")

        choice_execution = input("Voulez-vous exécuter l'image docker pour macOS? (o/n): ")

        if choice_execution == 'o':
            load_command = "docker load -i " + api_choice + "-" + format_image_version + ".tar" 
            if api_choice == 'api-nodejs-dp-bo':
                run_command = "docker run -d --name " + api_choice + " -e NAME=BO -e REDIS_ACTIVATE=true -e PORT=4000 " + api_choice + ":" + image_version
            else:
                run_command = "docker run -d --name " + api_choice + " -e NAME=CLIENT -e REDIS_ACTIVATE=true -e PORT=4000 " + api_choice + ":" + image_version

            try:
                subprocess.run(load_command, shell=True)
                working_directory = os.getcwd()
                os.chdir("../..")
                subprocess.run(run_command, shell=True)
                print(f"{GREEN}L'image docker pour macOS a été exécutée avec succès!{RESET}")
            except Exception as e:
                print(f"{RED}Une erreur s'est produite lors de l'exécution de l'image docker pour macOS: {e}{RESET}")
        else:
            return
        
        
    elif os_choice == 'ubuntu':
        platform = 'linux/amd64'
        format_image_version = image_version.replace('.', '-')

        docker_build_command = "docker buildx build --platform " + platform +  " -t " + api_choice + ":" + image_version + " -f ./Dockerfile-prod ./ --load"
        docker_save_command = "docker save -o " + api_choice + "-" + format_image_version + ".tar " + api_choice + ":" + image_version
        zip_command = "zip " + api_choice + "-" + format_image_version + ".zip " + api_choice + "-" + format_image_version + ".tar"

        try:
            print(f"{GREEN}Création de l'image docker pour Ubuntu version {image_version}...{RESET}")

            subprocess.run(docker_build_command, shell=True)
            working_directory = os.getcwd()
            os.chdir(working_directory + "/docker-image/ubuntu-amd64")
            subprocess.run(docker_save_command, shell=True)
            subprocess.run(zip_command, shell=True)
            print(f"{GREEN}L'image docker pour Ubuntu a été créée avec succès dans le dossier docker-image/ubuntu-amd64{RESET}")
    
            return
        except Exception as e:
            print(f"{RED}Une erreur s'est produite lors de la création de l'image docker pour Ubuntu: {e}{RESET}")

        try:
            print(f"{GREEN}Création de l'image docker pour Ubuntu version {image_version}...{RESET}")
            subprocess.run(docker_build_command, shell=True)
            print(f"{GREEN}L'image docker pour Ubuntu a été créée avec succès!{RESET}")
        except Exception as e:
            print(f"{RED}Une erreur s'est produite lors de la création de l'image docker pour Ubuntu: {e}{RESET}")

        



    elif os_choice == 'windows':
        print("Aucune configuration pour Windows.")
        return 
    
def main():
    
    os_choice = get_user_os()

    image_version = get_choice_version()
    api_choice = get_choice_api()

    recap_configuration(os_choice, image_version, api_choice)
    
    execute_command_for_os(os_choice, image_version , api_choice)

if __name__ == "__main__":
    main()
