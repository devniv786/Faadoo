from nsepy.history import get_price_list
from datetime import date
import pandas as pd
##stock_opt = get_history(symbol="SBIN",
##                        start=date(2015,1,1),
##                        end=date(2015,1,10),
##                        option_type="CE",
##                        strike_price=300,
##                        expiry_date=date(2015,1,29))
##print(type(stock_opt))
##stock_opt.to_csv("options.csv")

prices = get_price_list(dt = date(2018,11,2))
prices.to_csv("Bhav.csv")
