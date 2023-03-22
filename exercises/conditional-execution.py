## Chapter 4

## Conditional Execution
#$ Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hour_wrk = float(input("Enter hours worked: "))
hour_vl = float(input("Enter rate: "))

if float(hour_wrk) > 40 :
    extra_pay = float(hour_wrk) * 0.5
    pay = float(hour_wrk) * float(hour_vl) + extra_pay
    print("You will get: ", pay)

elif hour_wrk > 0  or hour_wrk <= 40 :
    pay = float(hour_wrk) * int(hour_vl)
    print("You will get: ", pay)

else :
    print("You didn´t work, soo.. No money for u")
