# Context7 API Developer Guide

> Search and retrieve library documentation using curl commands

## Overview

Context7 provides two main API endpoints for searching libraries and retrieving their documentation. This guide demonstrates how to use curl to interact with these endpoints.

## API Endpoints

### 1. Library Search

Search for libraries by query string.

```
https://context7.com/api/v1/search?query=${query}
```

### 2. Library Documentation

Retrieve documentation for a specific library with pagination and topic filtering.

```
https://context7.com/api/v2/docs/code/${libraryID}?type=txt&page=${page}&limit=${limit}&topic=${topic}
```

## Search Libraries

### Basic Search Request

Search for a library by name or keyword:

```bash
curl "https://context7.com/api/v1/search?query=react"
```

### Search Parameters

| Parameter | Type   | Description                               |
| --------- | ------ | ----------------------------------------- |
| `query`   | string | The library name or keyword to search for |

### Search Examples

```bash
# Search for React library
curl "https://context7.com/api/v1/search?query=react"

# Search for TypeScript
curl "https://context7.com/api/v1/search?query=typescript"

# Search for a specific framework
curl "https://context7.com/api/v1/search?query=next.js"
```

### Response Format

The search endpoint returns a JSON response with matching libraries, typically including:

- Library ID
- Name
- Description
- Version information

Example response structure:

```json
{
  "results": [
    {
      "libraryID": "react-18",
      "name": "React",
      "description": "A JavaScript library for building user interfaces",
      "version": "18.x"
    }
  ]
}
```

## Get Library Documentation

### Basic Documentation Request

Retrieve documentation for a library using its ID:

```bash
curl "https://context7.com/api/v2/docs/code/websites/react_dev"
```

### Documentation Parameters

| Parameter   | Type    | Required | Description                                       |
| ----------- | ------- | -------- | ------------------------------------------------- |
| `libraryID` | string  | Yes      | The unique identifier of the library              |
| `type`      | string  | No       | Response format (e.g., `txt`, `json`, `markdown`) |
| `page`      | integer | No       | Page number for pagination (default: 1)           |
| `limit`     | integer | No       | Number of results per page (max: 50)              |
| `topic`     | string  | No       | Filter documentation by topic/section             |

### Documentation Examples

```bash
# Get all documentation for React
curl "https://context7.com/api/v2/docs/code/websites/react_dev"

# Get documentation as plain text, page 2
curl "https://context7.com/api/v2/docs/code/websites/react_dev?type=txt&page=2"

# Get documentation with 100 results per page
curl "https://context7.com/api/v2/docs/code/websites/react_dev?limit=100"

# Get documentation for a specific topic (e.g., hooks)
curl "https://context7.com/api/v2/docs/code/websites/react_dev?topic=hooks"

# Combined parameters
curl "https://context7.com/api/v2/docs/code/websites/react_dev?type=txt&page=1&limit=50&topic=api-reference"
```

## Advanced Usage

### Chaining Search and Documentation

Search for a library and retrieve its documentation in a single workflow:

```bash
# 1. Search for the library
LIBRARY=$(curl -s "https://context7.com/api/v1/search?query=lodash" | jq -r '.results[0].libraryID')

# 2. Get documentation using the library ID
curl "https://context7.com/api/v2/docs/code/$LIBRARY"
```

### Pretty Print JSON Responses

```bash
# Format JSON response nicely
curl -s "https://context7.com/api/v1/search?query=react" | jq '.'

# Pretty print documentation response
curl -s "https://context7.com/api/v2/docs/code/websites/react_dev" | jq '.'
```

### Save Documentation to File

```bash
# Save library documentation to file
curl "https://context7.com/api/v2/docs/code/websites/react_dev" > react-docs.txt

# Save with type specification
curl "https://context7.com/api/v2/docs/code/websites/react_dev?type=markdown" > react-docs.md
```

### Filtering and Processing

```bash
# Get documentation and filter by specific content
curl -s "https://context7.com/api/v2/docs/code/websites/react_dev" | jq '.documentation[] | select(.type == "example")'

# Get documentation paginated with custom headers
curl -H "Accept: application/json" \
  "https://context7.com/api/v2/docs/code/websites/react_dev?page=1&limit=25"
```

## Common Workflows

### Workflow 1: Search and Get Documentation

```bash
#!/bin/bash

# Search for a library
QUERY="express"
echo "Searching for: $QUERY"

LIBRARY_ID=$(curl -s "https://context7.com/api/v1/search?query=$QUERY" | \
  jq -r '.results[0].libraryID')

echo "Found library: $LIBRARY_ID"

# Get documentation
echo "Retrieving documentation..."
curl "https://context7.com/api/v2/docs/code/$LIBRARY_ID?type=txt"
```

### Workflow 2: Paginated Documentation Retrieval

```bash
#!/bin/bash

LIBRARY_ID="react-18"
PAGE=1
LIMIT=50

while true; do
  RESPONSE=$(curl -s "https://context7.com/api/v2/docs/code/$LIBRARY_ID?page=$PAGE&limit=$LIMIT")

  # Check if response is empty
  if [ -z "$RESPONSE" ]; then
    break
  fi

  echo "$RESPONSE"
  PAGE=$((PAGE + 1))
done
```

### Workflow 3: Search Multiple Libraries

```bash
#!/bin/bash

LIBRARIES=("react" "vue" "angular" "svelte")

for lib in "${LIBRARIES[@]}"; do
  echo "=== $lib ==="
  curl -s "https://context7.com/api/v1/search?query=$lib" | jq '.results[0]'
  echo ""
done
```

## Error Handling

### Check for Errors

```bash
# Make request and check HTTP status
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  "https://context7.com/api/v1/search?query=react")

if [ "$HTTP_CODE" -ne 200 ]; then
  echo "Error: HTTP $HTTP_CODE"
  exit 1
fi
```

### Handling Empty Results

```bash
# Check if search returned results
RESULTS=$(curl -s "https://context7.com/api/v1/search?query=nonexistent-lib")

if [ $(echo "$RESULTS" | jq '.results | length') -eq 0 ]; then
  echo "No libraries found"
  exit 1
fi
```

## Tips and Best Practices

1. **Use `-s` flag**: Silent mode to suppress progress information

   ```bash
   curl -s "https://context7.com/api/v1/search?query=react"
   ```

2. **Pipe to jq**: Process JSON responses easily

   ```bash
   curl -s "https://context7.com/api/v1/search?query=react" | jq '.results'
   ```

3. **Cache results**: Store responses to avoid repeated requests

   ```bash
   curl -s "https://context7.com/api/v1/search?query=react" > cache.json
   ```

4. **Use topic filtering**: Get specific sections of documentation

   ```bash
   curl "https://context7.com/api/v2/docs/code/websites/react_dev?topic=hooks"
   ```

5. **Set reasonable page limits**: Optimize response size
   ```bash
   curl "https://context7.com/api/v2/docs/code/websites/react_dev?limit=100"
   ```

## References

- **Search API**: `/api/v1/search`
- **Docs API**: `/api/v2/docs/code/{libraryID}`
- **Base URL**: `https://context7.com`
