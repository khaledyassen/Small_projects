import aiohttp
import asyncio
from urllib.parse import urljoin
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define ANSI escape codes for colors and formatting
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
UNDERLINE = '\033[4m'
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE

async def process_path(session, base_url, path):
    full_url = urljoin(base_url, path)
    async with session.get(full_url) as response:
        if response.status != 404:
            print_status(full_url, response.status)
        await asyncio.sleep(0.5)

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

async def enumerate_paths(base_url, paths, requests_per_second, delay_between_threads):
    try:
        async with aiohttp.ClientSession() as session:
            # Control the number of requests per second
            for path in paths:
                await asyncio.gather(process_path(session, base_url, path))
                await asyncio.sleep(1 / requests_per_second)  # Introduce delay based on requests per second

                # Introduce delay between threads
                await asyncio.sleep(delay_between_threads)

    except Exception as e:
        print(f"{BOLD}{RED}An error occurred:{WHITE} {e}")

# Example usage
base_url = "http://localhost"
paths_file = "path_list.txt"
requests_per_second = float(input("Enter number of requests per second: "))
delay_between_threads = float(input("Enter delay between threads (in seconds): "))

with open(paths_file, 'r') as file:
    paths = [path.strip() for path in file.readlines()]

# Run the event loop to execute asynchronous code
asyncio.run(enumerate_paths(base_url, paths, requests_per_second, delay_between_threads))
