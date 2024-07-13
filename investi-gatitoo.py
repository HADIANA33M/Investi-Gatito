import socket
import dns.resolver
import requests
import random

def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "Not found"

def get_dns_records(domain):
    records = {}
    for qtype in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']:
        try:
            answers = dns.resolver.resolve(domain, qtype)
            records[qtype] = [rdata.to_text() for rdata in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            records[qtype] = "Not found"
    return records

def get_server_details(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        return {k: v for k, v in response.headers.items() if k in ['Server', 'Content-Type', 'Date']}
    except requests.exceptions.RequestException:
        return "Not found"

def gather_domain_info(domain):
    domain_info = {
        'IP Address': get_ip_address(domain),
        'DNS Records': get_dns_records(domain),
        'Server Details': get_server_details(domain)
    }
    return domain_info
    

    
def display_investigatito():
    ascii_art = r"""

 
.-./`),---.   .--,---.  ,---.  .-''-.    .-'''-.,---------..-./`)     ,-.       _,---._ __  / \          .-_'''-.     ____  ,---------..-./`),---------.   ,-----.     
\ .-.'|    \  |  |   /  |   |.'_ _   \  / _     \          \ .-.')   /  )    .-'       `./ /   \       '_( )_   \  .'  __ `\          \ .-.'\          \.'  .-,  '.   
 `-' |  ,  \ |  |  |   |  ./ ( ` )   '(`' )/`--'`--.  ,---/ `-' \   (  (   ,'            `/    /|      |(_ o _)|  '/   '  \  `--.  ,---/ `-' \`--.  ,---/ ,-.|  \ _ \  
 `-'`"|  |\_ \|  |  | _ |  . (_ o _)  (_ o _).      |   \   `-'`"`   \  `-"             \'\   / |      . (_,_)/___||___|  /  |  |   \   `-'`"`   |   \ ;  \  '_ /  | : 
 .---.|  _( )_\  |  _( )_  |  (_,_)___|(_,_). '.    :_ _:   .---.     `.              ,  \ \ /  |      |  |  .-----.  _.-`   |  :_ _:   .---.    :_ _: |  _`,/ \ _/  | 
|   || (_ o _)  \ (_ o._) '  \   .---.---.  \  :   (_I_)   |   |       /`.          ,'-`----Y   |      '  \  '-   ..'   _    |  (_I_)   |   |    (_I_) : (  '\_/ \   ; 
|   ||  (_,_)\  |\ (_,_) / \  `-'    \    `-'  |  (_(=)_)  |   |      (            ;        |   '      \  `-'`   ||  _( )_  | (_(=)_)  |   |   (_(=)_) \ `"/  \  ) /  
|   ||  |    |  | \     /   \       / \       /    (_I_)   |   |      |  ,-.    ,-'         |  /         \        /\ (_ o _) /  (_I_)   |   |    (_I_)   '. \_/``".'   
'---''--'    '--'  `---`     `'-..-'   `-...-'     '---'   '---'      |  | (   |        hjw | /           `'-...-'  '.(_,_).'   '---'   '---'    '---'     '-----'     
                                                                       )  |  \  `.___________|/                                                                  
 								       `--'   `--'                 
                                                                                              


    """
    print(ascii_art)






if __name__ == "__main__":
    display_investigatito()

    domain = input("\n\nEnter the domain(example.com): ")
    domain_info = gather_domain_info(domain)
    
    print("\n---------Domain Information------------")
    print(f"IP Address: {domain_info['IP Address']}")
    print("\n--------------DNS Records---------------")
    for qtype, records in domain_info['DNS Records'].items():
        print(f"  {qtype}: {records}")
    print("\n-------------Server Details--------------")
    if isinstance(domain_info['Server Details'], dict):
        for key, value in domain_info['Server Details'].items():
            print(f"  {key}: {value}")
    else:
        print(f"  {domain_info['Server Details']}")
