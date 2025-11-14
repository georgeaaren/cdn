# REACT.md: A Guide to Modern React (React 19+)

This document outlines best practices and crucial features for developing applications using modern React, focusing primarily on the advancements and breaking changes introduced in React 19 and subsequent minor releases.

---

## 1. Core Architectural Shift: Server Components and Frameworks

React 19 marks a major evolution toward full-stack architecture, emphasizing server-side rendering (SSR) and framework integration.

### Server Components (RSCs)

**Server Components** are designed to run ahead of time, before bundling, on a separate server environment (at build time or per request).

- **Benefit:** They reduce the amount of JavaScript executed on the client, resulting in quicker load times, improved performance, and better initial SEO.
- **Availability:** RSC features, along with Server Actions, are included in the React 19 stable release.
- **Server Actions:** These allow Client Components to call asynchronous functions executed securely on the server, leveraging the `"use server"` directive.

### Framework Recommendation

The React team strongly encourages developers to use a framework due to the subtleties involved in making an application load quickly as it scales.

- Next.js is specifically mentioned as the most complete implementation for data fetching with Suspense and for running bleeding-edge React features.

---

## 2. Performance and Optimization: The React Compiler

The React Compiler aims to solve the complexity of manual memoization by automatically optimizing components and addressing performance issues caused by cascading re-renders.

### Compiler Functionality

The experimental **React Compiler** plugs into the build system, grabbing component code and converting it into code where components, props, and hook dependencies are memoized by default.

- This process effectively achieves results similar to wrapping everything in `React.memo`, `useMemo`, or `useCallback`.
- **Automatic Optimization:** The compiler automatically optimizes components, reducing the need for manual memoization, which was previously considered difficult to use correctly.

### Best Practices (Post-Compiler Installation)

While the Compiler aims to make memoization automatic, manual attention is still necessary, especially for complex real-world codebases, where the compiler might only fix a fraction of observable re-renders.

- **Do Not Forget Manual Memoization:** Developers cannot yet forget about `React.memo`, `useMemo`, and `useCallback`. They may still be necessary or useful for debugging unexpected re-renders.
- **Optimize Component Structure:** To enable better Compiler performance:
  - **Extract Hooks:** Extract non-memoized return values from complex hooks (e.g., extract `mutate` from the object returned by `useMutation`) and pass the memoized function directly as a dependency.
  - **Isolate Dynamic Lists:** Extract dynamically rendered list items (like table rows) into their own isolated components, passing data via props.
  - **Use Proper Keys:** Ensure unique, stable keys (like `name` or `id`) for elements in dynamic lists, rather than using the array `index`.

---

## 3. New Hooks and APIs (Form Handling and Data Fetching)

React 19 introduces several new hooks focused on simplifying asynchronous operations, form handling, and state management.

| Hook Name                     | Description                                                                                                                                                                                                                                                                                                               | Previous Approach                                                                                                                       |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **`useActionState()`**        | A generalized hook to manage the lifecycle of asynchronous actions (like form submissions or API calls), encapsulating loading, success, and error states into a single return object.                                                                                                                                    | Required multiple manual `useState` variables to track submitting, error, and success states.                                           |
| **`useFormStatus()`**         | Tracks the status of the closest parent `<form>` (e.g., `pending`, `data`, `method`), simplifying the management of UI elements inside the form, such as disabling a submit button during submission.                                                                                                                     | Required drilling state variables (like `isSubmitting`) down to form children.                                                          |
| **`<form>` Actions**          | Allows passing asynchronous functions directly to the `action` or `formAction` props of `<form>`, `<input>`, or `<button>` elements, automatically handling submission using Actions.                                                                                                                                     | Manual `onSubmit` handler required calling `e.preventDefault()`, setting pending state, and handling the async request.                 |
| **`useOptimistic()`**         | Provides an easy way to handle optimistic UI updates, where the UI updates instantly before server confirmation. It automatically reverts the state if the server request fails.                                                                                                                                          | Required complex boilerplate using `useState` and manual error handling to revert state upon failure.                                   |
| **`use()`**                   | Allows direct reading of resources (like promises or Context values) inside components during the render phase, eliminating the need for complex `useEffect`/`useState` management for asynchronous data fetching.                                                                                                        | Asynchronous data fetching required combining `useEffect` and `useState` with manual loading state management.                          |
| **`useEffectEvent()`** (19.2) | Splits "event" logic out of the `useEffect` hook to prevent the Effect from re-running unnecessarily when props or state used inside the event handler change, if those values aren't dependencies of the Effect logic itself. **Event functions created with this hook should not be declared in the dependency array**. | Manual techniques (like wrapping handlers in `useCallback` or suppressing lint errors) were often necessary, sometimes leading to bugs. |
| **`<Activity />`** (19.2)     | Enables breaking the app into logical "activities" (modes: `visible`, `hidden`) to pre-render hidden parts of the application (loading data, CSS, images) in the background without affecting the performance of the visible content.                                                                                     | N/A (New feature for fine-grained concurrent control).                                                                                  |

---

## 4. Migration Guide and Breaking Changes (React 19)

Upgrading to React 19 requires methodical testing and refactoring of deprecated patterns. Running upgrades without reviewing changes often leads to runtime errors.

