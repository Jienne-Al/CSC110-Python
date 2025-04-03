'''Write a function that takes two parameters – a pay rate and the number of hours worked – and returns the pay.
Any hours over 40 are paid at time and a half.'''
def wages(pay_rate, hours):
    if hours>40:
        overtime_hours=hours-40
        reg_pay=40*pay_rate
        overtime_pay=overtime_hours * (pay_rate*1.5)
        return reg_pay + overtime_pay
    else:
        return hours * pay_rate

print(wages(20.67,52))
