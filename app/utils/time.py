from datetime import datetime
from pytz import timezone, utc


KST = timezone('Asia/Seoul')


def kst_now() -> datetime:
    now = datetime.utcnow()
    return utc.localize(now).astimezone(KST)
