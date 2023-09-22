import json
from datetime import datetime


file = open('romanToInt.json', 'r')
tests = json.load(file)

try:
    def romanToInt(s):
        return len(s)
    
    start = datetime.now()
    error = False

    for test in tests:
        result = romanToInt(test['input'][0])
        if result != test['output']:
            error = True
            print('Input:', str(test['input'])[1:-1])
            print('Expected:', test['output'])
            print('Got:', result)
            break

    if error:
        print('Error')
    else:
        end = datetime.now()
        time = end - start
        print(time.seconds * 1000 + time.microseconds / 1000, 'ms')

except Exception as e:
    print(type(e).__name__)
    print(e)
    print('Error')
