import argparse
import grep
import cut
import skrypt1
import sys


def grepFnc():
    grepParser = argparse.ArgumentParser(description="Funkcja wyszukująca tekst.")

    grepParser.add_argument(
        "-i",
        action="store_true",
        help="Pozwala na wyszukiwanie pomijając wielkości liter.",
    )
    grepParser.add_argument(
        "-w",
        action="store_true",
        help="Pozwala na wyszukiwanie DOKŁADNIE według wzoru.",
    )
    grepParser.add_argument(
        "textToCompare",
        # action="store_const",
        help="Po czym powinien szukać",
    )

    args = grepParser.parse_args()

    result = ""

    if args.w:
        result += " -w działa"

    if args.i:
        result += " -i działa"

    if args.textToCompare:
        result += " " + args.textToCompare

    grep.grep(sys.argv[2::])

    return result


def cutFnc():
    cutParser = argparse.ArgumentParser(
        description="Funkcja wycinająca fragment tekstu."
    )

    cutParser.add_argument(
        "-f",
        action="store_true",
        help="Pozwala pokazać tylko wybrane kolumny tekstu.",
    )
    cutParser.add_argument(
        "columns",
        # action="store_const",
        help="Kolumny które mają być wyświetlone",
    )
    cutParser.add_argument(
        "-d",
        action="store_true",
        help="Pozwala zastosować separator tekstu wybrany przez użytkownika.",
    )
    cutParser.add_argument(
        "separator",
        # action="store_const",
        help="Separator, jaki ma być wykorzystany.",
    )

    args = cutParser.parse_args()

    result = ""

    if args.f:
        result += " -f działa"

    if args.columns:
        result += " " + args.columns

    if args.d:
        result += " -d działa"

    if args.separator:
        result += " " + args.separator

    cut.cut(sys.argv[2::])

    return result


# def operationsFnc():
#     args = operationsParser.parse_args()

#     result = ""

#     if args.string:
#         result += args.string

#     if args.operation:
#         result += args.operation

#     operations[args.operation](sys.argv[2::])

#     return result


# mainParser = argparse.ArgumentParser(description="Funkcja wyszukująca tekst.")

# mainParser.add_argument("operation", help="Jaka operacja ma zostać wykonana.")

# mainArgs = mainParser.parse_args()

# if mainArgs.operation:
#     if mainArgs.operation == "cut":
#         cutFnc()
#     if mainArgs.operation == "grep":
#         grepFnc()
#     if mainArgs.operation == "operation":
#         operationsFnc()
# else:
#     print("Błąd!")


def main(command_line=None):
    mainParser = argparse.ArgumentParser(
        description="Skrypt wywołujący jedną z 3 operacji."
    )

    subparsers = mainParser.add_subparsers(dest="function", required=True)

    # operations
    operationsParser = subparsers.add_parser(
        "operations", help="Funkcja wykonująca proste operacje na tekście."
    )

    operationsParser.add_argument(
        "string",
        # action="store_const",
        help="Teskt, na którym ma zostać wykonana operacja.",
    )

    # cut

    cutParser = subparsers.add_parser(
        "cut", description="Funkcja wycinająca fragment tekstu."
    )

    cutParser.add_argument(
        "-f",
        help="Pozwala pokazać tylko wybrane kolumny tekstu.",
    )

    cutParser.add_argument(
        "-d",
        help="Pozwala zastosować separator tekstu wybrany przez użytkownika.",
    )

    # grep

    grepParser = subparsers.add_parser("grep", description="Funkcja wyszukująca tekst.")

    grepParser.add_argument(
        "-i",
        action="store_true",
        help="Pozwala na wyszukiwanie pomijając wielkości liter.",
    )
    grepParser.add_argument(
        "-w",
        action="store_true",
        help="Pozwala na wyszukiwanie DOKŁADNIE według wzoru.",
    )
    grepParser.add_argument(
        "textToCompare",
        help="Po czym powinien szukać",
    )

    mainArgs = mainParser.parse_args()

    if mainArgs.function:
        if mainArgs.function == "cut":
            params = []
            if mainArgs.f:
                params.append("-f")
                params.append(mainArgs.f)
            if mainArgs.d:
                params.append("-d")
                params.append(mainArgs.d)
            print(cut.cut(params))

        if mainArgs.function == "grep":
            params = []
            params = []
            if mainArgs.i:
                params.append("-i")
            if mainArgs.w:
                params.append("-w")
            if mainArgs.textToCompare:
                params.append(mainArgs.textToCompare)
            print(grep.grep(params))

        if mainArgs.function == "operations":
            skrypt1.doOperations(mainArgs.string)
    else:
        print("Błąd!")


if __name__ == "__main__":
    main()
