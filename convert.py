# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

mph = input("Input speed in mph: ")
mph = float(mph)

print('How would you like your speed to be outputted?')
print('1: kph')
print('2: ms')
print('3: fts')
choice = input('Input the number corresponding with your choice: ')

if choice == '1':
    print("Speed in kph is", mph_to_kph(mph))
elif choice == '2':
    print("Speed in m/s is", mph_to_ms(mph))
elif choice == '3':
    print("Speed in ft/s is", mph_to_fts(mph))
else:
    print('Error: Invalid menu option, please choose a valid option')
