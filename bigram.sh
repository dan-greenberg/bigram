#!/bin/bash

# Help
usage() {
  echo "Usage:"
  echo " $0 -f <filename> # Pass in file"
  echo " $0 -t \"<text input>\" # Directly pass in text"
  exit 1
}

# Accepts either -f or -t
while getopts ":f:t:" opt; do
  case ${opt} in
    f )
      input_text=$(<"$OPTARG") || { echo "Error reading file $OPTARG"; exit 1; }
      ;;
    t )
      input_text="$OPTARG"
      ;;
    \? )
      echo "Invalid option: -$OPTARG"
      usage
      ;;
    : )
      echo "Missing argument for -$OPTARG"
      usage
      ;;
  esac
done

# Only valid options are -f and -t
if [[ -z "$input_text" || "$OPTIND" -ne 3 ]]; then
  usage
fi

# If no errors, pass input to script
python3 main.py "$input_text"