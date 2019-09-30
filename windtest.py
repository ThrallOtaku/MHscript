from WindPy import *

begin_date='20150201'
end_date=datetime.today()
data=w.wsd("399106.SZ", "pe_ttm", begin_date, end_date, "")
print(data)