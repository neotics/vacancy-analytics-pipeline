#!/bin/bash

INPUT="raw/data.json"
OUTPUT="raw/data.csv"

echo "id,name,published_at,employer_name,alternate_url" > "$OUTPUT"

jq -r '
.[] |
[
    .id,
    .name,
    .published_at,
    (.employer?.name // ""),
    .alternate_url
]
| @csv
' "$INPUT" >> "$OUTPUT"

