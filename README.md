# HSBCHKCSVImporter

A Beancount CSV importer for HSBC Hong Kong statements.

## Convert PDF Statements to CSV

Thanks to [sinopsysHK](https://github.com/sinopsysHK), converting your PDF statements to CSV is simple:

1. Clone or download the scraper repository.  
2. Follow the steps in that repo to generate a CSV file from your PDF statement.

### Origin

This utilizes [sinopsysHK's HsbcHkPdfScraper](https://github.com/sinopsysHK/HsbcHkPdfScraper).

### Alternative Option

If you're investing or using fixed‑term deposits, you might prefer my modified version:

[My HsbcHkPdfScraper](https://github.com/ckyOL/HsbcHkPdfScraper)

---

## CSV Importer

> Details can be found in my [blog post](https://blog.ckyol.moe/2023/05/16/HSBCHKCSVImporter/).

1. Edit `config.py` with your account details and preferences.  
2. Run the importer:

   ```bash
   bean-extract config.py /path/to/BANK-<YourAccountNumber>-<YYYYMM>.csv > output.beancount
   ```
This command produces a Beancount ledger file (output.beancount) populated with your HSBC Hong Kong transactions.
