import nu_get_data as ngd
import search_data as sd
import pandas as pd
import math_tools as mt



x = ngd.open_data('basedata/')



dat = sd.search_period(x, '2022-02-01', '2022-02-28')



y = dat


g = mt.do_math(y, 'input')

print(g)
# x = 0 

# for i in y:
#     x+= i
    


#multiple filters 

#Test values_calculations


#Next steps
#What analysis?
#Screen showing, what framework to use? #kivy?
#api
