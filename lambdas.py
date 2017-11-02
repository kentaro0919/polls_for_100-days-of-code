import datetime
import calendar


year = int(input("年"))
month = int(input("月"))

first_day = lambda year, month: datetime.date(year, month, 1).strftime('%Y-%m-%d')
last_day = lambda year, month, num_days: datetime.date(year, month, num_days).strftime('%Y-%m-%d')
setnum_days = lambda year, month: calendar.monthrange(year, month)
setLasetDay = lambda year, month: last_day( year, month, setnum_days(year, month)[1])
setParametersNoS = lambda d=maya.when("1 month ago"): {"billingDayOnly": "true","month": d.month, "year": d.year,}
