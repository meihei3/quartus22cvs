import argparse
import os
import re


COLUMNS = ("Fitter Status", "Quartus II 64-Bit Version", "Revision Name", "Top-level Entity Name",
           "Family", "Device", "Timing Models", "Total logic elements", "Total combinational functions",
           "Dedicated logic registers", "Total registers", "Total pins", "Total virtual pins",
           "Total memory bits", "Embedded Multiplier 9-bit elements", "Total PLLs", "More Information")
SUB_ABLE = (7, 8, 9, 10, 11, 12, 13, 14, 15)
OUTPUT_FILENAME_PATTERN = re.compile(r".+\.fit\.summary")
GABARAGE_SPARCE_PATTERN = re.compile(r"[\s\n]")


def __get_summary_file(tdir: str) -> str:
    out_tdir = tdir + ("/" if tdir[-1] != '/' else '') + "output_files"
    if not os.path.isdir(out_tdir):
        raise FileExistsError(f"The directry : {out_tdir} is not found.")
    for file in os.listdir(out_tdir):
        if OUTPUT_FILENAME_PATTERN.match(file):
            return out_tdir+'/'+file
    raise FileExistsError("The file : \".+\.fit\.summary\" is not found.")


def __generate_csv_file(target_dir: str, more: str, output: str, is_append: bool):
    summary_file = __get_summary_file(target_dir)
    data_parser = lambda text, sa: (lambda t: GABARAGE_SPARCE_PATTERN.sub("", t) if sa else t[1:-1])(":".join(text.split(':')[1:]))
    with open(summary_file, 'r') as f:
        data = [data_parser(line, i in SUB_ABLE) for i, line in enumerate(f.readlines())]
        data.append(more)
    if is_append:
        with open(output, 'a') as f:
            if not os.path.exists(output):
                f.write(",".join(COLUMNS) + '\n')
            f.write(",".join(data) + '\n')
    else:
        with open(output, 'w') as f:
            f.write(",".join(COLUMNS) + '\n')
            f.write(",".join(data) + '\n')


parser = argparse.ArgumentParser(description="summary file to csv")
parser.add_argument('-t', '--target_dir', help="workspace dir", default=".", type=str)
parser.add_argument('-m', '--more', help="more information", default="", type=str)
parser.add_argument('-o', '--output', help="csv file name", default="out.csv", type=str)
parser.add_argument('--append',  help="Add data if datd exists ", action='store_false')
args = parser.parse_args()


if __name__ == "__main__":
    print("t:", args.target_dir)
    print("m:", args.more)
    print("o:", args.output)
    print("a:", args.append)
    __generate_csv_file(target_dir=args.target_dir, more=args.more, output=args.output, is_append=args.append)
