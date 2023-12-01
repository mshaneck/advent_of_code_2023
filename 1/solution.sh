#!/bin/bash

cat puzzle_input.txt | sed -E 's/[a-z]*([0-9])[a-z0-9]*([0-9])[a-z]*/\1\2/g' | sed -E '/[a-z]/ s/.*([0-9]).*/\1\1/g' | awk '{ sum += $1 } END { print sum }'