NEW_VALUE = 5

def test_retrieve_call(contract):
    assert contract.retrieve() == 0


def test_storee_call(contract, signer):
    assert contract.store(NEW_VALUE, sender=signer)


"""
Need to run tests with --disable-isolation for this one to pass
"""
# def test_retrieve_call2(contract):
#     assert contract.retrieve() == NEW_VALUE
