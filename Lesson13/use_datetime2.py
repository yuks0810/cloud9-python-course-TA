from datetime import datetime, timedelta, timezone

jst = timezone(timedelta(hours=+9), 'JST')

dtm_str = "2019-04-01 21:59:06"
dtm = datetime.strptime(dtm_str, "%Y-%m-%d %H:%M:%S")

print(dtm + timedelta(weeks=5))