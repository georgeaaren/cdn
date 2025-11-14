# Research Methodology

This guide establishes best practices for technical research, documentation gathering, and source evaluation.

## Source Evaluation Criteria

### Primary Sources (Preferred)

These are the most authoritative and should be consulted first:

1. **Official Documentation**
   - Framework and library official docs
   - Language specifications and standards
   - API references and guides
   - RFC documents

2. **Source Code**
   - Official repositories
   - Well-maintained projects
   - Test suites (demonstrate usage)

3. **Official Blog Posts**
   - Framework team announcements
   - Release notes and changelogs
   - Migration guides

### Secondary Sources (Validate Carefully)

Useful but require cross-referencing:

1. **Technical Articles**
   - Established technical blogs
   - Conference talks and papers
   - Well-regarded tutorials

2. **Community Resources**
   - Stack Overflow (high-voted, recent)
   - GitHub issues and discussions
   - Reddit technical communities

3. **Books**
   - Recent publications (check publication date)
   - Recognized authors
   - Published by reputable publishers

### Red Flags

Be cautious of sources with:

- **Outdated information**: Check publication/update dates
- **No citations**: Unsupported claims
- **Promotional content**: Hidden commercial agenda
- **Conflicting information**: Cross-reference multiple sources
- **Poor quality**: Typos, broken examples, vague explanations

## When to Use Different Research Tools

### Context7 MCP Tools

**Use for:**
- Official framework and library documentation
- Version-specific API references
- Standard library documentation
- Language specifications

**Tools:**
- `mcp__context7__resolve-library-id`: Find library identifiers
- `mcp__context7__get-library-docs`: Retrieve documentation

**Example workflow:**
```bash
# 1. Resolve library ID
mcp__context7__resolve-library-id --query "React hooks"

# 2. Get documentation
mcp__context7__get-library-docs --library-id "react-hooks"
```

**Best for:**
- API usage examples
- Configuration options
- Migration guides
- Best practices from maintainers

### WebSearch

**Use for:**
- Current best practices and patterns
- Real-world implementation examples
- Comparing different approaches
- Recent developments and trends
- Community discussions

**Search strategies:**

```bash
# Include current year for recent information
"[technology] best practices 2024"
"[framework] patterns 2024"

# Specific problem solutions
"[error message] [framework version]"

# Comparison research
"[approach A] vs [approach B] pros cons"

# Real-world examples
"[feature] implementation example github"
```

**Best for:**
- Industry trends and adoption
- Performance comparisons
- Architecture decisions
- Debugging specific issues

### WebFetch

**Use for:**
- Retrieving specific article content
- Processing documentation pages
- Analyzing blog posts or tutorials
- Extracting information from known URLs

**Best for:**
- Deep reading of specific resources
- Extracting code examples
- Processing structured content

### Source Code Exploration

**Use for:**
- Understanding implementation details
- Finding usage examples in tests
- Checking configuration options
- Exploring undocumented features

**Finding installed packages:**

```bash
# Ruby
bundle show <gem_name>

# Node.js
npm list <package>
ls node_modules/<package>

# Python
pip show <package>
python -c "import <package>; print(<package>.__file__)"
```

**Best for:**
- Advanced usage patterns
- Implementation details
- Edge cases and limitations

## Version-Specific Research

### Determining Installed Versions

**Ruby:**
```bash
# Check Gemfile.lock
cat Gemfile.lock | grep -A 2 "gem_name"

# Find gem installation
bundle show gem_name
```

**JavaScript/TypeScript:**
```bash
# Check package-lock.json or yarn.lock
cat package-lock.json | jq '.dependencies.package_name.version'

# List installed version
npm list package_name
```

**Python:**
```bash
# Check requirements.txt or Pipfile.lock
cat requirements.txt | grep package_name

# Show installed version
pip show package_name
```

### Finding Version-Specific Documentation

1. **Check project dependencies** first
2. **Search for exact version docs**: "[library] [version] documentation"
3. **Review changelog** for breaking changes
4. **Check migration guides** between versions

## Currency Evaluation

### Assessing Information Freshness

Information becomes outdated quickly in software development. Evaluate:

- **Publication date**: Is it recent?
- **Framework version**: Does it match your version?
- **Deprecation warnings**: Are suggested approaches deprecated?
- **Community feedback**: Are there comments noting outdated info?

### Determining Current Year

