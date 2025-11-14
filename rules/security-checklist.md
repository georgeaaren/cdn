# Security Checklist

This comprehensive security checklist covers common vulnerabilities and best practices. All code should be evaluated against these criteria before deployment.

## OWASP Top 10 Compliance

Every security review should systematically check compliance with the OWASP Top 10:

1. **A01:2021 - Broken Access Control**
2. **A02:2021 - Cryptographic Failures**
3. **A03:2021 - Injection**
4. **A04:2021 - Insecure Design**
5. **A05:2021 - Security Misconfiguration**
6. **A06:2021 - Vulnerable and Outdated Components**
7. **A07:2021 - Identification and Authentication Failures**
8. **A08:2021 - Software and Data Integrity Failures**
9. **A09:2021 - Security Logging and Monitoring Failures**
10. **A10:2021 - Server-Side Request Forgery (SSRF)**

## Input Validation and Sanitization

### Systematic Input Scanning

Scan all input entry points in the codebase:

**JavaScript/TypeScript:**
```bash
grep -r "req\.\(body\|params\|query\)" --include="*.js" --include="*.ts"
```

**Ruby/Rails:**
```bash
grep -r "params\[" --include="*.rb"
```

**Python (Flask/FastAPI):**
```bash
grep -r "request\.\(json\|form\|args\)" --include="*.py"
```

### Validation Requirements

For every input point, verify:

- [ ] **Type validation**: Ensure correct data types
- [ ] **Length limits**: Prevent buffer overflows and DOS
- [ ] **Format constraints**: Regex or schema validation
- [ ] **Whitelist validation**: Accept known-good values
- [ ] **Sanitization**: Remove or escape dangerous characters
- [ ] **Schema validation**: Use libraries (Zod, Joi, Pydantic)

### Validation Example

```typescript
import { z } from 'zod';

const userInputSchema = z.object({
  email: z.string().email().max(255),
  age: z.number().int().positive().max(150),
  username: z.string().min(3).max(20).regex(/^[a-zA-Z0-9_]+$/)
});

// At system boundary
const validatedInput = userInputSchema.parse(req.body);
```

## SQL Injection Prevention

### Detection Patterns

Scan for SQL injection vulnerabilities:

**JavaScript/TypeScript:**
```bash
grep -r "query\|execute" --include="*.js" --include="*.ts" | grep -v "?"
```

**Python:**
```bash
grep -r "execute\|cursor" --include="*.py"
```

Look for:
- String concatenation in queries
- Template literals with variables
- Missing parameterization

### Prevention Requirements

- [ ] **Always use parameterized queries**
- [ ] **Never concatenate user input into SQL**
- [ ] **Use ORM query builders properly**
- [ ] **Escape identifiers if dynamic**
- [ ] **Principle of least privilege** for database users

### Safe Query Examples

```javascript
// DANGEROUS - SQL Injection vulnerability
const query = `SELECT * FROM users WHERE email = '${userEmail}'`;

// SAFE - Parameterized query
const query = 'SELECT * FROM users WHERE email = ?';
db.query(query, [userEmail]);

// SAFE - ORM
const user = await User.findOne({ where: { email: userEmail } });
```

## XSS (Cross-Site Scripting) Protection

### Output Encoding

- [ ] **Escape all user-generated content** in HTML contexts
- [ ] **Use framework-provided escaping** (React, Vue auto-escape)
- [ ] **Content Security Policy (CSP)** headers configured
- [ ] **Avoid `innerHTML` or `dangerouslySetInnerHTML`**
- [ ] **Sanitize rich text** with libraries (DOMPurify)

### Framework-Specific

**React:**
```jsx
// SAFE - React escapes by default
<div>{userInput}</div>

// DANGEROUS - Bypasses escaping
<div dangerouslySetInnerHTML={{ __html: userInput }} />

// SAFE - Sanitize first
import DOMPurify from 'dompurify';
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userInput) }} />
```

### CSP Headers

```javascript
// Express.js example
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
  );
  next();
});
```

## Authentication and Authorization

### Authentication Requirements

