import argparse
from compiler.compiler import compile

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Path to F-Stroke file")
    parser.add_argument("output_file", type=str, help="Path to output bytecode file")

    args = parser.parse_args()
    if not args.input_file:
        print("Error: Specify the input file")
        exit(1)
    if not args.output_file:
        print("Error: Specify the output file")
        exit(1)
    try:
        compile(args.input_file, args.output_file)
    except Exception as e:
        print(f"Error: There is some problem with files")
        print(e)
        exit(3)
else:
    raise ImportError("Please import compiler.py")
