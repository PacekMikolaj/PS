import cut
import grep
import sys

params = sys.argv
operation = params[1]

if operation == "cut":
    print(cut.cut(params[2::]))
elif operation == "grep":
    print(grep.grep(params[2::]))
else:
    print("Error! not command found.")
