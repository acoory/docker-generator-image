import subprocess
import os
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

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