```bash
# In shell commands
current_year=$(date +%Y)
echo "Searching for ${current_year} best practices"
```

### Timeliness Guidelines

- **< 1 year old**: Generally current
- **1-2 years old**: Verify against recent docs
- **2-3 years old**: Likely outdated, cross-reference
- **> 3 years old**: Treat with caution, verify heavily

### Red Flags for Outdated Content

- Deprecated APIs or patterns
- Missing recent framework features
- References to old versions
- Syntax that doesn't match current standards
- Comments noting outdated information

## Cross-Referencing Practices

### Validation Process

Never rely on a single source. Cross-reference:

1. **Check official docs** first
2. **Find 2-3 secondary sources** confirming approach
3. **Look for recent discussions** (Stack Overflow, GitHub issues)
4. **Test in small example** when possible

### When Sources Conflict

1. **Prioritize official documentation**
2. **Check publication dates** (newer may be better)
3. **Consider context** (different use cases)
4. **Look for explanations** of trade-offs
5. **Test both approaches** if possible

### Multiple Valid Approaches

Some problems have multiple valid solutions:

- **Document all approaches** with pros/cons
- **Cite sources** for each approach
- **Note trade-offs** explicitly
- **Consider project context** when recommending

## Citation Standards

### Required Information

For every external source cited, include:

- **Title** of the resource
- **URL** (full, working link)
- **Publication date** (if available)
- **Author** (if identified)
- **Last accessed date** (for web content)

### Citation Format

**Inline citations:**
```markdown
According to the [React documentation on hooks][1], useState is the most common hook.

[1]: https://react.dev/reference/react/useState (Accessed: 2024-01-15)
```

**Footnote style:**
```markdown
useState is the most common hook[^1].

[^1]: React Hooks Reference, https://react.dev/reference/react/useState
```

**Code location references:**
```markdown
See implementation in `src/utils/validation.ts:45-67`
```

### When to Cite

- Official documentation references
- Best practices from recognized sources
- Specific implementation patterns
- Performance benchmarks
- Security recommendations
- Controversial or non-obvious choices

## Research Workflow

### Phase 1: Initial Assessment

1. **Clarify the requirement**
   - What information is needed?
   - Why is it needed?
   - What's the context?

2. **Check existing research**
   - Has this been researched before?
   - Are there existing docs?
   - What's already implemented?

### Phase 2: Information Gathering

3. **Start with official documentation**
   - Use Context7 for framework docs
   - Check version compatibility
   - Read thoroughly, don't skim

4. **Expand to secondary sources**
   - WebSearch for best practices
   - Find real-world examples
   - Check recent discussions

5. **Validate with multiple sources**
   - Cross-reference findings
   - Note conflicting information
   - Identify consensus patterns

### Phase 3: Synthesis

6. **Organize findings**
   - Group related information
   - Note patterns and themes
   - Identify gaps

7. **Evaluate quality**
   - Check source credibility
   - Verify currency
   - Test claims when possible

8. **Document clearly**
   - Cite all sources
   - Note version requirements
   - Flag uncertainties

## Quality Checklist

Before finalizing research, verify:

- [ ] Primary sources consulted (official docs)
- [ ] Cross-referenced with 2+ sources
- [ ] Version compatibility checked
- [ ] Publication dates noted
- [ ] All sources cited with URLs
- [ ] Conflicting information addressed
- [ ] Trade-offs documented
- [ ] Code examples tested (if applicable)
- [ ] Security implications considered
- [ ] Performance implications noted

## Common Research Patterns

### Pattern: Framework Feature Research

1. Check official docs via Context7
2. Find version-specific examples
3. Search for best practices articles
4. Look for real implementations on GitHub
5. Check for known issues in GitHub issues
6. Document with code examples

### Pattern: Architecture Decision Research

1. Search for comparison articles
2. Read pros/cons from multiple sources
3. Find case studies of implementations
4. Consider project-specific constraints
5. Document trade-offs explicitly
6. Cite decision rationale

### Pattern: Debugging Research

1. Search exact error message
2. Check framework issue trackers
3. Find similar Stack Overflow questions
4. Look for recent discussions
5. Test proposed solutions
6. Document root cause and fix

## Related Foundations

- See **code-quality-standards.md** for documentation standards
- See **security-checklist.md** for security research considerations
- See **design-principles.md** for architectural research guidance
