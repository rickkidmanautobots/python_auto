from Common import fib


def test_fib():
    nterms = 9

    uni = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dec = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    cen = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hun = "hundred"
    mil = "thousand"

# check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("")
        print("Fibonacci sequence:")
        for i in range(nterms):
            if fib(i) < 10:
                print(str(fib(i)) + " - " + uni[fib(i)])
            if 10 < fib(i) < 20:
                print(str(fib(i)) + " - " + dec[int(str(fib(i))[-1])])
            if 20 < fib(i) < 100:
                print(str(fib(i)) + " - " + cen[int(str(fib(i))[0])-2] + " " + uni[int(str(fib(i))[1])])
            if 100 < fib(i) < 1000:
                if str(fib(i))[0] == "6":
                    print(str(fib(i)) + " - " + uni[int(str(fib(i))[0])] + " " + hun + " " + dec[int(str(fib(i))[1])-1])
                else:
                    print(str(fib(i)) + " - " + uni[int(str(fib(i))[0])] + " " + hun + " " + cen[int(str(fib(i))[1])-2] + " " + uni[int(str(fib(i))[2])])
            if 1000 < fib(i) < 10000:
                print(str(fib(i)) + " - " + uni[int(str(fib(i))[0])] + " " + mil + " " + uni[int(str(fib(i))[1])] + " " + hun + " " + cen[int(str(fib(i))[2])-2] + " " + uni[int(str(fib(i))[3])])