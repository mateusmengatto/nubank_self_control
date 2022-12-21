import nu_get_data as ngd
import search_data as sd
import pandas as pd

x = ngd.open_data('basedata/')



dat = sd.search_period(x, '2022-01-20', '2022-03-31')

y = sd.search_receive_pix(dat)
print(y)

#multiple filters 

#Test values_calculations


#Next steps
#What analysis?
#Screen showing, what framework to use? #kivy?
#api
