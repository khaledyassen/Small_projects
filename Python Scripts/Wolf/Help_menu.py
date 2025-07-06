import argparse , textwrap
import os
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define ANSI escape codes for colors and formatting
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE

# Look for file validation
def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error(f"{BOLD}{RED}{GREEN}\'{arg}\'{RED} does not exist..{RESET}")
    else:
        return arg

# Look for folder validation
def is_valid_folder_path(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return folder_path
    else:
        raise argparse.ArgumentTypeError(f"{BOLD}{RED}Invalid folder path: {folder_path}{RESET}")

def help_menu():
    parser = argparse.ArgumentParser(description=f'{BOLD}{GREEN}Wolf is a tool for web application crawling..{WHITE}',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent(f'''
    {BOLD}{YELLOW}{BOLD}Example: {WHITE}{BOLD}python3 Wolf.py (-t {UNDERLINE}{BLUE}\'https://target.com\'{RESET}{BOLD} | -tf {BLUE}\'Targets_File.txt\'{WHITE}{BOLD} | -tn {BLUE}\'Nmap_File.\'{WHITE}{BOLD}) --scan 
    '''))
    print(f"{BOLD}")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--Target', metavar='\'Url\'', help=f'{BLUE}Target URL to check.{WHITE}')
    group.add_argument('-tf', '--Targets-File', metavar='\'File_Path\'', help=f'{BLUE}Targets file to check{WHITE}', type=lambda x: is_valid_file(parser, x))
    group.add_argument('-tn', '--TNmap-File', metavar='\'File_Path\'', help=f'{BLUE}Targets Nmap file to check{WHITE}', type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-w', '--word-list', metavar='\'File_Path\'', help=f'{BLUE}Custom wordlist file default: common.txt {WHITE}', type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-tr', '--threads', metavar='Number', type=float, default=30, help=f'{BLUE}Number of threads per second default: 40{WHITE}')
    parser.add_argument('-d', '--delay', metavar='Number', type=float, default=0.5, help=f'{BLUE}Delay between threads in seconds default: 0.6s{WHITE}')
    parser.add_argument('-c', '--cookie', metavar='{\"parameter\": \"value\"}', help=f'{BLUE}Enter cookies as a dictionary {WHITE}')
    parser.add_argument('-hr', '--header', metavar='{\"header\": \"value\"}', help=f'{BLUE}Enter headers as a dictionary{WHITE}')
    parser.add_argument('-ua', '--user-agent', metavar='\'User_Agent\'',  help=f'{BLUE}Set custom user-agent{WHITE}')
    parser.add_argument('-p', '--proxy', metavar='{\"http|https\": \"url\"}', help=f'{BLUE}Intercept Requests using proxy server default: http|https://127.0.0.1:8080{WHITE}')
        # Try to change the output file to directory like parser.add_argument('-o', help='folder that contain results', nargs="?", const='output')
    parser.add_argument('-o', '--output', metavar='\'Folder_Path\'', default='output', help=f'{BLUE}Save Results in output folder{WHITE}', type=is_valid_folder_path)
    parser.add_argument('-s', '--scan', help=f'{BLUE}Run the Tool{WHITE}', action='store_true', required=True)
    args = parser.parse_args()
    RESET
    return args

if __name__=='__main__':
    args = help_menu()
    
                 