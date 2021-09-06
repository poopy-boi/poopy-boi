clouds = str(input('Is it cloudy today? Only answer with yes/no'))
temp = str(input('Does it feel cold? Only answer with yes/no'))

if clouds == 'yes' and temp == 'yes':
    print('Highly likely it will rain today')
if clouds == 'yes' and temp == 'no':
    print('It wont rain today')
if clouds == 'no' and temp == 'yes':
    print('It wont rain today')
if clouds == 'no' and temp == 'no':
    print('it wont rain today')
