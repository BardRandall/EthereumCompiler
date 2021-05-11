import argparse
import sys
from emulator import emulator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Path to bytecode file")
    parser.add_argument(
        "-input_data",
        type=str,
        help="Path to input data file",
        default="sys.stdin",
        required=False,
    )
    parser.add_argument(
        "-debug",
        action="store_true",
        help="Turns on debug mode",
        default=False,
        required=False,
    )

    args = parser.parse_args()
    if not args.input_file:
        print("Error: Specify the input file")
        exit(1)
    try:
        f = open(args.input_file, mode="r")
        bytecode = f.read().rstrip()
        if args.input_data == "sys.stdin":
            print("Turned on mode for specifying input data")
            emulator.emulate(bytecode, sys.stdin.read(), args.debug)
        else:
            try:
                input_f = open(args.input_data, mode="r")
                emulator.emulate(bytecode, input_f.read(), args.debug)
            except Exception as e:
                print(
                    f"Error: There is some problem with input data file {args.input_file}"
                )
                print(e)
                exit(2)
        f.close()
    except Exception as e:
        print(f"Error: There is some problem with bytecode file {args.input_file}")
        print(e)
        exit(3)
else:
    raise ImportError("Please import emulator.py")
