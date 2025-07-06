import random
from colorama import init, Fore, Style
import argparse , textwrap
import os
import requests
import sys
import io
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import json
import xml.etree.ElementTree as ET
# =================================================================================================================================================== #

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

# Print the logo and the copyright
def Print_Logo():
    colors = [GREEN,YELLOW,BLUE,RED,MAGENTA]
    color_code = random.choice(colors)
    text= f"""
    Wolf+MNK0XNMMMMMMMMMMMMMMMMWXKKNW+Wolf
    MMMMMK;..';xNMMMMMMMMMMMMNO:'..'OWMMMM
    MMMMNc x0Kx..dNWMMMMMMMNk'.d00k.,XMMMM
    MMMMX',Ox0WN' .l00OO00d' .KW0xOc KWMMM
    MMMMK.:Od'oW:.;........,.'Nx'l0o OWMMM
    MMMWK 'dK' ..';:::::::::,.. .Kx; xWMMM
    MMMW0 :dk' lc::::::::::::cl..xoo dNMMM
    MMMNd  ;:;,c:clll::::lllc:c;;;c. :NMMM
    MWXx. .:lcc:loloo:::;oollo:cclc.  oXWM
    N0l .:lc::ddo;.l:.::.;l''oodc::lc. :ON
    WK'.l:;;''xlc' ..;:::.. .ccx;.;;;l'.OW
    Nl '.;:,. .dNXdccc:::cllKNk' .,::.'.;X
    X;  .;cc' ..'kOdkklckOdOO;.. .:l;.  .X
    N:. .lko.k;'lc000OOkOKOKol,,O'lkd. .'X
    W0k' k; lOd..l0XXNKKXNXKl; lOx 'k..x0W
    MWNO.'  lccc..WW,.  ..XM; l;ld  ' dNWM
    XMMWO. ..'c,  dNx,  'oNO. ,,;....xNMMK
    0MMMMXlko .... .,cccc;. . .. :0cKWMMMO
    MMMMMMWNNk.  .;. .... .,. ..dNNWMMMMMW
    MMMMMMMMMMNxd, ;c    ;c..oxXMMMMMMMMMM
    MMMMMMMMMMMMWN0l,'. .'cONWMMMMMMMMMMMM
    Wolf+MMMMMMMMMMMWKc:ONMMMMMMMMMMM+Wolf
    {BOLD}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Code By:       Khaled Yassen
    Twitter:       https://twitter.com/khaledyasse1882
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """
    print(f"{color_code}{text}{RESET}")
# =================================================================================================================================================== #

# validate file path
def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error(f"{BOLD}{RED}{GREEN}\'{arg}\'{RED} does not exist..{RESET}")
    else:
        return arg

