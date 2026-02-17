#!/bin/bash

KEYWORD="${1:-python}"
TOTAL_RESULTS="${2:-100}"
PER_PAGE=20

if ! [[ "$TOTAL_RESULTS" =~ ^[0-9]+$ ]]; then
    echo "Second argument must be a number"
    exit 1
fi

MAX_PAGES=$(( (TOTAL_RESULTS + PER_PAGE - 1) / PER_PAGE ))
BASE_URL="https://api.hh.ru/vacancies"

TMP_ALL=$(mktemp)

for (( page=0; page<MAX_PAGES; page++ ))
do
    RESPONSE=$(curl -s -G \
        -H "User-Agent: vacancy-analytics-app" \
        --data-urlencode "text=${KEYWORD}" \
        --data-urlencode "per_page=${PER_PAGE}" \
        --data-urlencode "page=${page}" \
        -w "%{http_code}" \
        "$BASE_URL")

    HTTP_CODE="${RESPONSE: -3}"
    BODY="${RESPONSE::-3}"

    if [ "$HTTP_CODE" -ne 200 ]; then
        echo "Error: HTTP status $HTTP_CODE on page $page"
        exit 1
    fi

    echo "$BODY" >> "$TMP_ALL"
done


jq -s '[ .[] | .items[] ]' "$TMP_ALL" > ../../raw/data.json

rm -f "$TMP_ALL"
