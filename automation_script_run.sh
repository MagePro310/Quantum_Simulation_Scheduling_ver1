#!/bin/bash

# chmod +x automation_script_run.sh
# files=("runLoopTestFFD.py" "runLoopTestMTMC.py" "runLoopTestNoTaDS.py" "runLoopTestMILQ.py")
# files=("runLoopTestNoTaDS.py" "runLoopTestMILQ.py")
files=("runLoopTestMILQ.py")
for file in "${files[@]}"
do
  for argv1 in {3..5}
  do
    for argv2 in {2..10}
    do
      echo "Running: python $file $argv1 $argv2"
      python "$file" "$argv1" "$argv2"
    done
  done
done
