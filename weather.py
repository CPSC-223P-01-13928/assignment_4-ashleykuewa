import calendar
import json

def read_data(filename):
    try:
        with open(filename,'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def write_data(data,filename):
    with open(filename,'w') as f:
        json.dump(data,f)

def max_temperature(data,date):
    x=0
    for key in data:
        if date == key[0:8]:
            if date[key]['t'] > x:
                x = data[key]['t']
    return x

def min_temperature(data,date):
    x= 9999
    for key in data:
        if date == key[0:8]:
            if date[key]['t'] < x:
                x = data[key]['t']
    return x

def max_humidity(data,date):
    x=0
    for key in data:
        if date == key[0:8]:
            if date[key]['h'] > x:
                x = data[key]['h']
    return x

def min_humidity(data,date):
    x= 9999
    for key in data:
        if date == key[0:8]:
            if date[key]['h'] < x:
                x = data[key]['h']
    return x

def tot_rain(data,date):
    x = 0
    for key in data:
        if date == key[0:8]:
            x += date[key]['r']
    print(type(date))

def report_daily(data,date):
    display =  "========================= DAILY REPORT ========================\n"
    display += "Date                      Time  Temperature  Humidity  Rainfall\n"
    display += "====================  ========  ===========  ========  ========"
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name( int( date[4:6] ) ) + str( int(date[6:8]) ), "," ,  + str( int(date[0:4]) )
            tm = key[8:10] +":" + key[10:12]+ ":" +key[12:14]
            t = data[key][t]
            h = data[key][h]
            r = data[key][r]
            display += f'{m:22}{tm:8}{t:13}{h:10}{r:10.2f}' + "\n"
            # if format wrong, try  f'{m<22}'+ f'{tm<10}'+ 'f{t>11}'+ f'{h>10}'+ f'{r>10}'
    return display

def report_historical(data):
    display =  "============================== HISTORICAL REPORT ===========================\n"
    display += "			              Minimum      Maximum   Minumum   Maximum     Total\n"
    display += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display += "====================  ===========  ===========  ========  ========  ========\n"
    date = ' '
    for key in data:
        if date == key[0:8]:
            continue
        else:
            date = key[0:8]
            m = calendar.month_name( int(date[4:6]) ) + str(int(key[6:8])), "+", +str(int(key[0:4]))
            #tm = key[8:10] +":" + key[10:12]+ ":" + key[12:14]    
            maxT = max_temperature(data, date)
            minT = min_temperature(data,date)
            maxH = max_humidity(data,date)
            minH = min_humidity(data,date)
            rain = tot_rain(data,date)
            display += f'{m:22}{minT:13}{maxT:13}{minH:10}{maxH:10}{rain:10.2f}' + "\n"
    return display