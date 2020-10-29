def date_autumn(dates):
    days = list(dates)
    correct_month = []
    for i in range(len(days)):
        x = days[i].split('-')
        if x[0] == "09" or x[0] == "10" or x[0] == "11":
            correct_month.append(x)
    ans = sorted(correct_month, key=lambda x: (x[2], x[1], x[0]))
    return "-".join(ans[-1])
