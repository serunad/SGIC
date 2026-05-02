def convert_hour(hourmin:list) -> str:
        hour:str = hourmin[0]
        hour = hour.rjust(2, "0")
        min:str = hourmin[1]
        min = min.rjust(2, "0")
        return f"{hour}:{min}"

def validate_maxmin_time(hourmin:list) -> bool:
    try:
        valMaxHour = True if 24 >= int(hourmin[0]) >= 0 else False
        valMaxMin = True if 59 >= int(hourmin[1]) >= 0 else False
        return valMaxHour and valMaxMin
    
    except Exception as e:
         print("Error validate maxmin time:" + e)
         return False
