#!/usr/bin/env python3
"""
Search shadcn/ui components by name, category, or use case.

Usage:
  python search_components.py --query "button"
  python search_components.py --category "form"
  python search_components.py --use-case "modal"

This script is part of the shadcn/ui Agent Skill.
It helps Claude quickly find relevant components without parsing
the entire reference documentation.
"""

import sys
import json
import argparse
from typing import List, Dict

# Complete component database
COMPONENTS = [
    # Form & Input
    {"name": "button", "category": "form", "description": "Primary actions, form submissions, navigation", "keywords": ["click", "action", "submit", "cta"]},
    {"name": "input", "category": "form", "description": "Text input fields, email, password, number inputs", "keywords": ["text", "field", "email", "password"]},
    {"name": "select", "category": "form", "description": "Dropdown selection from predefined options", "keywords": ["dropdown", "options", "choose"]},
    {"name": "checkbox", "category": "form", "description": "Boolean toggles, multi-select options", "keywords": ["check", "multi", "select"]},
    {"name": "radio-group", "category": "form", "description": "Mutually exclusive options", "keywords": ["radio", "exclusive", "choice"]},
    {"name": "switch", "category": "form", "description": "Toggle settings on/off", "keywords": ["toggle", "boolean", "on-off"]},
    {"name": "slider", "category": "form", "description": "Numeric value selection with range", "keywords": ["range", "number", "scale"]},
    {"name": "textarea", "category": "form", "description": "Multi-line text input", "keywords": ["text", "multiline", "paragraph"]},
    {"name": "date-picker", "category": "form", "description": "Date selection with calendar", "keywords": ["date", "calendar", "time"]},
    {"name": "combobox", "category": "form", "description": "Searchable dropdown with autocomplete", "keywords": ["search", "autocomplete", "filter"]},
    {"name": "form", "category": "form", "description": "Form wrapper with validation", "keywords": ["validation", "hook-form", "zod"]},
    {"name": "label", "category": "form", "description": "Accessible labels for form inputs", "keywords": ["accessibility", "for"]},
    {"name": "command", "category": "form", "description": "Command palette, searchable command menu", "keywords": ["palette", "search", "keyboard", "cmdk"]},
    {"name": "input-otp", "category": "form", "description": "One-time password input fields", "keywords": ["otp", "2fa", "verification"]},
    {"name": "multi-select", "category": "form", "description": "Select multiple items from a list", "keywords": ["multiple", "tags", "selection"]},
    {"name": "file-upload", "category": "form", "description": "File selection and upload interface", "keywords": ["file", "upload", "drag", "drop"]},

    # Layout & Navigation
    {"name": "sidebar", "category": "layout", "description": "Application navigation sidebar", "keywords": ["nav", "navigation", "menu", "collapsible"]},
    {"name": "tabs", "category": "layout", "description": "Organize content into switchable panels", "keywords": ["panels", "switch", "sections"]},
    {"name": "accordion", "category": "layout", "description": "Collapsible content sections", "keywords": ["collapse", "expand", "faq"]},
    {"name": "navigation-menu", "category": "layout", "description": "Main site navigation with dropdowns", "keywords": ["nav", "header", "menu"]},
    {"name": "breadcrumb", "category": "layout", "description": "Show current location in hierarchy", "keywords": ["navigation", "path", "hierarchy"]},
    {"name": "separator", "category": "layout", "description": "Visual divider between content", "keywords": ["divider", "line", "hr"]},
    {"name": "resizable", "category": "layout", "description": "Panels with adjustable sizes", "keywords": ["split", "resize", "panels"]},
    {"name": "scroll-area", "category": "layout", "description": "Custom styled scrollable regions", "keywords": ["scroll", "overflow", "scrollbar"]},

    # Overlays & Dialogs
    {"name": "dialog", "category": "overlay", "description": "Modal dialogs, confirmations, forms", "keywords": ["modal", "popup", "overlay"]},
    {"name": "sheet", "category": "overlay", "description": "Slide-out panels from screen edges", "keywords": ["drawer", "slide", "panel", "mobile"]},
    {"name": "popover", "category": "overlay", "description": "Non-modal floating content", "keywords": ["popup", "float", "trigger"]},
    {"name": "tooltip", "category": "overlay", "description": "Brief help text on hover", "keywords": ["hint", "help", "hover"]},
    {"name": "dropdown-menu", "category": "overlay", "description": "Context menus, action menus", "keywords": ["menu", "actions", "context"]},
    {"name": "context-menu", "category": "overlay", "description": "Right-click context menus", "keywords": ["right-click", "menu"]},
    {"name": "hover-card", "category": "overlay", "description": "Rich preview content on hover", "keywords": ["preview", "hover", "card"]},
    {"name": "menubar", "category": "overlay", "description": "Desktop application-style menu bar", "keywords": ["menu", "desktop", "bar"]},
    {"name": "alert-dialog", "category": "overlay", "description": "Important confirmations, destructive actions", "keywords": ["confirm", "warning", "destructive"]},
    {"name": "drawer", "category": "overlay", "description": "Mobile-friendly bottom sheet", "keywords": ["mobile", "bottom", "sheet", "swipe"]},
    {"name": "sonner", "category": "overlay", "description": "Toast notifications alternative", "keywords": ["toast", "notification", "snackbar"]},

    # Feedback & Status
    {"name": "toast", "category": "feedback", "description": "Temporary notification messages", "keywords": ["notification", "alert", "message"]},
    {"name": "alert", "category": "feedback", "description": "Important inline messages", "keywords": ["warning", "error", "info"]},
    {"name": "progress", "category": "feedback", "description": "Show task completion percentage", "keywords": ["loading", "percent", "bar"]},
    {"name": "skeleton", "category": "feedback", "description": "Loading placeholders", "keywords": ["loading", "placeholder", "shimmer"]},
    {"name": "badge", "category": "feedback", "description": "Status indicators, labels, counts", "keywords": ["label", "tag", "status", "count"]},
    {"name": "spinner", "category": "feedback", "description": "Loading indicator", "keywords": ["loading", "spin", "wait"]},

    # Display & Media
    {"name": "card", "category": "display", "description": "Container for grouped content", "keywords": ["container", "box", "panel"]},
    {"name": "table", "category": "display", "description": "Tabular data display", "keywords": ["data", "grid", "rows"]},
    {"name": "chart", "category": "display", "description": "Data visualizations", "keywords": ["graph", "visualization", "recharts"]},
    {"name": "avatar", "category": "display", "description": "User profile images", "keywords": ["profile", "user", "image"]},
    {"name": "carousel", "category": "display", "description": "Image/content slider", "keywords": ["slider", "slideshow", "gallery"]},
    {"name": "aspect-ratio", "category": "display", "description": "Maintain aspect ratio for images/videos", "keywords": ["ratio", "responsive", "image"]},
    {"name": "calendar", "category": "display", "description": "Date selection calendar", "keywords": ["date", "picker", "schedule"]},
    {"name": "data-table", "category": "display", "description": "Advanced tables with sorting, filtering, pagination", "keywords": ["table", "tanstack", "sort", "filter"]},

    # Miscellaneous
    {"name": "toggle", "category": "misc", "description": "Button with pressed/unpressed state", "keywords": ["press", "state", "button"]},
    {"name": "toggle-group", "category": "misc", "description": "Group of toggle buttons", "keywords": ["group", "toggle", "buttons"]},
    {"name": "pagination", "category": "misc", "description": "Navigate between pages", "keywords": ["pages", "next", "previous"]},
    {"name": "collapsible", "category": "misc", "description": "Show/hide content section", "keywords": ["collapse", "expand", "toggle"]},
]

