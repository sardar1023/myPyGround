###Simple Calendar showing python script###
import calendar

print("-----Calendar program in python -----")
print("Enter 'x' for exit.")
y = input("Enter Year: ")

if y == 'x':
    exit()
else:
    m = input("Enter month:")
    yy = int(y)
    mm = int(m)
    print("\n",calendar.month(yy,mm))