# validate folder path
def is_valid_folder_path(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return folder_path
    else:
        raise argparse.ArgumentTypeError(f"{BOLD}{RED}Invalid folder path: {folder_path}{RESET}")
# =================================================================================================================================================== #

#  Parsing the xml namp output file 
def parse_nmap_results(xml_file, output_file):
    if not xml_file.endswith('.xml'):
        raise ValueError("Input file is not an XML file")

    with open(output_file, 'w') as f_out:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for host in root.findall('.//host'):
            ip_address = host.find('.//address').attrib['addr']

            for port in host.findall('.//port'):
                port_number = port.attrib['portid']
                service_elem = port.find('.//service')

                if service_elem is not None:
                    service_name = service_elem.attrib['name']
                    product = service_elem.attrib.get('product', '')
                    version = service_elem.attrib.get('version', '')

                    if 'http' in service_name.lower():
                        protocol = 'https' if port_number == '443' else 'http'
                        # Combine host, port, and protocol and write to the file
                        host_port_combo = f"{protocol}://{ip_address}:{port_number}"
                        f_out.write(f"{host_port_combo}\n")
# =================================================================================================================================================== #

def help_menu():
    parser = argparse.ArgumentParser(description=f'{BOLD}{GREEN}Wolf is a tool for web application crawling..{WHITE}',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent(f'''
    {BOLD}{YELLOW}{BOLD}Example: {WHITE}{BOLD}python3 Wolf.py (-t {UNDERLINE}{BLUE}\'https://target.com\'{RESET}{BOLD} | -tf {BLUE}\'Targets_File.txt\'{WHITE}{BOLD} | -tn {BLUE}\'Nmap_File.\'{WHITE}{BOLD}) --scan 
    '''))
    print(f"{BOLD}")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--target', metavar='\'Url\'', help=f'{BLUE}Target URL to check.{WHITE}')
    group.add_argument('-tf', '--targets-File', metavar='\'File_Path\'', help=f'{BLUE}Targets file to check{WHITE}', type=lambda x: is_valid_file(parser, x))
    group.add_argument('-tn', '--TNmap-File', metavar='\'File_Path.xml\'', help=f'{BLUE}Targets Nmap file in xml format to check{WHITE}', type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-w', '--word-list', metavar='\'File_Path\'', default='src/common.txt', help=f'{BLUE}Custom wordlist file default: common.txt {WHITE}', type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-tr', '--threads', metavar='Number', type=int, default=30, help=f'{BLUE}Number of threads per second default: 40{WHITE}')
    parser.add_argument('-d', '--delay', metavar='Number', type=float, default=0, help=f'{BLUE}Delay between threads in seconds default: 0.5s{WHITE}')
    parser.add_argument('-c', '--cookie', metavar='\'{\"parameter\": \"value\"}\'', default=None, help=f'{BLUE}Enter cookies as a dictionary {WHITE}')
    parser.add_argument('-hr', '--header', metavar='\'{\"header\": \"value\"}\'', help=f'{BLUE}Enter headers as a dictionary{WHITE}')
    parser.add_argument('-ua', '--user-agent', metavar='\'User_Agent\'', default=random.choice(random_agents),  help=f'{BLUE}Set custom user-agent{WHITE}')
    parser.add_argument('-p', '--proxy', metavar='\'{\"http\": \"url:port\", \"https\": \"url:port\"}\'', default=None, help=f'{BLUE}Intercept Requests using proxy server{WHITE}')
    parser.add_argument('-o', '--output', metavar='\'Folder_Path\'', help=f'{BLUE}Save Results in output folder default output{WHITE}',default='output', type=is_valid_folder_path)
    parser.add_argument('-s', '--scan', help=f'{BLUE}Run the Tool{WHITE}', action='store_true', required=True)
    args = parser.parse_args()
    RESET
    return args
# =================================================================================================================================================== #

random_agents = [
    'Mozilla/5.0 (Linux i686; U; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.51',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
    'Opera/9.64 (Windows NT 6.1; U; MRA 5.5 (build 02842); ru) Presto/2.1.1',
    'Mozilla/5.0 (compatible; Windows; U; Windows NT 6.2; WOW64; en-US; rv:12.0) Gecko/20120403211507 Firefox/12.0',
    'Mozilla/5.0 (Linux i686; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0',
    'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b11pre) Gecko/20110126 Firefox/4.0b11pre',
    'Mozilla/5.0 Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.13) Firefox/3.6.13',
    'Mozilla/5.0 (X11; U; Slackware Linux i686; en-US; rv:1.9.0.10) Gecko/2009042315 Firefox/3.0.10',
    'Mozilla/4.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11.0.1245.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.68 Safari/534.30',
    'Mozilla/5.0 (Windows 8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
    'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Opera/9.61 (Windows NT 6.0; U; pt-BR) Presto/2.1.1',
    'Mozilla/4.0 (compatible; Intel Mac OS X 10.6; rv:2.0b8) Gecko/20100101 Firefox/4.0b8)',
    'Mozilla/5.0 ArchLinux (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0b11pre) Gecko/20110126 Firefox/4.0b11pre',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'
    ]

# Get the links in the target url using BeautifulSoup
async def spider(url, header, cookie, proxy=None):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url, headers=header, cookies=cookie, proxies=proxy)
        # Check if the request was successful (status code 200)
        if response.status_code != 404:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all a tags (links) on the page
            links = soup.find_all('a')

            # Enumerate links
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)
                    domain = re.search(r'https?://([^/]+)', url).group(1) if re.search(r'https?://([^/]+)', url) else None
                    if domain in full_url:
                        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}")
                else:
                    pass
        else:
            print(f"{BOLD}{RED}URL Not found{RESET}")
        await asyncio.sleep(0.1)
    except requests.RequestException as req_err:
        print(f"{BOLD}{RED}Error for URL {BLUE}{UNDERLINE}'{url}': {req_err}{RESET}")
    except Exception as e:
        print(f"An error occurred: {e}")
# =================================================================================================================================================== #

# Enumerating paths from the Archive
async def Archive_paths(base_url):
    try:
        url = f"http://web.archive.org/cdx/search/cdx?url={base_url}*&output=text&fl=original&collapse=urlkey&filter=statuscode%3A200"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    print(f"{BOLD}{GREEN}{url}")
                    # Correct way to read response content and decode it
                    content = await response.text()
                    print(f"{BLUE}{UNDERLINE}{content}{RESET}")
                else:
                    print(f"{RED}Something bad happened, check your target URL")
                    
        await asyncio.sleep(0.1)
    except aiohttp.ClientError as req_err:
        print(f"{BOLD}{RED}Error for URL {BLUE}{UNDERLINE}'{base_url}': {req_err}{RESET}")
    except Exception as e:
        print(f"{BOLD}{RED}An error occurred:{WHITE} {e}")

