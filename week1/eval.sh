# set -euxo pipefail
export PATH=${PATH}:${HOME}/.codon/bin
ulimit -s 8192000

n50() {
    local arr=($1)

    sum=0

    for ((i=10; i<${#arr[@]}; i+=2)); do
        sum=$((sum + arr[i]))
    done
    
    sum=$((sum / 2))

    for ((i=10; i<${#arr[@]}; i+=2)); do
        if (( arr[i] >= sum )); then
            echo ${arr[i]}
            return
        fi
        sum=$((sum - arr[i]))
    done
    


}

{
    echo "Dataset Language Runtime N50"
    echo "------- -------- ------- ---"
    for ((i=1; i<=4; i++)); do
        output=$( /usr/bin/time -f "%e" -o /dev/stderr codon run -release ./week1/code/codon/main.py ./week1/data/data$i 2>&1 )
        runtime=$(echo "$output" | tail -n1)
        stdout=$(echo "$output" | head -n -1)
        line="data$i codon ${runtime}s $(n50 "$stdout")"
        echo "$line"

        output=$( /usr/bin/time -f "%e" -o /dev/stderr python3 ./week1/code/python/main.py ./week1/data/data$i 2>&1 )
        runtime=$(echo "$output" | tail -n1)
        stdout=$(echo "$output" | head -n -1)
        line="data$i python ${runtime}s $(n50 "$stdout")"
        echo "$line"
    done
} | column -t -s $' '