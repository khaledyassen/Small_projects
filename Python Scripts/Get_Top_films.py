import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

# Initialize colorama
init()

# Define color constants
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RED = Fore.RED

def get_movie_details(movie_url, header):
    try:
        new_url_re = requests.get(movie_url, headers=header)
        htm_contn = new_url_re.text
        HTML_Soup2 = BeautifulSoup(htm_contn, 'html.parser')
        stars_container = HTML_Soup2.find('li', {'data-testid': 'title-pc-principal-credit'})
        stars_links = stars_container.find_all('a', {'class': 'ipc-metadata-list-item__list-content-item--link'})
        star_names = [star.text for star in stars_links]
        print(f"{GREEN}Name of the film: {YELLOW}{HTML_Soup2.title.text} \n{GREEN}Director:{YELLOW} {', '.join(star_names)}")
        print(f"{GREEN}Link for more detail {BLUE}{movie_url}")
        print("\n")
        print(f"{RED}==============================================================")
        print("\n")

    except Exception as e:
        print(f"{RED}Error occurred: {e}")

if __name__ == '__main__':
    url = "https://www.imdb.com/chart/top/?sort=user_rating%2Cdesc"
    try:
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
        snt = requests.get(url, headers=header)

        if snt.status_code == 200:
            html_content = snt.text
            HTML_Soup = BeautifulSoup(html_content, 'html.parser')
            value = HTML_Soup.find('div', class_="sc-29b01cb5-3 fEQdZD ipc-page-grid__item ipc-page-grid__item--span-2")
            a_va = value.find_all('a')

            # Use ThreadPoolExecutor for parallel processing
            with ThreadPoolExecutor(max_workers=8) as executor:
                # Submit each movie URL for processing
                futures = [executor.submit(get_movie_details, f"https://www.imdb.com/{i['href']}", header) for i in a_va]

                # Wait for all threads to complete
                for future in futures:
                    future.result()

        else:
            print(f"{RED}Something bad happened. Try again with a valid value.")
    except Exception as e:
        print(f"{RED}Error occurred: {e}")
