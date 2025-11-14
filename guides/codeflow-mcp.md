## Codeflow MCP

- When creating documents, task descriptions, memories, you can mention existing entities by `@[entity_type:entity_short_id]`. For example: `@[task:T-123456]`, `@[document:D-123456]`, `@[memory:M-123456]`, `@[file:F-123456]`

### Creating Tasks and Subtasks

When creating subtasks for a parent task, create each subtask individually with separate tool calls:

```typescript
// CORRECT: Create each subtask individually
mcp__codeflow__tasks({
  type: "create",
  params: {
    name: "Subtask Name",
    description: "Detailed description...",
    parent_id: "T-XXXXXX", // Parent task short_id
    task_type: "Feature", // Feature/Bug/Chore/Refactor/etc
    complexity_score: 7,
    priority: "High",
  },
});

// INCORRECT: Do NOT use bulk creation with parent_id
// The API does not support creating multiple subtasks in one call
```

**Important Notes:**

- Use `parent_id` to link subtasks to their parent task
- Each subtask must be created with a separate tool call
- Include task metadata: `task_type`, `complexity_score`, `priority`
- For bulk creation without parent relationships, use `project_id` with `tasks` array
