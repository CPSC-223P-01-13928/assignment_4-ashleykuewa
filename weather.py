import calendar

def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)

def write_data(filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def max_temperature(data, date):
    x = 0
    for key in data:
        if data == key[0:8]:
            if data[key]['t'] > x:
                x = data[key]['t']
    return x

def report_daily(data, date):
    display = "==== daily ====\n"
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name[int(date[4:6])] + str(int(date[6:8])), ", " + str(int(date[0:4]))
        = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
        = data[key]['t']
        = data[key]['h']
        = data[key]['r']
    display = display + f'{m<22}'  + f'{tm<10}' + f'{h>10}' + f'{r>10}'
    display

def report_historical(data):
    display = "================ HISTORICAL REPORT ====================\n"
    display += "                             Minimum     Maximum    Minimum    Maximum    Total\n"
    display += "Date                   Temperature   Temperature  Humidity    Humidity    Rainfall\n"
    display += "===========  =========  =========  =======  =======  =======\n"

    h = ' '

    for key in data:
        if h == key[0:8]:
            continue
        else:
            h == key[0:8]
            m = calendar.month[int(h[4:6])] + " " +str(int(h[6:8])) + " ,  " + str(int(h[0:4]))
    min_temp = min_temperature(data, h)
    max_temp = max_temperature(data, h)
    max_hum = max_humidity(data, h)
    min_hum = min_humidity(data, h)
    rain = total_rain(data, h)

    display += f'{m:20}{min_temp:13}{max_temp:13}{min_hum:10}{max_hum:10}{rain:10:2f}' + "\n"
    return display
