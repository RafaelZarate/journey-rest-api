
import arrow
from datetime import timedelta

def local_now():
    return arrow.utcnow().to('America/Mexico_City').datetime

def utc_now():
    return arrow.utcnow().datetime