### A. Pre-Upgrade Steps

1.  **Intermediate Upgrade:** Before migrating to React 19, install **`react@18.3`** to receive warnings about deprecated APIs and other required changes.
2.  **Compatibility Check:** Update critical third-party libraries (e.g., React Router, Redux) to React 19-compatible versions first. Use `npm outdated | grep -E 'react|react-dom'` to check dependency compatibility.
3.  **Required JSX Transform:** The new JSX transform is now mandatory in React 19.

### B. Deprecated and Removed APIs

Many legacy APIs have been removed in React 19 to simplify the codebase.

| Legacy API / Pattern                                           | Replacement / Fix                                                                        | Codemod Command (Recommended)                           |
| :------------------------------------------------------------- | :--------------------------------------------------------------------------------------- | :------------------------------------------------------ |
| **`ReactDOM.render`** and **`ReactDOM.hydrate`**               | Use `ReactDOM.createRoot` and `ReactDOM.hydrateRoot` from `react-dom/client`.            | `npx codemod@latest react/19/replace-reactdom-render`   |
| **`ReactDOM.unmountComponentAtNode`**                          | Use `root.unmount()`.                                                                    | `npx codemod@latest react/19/replace-reactdom-render`   |
| **`ReactDOM.findDOMNode`**                                     | Use callback refs or DOM refs (e.g., `useRef`).                                          | (No specific codemod listed for this replacement)       |
| **`propTypes`** and **`defaultProps`** for function components | Migrate to TypeScript or use ES6 default parameters for function components.             | `npx codemod@latest react/prop-types-typescript`        |
| **String refs**                                                | Migrate to ref callbacks.                                                                | `npx codemod@latest react/19/replace-string-ref`        |
| **Legacy Context** (`contextTypes`, `getChildContext`)         | Migrate to the modern Context API using `React.createContext` and the `contextType` API. | (The primary migration recipe includes context updates) |
| **`element.ref`** access                                       | Use `element.props.ref` instead.                                                         | (No specific codemod listed for this deprecation)       |
| **`ReactDOMTestUtils.act`**                                    | Import `act` directly from the `react` package: `import { act } from 'react'`.           | `npx codemod@latest react/19/replace-act-import`        |
| **`react-test-renderer`**                                      | Migration is recommended to modern testing libraries like `@testing-library/react`.      | (No specific codemod listed for this deprecation)       |
| **UNSAFE Lifecycle Methods** (`componentWillMount`, etc.)      | These are being phased out; rewrite them to safer alternatives like `useEffect`.         | (No specific codemod listed in sources)                 |

### C. Ref Handling and Forwarding

Ref handling rules are stricter in React 19, enforcing type safety.

- **Ref as a Prop:** Function components can now access `ref` directly as a prop, eliminating the need for `React.forwardRef`.

  ```javascript
  // Correct pattern for React 19
  function MyInput({ placeholder, ref }) {
    return <input placeholder={placeholder} ref={ref} />;
  }
  // Usage remains consistent: <MyInput ref={myRef} />
  ```

- **Ref Cleanup Functions:** Ref callbacks now support returning a cleanup function that React calls when the element is removed from the DOM. This replaces the prior behavior of calling refs with `null` upon unmount.
- **Avoiding Implicit Returns in Ref Callbacks:** Due to the cleanup function feature, implicitly returning a value from a ref callback will be rejected by TypeScript (to prevent accidental cleanup function usage).

  ```javascript
  // Before (Implicit return - now rejected)
  // <div ref={current => (instance = current)} />

  // After (Block statement to avoid implicit return)
  <div
    ref={(current) => {
      instance = current;
    }}
  />
  ```

### D. Concurrent Features and Testing

React 19 enables concurrent rendering by default.

- **Testing Concurrent Code:** Use `act()` from React Testing Library for asynchronous tests. Verify `Suspense` fallbacks render correctly.
- **Error Reporting:** React 19 improves error handling by reducing duplicate logs. Errors caught by an Error Boundary are reported to `console.error`; uncaught errors are reported to `window.reportError`. Custom error handling can be configured using `onUncaughtError` and `onCaughtError` options on `createRoot`.

---

## 5. Developer Experience (DX) Enhancements

React 19 includes several features to simplify common development tasks:

- **Document Metadata:** Elements like `<title>`, `<link>`, and `<meta>` can be rendered directly inside components, and React will automatically hoist them to the document's `<head>` section, ensuring compatibility with client-only apps and streaming SSR.
- **Stylesheets Integration:** React manages the insertion order and loading of external stylesheets (`<link rel="stylesheet">`) or inline styles (`<style>`) using the **`precedence`** prop. This ensures styles load before dependent content is revealed, supporting composability within components.
- **Asset Preloading APIs:** New `react-dom` APIs like **`preload`**, **`preinit`**, **`prefetchDNS`**, and **`preconnect`** allow developers to optimize initial page loads and client-side transitions by proactively telling the browser about necessary resources (fonts, scripts, styles).
- **Context as Provider:** You can now render a context object directly as a provider using `<Context value="dark">` instead of the older `<Context.Provider value="dark">`.
- **Custom Elements Support:** React 19 adds full support for Custom Elements, treating unrecognized props as properties rather than attributes, simplifying integration with Web Components.
