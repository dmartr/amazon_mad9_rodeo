import math

def format_HM(s: int) -> str:
    """Formats a given time in 
    hours into hours and seconds. 
    """
    frac, whole = math.modf(s)
    h = int(whole)
    if h > 0:
        s = f"{h}h {int(frac*60)} min"
    else: 
        s = f"{int(frac*60)} min"
    return s