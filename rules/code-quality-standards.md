# Code Quality Standards

These standards ensure code is readable, maintainable, and self-documenting. They apply across all languages and frameworks.

## Naming Conventions

### Intention-Revealing Names

Names should explain purpose and intent, not just describe data types or operations.

**Guidelines:**
- Explain "why" not just "what"
- Avoid mental mapping and abbreviations
- Use pronounceable, searchable names
- Be consistent with terminology
- Use domain language where appropriate

**Examples:**

```javascript
// Poor
const d = 86400; // seconds in a day
const u = getU();

// Better
const SECONDS_IN_A_DAY = 86400;
const currentUser = getCurrentUser();
```

### Consistency

Maintain consistent naming patterns throughout the codebase:

- **Variables/Functions**: `camelCase` (JavaScript/TypeScript), `snake_case` (Python/Ruby)
- **Classes**: `PascalCase` (all languages)
- **Constants**: `SCREAMING_SNAKE_CASE`
- **Private members**: Prefix with `_` or use language conventions
- **Boolean variables**: Prefix with `is`, `has`, `should`, `can`

## Function Standards

### Do One Thing

Functions should do one thing and do it well. If a function does multiple things, extract them into separate functions.

**Guidelines:**
- Single level of abstraction per function
- Extract complex logic into named helper functions
- Clear, focused purpose
- Easy to name (if naming is hard, it does too much)

### Function Size

- **Target**: Under 20 lines
- **Maximum**: 30 lines for complex logic
- **If longer**: Extract sub-operations into helper functions

### Function Parameters

- **Ideal**: 0 parameters (niladic)
- **Good**: 1-2 parameters (monadic/dyadic)
- **Maximum**: 3 parameters (triadic)
- **Avoid**: More than 3 parameters

**For many parameters:**
- Use object/dictionary parameters
- Consider if function does too much
- Group related parameters into objects

**Examples:**

```javascript
// Poor: Too many parameters
function createUser(name, email, age, address, phone, role, department) {
  // ...
}

// Better: Object parameter
function createUser(userData) {
  const { name, email, age, address, phone, role, department } = userData;
  // ...
}
```

### No Side Effects

Functions should not have hidden side effects beyond their stated purpose.

**Guidelines:**
- Make side effects explicit in function names
- Avoid modifying parameters
- Be clear about what the function changes
- Pure functions when possible

## Comment Philosophy

### Self-Documenting Code First

Code should be readable without comments. Comments explain "why," not "what."

**When to Comment:**
- Explain complex business logic or algorithms
- Document why a particular approach was chosen
- Warn about non-obvious consequences
- Clarify regulatory or compliance requirements
- Explain workarounds for external bugs

**When NOT to Comment:**
- Redundant descriptions of obvious code
- Commented-out code (use version control)
- Change logs (use git history)
- Author attribution (use git blame)

**Examples:**

```javascript
// Poor: Comments state the obvious
// Get the user by ID
const user = getUserById(id);

// Check if user exists
if (user) {
  // Set the user's name
  user.name = newName;
}

// Better: Self-documenting code
const user = getUserById(id);
if (user) {
  user.name = newName;
}

// Good: Explains WHY
// Use exponential backoff to avoid overwhelming the API during rate limit recovery
const delay = Math.pow(2, retryCount) * 1000;
await sleep(delay);
```

## Error Handling

### Exceptions for Exceptional Cases

Use exceptions/errors for exceptional situations, not control flow.

**Guidelines:**
- Never return null/undefined for expected cases
- Use Maybe/Option types or empty collections
- Fail fast with meaningful messages
- Centralize error handling
- Log errors with context

### Schema Validation at Boundaries

Validate and transform data at system boundaries.

**Guidelines:**
- Use schema validation libraries (Zod, Joi, Yup, Pydantic)
- Parse, don't validate: transform invalid data early
- Use typed data internally
- Clear error messages for validation failures

**Example:**

```typescript
// Good: Validate at boundary
const userSchema = z.object({
  email: z.string().email(),
  age: z.number().positive().int(),
  name: z.string().min(1)
});

// Transform and validate
const validatedUser = userSchema.parse(inputData); // Throws on invalid
// Now use validatedUser with confidence - it's properly typed
```

### Meaningful Error Messages

Error messages should be:
- Clear and specific
- Actionable (what to do to fix)
- Include relevant context
- Safe (don't leak sensitive information)

## Testing Standards

### Testing Pyramid

- **70% Unit Tests**: Fast, isolated, testing single units
- **20% Integration Tests**: Testing component interactions
- **10% E2E Tests**: Testing critical user journeys

### Testing Principles

**Test Behavior, Not Implementation:**
- Test what the code does, not how it does it
- Tests should survive refactoring
- Focus on inputs and outputs

**Arrange-Act-Assert (AAA):**
```javascript
test('user registration', () => {
  // Arrange
  const userData = { email: 'test@example.com', password: 'secure123' };

  // Act
  const user = registerUser(userData);

  // Assert
  expect(user.email).toBe('test@example.com');
  expect(user.isVerified).toBe(false);
});
```

**Test Independence:**
- Tests must run in any order
- No shared state between tests
- Clean setup and teardown

**Fast Feedback:**
- Unit tests should complete in seconds
- Mock external dependencies
- Parallel test execution

### TDD Mindset

For complex logic, consider Test-Driven Development:
1. **Red**: Write failing test
2. **Green**: Write minimal code to pass
3. **Refactor**: Clean up while keeping tests green

## Performance Standards

### Measure, Don't Assume

- Profile applications to find actual bottlenecks
- Use concrete metrics, not intuition
- Optimize based on data
- Monitor performance in production

### Optimization Priority

1. Correctness first
2. Clarity second
3. Performance third (when needed)

### Common Optimizations

- Strategic indexing for databases
- Caching at appropriate levels
- Lazy loading and code splitting
- Connection pooling
- Appropriate data structures for access patterns

## Related Foundations

- See **design-principles.md** for architectural guidance
- See **security-checklist.md** for security-specific standards
