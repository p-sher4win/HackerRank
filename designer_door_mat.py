# N = rows, 5 < N < 101
# M = columns, 15 < M 303

N, M = map(int, input().split())

for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(N-2, -1, -2):
    print(('.|.' * i).center(M, '-'))
