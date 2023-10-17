import argparse
import grep
import cut
import skrypt1


def main():
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
