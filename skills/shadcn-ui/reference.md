# shadcn/ui Component Reference

Complete catalog of all shadcn/ui components organized by category.

## Form & Input Components (16)

### Button
- **Install**: `npx shadcn@latest add button`
- **Usage**: Primary actions, form submissions, navigation
- **Variants**: default, destructive, outline, secondary, ghost, link
- **Sizes**: default, sm, lg, icon

### Input
- **Install**: `npx shadcn@latest add input`
- **Usage**: Text input fields, email, password, number inputs
- **Features**: Placeholder, disabled state, error state

### Select
- **Install**: `npx shadcn@latest add select`
- **Usage**: Dropdown selection from predefined options
- **Features**: Single select, disabled options, placeholder

### Checkbox
- **Install**: `npx shadcn@latest add checkbox`
- **Usage**: Boolean toggles, multi-select options
- **Features**: Checked, unchecked, indeterminate states

### Radio Group
- **Install**: `npx shadcn@latest add radio-group`
- **Usage**: Mutually exclusive options
- **Features**: Grouped radio buttons with labels

### Switch
- **Install**: `npx shadcn@latest add switch`
- **Usage**: Toggle settings on/off
- **Features**: Boolean state with smooth animation

### Slider
- **Install**: `npx shadcn@latest add slider`
- **Usage**: Numeric value selection with range
- **Features**: Min/max values, step increments, single or range

### Textarea
- **Install**: `npx shadcn@latest add textarea`
- **Usage**: Multi-line text input
- **Features**: Auto-resize, character count

### Date Picker
- **Install**: `npx shadcn@latest add date-picker`
- **Usage**: Date selection with calendar
- **Features**: Single date, date range, disabled dates
- **Dependencies**: date-fns or day.js

### Combobox
- **Install**: `npx shadcn@latest add combobox`
- **Usage**: Searchable dropdown with autocomplete
- **Features**: Filter options, keyboard navigation

### Form
- **Install**: `npx shadcn@latest add form`
- **Usage**: Form wrapper with validation
- **Features**: Integration with React Hook Form, Zod validation
- **Components**: FormField, FormItem, FormLabel, FormControl, FormMessage

### Label
- **Install**: `npx shadcn@latest add label`
- **Usage**: Accessible labels for form inputs
- **Features**: Associated with form controls via htmlFor

### Command
- **Install**: `npx shadcn@latest add command`
- **Usage**: Command palette, searchable command menu
- **Features**: Keyboard shortcuts, fuzzy search
- **Uses**: cmdk library

### Input OTP
- **Install**: `npx shadcn@latest add input-otp`
- **Usage**: One-time password input fields
- **Features**: Auto-focus, numeric/alphanumeric modes

### Multi Select
- **Install**: `npx shadcn@latest add multi-select`
- **Usage**: Select multiple items from a list
- **Features**: Tags, clear all, search

### File Upload
- **Install**: `npx shadcn@latest add file-upload`
- **Usage**: File selection and upload interface
- **Features**: Drag-and-drop, file type restrictions, preview

## Layout & Navigation Components (8)

### Sidebar
- **Install**: `npx shadcn@latest add sidebar`
- **Usage**: Application navigation sidebar
- **Features**: Collapsible, mobile-responsive, nested items

### Tabs
- **Install**: `npx shadcn@latest add tabs`
- **Usage**: Organize content into switchable panels
- **Features**: Keyboard navigation, controlled/uncontrolled

### Accordion
- **Install**: `npx shadcn@latest add accordion`
- **Usage**: Collapsible content sections
- **Features**: Single or multiple items open, controlled state

### Navigation Menu
- **Install**: `npx shadcn@latest add navigation-menu`
- **Usage**: Main site navigation with dropdowns
- **Features**: Keyboard accessible, hover/click triggers

### Breadcrumb
- **Install**: `npx shadcn@latest add breadcrumb`
- **Usage**: Show current location in hierarchy
- **Features**: Custom separators, truncation

### Separator
- **Install**: `npx shadcn@latest add separator`
- **Usage**: Visual divider between content
- **Features**: Horizontal or vertical orientation

### Resizable
- **Install**: `npx shadcn@latest add resizable`
- **Usage**: Panels with adjustable sizes
- **Features**: Drag handle, min/max constraints

