This developer documentation outlines how to utilize the **Jules API** to integrate Jules's capabilities into custom workflows and software development tools.

---

# Jules API Developer Documentation

The Jules API allows you to programmatically access Jules's capabilities to **automate and enhance your software development lifecycle**. You can leverage the API to automate tasks like bug fixing and code reviews, create custom workflows, and embed Jules's intelligence directly into daily tools such as Slack, GitHub, and Linear.

## Alpha Release Status

**Note:** The Jules API is currently in an **alpha release**, meaning it is experimental. As we work toward stabilization, be aware that definitions, specifications, and API keys may change. In the future, we plan to maintain at least one stable version and one experimental version.

## API Concepts

The Jules API is built around a few core resources that facilitate effective usage of the service.

| Resource     | Description                                                                                                                                                                                                                |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Source**   | An input source for the agent, such as a GitHub repository. Before using a source with the API, you must first install the Jules GitHub app through the Jules web app.                                                     |
| **Session**  | A continuous unit of work within a specific context, analogous to a chat session. A Session is initiated using both a source and a prompt.                                                                                 |
| **Activity** | A single unit of work that occurs within a Session. A Session comprises multiple activities originating from both the user and the agent, including tasks like updating progress, generating a plan, or sending a message. |

## Authentication

To begin using the Jules API, you must obtain an API key.

### Generate Your API Key

1.  Navigate to the **Settings** page within the Jules web app.
2.  Create a new API key there.

**Limit:** You may have at most 3 API keys active at any given time.

### Use Your API Key

To authenticate requests made to the API, you must pass your API key in the `X-Goog-Api-Key` header of your API calls.

### Security Warning

**Important:** You must keep your API keys secure. Do not embed your keys in public code or share them. To protect against abuse, any API keys discovered to be publicly exposed will be automatically disabled.

## Quickstart Guide

This quickstart walks through creating your first session using the `curl` command line utility.

### Step 1: List your available sources

Before creating a session, you must determine the name of the source (e.g., your GitHub repository) you intend to work with.

**Command Example (List Sources):**

```bash
curl 'https://jules.googleapis.com/v1alpha/sources' \
 -H 'X-Goog-Api-Key: YOUR_API_KEY '
```

**Example Response Snippet:**

```json
{
  "sources": [
    {
      "name": "sources/github/bobalover/boba",
      "id": "github/bobalover/boba",
      "githubRepo": {
        "owner": "bobalover",
        "repo": "boba"
      }
    }
  ],
  "nextPageToken": "github/bobalover/boba-web"
}
```

### Step 2: Create a new session

Use the source name obtained in Step 1 to create a new session. This example instructs Jules to create a "boba app" in the specified repository.

**Session Default Behavior:** By default, sessions created via the API will have their plans automatically approved. If you require explicit plan approval, set the `requirePlanApproval` field to `true`.

**Automation Mode:** The `automationMode` field is optional. By default, no Pull Request (PR) will be automatically created. Setting `automationMode` to `"AUTO_CREATE_PR"` enables automatic PR creation.

**Command Example (Create Session):**

```bash
curl 'https://jules.googleapis.com/v1alpha/sessions' \
 -X POST \
 -H "Content-Type: application/json" \
 -H 'X-Goog-Api-Key: YOUR_API_KEY ' \
 -d '{
  "prompt": "Create a boba app!",
  "sourceContext": {
    "source": "sources/github/bobalover/boba",
    "githubRepoContext": {
      "startingBranch": "main"
    }
  },
  "automationMode": "AUTO_CREATE_PR",
  "title": "Boba App"
}'
```

**Immediate Response Example:**

```json
{
  "name": "sessions/31415926535897932384",
  "id": "31415926535897932384",
  "title": "Boba App",
  "sourceContext": {
    "source": "sources/github/bobalover/boba",
    "githubRepoContext": {
      "startingBranch": "main"
    }
  },
  "prompt": "Create a boba app!"
}
```

You can poll the latest session information using `ListSessions` or `GetSession`. If a PR was automatically created, you can view the PR details in the session output.

### Step 3: Listing sessions

You can retrieve a list of your existing sessions.

**Command Example (List Sessions):**

```bash
curl 'https://jules.googleapis.com/v1alpha/sessions?pageSize=5' \
 -H 'X-Goog-Api-Key: YOUR_API_KEY '
```

### Step 4 (Conditional): Approve plan

If you set the session to require explicit plan approval (`requirePlanApproval: true`), you must approve the latest plan.

**Command Example (Approve Plan):**

```bash
curl 'https://jules.googleapis.com/v1alpha/sessions/ SESSION_ID :approvePlan' \
 -X POST \
 -H "Content-Type: application/json" \
 -H 'X-Goog-Api-Key: YOUR_API_KEY '
```

### Step 5: Activities and interacting with the agent

Sessions contain multiple Activities, which track progress, user interaction, and agent actions.

#### Listing Activities in a Session

Use the `activities` endpoint to retrieve a list of actions taken within a session. The response includes details about agent-generated plans (`planGenerated`), progress updates (`progressUpdated`), and command outputs (`bashOutput`).

**Command Example (List Activities):**

```bash
curl 'https://jules.googleapis.com/v1alpha/sessions/ SESSION_ID /activities?pageSize=30' \
 -H 'X-Goog-Api-Key: YOUR_API_KEY '
```

#### Sending a Message to the Agent

You can send additional instructions or context to the agent within an active session.

**Command Example (Send Message):**

```bash
curl 'https://jules.googleapis.com/v1alpha/sessions/ SESSION_ID :sendMessage' \
 -X POST \
 -H "Content-Type: application/json" \
 -H 'X-Goog-Api-Key: YOUR_API_KEY ' \
 -d '{ "prompt": "Can you make the app corgi themed?" }'
```

**Note on Response:** The immediate response to `sendMessage` will be empty. To view the agent's response to the new prompt, you must list the activities again.

## Full API Reference

You can view the full API reference documentation for the Jules API.
