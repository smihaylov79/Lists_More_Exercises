initial_list = input().split()

command = ''

while command != 'end':
    command = input()
    command_list = command.split()
    if 'exchange' in command:
        index = int(command_list[len(command_list) - 1])
        if index >= len(initial_list) or index < 0:
            print('Invalid index')
            continue
        initial_list = initial_list[index + 1:] + initial_list[:index + 1]
    if 'even' in command:
        even_list = []
        for item in initial_list:
            if int(item) % 2 == 0:
                even_list.append(int(item))
        if 'max' in command:
            if len(even_list) > 0:
                max_even = max(list(even_list))
                if initial_list.count(str(max_even)) == 1:
                    result_max = initial_list.index(str(max_even))
                else:
                    result_max = len(initial_list) - 1 - initial_list[::-1].index(str(max_even))
                print(result_max)
            else:
                print('No matches')
        if 'min' in command:
            if len(even_list) > 0:
                min_even = min(list(even_list))
                if initial_list.count(str(min_even)) == 1:
                    result_min = initial_list.index(str(min_even))
                else:
                    result_min = len(initial_list) - 1 - initial_list[::-1].index(str(min_even))
                print(result_min)
            else:
                print('No matches')
        if 'first' in command:
            first_n_even = even_list[:int(command_list[1])]
            if len(initial_list) < int(command_list[1]):
                print('Invalid count')
            else:
                print(first_n_even)
        if 'last' in command:
            last_n_even = even_list[-int(command_list[1]):]
            if len(initial_list) < int(command_list[1]):
                print('Invalid count')
            else:
                print(last_n_even)
    # for odd
    if 'odd' in command:
        odd_list = []
        for item in initial_list:
            if int(item) % 2 != 0:
                odd_list.append(int(item))
        if 'max' in command:
            if len(odd_list) > 0:
                max_odd = max(list(odd_list))
                if initial_list.count(str(max_odd)) == 1:
                    result_max_odd = initial_list.index(str(max_odd))
                else:
                    result_max_odd = len(initial_list) - 1 - initial_list[::-1].index(str(max_odd))
                print(result_max_odd)
            else:
                print('No matches')
        if 'min' in command:
            if len(odd_list) > 0:
                min_odd = min(list(odd_list))
                if initial_list.count(str(min_odd)) == 1:
                    result_min_odd = initial_list.index(str(min_odd))
                else:
                    result_min_odd = len(initial_list) - 1 - initial_list[::-1].index(str(min_odd))
                print(result_min_odd)
            else:
                print('No matches')
        if 'first' in command:
            first_n_odd = odd_list[:int(command_list[1])]
            if len(initial_list) < int(command_list[1]):
                print('Invalid count')
            else:
                print(first_n_odd)
        if 'last' in command:
            last_n_odd = odd_list[-int(command_list[1]):]
            if len(initial_list) < int(command_list[1]):
                print('Invalid count')
            else:
                print(last_n_odd)
print(f'[{", ".join(initial_list)}]')