### Scroll Area
- **Install**: `npx shadcn@latest add scroll-area`
- **Usage**: Custom styled scrollable regions
- **Features**: Horizontal/vertical scroll, styled scrollbar

## Overlays & Dialogs Components (11)

### Dialog
- **Install**: `npx shadcn@latest add dialog`
- **Usage**: Modal dialogs, confirmations, forms
- **Features**: Focus trap, backdrop, ESC to close
- **Components**: DialogTrigger, DialogContent, DialogHeader, DialogFooter

### Sheet
- **Install**: `npx shadcn@latest add sheet`
- **Usage**: Slide-out panels from screen edges
- **Features**: Top, right, bottom, left positions
- **Use Cases**: Mobile menus, sidebars, detail panels

### Popover
- **Install**: `npx shadcn@latest add popover`
- **Usage**: Non-modal floating content
- **Features**: Click or hover trigger, positioning

### Tooltip
- **Install**: `npx shadcn@latest add tooltip`
- **Usage**: Brief help text on hover
- **Features**: Auto-positioning, delay configuration

### Dropdown Menu
- **Install**: `npx shadcn@latest add dropdown-menu`
- **Usage**: Context menus, action menus
- **Features**: Nested menus, checkboxes, radio items, shortcuts

### Context Menu
- **Install**: `npx shadcn@latest add context-menu`
- **Usage**: Right-click context menus
- **Features**: Similar to dropdown menu, trigger on right-click

### Hover Card
- **Install**: `npx shadcn@latest add hover-card`
- **Usage**: Rich preview content on hover
- **Features**: Delay before showing, positioning

### Menubar
- **Install**: `npx shadcn@latest add menubar`
- **Usage**: Desktop application-style menu bar
- **Features**: Keyboard navigation, nested menus

### Alert Dialog
- **Install**: `npx shadcn@latest add alert-dialog`
- **Usage**: Important confirmations, destructive actions
- **Features**: Focus on primary action, cannot dismiss easily

### Drawer
- **Install**: `npx shadcn@latest add drawer`
- **Usage**: Mobile-friendly bottom sheet
- **Features**: Swipe to dismiss, snap points
- **Library**: vaul

### Sonner
- **Install**: `npx shadcn@latest add sonner`
- **Usage**: Toast notifications (alternative to Toast)
- **Features**: Queued toasts, promise handling, custom JSX
- **Library**: sonner

## Feedback & Status Components (7)

### Toast
- **Install**: `npx shadcn@latest add toast`
- **Usage**: Temporary notification messages
- **Features**: Success, error, info variants, auto-dismiss
- **Hook**: useToast()

### Alert
- **Install**: `npx shadcn@latest add alert`
- **Usage**: Important inline messages
- **Variants**: default, destructive
- **Components**: Alert, AlertTitle, AlertDescription

### Progress
- **Install**: `npx shadcn@latest add progress`
- **Usage**: Show task completion percentage
- **Features**: Determinate progress bar

### Skeleton
- **Install**: `npx shadcn@latest add skeleton`
- **Usage**: Loading placeholders
- **Features**: Animated shimmer effect

### Badge
- **Install**: `npx shadcn@latest add badge`
- **Usage**: Status indicators, labels, counts
- **Variants**: default, secondary, destructive, outline

### Spinner
- **Install**: `npx shadcn@latest add spinner`
- **Usage**: Loading indicator
- **Features**: Size variants, overlay mode

### Loading Button
- **Install**: Part of Button component
- **Usage**: Button with loading state
- **Features**: Spinner + disabled state during async operations

## Display & Media Components (10)

### Card
- **Install**: `npx shadcn@latest add card`
- **Usage**: Container for grouped content
- **Components**: Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter

### Table
- **Install**: `npx shadcn@latest add table`
- **Usage**: Tabular data display
- **Components**: Table, TableHeader, TableBody, TableRow, TableCell
- **Features**: Sortable columns, pagination integration

### Chart
- **Install**: `npx shadcn@latest add chart`
- **Usage**: Data visualizations
- **Types**: Bar, Line, Pie, Area charts
- **Library**: Recharts

