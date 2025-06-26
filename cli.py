import argparse
from main import run

def main():
    parser = argparse.ArgumentParser(prog="wattpad-scraper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    epubit_parser = subparsers.add_parser("epubit", help="Export a Wattpad book to EPUB.")
    epubit_parser.add_argument("book_id", type=int, help="The Wattpad book ID.")

    args = parser.parse_args()

    if args.command == "epubit":
        run(args.book_id)

if __name__ == "__main__":
    main()
