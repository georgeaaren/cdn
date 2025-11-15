# shadcn/ui Agent Skill

Complete Agent Skill for working with shadcn/ui components in React applications.

## Overview

This skill enables Claude to help with installing, configuring, and using shadcn/ui components—a collection of beautifully-designed, accessible components built on TypeScript, Tailwind CSS, and Radix UI primitives.

## Directory Structure

```
shadcn-ui/
├── SKILL.md                      # Main skill file with workflows and instructions
├── reference.md                  # Complete component catalog (50+ components)
├── examples.md                   # Practical implementation examples
├── README.md                     # This file
└── scripts/
    └── search_components.py      # Component search utility
```

## Skill Activation

Claude will automatically use this skill when you:
- Ask to add UI components to React/Next.js projects
- Request help with shadcn/ui setup or configuration
- Want to find components for specific UI needs
- Need integration help with forms, dark mode, or other features

## Components Covered

The skill includes documentation for 50+ components organized into:

- **Form & Input** (16): Button, Input, Select, Checkbox, Date Picker, Combobox, Form, etc.
- **Layout & Navigation** (8): Sidebar, Tabs, Accordion, Navigation Menu, Breadcrumb, etc.
- **Overlays & Dialogs** (11): Dialog, Sheet, Popover, Tooltip, Dropdown Menu, etc.
- **Feedback & Status** (7): Toast, Alert, Progress, Skeleton, Badge, Spinner
- **Display & Media** (10): Card, Table, Chart, Avatar, Carousel, Calendar, etc.
- **Miscellaneous** (4): Toggle, Pagination, Collapsible

## Search Utility

The included Python script helps find components quickly:

```bash
# Search by name or keyword
python3 scripts/search_components.py --query "button"

# Filter by category
python3 scripts/search_components.py --category "form"

# Search by use case
python3 scripts/search_components.py --use-case "modal"

# List all categories
python3 scripts/search_components.py --list-categories
```

## Usage Examples

The `examples.md` file contains complete implementation examples for:
1. Form with validation (React Hook Form + Zod)
2. Confirmation dialog
3. Data table with sorting/filtering
4. Toast notifications
5. Responsive sidebar navigation
6. Settings page with tabs
7. Loading states with skeleton
8. Dropdown menu with actions

## Installation in Claude Code

This skill is already installed in your Claude Code environment at:
```
~/.claude/skills/shadcn-ui/
```

Claude will automatically discover and use it when relevant.

## Key Features

- **Progressive Documentation**: Core info in SKILL.md, detailed reference in separate files
- **Searchable Component Catalog**: Python script for quick component lookup
- **Real-World Examples**: 8 complete implementation examples
- **Framework Coverage**: Next.js, Vite, Remix, Astro, and more
- **Best Practices**: Accessibility, TypeScript, and Tailwind patterns

## Documentation Sources

- Official shadcn/ui docs: https://ui.shadcn.com/docs
- Component examples: https://ui.shadcn.com/examples
- LLM-optimized docs: https://ui.shadcn.com/llms.txt

## Maintenance

To update this skill with new components or changes:
1. Fetch latest docs from https://ui.shadcn.com/llms.txt
2. Update `reference.md` with new components
3. Add new components to `scripts/search_components.py` COMPONENTS list
4. Update examples in `examples.md` if needed

## License

This skill documentation is created for use with Claude Code. shadcn/ui itself is MIT licensed.

---

**Created**: 2025-11-10  
**Based on**: shadcn/ui documentation (https://ui.shadcn.com)
