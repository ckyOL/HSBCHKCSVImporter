"""Importer for csv statement from HSBC in Hong Kong.
Please convert pdf into csv first.
"""
__copyright__ = "Copyright (C) 2023 ckyOL"
__license__ = "GNU GPLv3"

from os import path
import csv
from datetime import datetime
from beancount.core.number import D
from beancount.core.amount import Amount
from beancount.core.data import Transaction, Posting

EMPTY_SET = frozenset()

class HSBCHKCsvImporter:
    '''An importer for HSBC HK statement csv file.'''

    def __init__(self, account_mapping, last4_map, file_account_name):
        self.account_mapping = account_mapping
        self.last4_map = last4_map
        self.file_account_name = file_account_name

    def name(self):
        return self.__class__.__name__
    
    def identify(self, file):
        clean_filename = path.basename(file.name)
        # filename is 'BANK-(your bank number)-(year and month).csv'
        return clean_filename.startswith('BANK-') and clean_filename.endswith('.csv')

    def file_account(self, _):
        return self.file_account_name

    def file_date(self, file):
        return datetime.now()
        
    def file_name(self, file):
        return file.name

    def extract(self, file):
        entries = []
        filename = file.name
        with open(file.name) as csvfile:
            reader = csv.DictReader(csvfile)
            for index, row in enumerate(reader, 1):
                date = datetime.strptime(row['transaction_date'], '%Y-%m-%d %H:%M:%S').date()
                description = row['description']
                currency = row['currency']
                amount = D(row['amount'])
                units = Amount(amount, currency)
                account = self.account_mapping[row['account']]
                posting = Posting(account, units, None, None, None, None)

                main_account = row['main_account'] 
                meta = {
                    'filename': filename,
                    'lineno': index,
                    'card': self.last4_map.get(main_account.strip()),
                    'date': date
                    } 

                txn = Transaction(
                    date=date,
                    flag='*',
                    payee=None,
                    narration=description,
                    tags=EMPTY_SET,
                    links=EMPTY_SET,
                    postings=[posting],
                    meta=meta
                )
                entries.append(txn)
        return entries