CATEGORY_MAP = {
    "form": "Form & Input",
    "layout": "Layout & Navigation",
    "overlay": "Overlays & Dialogs",
    "feedback": "Feedback & Status",
    "display": "Display & Media",
    "misc": "Miscellaneous"
}

USE_CASE_MAP = {
    "modal": ["dialog", "sheet", "alert-dialog", "drawer"],
    "notification": ["toast", "sonner", "alert"],
    "navigation": ["sidebar", "navigation-menu", "breadcrumb", "tabs", "menubar"],
    "loading": ["skeleton", "spinner", "progress"],
    "user-input": ["input", "textarea", "select", "combobox", "checkbox", "radio-group"],
    "data-display": ["table", "data-table", "card", "chart"],
    "menu": ["dropdown-menu", "context-menu", "menubar", "navigation-menu"],
}

def search_by_query(query: str) -> List[Dict]:
    """Search components by name, description, or keywords."""
    query_lower = query.lower()
    results = []

    for component in COMPONENTS:
        # Check name
        if query_lower in component["name"]:
            results.append({"component": component, "relevance": 3})
            continue

        # Check description
        if query_lower in component["description"].lower():
            results.append({"component": component, "relevance": 2})
            continue

        # Check keywords
        if any(query_lower in keyword for keyword in component["keywords"]):
            results.append({"component": component, "relevance": 1})

    # Sort by relevance (highest first)
    results.sort(key=lambda x: x["relevance"], reverse=True)
    return [r["component"] for r in results]

