def check_if_lucky():
    ticket = [int(i) for i in input("Введіть шестизначний номер вашого квитка:\n")]
    if len(ticket) == 6:
        first_sum = sum(ticket[0:3])
        second_sum = sum(ticket[3:7])
        if first_sum == second_sum:
            print("Щасливий")
        else:
            print("Звичайний")
    else:
        print("Введіть правильний номер вашого квитка")


if __name__ == '__main__':
    check_if_lucky()
