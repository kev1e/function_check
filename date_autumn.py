def date_autumn(dates):
    today = "10-22-2020"
    today_ = today.split("-")
    autumn_days = []
    answer = []
    min_month = 1000000
    min_year = 1000000
    min_day = 1000000
    for i in range(len(dates)):
        data = dates[i].split("-")
        if data[0] == "09" or data[0] == "10" or data == "11":
            autumn_days.append(data)
    for i in range(len(autumn_days)):
        x = autumn_days[i].split('-')
        if (abs(int(x[i][0]) - int(today_[0])) <= min_month) and (abs(int(x[i][2]) - int(today_[2])) <= min_year) and (
                abs(int(x[i][1]) - int(today_[1])) <= min_day):
            min_month = abs(int(x[i][0]) - int(today_[0]))
            min_day = abs(int(x[i][1]) - int(today_[1]))
            min_year = abs(int(x[i][2]) - int(today_[2]))
            answer.append(i)
    return answer
