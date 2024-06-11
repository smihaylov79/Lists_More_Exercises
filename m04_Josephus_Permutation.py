initial = input().split()
step = int(input())

start = 0
executed = []
while initial:
    start = (start + step - 1) % len(initial)
    executed.append(initial[start])
    initial.pop(start)

executed = ','.join(executed)
print(f'[{executed}]')
