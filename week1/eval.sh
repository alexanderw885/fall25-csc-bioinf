set -euxo pipefail
export PATH=${PATH}:${HOME}/.codon/bin

test=$(codon run ./week1/code/codon/main.py ./week1/data/data1)
echo $test