### Avatar
- **Install**: `npx shadcn@latest add avatar`
- **Usage**: User profile images
- **Features**: Fallback text, image loading states
- **Components**: Avatar, AvatarImage, AvatarFallback

### Carousel
- **Install**: `npx shadcn@latest add carousel`
- **Usage**: Image/content slider
- **Features**: Auto-play, navigation arrows, dots
- **Library**: embla-carousel-react

### Aspect Ratio
- **Install**: `npx shadcn@latest add aspect-ratio`
- **Usage**: Maintain aspect ratio for images/videos
- **Common ratios**: 16/9, 4/3, 1/1

### Calendar
- **Install**: `npx shadcn@latest add calendar`
- **Usage**: Date selection calendar
- **Features**: Single/multi-select, disabled dates, range selection
- **Library**: react-day-picker

### Data Table
- **Install**: Via Table component + TanStack Table
- **Usage**: Advanced tables with sorting, filtering, pagination
- **Features**: Column resizing, row selection, server-side data

### Markdown Preview
- **Install**: Custom implementation
- **Usage**: Render markdown content
- **Libraries**: react-markdown, remark plugins

### Image Gallery
- **Install**: Combination of Dialog + Carousel
- **Usage**: Lightbox image viewer
- **Features**: Thumbnails, full-screen view, navigation

## Miscellaneous Components (4)

### Toggle
- **Install**: `npx shadcn@latest add toggle`
- **Usage**: Button with pressed/unpressed state
- **Variants**: default, outline
- **Use Cases**: Text formatting, view toggles

### Toggle Group
- **Install**: `npx shadcn@latest add toggle-group`
- **Usage**: Group of toggle buttons
- **Features**: Single or multiple selection

### Pagination
- **Install**: `npx shadcn@latest add pagination`
- **Usage**: Navigate between pages
- **Components**: PaginationContent, PaginationItem, PaginationLink, PaginationNext, PaginationPrevious

### Collapsible
- **Install**: `npx shadcn@latest add collapsible`
- **Usage**: Show/hide content section
- **Features**: Controlled expand/collapse, animation

---

## Component Composition Examples

### Authentication Form
Components needed:
- Form + Input + Button + Label
- Card (optional wrapper)
- Toast (for error messages)

### Dashboard Layout
Components needed:
- Sidebar + Navigation Menu
- Card + Chart
- Table + Pagination
- Avatar + Dropdown Menu

### Settings Page
Components needed:
- Tabs (for sections)
- Form + Input + Switch + Select
- Button + Alert Dialog (for destructive actions)
- Toast (for save confirmation)

### E-commerce Product Page
Components needed:
- Carousel (product images)
- Button + Badge
- Accordion (product details)
- Dialog (add to cart confirmation)
- Toast (cart notification)

---

## Installation Tips

**Install multiple related components at once:**
```bash
# Complete form setup
npx shadcn@latest add form input button label select checkbox

# Dialog with form
npx shadcn@latest add dialog form input button

# Dashboard components
npx shadcn@latest add card table pagination chart

# Navigation setup
npx shadcn@latest add sidebar navigation-menu breadcrumb
```

**Check installed components:**
Look in your `components/ui` directory or check `components.json`.

**Update a component:**
Re-run the add command. Note: This will overwrite customizations unless you use git to manage changes.

---

## Finding Components

**By Use Case:**
- Need a button? → `button`
- Need user input? → `input`, `textarea`, `select`, `combobox`
- Need a modal? → `dialog`, `sheet`, `alert-dialog`
- Need notifications? → `toast`, `sonner`, `alert`
- Need navigation? → `sidebar`, `navigation-menu`, `tabs`, `breadcrumb`
- Need to display data? → `table`, `data-table`, `card`
- Need loading states? → `skeleton`, `spinner`, `progress`

**By Interaction Pattern:**
- Click to open → `dialog`, `popover`, `dropdown-menu`
- Hover to show → `tooltip`, `hover-card`
- Right-click → `context-menu`
- Swipe (mobile) → `drawer`, `sheet`
- Toggle state → `switch`, `toggle`, `checkbox`

**By Complexity:**
- Simple → `button`, `input`, `label`, `badge`, `separator`
- Medium → `card`, `dialog`, `dropdown-menu`, `tabs`
- Complex → `form`, `data-table`, `command`, `calendar`
