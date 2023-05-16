from hsbchk import HSBCHKCsvImporter

CONFIG = [
    HSBCHKCsvImporter(
    # The HSBC Hong Kong account is a multi-currency account,
    # and you need to set up mappings for two Beancount accounts.
    account_mapping={
        'HKDSavings': 'Assets:Bank:HSBC:HK:HKDSavings',
        'FCYSavings': 'Assets:Bank:HSBC:HK:FCYSavings'
    },
    # Your bank account number
    last4_map={
        '123-456789-833': 'HSBC One'
    },
    # Although you have set up two Beancount accounts, the CSV statement is a single file.
    file_account_name='Assets:Bank:HSBC:HK'
    )
]