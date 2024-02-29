#!/bin/sh

chmod +x $0

# Get the directory of the current script
dir=$(dirname "$0")

# Function to display usage
usage() {
    echo "Usage: $0 [--extractor|-e] [--cutter|-c]"
    exit 1
}

# Parse command line arguments
while getopts ":ec" opt; do
    case ${opt} in
        e)
            echo "Extracting documents"
            if [ -f "$dir/src/main.py" ]; then
                python3 "$dir/src/main.py"
            else
                echo "Error: $dir/src/main.py does not exist"
                exit 1
            fi
            ;;
        c)
            echo "Cutting documents"
            if [ -f "$dir/src/utils/cutter.py" ]; then
                python3 "$dir/src/utils/cutter.py"
            else
                echo "Error: $dir/src/utils/cutter.py does not exist"
                exit 1
            fi
            ;;
        \?)
            echo "Invalid option: $OPTARG" 1>&2
            usage
            ;;
    esac
done
shift $((OPTIND -1))
exit

# Check if no arguments were passed and display usage
if [ $# -eq 0 ]; then
    usage
fi