import os

import pytest
from ape import accounts, networks
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def signer():
    ecosystem = networks.active_provider.network.ecosystem.name
    if ecosystem == 'milkomeda':
        account = accounts.load('test')
        account.set_autosign(True, passphrase=os.environ.get("PASS"))
        return account
    else:
        return accounts[0]



@pytest.fixture(scope="session")
def contract(project, signer):
    return project.Storage.deploy(sender=signer)