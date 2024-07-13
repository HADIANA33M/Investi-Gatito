
# Investi Gatito

Investi-gatito retrieves various information about a given domain, including its IP address, DNS records, and server details.



## Features

- **Get IP Address**: Resolves the domain to its corresponding IP address.
- **Retrieve DNS Records**: Fetches different DNS record types: A, AAAA, MX, NS, TXT, and SOA.
- **Server Details**: Obtains the server information, including server type, content type, and response date.


## Prerequisites

To run this script, you need to have Python 3 installed on your Linux machine. Also, you will need to install the Python packages that are required.


### Required Packages

- `dnspython`: For DNS resolution.
- `requests`: For making HTTP requests.

## Installation

1. Clone the repository

```bash
  git clone https://github.com/HADIANA33M/Investi-Gatito.git 
  cd Investi-Gatito
```

2. Install the required packages:    
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install dnspython requests

```
## Usage

Run the script using Python 3:

```bash
python3 investi-gatitoo.py

```

You will be prompted to enter a domain name (e.g., example.com):
```scss
Enter the domain(example.com): 

```
## Example Output

```less
---------Domain Information------------
IP Address: 93.184.216.34

--------------DNS Records---------------
  A: ['93.184.216.34']
  AAAA: ['2606:4700:30::681c:d8']
  MX: ['mail.example.com.']
  NS: ['ns1.example.com.']
  TXT: ['"v=spf1 include:_spf.example.com ~all"']
  SOA: ['dns.example.com.']

-------------Server Details--------------
  Server: nginx
  Content-Type: text/html; charset=utf-8
  Date: Thu, 01 Jan 2024 00:00:00 GMT


```
