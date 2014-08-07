#!/usr/bin/env python3


class ans ():

    def run():
        total = 0
        count = 0
        numbers = []
        while True:
            line = input("enter a number or Enter to finish: ")
            if line:
                try:
                    num = int(line)
                except ValueError as e:
                    print(e)
                    continue
                total += num
                count += 1
                numbers.append(num)
            else:
                break
        if count:
            print('count = ', count, 'sum = ', total, 'lowest = ',
                  sorted(numbers)[0],
                  'highest = ',
                  sorted(numbers)[-1],
                  'mean = ', total/count)

ans.run()