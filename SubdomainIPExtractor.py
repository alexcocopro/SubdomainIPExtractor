import re
import argparse
from colorama import init, Fore, Style

# Inicializa colorama (especialmente para Windows)
init(autoreset=True)

ip_regex = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
subdomain_regex = re.compile(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b')

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False
    return True

def extract_from_file(input_file):
    ips = set()
    subdomains = set()

    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            for ip_match in ip_regex.findall(line):
                if is_valid_ip(ip_match):
                    ips.add(ip_match)

            for sub_match in subdomain_regex.findall(line):
                if not ip_regex.match(sub_match):
                    if not sub_match.endswith('.in-addr.arpa') and not sub_match.endswith('.ip6.arpa'):
                        subdomains.add(sub_match.lower())

    with open('subdomains.txt', 'w') as f_sub:
        for sub in sorted(subdomains):
            f_sub.write(sub + '\n')

    with open('ips.txt', 'w') as f_ip:
        for ip in sorted(ips):
            f_ip.write(ip + '\n')

    print(f"{Fore.GREEN}[+] Processed input file: {Fore.CYAN}{input_file}")
    print(f"{Fore.GREEN}[+] Extraction completed successfully!")
    print(f"{Fore.YELLOW}[+] Results saved in: {Fore.MAGENTA}subdomains.txt{Fore.RESET} and {Fore.MAGENTA}ips.txt")
    print(f"\n{Style.BRIGHT}Software developed by Alex Cabello Leiva, Cybersecurity Consultant{Style.RESET_ALL}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract subdomains and IPs from any text file")
    parser.add_argument('-i', '--input', required=True, help='Input text file path')
    args = parser.parse_args()

    extract_from_file(args.input)

