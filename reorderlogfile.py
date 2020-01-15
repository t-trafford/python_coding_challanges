
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]


def reorderLogFiles(logs):

    letter_logs = []
    digit_logs = []

    for log in logs:
        if log.split()[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(key=lambda log: log.split()[0])  # when suffix is tie, sort by identifier
    letter_logs.sort(key=lambda log: log.split()[1:])  # sorted by suffix
    digit_logs.sort(key=lambda log: log.split()[0])

    return letter_logs + digit_logs

x = reorderLogFiles(logs)
print(x)