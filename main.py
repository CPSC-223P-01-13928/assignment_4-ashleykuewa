def read_data(filename):
    return xyz

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
    display = "==== daily ====\n
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name[int(date[4:6])] + str(int(date[6:8])), ", " + str(int(date[0:4]))