# =================================================================================================================================================== #

def print_status(full_url, status_code):
    if status_code == 200:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {GREEN}{status_code}")
    elif status_code in {302, 301, 307}:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {MAGENTA}{status_code}")
    elif status_code in {403, 401}:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {YELLOW}{status_code}")
    elif status_code == 405:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {WHITE}{status_code} Method Not Allowed")
    else:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {RED}{status_code}")

async def process_path(session, base_url, path, header, cookie, proxy):
    full_url = urljoin(base_url, path)
    try:
        async with session.get(full_url, headers=header, cookies=cookie) as response: # here is a problem with the proxy 
            if response.status != 404:
                print_status(full_url, response.status)
            await asyncio.sleep(0.1)
    except aiohttp.ClientError as req_err:
        print(f"{BOLD}{RED}Error for URL {BLUE}{UNDERLINE}'{full_url}': {req_err}{RESET}")
        

# Fuzzing the target using wordlist
async def enumerate_paths(base_url,header, cookie, paths, requests_per_second, delay_between_threads,proxy=None):
    try:
        async with aiohttp.ClientSession() as session:
            # Control the number of requests per second
            for path in paths:
                try:
                    await asyncio.gather(process_path(session, base_url, path, header, cookie, proxy))
                    await asyncio.sleep(1 / requests_per_second)

                    # delay between threads
                    await asyncio.sleep(delay_between_threads)
                except Exception as e:
                    print(f"{BOLD}{RED}An error occurred for URL {BLUE}'{path}': {e}{RESET}")

    except Exception as e:
        print(f"{BOLD}{RED}An error occurred:{WHITE} {e}")
# =================================================================================================================================================== #


# Start the Main Function
async def main(target, header, cookie, delay, threads, wordlist_Path, output_Path, proxy=None):
    #  update the Referer header with the target url
    header['Referer'] = target
    sys.stdout = io.StringIO()
    main.counter = getattr(main, 'counter', 0) + 1
    counter = main.counter
    
    with open(wordlist_Path, 'r') as file:
        paths = [path.strip() for path in file.readlines()]

    batch =  asyncio.gather(
        spider(target, header, cookie, proxy),
        Archive_paths(target),
        enumerate_paths(target,header, cookie, paths, threads, delay, proxy)
        )
    await batch

    # Capture the output
    captured_output = sys.stdout.getvalue()
    # Reset standard output to the original value
    sys.stdout = sys.__stdout__
    print(captured_output)
    # Save captured output to files
    with open(f'{output_Path}/Wolf_Result_Target_{counter}.txt', 'w') as file:
        file.write(captured_output)

    print(f"{BOLD}{GREEN}Results saved to: {UNDERLINE}{BLUE}{output_Path}/Wolf_Result_Target_{counter}.txt")

# =================================================================================================================================================== #

if __name__=='__main__':
    Print_Logo()
    args = help_menu()
    header = {'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': args.user_agent,'Referer': 'Target URL'}
    try:
        if args.header:
            header_in = json.loads(args.header)
            header.update(header_in)
        if args.cookie:
            args.cookie = json.loads(args.cookie)
        if args.proxy:
            args.proxy = json.loads(args.proxy)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        print("Invalid input for dictionary. Please enter a valid JSON-formatted dictionary.")
        exit()
    except ValueError as ve:
        print(ve)
        exit()
    
    # run the tool
    if args.target:
        asyncio.run(main(args.target, header, args.cookie, args.delay, args.threads, args.word_list, args.output, args.proxy))
    elif args.targets_File:
        with open(args.targets_File, 'r') as t:
            targets = [targ.strip() for targ in t.readlines()]
        for target in targets:
            asyncio.run(main(target, header, args.cookie, args.delay, args.threads, args.word_list, args.output, args.proxy))
    elif args.TNmap_File:
        nmap_output_file = f"{args.output}/Nmap_Out.txt"
        try:
            parse_nmap_results(args.TNmap_File, nmap_output_file)
        except ValueError as e:
            print(f"{BOLD}{RED}Error in parsing the xml file Try again: {e}{RESET}")
        with open(nmap_output_file, 'r') as t:
            targets = [targ.strip() for targ in t.readlines()]
        for target in targets:
            asyncio.run(main(target, header, args.cookie, args.delay, args.threads, args.word_list, args.output, args.proxy))


    # print(header)
    # print(args.cookie)
    # print(args.proxy)
    # print(args.delay)
    # print(args.threads)
    # print(args.word_list)
    # print(args.user_agent)
    # header['Referer'] = args.target
    # print(header)

