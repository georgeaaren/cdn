---
name: shadcn/ui
description: Install and configure shadcn/ui components for React applications. Use when adding UI components (buttons, forms, dialogs, etc.) to Next.js, Vite, Remix, or other React projects using Tailwind CSS and Radix UI primitives.
---

# shadcn/ui Component Integration

This skill helps you install, configure, and use shadcn/ui components in React applications.

## What is shadcn/ui?

shadcn/ui is a collection of beautifully-designed, accessible components built on:
- TypeScript
- Tailwind CSS
- Radix UI primitives

**Key Concept**: Unlike traditional npm packages, shadcn/ui copies component source code directly into your project, giving you full control and customization.

## When to Use This Skill

- Setting up shadcn/ui in a new project
- Installing specific UI components (buttons, forms, dialogs, cards, etc.)
- Configuring dark mode with shadcn/ui
- Integrating with form libraries (React Hook Form, TanStack Form)
- Troubleshooting component installation or configuration
- Finding the right component for a specific UI need

## Workflows

### Workflow 1: Initial Project Setup

**For Next.js projects:**
```bash
npx shadcn@latest init
```

**For Vite projects:**
```bash
npx shadcn@latest init -d
```

**For other frameworks (Remix, Astro, Laravel, etc.):**
Visit the framework-specific guide at https://ui.shadcn.com/docs/installation

**Configuration:**
The init command creates `components.json` with:
- `$schema`: Configuration schema URL
- `style`: Component style (default or new-york)
- `tailwind.config`: Tailwind config location
- `aliases.components`: Component import path (e.g., "@/components")
- `aliases.utils`: Utilities import path (e.g., "@/lib/utils")

### Workflow 2: Installing Components

**Single component:**
```bash
npx shadcn@latest add button
```

**Multiple components:**
```bash
npx shadcn@latest add button input card dialog
```

**All components:**
```bash
npx shadcn@latest add
```
Then select components interactively.

**What happens:**
1. Component files are copied to your `components/ui` directory
2. Dependencies are added to package.json
3. Required utilities are created in `lib/utils.ts`

### Workflow 3: Finding the Right Component

Use the `scripts/search_components.py` to search by name or category:

```bash
python scripts/search_components.py --query "form"
python scripts/search_components.py --category "overlays"
```

Or refer to `reference.md` for the complete component catalog organized by category.

### Workflow 4: Using Components

After installation, import and use components in your React code:

```tsx
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export function MyComponent() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Welcome</CardTitle>
      </CardHeader>
      <CardContent>
        <Input placeholder="Enter your name" />
        <Button>Submit</Button>
      </CardContent>
    </Card>
  )
}
```

### Workflow 5: Dark Mode Setup

**For Next.js with App Router:**
```bash
npx shadcn@latest add dark-mode
```

**Manual setup:**
1. Install `next-themes`: `npm install next-themes`
2. Create a theme provider component
3. Wrap your app with the provider
4. Use the `useTheme` hook to toggle themes

See framework-specific guides at https://ui.shadcn.com/docs/dark-mode

### Workflow 6: Form Integration

**With React Hook Form:**
1. Install form components: `npx shadcn@latest add form`
2. Install React Hook Form: `npm install react-hook-form @hookform/resolvers zod`
3. Use the `Form` component with `useForm` hook

**Example:**
```tsx
import { useForm } from "react-hook-form"
import { Form, FormControl, FormField, FormItem, FormLabel } from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export function MyForm() {
  const form = useForm()

  return (
    <Form {...form}>
      <FormField
        control={form.control}
        name="email"
        render={({ field }) => (
          <FormItem>
            <FormLabel>Email</FormLabel>
            <FormControl>
              <Input placeholder="email@example.com" {...field} />
            </FormControl>
          </FormItem>
        )}
      />
      <Button type="submit">Submit</Button>
    </Form>
  )
}
```

## Component Categories

shadcn/ui provides 50+ components organized into:

- **Form & Input** (16 components): Button, Input, Select, Checkbox, Date Picker, etc.
- **Layout & Navigation** (8 components): Sidebar, Tabs, Accordion, Navigation Menu, etc.
- **Overlays & Dialogs** (11 components): Modal, Sheet, Popover, Tooltip, Dropdown Menu, etc.
- **Feedback & Status** (7 components): Toast, Alert, Progress, Spinner, Badge, etc.
- **Display & Media** (10 components): Card, Table, Chart, Avatar, Carousel, etc.
- **Miscellaneous** (4 components): Toggle, Pagination, Collapsible, etc.

See `reference.md` for the complete catalog with descriptions.

## Best Practices

1. **Install Only What You Need**: Components are copied to your project, so only add components you'll use
2. **Customize After Installation**: Edit component files directly for project-specific needs
3. **Keep Dependencies Updated**: Run `npm update` periodically for Radix UI and other dependencies
4. **Use TypeScript**: While JavaScript is supported, TypeScript provides better type safety
5. **Follow Tailwind Patterns**: Components use Tailwind CSS classes; maintain consistency
6. **Test Accessibility**: Components are built on Radix UI (accessible by default), but test your implementations
7. **Version Control**: Commit component files to track customizations

## Common Issues & Solutions

**Issue**: Import paths not resolving
**Solution**: Check `tsconfig.json` or `jsconfig.json` has correct path aliases matching `components.json`

**Issue**: Tailwind classes not applying
**Solution**: Ensure `tailwind.config.js` includes component paths in `content` array

**Issue**: Component not found after installation
**Solution**: Verify component was copied to correct directory (check `components.json` aliases)

**Issue**: Style conflicts with existing CSS
**Solution**: Use Tailwind's `@layer` directive or adjust component specificity

## Advanced Topics

- **Monorepo Setup**: Special configuration for turborepo/nx workspaces
- **Custom Registry**: Create and publish your own component registry
- **React 19 Support**: Migration guides available
- **Tailwind CSS v4**: Beta support with configuration updates

## Additional Resources

- Component Catalog: See `reference.md`
- Component Search: Use `scripts/search_components.py`
- Official Docs: https://ui.shadcn.com/docs
- Component Examples: https://ui.shadcn.com/examples
- Figma Design Kit: https://ui.shadcn.com/figma

## Constraints and Limitations

- **Requires Tailwind CSS**: Must have Tailwind configured in your project
- **React Only**: Not available for Vue, Svelte, or other frameworks
- **Node.js Required**: CLI tool needs Node.js environment
- **Manual Updates**: Component updates require re-running add command (overwrites customizations)
- **No Auto-Import**: Must manually import components in your code
