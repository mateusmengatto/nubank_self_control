import nu_get_data as ngd
import search_data as sd
import pandas as pd
import math_tools as mt


x = ngd.open_data('basedata/')

dat = sd.search_period(x, '2022-02-01', '2022-02-28')

output = mt.do_math(dat, 'outcome')

print(output)
