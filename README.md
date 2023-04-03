# Tests for ape-milkomeda ApeworX plugin

Install apeworx and the plugin from local repo

```
pip install eth-ape
```

From ape-milkomeda folder...

```
pip install .
```

This will install the Milkomeda chains connecting through their rpc. To check:

```
ape networks list --ecosystem milkomeda

```

You should see

```
milkomeda  (default)
├── c1
│   └── milkomeda  (default)
├── c1-testnet
│   └── milkomeda  (default)
├── a1
│   └── milkomeda  (default)
├── a1-testnet
│   └── milkomeda  (default)
└── local  (default)
    └── test  (default)
```





Add test account (this account should have funds on the several Milkomeda chains)

```
ape accounts import test
```

If you don't want to enter Y to agree to each transaction, comment out this line in `tests/conftest.py`

```
        #account.set_autosign(True, passphrase=os.environ.get("PASS"))
```

And enter the pass used to encrypto the test account in the .env file (from the `ape accounts import ...` step)


Run the tests on the different chains:

```
ape test --network :a1
ape test --network :a1-testnet
ape test --network :c1
ape test --network :c1-testnet
```

(If you didn't comment out the `set_autosign` then you will need the -s flag to be able to input)

```
ape test --network :a1 -s
ape test --network :a1-testnet -s
ape test --network :c1 -s
ape test --network :c1-testnet -s
```
