#!/usr/bin/env python3
import sys


class BigDigits():

    def run(self):
        # self.Digits = self.int_list()
        self.Digits = self.num_list()
        try:
            digits = sys.argv[1]
            row = 0
            while row < 7:
                line = ""
                column = 0
                while column < len(digits):
                    number = int(digits[column])
                    digit = self.Digits[number]
                    line += digit[row] + "  "
                    column += 1
                print(line)
                row += 1
        except IndexError:
            print("usage: digdigits.py <number>")
        except ValueError as err:
            print(err, "in", digits)

    def int_list(self):
        zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]

        one = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]

        two = ["  ***  ", " *   * ", "*     *", "     * ", "    *  ", "  *    ", "*******"]

        three = ["*******", "      *", "      *", "*******", "      *", "      *", "*******"]

        four = ["    *  ", "   *   ", "  *  * ", " *   * ", "*******", "     * ", "     * "]

        five = ["*******", "*      ", "*      ", "*******", "      *", "      *", "*******"]

        six = ["*******", "*      ", "*      ", "*******", "*     *", "*     *", "*******"]

        seven = ["*******", "      *", "      *", "      *", "      *", "      *", "      *"]

        eight = ["*******", "*     *", "*     *", "*******", "*     *", "*     *", "*******"]

        nine = ["*******", "*     *", "*     *", "*******", "      *", "      *", "*******"]

        return [zero, one, two, three, four, five,six,seven,eight,nine]

    def num_list(self):
        new_list = []
        n = []
        for num in range(10):
            _list = BigDigits.int_list(self)[num]
            for i in _list:
                new_list.append(i.replace('*', str(num)))

        for i in range(0, len(new_list) + 1, 7):
            n.append(new_list[i:i+7])

        return n

BigDigits().run()