def search_by_category(category: str) -> List[Dict]:
    """Search components by category."""
    category_lower = category.lower()

    # Handle partial matches
    for key, value in CATEGORY_MAP.items():
        if category_lower in key or category_lower in value.lower():
            return [c for c in COMPONENTS if c["category"] == key]

    return []

def search_by_use_case(use_case: str) -> List[Dict]:
    """Search components by common use case."""
    use_case_lower = use_case.lower()

    # Direct match
    if use_case_lower in USE_CASE_MAP:
        component_names = USE_CASE_MAP[use_case_lower]
        return [c for c in COMPONENTS if c["name"] in component_names]

    # Partial match
    for key, component_names in USE_CASE_MAP.items():
        if use_case_lower in key:
            return [c for c in COMPONENTS if c["name"] in component_names]

    return []

def format_results(components: List[Dict]) -> str:
    """Format search results as readable text."""
    if not components:
        return "No components found."

    output = []
    for comp in components:
        category_name = CATEGORY_MAP.get(comp["category"], comp["category"])
        output.append(f"• {comp['name']} ({category_name})")
        output.append(f"  Description: {comp['description']}")
        output.append(f"  Install: npx shadcn@latest add {comp['name']}")
        output.append("")

    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(
        description='Search shadcn/ui components',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python search_components.py --query "button"
  python search_components.py --category "form"
  python search_components.py --use-case "modal"
  python search_components.py --list-categories
        """
    )

    parser.add_argument('--query', '-q', help='Search by name or keyword')
    parser.add_argument('--category', '-c', help='Filter by category')
    parser.add_argument('--use-case', '-u', help='Search by use case')
    parser.add_argument('--list-categories', '-l', action='store_true', help='List all categories')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        # List categories
        if args.list_categories:
            categories = "\n".join([f"• {key}: {value}" for key, value in CATEGORY_MAP.items()])
            print("Available Categories:\n" + categories)
            print("\nAvailable Use Cases:")
            print("\n".join([f"• {key}" for key in USE_CASE_MAP.keys()]))
            return 0

        # Require at least one search parameter
        if not any([args.query, args.category, args.use_case]):
            parser.print_help()
            return 1

        # Perform search
        results = []

        if args.query:
            results = search_by_query(args.query)
        elif args.category:
            results = search_by_category(args.category)
        elif args.use_case:
            results = search_by_use_case(args.use_case)

        # Output results
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(format_results(results))

        return 0

    except Exception as e:
        error = {"status": "error", "message": str(e)}
        if args.json:
            print(json.dumps(error), file=sys.stderr)
        else:
            print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
