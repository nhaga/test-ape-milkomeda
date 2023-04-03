import os

from ape import accounts, chain, config, networks, project
from dotenv import load_dotenv

load_dotenv()



def main():
    #account = get_account()

    print(os.environ.get("PASS"))
    return 1
    ecosystem = networks.active_provider.network.ecosystem.name
    if ecosystem == 'milkomeda':
        account = accounts.load('test')
    else:
        account = accounts.test_accounts[0]

    print(ecosystem)
