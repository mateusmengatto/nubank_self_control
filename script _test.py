import nu_get_data as ngd
import search_data as sd

x = ngd.open_data('basedata/')

y = sd.search_receive_pix(x)

print(y.head())

#Next steps
#What analysis?
#Screen showing, what framework to use? #kivy?
#api
