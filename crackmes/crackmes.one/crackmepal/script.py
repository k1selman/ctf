import string
from random import choice, randint
from subprocess import PIPE, run

def keygen():
    chars = string.ascii_letters + string.digits
    key = [choice(chars) for i in range (7)]
    key.insert(randint(0, len(key)), '@')
    key.insert(4, '-')
    return ''.join(key)

def test(program, counter):
    for i in range(counter):
            key = keygen()
            print(f"Test {i+1}: {key}")
            j = run([program, key], stdout=PIPE, stderr=PIPE, universal_newlines=True)
            assert(j.returncode == 0)
    print(f"Completed {counter} runs")
    return True

test('./crackmeMario', 20)

