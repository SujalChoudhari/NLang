import basic
import sys

args = sys.argv

def execute(text):
    result, error = basic.run('<stdin>', text)
    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))


if len(args) == 2:
    with open(args[1], 'r') as f:
        data = f.read()
        if data.strip() == "": exit(0)
    execute(data)
else:
    while True:
        text = input('basic > ')
        if text.strip() == "": continue
        execute(text)

    