- [ ] **Strong password requirements** (length, complexity)
- [ ] **Password hashing** with bcrypt, Argon2, or PBKDF2
- [ ] **Multi-factor authentication (MFA)** for sensitive operations
- [ ] **Secure session management** (HTTPOnly, Secure flags)
- [ ] **Token expiration** and refresh mechanisms
- [ ] **Rate limiting** on authentication endpoints
- [ ] **Account lockout** after failed attempts

### Authorization Requirements

- [ ] **Authentication check** on all protected endpoints
- [ ] **Authorization check** at both route and resource level
- [ ] **Role-Based Access Control (RBAC)** implementation
- [ ] **Principle of least privilege**
- [ ] **No privilege escalation paths**
- [ ] **Owner checks** for resource access

### Example

```javascript
// Authentication middleware
async function requireAuth(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });

  try {
    const user = await verifyToken(token);
    req.user = user;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}

// Authorization middleware
function requireRole(role) {
  return (req, res, next) => {
    if (req.user.role !== role) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    next();
  };
}

// Usage
app.delete('/api/users/:id', requireAuth, requireRole('admin'), deleteUser);
```

## Sensitive Data Handling

### Detection

Scan for hardcoded secrets:

```bash
grep -r "password\|secret\|key\|token\|api_key" --include="*.js" --include="*.rb" --include="*.py"
```

### Requirements

- [ ] **No hardcoded credentials** in code
- [ ] **Environment variables** for secrets
- [ ] **Secrets management** system (Vault, AWS Secrets Manager)
- [ ] **Encryption at rest** for sensitive data
- [ ] **TLS/HTTPS** for data in transit
- [ ] **Sensitive data not in logs** or error messages
- [ ] **PII encryption** where required
- [ ] **Secure key storage and rotation**

### Example

```javascript
// DANGEROUS
const API_KEY = 'sk-1234567890abcdef';

// SAFE
const API_KEY = process.env.API_KEY;
if (!API_KEY) throw new Error('API_KEY not configured');
```

## CSRF Protection

- [ ] **CSRF tokens** for state-changing operations
- [ ] **SameSite cookie attribute** configured
- [ ] **Check Origin/Referer headers**
- [ ] **Double-submit cookies** pattern

## Security Headers

Configure these security headers:

```javascript
// helmet.js (Express)
const helmet = require('helmet');
app.use(helmet());

// Manual configuration
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  next();
});
```

## Dependency Security

- [ ] **Regular dependency updates**
- [ ] **Automated vulnerability scanning** (Snyk, Dependabot)
- [ ] **Pin dependency versions**
- [ ] **Review dependency licenses**
- [ ] **Minimal dependencies** (reduce attack surface)

```bash
# Check for vulnerabilities
npm audit
bundle audit
pip-audit
```

## Error Handling and Logging

### Safe Error Messages

- [ ] **Generic errors** to users
- [ ] **Detailed errors** in logs only
- [ ] **No stack traces** to users in production
- [ ] **No sensitive data** in error messages
- [ ] **No system information** leaked

### Logging Requirements

- [ ] **Log authentication events** (success/failure)
- [ ] **Log authorization failures**
- [ ] **Log data access** (especially sensitive data)
- [ ] **Structured logging** (JSON format)
- [ ] **Log rotation and retention** policies
- [ ] **PII redaction** in logs
- [ ] **Centralized logging** for monitoring

## Security Testing

- [ ] **Automated security scanning** in CI/CD
- [ ] **Regular penetration testing**
- [ ] **Security code reviews**
- [ ] **Threat modeling** for new features
- [ ] **Security-focused test cases**

## Quick Security Review Checklist

Use this for rapid security assessment:

- [ ] All inputs validated and sanitized
- [ ] No hardcoded secrets or credentials
- [ ] Proper authentication on all endpoints
- [ ] SQL queries use parameterization
- [ ] XSS protection implemented
- [ ] HTTPS enforced
- [ ] CSRF protection enabled
- [ ] Security headers configured
- [ ] Error messages don't leak information
- [ ] Dependencies up-to-date and vulnerability-free

## Think Like an Attacker

When reviewing code, ask:

- Where are the vulnerabilities?
- What could go wrong?
- How could this be exploited?
- What happens with malicious input?
- Can authentication/authorization be bypassed?
- Is sensitive data exposed?
- Are there race conditions?
- What about edge cases?

## Related Foundations

- See **design-principles.md** for fail-fast principles
- See **code-quality-standards.md** for validation standards
