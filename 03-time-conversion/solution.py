def timeConversion(s):
    period = s[-2:]
    hours = int(s[:2])
    rest = s[2:-2]
    if period == "AM":
        hours = 0 if hours == 12 else hours
    else:
        hours = hours if hours == 12 else hours + 12
    return f"{hours:02d}{rest}"
