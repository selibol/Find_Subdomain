import requests


def get_subdomain():
    domains_txt = open('domain.txt', 'r')
    subdomains_txt = open('subdomain.txt', 'r')
    domains = domains_txt.read().splitlines()
    subdomains = subdomains_txt.read().splitlines()
    for domain in domains:
        for subdomain in subdomains:
            url = f"https://{subdomain}.{domain}"
            try:
                response = requests.get(url, timeout=7)
                if response.status_code == 200:
                    print("Active Subdomain", url)

            except Exception as e:
                print("Passive Subdomain", url)


if __name__ == '__main__':
    get_subdomain()

