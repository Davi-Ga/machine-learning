#!/bin/sh

chmod +x $0

# Get the directory of the current script
dir=$(dirname "$0")

# Function to display usage
usage() {
    echo "Usage: $0 [--extractor|-e] [--cutter|-c] [--labeling|-l]"
    exit 1
}

# Parse command line arguments
while getopts ":ecl" opt; do
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
            if [ -f "$dir/src/features/cutter.py" ]; then
                python3 "$dir/src/features/cutter.py"
            else
                echo "Error: $dir/src/features/cutter.py does not exist"
                exit 1
            fi
            ;;
        l)
            echo "Labelling documents"
            if [ -f "$dir/src/features/labelling.py" ]; then
                python3 "$dir/src/features/labelling.py"
            else
                echo "Error: $dir/src/features/labelling.py does not exist"
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