# Quartus2 to CSV

## Description
Quartus2のsummaryのデータをCVSで保存する．

## Requirements
- Python 3.5 or more

## Usage
1. プログラムのダウンロード
    ```
    $ git clone https://github.com/yameholo/quartus22cvs.git
    $ cd quartus22cvs
    ```
2. Quartus2の作業ディレクトリを指定して実行
    ```
    python quartus22cvs.py -t [YOUR_WORKING_SPACE]
    ```
3. `out.csv`が現在のカレントディレクトリに作られます

## Options
    -h, --help                          Print this help text and exit
    -t, --target_dir [WORKING_SPACE]    指定したいQuartus2の作業ディレクトリ．ただし，
                                        コンパイル済でsummaryのファイルが生成されている必要がある．
    -m, --more [INFORMATION_TEXT]       メモ的な用途で，CSV内のカラム"More Information"に
                                        書き込むテキストを指定する．
    -o, --output [OUTPUT_FILE]          出力するファイル名．
