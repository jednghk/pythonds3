def simplify(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, top, bot):
        '''if type(top) == float or type(bot) == float:
            print(type(top))
            print(type(bot))
            raise TypeError('Float keyed in, please key in an integer value')'''
        self.num = top / simplify(top, bot)
        self.den = bot / simplify(top, bot)

    def __add__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)

        result_num = self.num * other.den + self.den * other.num
        result_den = self.den * other.den
        return Fraction(result_num, result_den)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        result_num = self.num * other.den - self.den * other.num
        result_den = self.den * other.den
        return Fraction(result_num, result_den)

    def __mul__(self, other):
        result_num = self.num * other.num
        result_den = self.den * other.den
        return Fraction(result_num, result_den)

    def __truediv__(self, other):
        other.num, other.den = other.den, other.num
        return self * other

    def __gt__(self, other):
        if self.num/self.den > other.num/other.den:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.num/self.den >= other.num/other.den:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.num/self.den < other.num/other.den:
            return True
        else:
            return False

    def __le__(self, other):
        if self.num/self.den <= other.num/other.den:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.num/self.den != other.num/other.den:
            return True
        else:
            return False

    def __repr__(self):
        gcd = simplify(self.num, self.den)
        self.num /= gcd
        self.num /= gcd

        return f'Fraction({int(self.num)}, {int(self.den)})'

    def __str__(self):
        #ensure fraction is in simplest form
        gcd = simplify(self.num, self.den)
        self.num /= gcd
        self.num /= gcd

        #if fraction simplifies to whole num, return whole num
        if self.num%self.den == 0:
            return f'{int(self.num/self.den)}'
        else:
            return f'{int(self.num)}/{int(self.den)}'

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


test = Fraction(5, 4)
test += 3
print(repr(test))