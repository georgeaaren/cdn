source .env.local

TITLE="$1"
PROMPT="$2"

curl 'https://jules.googleapis.com/v1alpha/sessions' \
    -X POST \
    -H "Content-Type: application/json" \
    -H "X-Goog-Api-Key: $JULES_API_KEY" \
    -d "{
      \"title\": \"$TITLE\",
      \"prompt\": \"$PROMPT\",
      \"sourceContext\": {
        \"source\": \"sources/github/georgeaaren/pixel-clip-v2\",
        \"githubRepoContext\": {
          \"startingBranch\": \"main\"
        }
      },
      \"automationMode\": \"AUTO_CREATE_PR\"
    }"
