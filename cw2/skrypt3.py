import argparse
import grep
import cut
import operations
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


def operationsFnc():
    operationsParser = argparse.ArgumentParser(
        description="Funkcja wykonująca proste operacje na tekście."
    )

    operationsParser.add_argument(
        "operation",
        # action="store_const",
        help="Operacja, jaka ma zostać wykonana.",
    )

    operationsParser.add_argument(
        "string",
        # action="store_const",
        help="Teskt, na którym ma zostać wykonana operacja.",
    )

    args = operationsParser.parse_args()

    result = ""

    if args.string:
        result += args.string

    if args.operation:
        result += args.operation

    operations[args.operation](sys.argv[2::])

    return result


mainParser = argparse.ArgumentParser(description="Funkcja wyszukująca tekst.")

mainParser.add_argument("operation", help="Jaka operacja ma zostać wykonana.")

mainArgs = mainParser.parse_args()

if mainArgs.operation:
    if mainArgs.operation == "cut":
        cutFnc()
    if mainArgs.operation == "grep":
        grepFnc()
    if mainArgs.operation == "operation":
        operationsFnc()
else:
    print("Błąd!")
