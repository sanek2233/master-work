languages = {
    "Python": {
        "docker-image": "python:3.8-alpine",
        "cmd": "python3 test.py",
        "extension": ".py",
        "prefix": """
import json
from datetime import datetime


file = open('test.json', 'r')
tests = json.load(file)

try:
""",
        "suffix": lambda func: f"""
    start = datetime.now()
    error = False

    for test in tests:
        result = {func}
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
""",
    },
}