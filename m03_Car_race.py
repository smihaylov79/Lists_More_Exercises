data = input().split()

middle = (len(data) - 1) // 2
time_left = 0
time_right = 0
left = data[:middle]
right = data[middle + 1:]
right.reverse()

for item_l in left:
    time_left += int(item_l)
    if int(item_l) == 0:
        time_left = time_left * 0.8
for item_r in right:
    time_right += int(item_r)
    if int(item_r) == 0:
        time_right = time_right * 0.8
winner_time = f'{min(time_left, time_right):.1f}'
if time_left < time_right:
    print(f'The winner is left with total time: {winner_time}')
else:
    print(f'The winner is right with total time: {winner_time}')
