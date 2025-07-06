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
import pkg_resources

modules = [
    'colorama', 'argparse', 'os', 'requests', 'sys', 'io', 'asyncio',
    'aiohttp', 'bs4', 'urllib', 're', 'json'
]

for module_name in modules:
    try:
        version = pkg_resources.get_distribution(module_name).version
        print(f"The version of {module_name} is: {version}")
    except pkg_resources.DistributionNotFound:
        print(f"{module_name} is not installed.")
    except Exception as e:
        print(f"{BeautifulSoup.__version__}")
        print(f"An error occurred while retrieving the version of {module_name}: {e}")

