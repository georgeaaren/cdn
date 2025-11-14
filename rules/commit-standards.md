## Commit Standards

Always use the conventional commit message format:

```bash
feat(search): add content type filtering to MCP search tool

- Extract search functionality from system.ts into dedicated search.ts tool
- Add optional contentType parameter supporting project, feature, task, document, memory
- Update external search API to support type filtering with proper enum casting
- Fix PostgreSQL enum type casting in database queries
- Maintain backward compatibility when no content type is specified
```
