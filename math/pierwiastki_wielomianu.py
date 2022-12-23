# Pierwiastki całkowite i wymierne wielomianu - Python
# Stworzone przez Adrian 'adyo'

def w(x):
    return 2*x**3 + 4*x**2 - 4*x - 13

def divisors(n, arr):
    for x in range(1, int(n) + 1):
        if n % x == 0:
            arr.append(x)
            arr.append(-x)

def search(arr1, arr2):
    for x in range(len(arr1)):
        m = arr1[x]
        res = w(m)

        if abs(res) <= 1e-6 : arr2.append(m)
        print('W({}) = {}'.format(m, res))

def main():
    
    nx, ny = [], []
    m = 1

    # Przechodzenie po liniach pliku i wyznaczanie liczb oraz stopni
    with open(__file__, 'r') as of: lines = of.readlines()
    function = ' '.join('^'.join(lines[4].split('**')).split()[1:]) + '\n'

    print('W(x) = {}'.format(function))
    if function[0] == 'x': m = 1
    else: m = float(function.split('*')[0])

    try: n = abs(float(''.join(function.split('\n')[0].split('x')[-1].split())))
    except: n = 0

    # Szukanie dzielników wyrazu wolnego
    divisors(n, nx)

    print('Dzielniki wyrazu wolnego:', nx)
    p, q = [], []

    # Szukanie dzielników liczby z największym stopniem
    divisors(m, ny)
    print('Dzielniki liczby z największym stopniem:', ny)

    # Obliczanie p/q
    pq = []
    for p in nx:
        for q in ny:
            if p/q not in pq: pq.append(p/q)

    pq = sorted(pq, reverse=True)
    print('p/q =', pq)

    # Poszukiwanie pierwiastków wymiernych
    print()

    z = []
    search(pq, z)

    print('\nZnalezione pierwiastki wymierne: {}\n'.format(sorted(z)))

if __name__ == '__main__':
    main()
