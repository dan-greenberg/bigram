#!/bin/bash

# Help
usage() {
  echo "Usage:"
  echo " $0 -f <filename> # Pass in file"
  echo " $0 -t \"<text input>\" # Directly pass in text"
  exit 1
}

# Args required
if [[ $# -eq 0 ]]; then
  usage
fi

mode=""
input_text=""

# Accepts either -f or -t
while [[ $# -gt 0 ]]; do
  case "$1" in
    -f)
      mode="file"
      shift
      [[ -z "$1" ]] && { echo "Filename required with -f flag"; usage; }
      [[ ! -f "$1" ]] && { echo "Error reading file $1"; exit 1; }
      input_text=$(<"$1")
      shift
      ;;
    -t)
      mode="text"
      shift
      [[ $# -eq 0 ]] && { echo "Missing text after -t flag"; usage; }
      input_text="$*"
      break
      ;;
    -*)
      echo "Invalid option: $1"
      usage
      ;;
    *)
      echo "Unexpected argument: $1"
      usage
      ;;
  esac
done

# mode should have been set
[[ -z "$mode" ]] && usage

# If no errors, pass input to script
python3 main.py "$input_text"