#!/bin/bash

 

 

URL=https://www.x-rates.com

 

curl -s "$URL" > rates.html

 

 

DATE=$(grep -o 'Mar [0-9]\{1,2\}, 2025 [0-9:]\{5,\} UTC' rates.html | head -1)

EXECUTION_DATE=$(date '+%Y-%m-%d %H:%M:%S')

 

OUTPUT_FILE="/home/azureuser/scraping_dir/data/exchange_rates.csv"

EXTRACTED_RATES=$(grep -Eo "from=[A-Z]+&amp;to=[A-Z]+'>[0-9]+\.[0-9]+" rates.html | sed -E "s/from=([A-Z]+)&amp;to=([A-Z]+)'>([0-9]+\.[0-9]+)/\1\/\2,\3/")

 

LINE="$EXECUTION_DATE"

for pair in $(echo "$EXTRACTED_RATES" | cut -d',' -f1); do

    RATE=$(echo "$EXTRACTED_RATES" | grep "^$pair," | cut -d',' -f2)

    LINE="$LINE,$RATE"

done

 

echo "$LINE" >> "$OUTPUT_FILE"

cat "$OUTPUT_FILE"

 

 
