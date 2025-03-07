
URL="https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1"

HTML=$(curl -s "$URL")
RATE=$(echo "$HTML" | grep 'ccOutputRslt' | sed -E 's/.*ccOutputRslt">([0-9.]+).*/\1/')

DATE=$(date '+%Y-%m-%d %H:%M:%S')
echo "$DATE,$RATE" >> rate_log.csv
echo "[$DATE] Taux USD/EUR : $RATE"
