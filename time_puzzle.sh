#!/bin/bash

# Check for correct number of arguments
if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <command_to_run> <number_of_times>"
  exit 1
fi

COMMAND=$1
NUM_TIMES=$2

# Validate that NUM_TIMES is a positive integer
if ! [[ $NUM_TIMES =~ ^[0-9]+$ ]] || [[ $NUM_TIMES -le 0 ]]; then
  echo "Error: <number_of_times> must be a positive integer."
  exit 1
fi

# Start the timer
echo "Starting timing for $NUM_TIMES runs of '$COMMAND'..."
START=$(date +%s)

# Run the command specified number of times
for ((i = 1; i <= NUM_TIMES; i++)); do
  eval "$COMMAND" > /dev/null 2>&1
  if [[ $? -ne 0 ]]; then
    echo "Error: '$COMMAND' failed on iteration $i."
    exit 1
  fi
done

# End the timer
END=$(date +%s)

# Calculate and display the elapsed time
ELAPSED=$((END - START))
echo "Completed $NUM_TIMES runs of '$COMMAND' in $ELAPSED seconds."

