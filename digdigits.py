#!/usr/bin/env python3
import sys

"""
love@LOVE:~/python3$ ./digdigits.py 12345
 *     ***    *******      *    *******
 **    *   *         *     *     *
 *   *     *        *    *  *   *
 *        *   *******   *   *   *******
 *       *          *  *******        *
 *     *            *       *         *
***  *******  *******       *   *******
"""
class BigDigits():

    def run(self):
        Digits = self.int_list()
        try:
            digits = sys.argv[1]
            row = 0
            while row < 7:
                line = ""
                column = 0
                while column < len(digits):
                    number = int(digits[column])
                    digit = Digits[number]
                    line += digit[row] + "  "
                    column += 1
                print(line)
                #return line
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



BigDigits().run()
