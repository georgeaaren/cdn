# Core Design Principles

These fundamental principles guide all software design and development decisions. They represent timeless best practices derived from Clean Code, The Pragmatic Programmer, Code Complete, Design Patterns, and The Mythical Man-Month.

## Fundamental Principles

### Design for Minimum Complexity

Choose the simplest solution that works. Every line of code is a liability that can contain bugs, needs maintenance, and adds cognitive load. Complexity must be justified by clear benefits.

**Key Points:**
- Exhaust simple solutions before suggesting complex patterns
- Question every line of code and abstraction
- Replace clever code with obvious code
- Complexity is a last resort, not a first choice

### Favor Composition Over Inheritance

Build flexibility through object relationships rather than class hierarchies. Composition reduces coupling and enables more flexible, maintainable systems.

**Key Points:**
- Prefer "has-a" relationships over "is-a" relationships
- Enable runtime behavior changes
- Avoid deep inheritance hierarchies
- Reduce coupling between components

### Single Responsibility Principle

Each module, class, or function should have one reason to change. Changes should affect only one module, minimizing the blast radius of modifications.

**Key Points:**
- One responsibility per component
- Changes localized to single modules
- Clear, focused purpose for each unit
- Easier testing and maintenance

### Open/Closed Principle

Software entities should be open for extension but closed for modification. Design for evolution without changing existing, tested code.

**Key Points:**
- Extend behavior without modifying existing code
- Use abstractions and interfaces for flexibility
- Protect stable code from changes
- Enable safe feature additions

### Maintain Conceptual Integrity

Ensure all parts of the system work together coherently. The system should feel like it was designed by a single mind, with consistent patterns and conventions throughout.

**Key Points:**
- Consistent design patterns across the system
- Uniform naming and coding conventions
- Coherent architectural decisions
- Clear system-wide standards

### Use Abstractions and Interfaces

Decouple components from specific implementations. Depend on abstractions, not concrete implementations, but avoid premature abstraction.

**Key Points:**
- Define clear contracts between components
- Enable implementation swapping
- Reduce coupling between modules
- Abstract only when patterns emerge (Rule of Three)

### Fail Fast and Provide Meaningful Feedback

Detect problems as early as possible. Make failures obvious and provide clear, actionable error messages that help developers understand and fix issues quickly.

**Key Points:**
- Validate inputs at system boundaries
- Use assertions to make assumptions explicit
- Provide clear, actionable error messages
- Detect and report problems immediately
- Never silently ignore errors

### Design for Flexibility and Maintainability

Plan for evolution from the beginning without over-engineering. Balance current needs with future flexibility, but never add features "just in case."

**Key Points:**
- Consider how the system might evolve
- Build in extension points where needed
- Avoid premature optimization
- Apply YAGNI: You Aren't Gonna Need It
- Refactor when patterns emerge, not before

## Application Guidelines

### When Applying These Principles

1. **Start Simple**: Always begin with the simplest solution
2. **Question Complexity**: Challenge every abstraction and pattern
3. **Refactor to Patterns**: Don't design patterns upfront - refactor toward them
4. **Consider Impact**: Think about how changes affect the entire system
5. **Maintain Consistency**: Follow existing patterns and conventions
6. **Balance Pragmatism**: Know when to bend rules for practical reasons

### The Boy Scout Rule

Leave code cleaner than you found it. Every change is an opportunity to improve the codebase incrementally.

## Related Foundations

- See **code-quality-standards.md** for implementation details
- See **security-checklist.md** for security-specific principles
