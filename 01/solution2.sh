#!/bin/bash

first_numbers=(`cat puzzle_input.txt | 
sed -E 's/(one|two|three|four|five|six|seven|eight|nine)/_&_/' | 
sed 's/_one_/1/g' |
sed 's/_two_/2/g' | 
sed 's/_three_/3/g' | 
sed 's/_four_/4/g' | 
sed 's/_five_/5/g' | 
sed 's/_six_/6/g' | 
sed 's/_seven_/7/g' | 
sed 's/_eight_/8/g' | 
sed 's/_nine_/9/g' | 
sed -E 's/^[a-z]*([0-9]).*$/\1/g'`)

second_numbers=(`cat puzzle_input.txt |
rev | 
sed -E 's/(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)/_&_/' | 
sed 's/_eno_/1/g' |
sed 's/_owt_/2/g' | 
sed 's/_eerht_/3/g' | 
sed 's/_ruof_/4/g' | 
sed 's/_evif_/5/g' | 
sed 's/_xis_/6/g' | 
sed 's/_neves_/7/g' | 
sed 's/_thgie_/8/g' | 
sed 's/_enin_/9/g' | 
sed -E 's/^[a-z]*([0-9]).*$/\1/g'`)

total=0
for i in "${!first_numbers[@]}"; do
    number="${first_numbers[i]}${second_numbers[i]}"
    ((total=total+number))
done

echo $total

