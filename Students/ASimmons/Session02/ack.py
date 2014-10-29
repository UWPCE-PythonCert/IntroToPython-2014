__author__ = 'Ari'


class ackerman:
    def ack(m,n):
        """Return a non-negative integer based on the Ackerman function

        Definition of Ackerman: http://en.wikipedia.org/wiki/Ackermann_function

        m, n: non-negative integers"""

        # validate that m is NOT a negative number
        if m < 0:
            return None

        # validate that n is NOT a negative number
        if n < 0:
            return None

        if m == 0:
            return n+1

        if m > 0 and n == 0:
            return ack(m-1,1)

        return ack(m-1, ack(m, n-1))

def main():

    input_m = int(sys.argv[1])
    input_n = int(sys.argv[2])

    ackerman.ack(input_m, input_n)

if __name__ == "__main__":
    main()