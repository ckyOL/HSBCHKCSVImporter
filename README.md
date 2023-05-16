# HSBCHKCSVImporter
A beancount csv importer for HSBC(HK)

## Convert PDF Statement to CSV

Thanks for primefission's work, you can convert pdf to csv simply by it.

Download it from [primefission/HsbcHkPdfScraper](https://github.com/primefission/HsbcHkPdfScraper)

## CSV importer

Modify the sample configuration file in config.py to your own configuration first.

Run `bean-extract config.py /path/to/BANK-(your bank number)-(year and month).csv > output.beancount`
