from lib.os_utils import get_user_os
from lib.docker_utils import execute_command_for_os
from lib.config_utils import get_choice_version, get_choice_api, recap_configuration

    
def main():
    
    os_choice = get_user_os()

    image_version = get_choice_version()
    api_choice = get_choice_api()

    recap_configuration(os_choice, image_version, api_choice)
    
    execute_command_for_os(os_choice, image_version , api_choice)

if __name__ == "__main__":
    main()
