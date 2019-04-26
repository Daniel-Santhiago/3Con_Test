# SOLUTION 3CON - DANIEL SANTHIAGO DE SOUZA

# Number is converted to a list of digits
def num2digits(num):
    if not type(num) is str:
        num = str(num)
    digits = []
    for digit in num:
        digits.append(digit)
    return digits

# List of digits is Classified as an Increasing, Decreasing, Bouncy or Constant Number
def classify_number(digits):
    meter = []
    for (key, digit) in enumerate(digits):
        if(key>=1):
            if (digits[key -1] < digits[key]):
                meter.append('I')
            elif (digits[key -1] > digits[key]):
                meter.append('D')
            else:
                meter.append('E')

    increase_count = meter.count('I')
    decrease_count = meter.count('D')
    if (increase_count >0) and (decrease_count == 0):
        classification = 'Increasing Number'
    elif (increase_count == 0) and (decrease_count > 0):
        classification = 'Decreasing Number'
    elif (increase_count >0) and (decrease_count > 0):
        classification = 'Bouncy Number'
    else:
        classification = 'Constant Number'
    return classification


# A dictionary is created to populate all the numbers starting from 1 to num_max ( The max number choosen by the user)
# The keys in the dictionary are: number, classification ( from classify_number) and bounce proportion
def create_bounce_dict(num_max):

    list_numbers = []
    bouncing = 0
    for num in range(1, (num_max +1)):
        numbers_dict={}
        number = num2digits(num)
        num_class = classify_number(number)
        numbers_dict['number'] = num
        numbers_dict['classification'] = num_class
        if num_class == 'Bouncy Number':
            bouncing = bouncing + 1
        numbers_dict['bounce_proportion'] = (bouncing / (num)) * 100
        list_numbers.append(numbers_dict)
    return list_numbers

# This function runs a loop until the desired percentage is achieved
def find_percent(list, percent):
    for key, item in enumerate(list):
        if item['bounce_proportion'] >= percent:
            print('Número: ' + str(item['number']))
            print('Percentual: ' + str(item['bounce_proportion']))
            break

# Parameters
numero_maximo_range = 1600000
percent = 99

# Function Calls
list_numbers = create_bounce_dict(numero_maximo_range)
find_percent(list_numbers, percent)

# Test
print( 'Percentual do número máximo do range '  +str(numero_maximo_range)+': '+ str(list_numbers[numero_maximo_range-1]['bounce_proportion']))


