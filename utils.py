#!/usr/bin/env python3

class utils:
    def reversed(num):
        if isinstance(num, int):
            reversed = 0
            while(num != 0):
                currentDigit = num%10
                num = num // 10

                reversed = 10*reversed + currentDigit

            return reversed
        else:
            return None
        
    def formatter(num):
        if isinstance(num, int):
            return([bin(num), oct(num)])
        else:
            return None


