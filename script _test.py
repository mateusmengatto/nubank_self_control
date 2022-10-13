from dataclasses import dataclass
import nu_get_data as ngd
import search_data as sd
import pandas as pd

x = ngd.open_data('basedata/')

y = sd.search_receive_pix(x)

dat = sd.search_period(x, '2022-01-20', '2022-02-03')

dat = sd.search_date(x, '2022-03-21')

print(dat)


#Next steps
#What analysis?
#Screen showing, what framework to use? #kivy?
#api
