import pandas
import pprint

pprint.pprint(pandas.date_range('2021', end='2022', freq='W-MON').strftime('%Y-%m-%d').tolist(), indent=4)