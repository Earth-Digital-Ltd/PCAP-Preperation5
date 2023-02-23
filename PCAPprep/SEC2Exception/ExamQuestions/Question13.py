# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -

"""
What is the output of the following code?

for x in range(1):
    try:
        print(x/x)
    finally:
        break
"""
for x in range(1):
    try:
        print(x/x)
    finally:
        break

# ZeroDivisionError: division by zero    #WRONG
# 0                                      #WRONG
# 1                                      #WRONG
# No output                              #CORRECT!!; if finally is presents, it specifies a "CLEANUP" Handler
                                         #; thus if an exception occurs in any of the clauses and is not
                                         # handled, the exception is temporarily saved and then the finally
                                         #clase is executed