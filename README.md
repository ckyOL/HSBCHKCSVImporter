# HSBCHKCSVImporter

A Beancount CSV importer for HSBC Hong Kong statements.

## Convert PDF Statements to CSV

Thanks to [sinopsysHK](https://github.com/sinopsysHK), you can easily convert your PDF statements to CSV:

1. Clone or download the scraper from [HsbcHkPdfScraper](https://github.com/sinopsysHK/HsbcHkPdfScraper).  
2. Follow the instructions in that repository to generate a CSV file from your PDF statement.

## CSV Importer

> Learn more in my [blog post](https://blog.ckyol.moe/2023/05/16/HSBCHKCSVImporter/)

1. Modify `config.py` and update it with your own account details and settings.  
2. Run the importer:

   ```bash
   bean-extract config.py /path/to/BANK-<YourAccountNumber>-<YYYYMM>.csv > output.beancount
   ```
This will generate a Beancount ledger file (output.beancount) containing all of your HSBC Hong Kong transactions.
