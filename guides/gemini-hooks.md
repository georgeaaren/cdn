The Gemini CLI provides a powerful and extensible command-line hooks system that allows you to inject custom logic at various lifecycle events. These hooks can execute external scripts or programs, enabling deep customization of the CLI's behavior. Hook configurations are managed in your [`settings.json`](%2Fgoogle-gemini%2Fgemini-cli%2FREADME.md#L321) file under the [`hooks`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fconfig%2FsettingsSchema.ts#L1354) property.

Here's a comprehensive guide to configuring hooks, covering every top-level event key and providing examples.

### Hook Event Types

The available top-level keys within the [`hooks`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fconfig%2FsettingsSchema.ts#L1354) object correspond to specific lifecycle events in the CLI's operation, as defined by the [`HookEventName`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L23) enumeration in `packages/core/src/hooks/types.ts`. These are: [`BeforeTool`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L24), [`AfterTool`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L25), [`BeforeModel`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L32), [`AfterModel`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L33), [`SessionStart`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L29), [`SessionEnd`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L30), and [`Notification`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L27).

Each event key expects an array of [`HookDefinition`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L51) objects, which allow for further customization such as a [`matcher`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2FhookPlanner.ts#L79) to filter events, and a [`sequential`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2FhookPlanner.ts#L51) flag to control execution order. Each [`HookDefinition`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L51) then contains an array of [`HookConfig`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L46) objects, specifying the actual command to run.

### Global Hook Structure in [`settings.json`](%2Fgoogle-gemini%2Fgemini-cli%2FREADME.md#L321)

```json
{
  "hooks": {
    "BeforeTool": [
      {
        "matcher": "glob_pattern_or_tool_name",
        "sequential": false,
        "hooks": [
          {
            "type": "command",
            "command": "path/to/script.sh",
            "timeout": 60000,
            "args": ["arg1", "arg2"],
            "env": {
              "MY_ENV_VAR": "value"
            },
            "cwd": "./"
          }
        ]
      }
    ],
    "AfterTool": [],
    "BeforeModel": [],
    "AfterModel": [],
    "SessionStart": [],
    "SessionEnd": [],
    "Notification": []
  }
}
```

### Hook Configuration Details

A [`HookDefinition`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L51) can contain:

- **[`matcher`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2FhookPlanner.ts#L79)**: (Optional, string) A glob pattern (e.g., [`run_shell_command`](%2Fgoogle-gemini%2Fgemini-cli%2Fdocs%2Ftools%2Fshell.md#L1), [`git*`](%2Fgoogle-gemini%2Fgemini-cli%2FCONTRIBUTING.md#L176), [`mcp-server__*`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fconfig%2Fpolicy-engine.integration.test.ts#L300)) to match against event-specific data. For [`BeforeTool`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L24) and [`AfterTool`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L25), this matches the tool's name. For other events, its application may vary or be non-existent.
- **[`sequential`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2FhookPlanner.ts#L51)**: (Optional, boolean, default [`false`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fconfig%2Fconfig.ts#L381)) If [`true`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fconfig%2Fconfig.ts#L558), the [`hooks`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fconfig%2FsettingsSchema.ts#L1354) within this definition will run one after another. The output of one hook is passed as input to the next. If [`false`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fconfig%2Fconfig.ts#L381), they run in parallel.
- **[`hooks`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fconfig%2FsettingsSchema.ts#L1354)**: (Required, array) An array of [`HookConfig`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L46) objects. Currently, only the [`command`](%2Fgoogle-gemini%2Fgemini-cli%2Fintegration-tests%2Ftest-helper.ts#L357) type is detailed.

A [`CommandHookConfig`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L40) (where [`"type": "command"`](%2Fgoogle-gemini%2Fgemini-cli%2FROADMAP.md#L35)) specifies:

- **[`command`](%2Fgoogle-gemini%2Fgemini-cli%2Fintegration-tests%2Ftest-helper.ts#L357)**: (Required, string) The command or script to execute.
- **[`timeout`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcli%2Fsrc%2Fcommands%2Fmcp%2Fadd.ts#L33)**: (Optional, number, default [`60`](%2Fgoogle-gemini%2Fgemini-cli%2FREADME.md#L18) seconds) Maximum execution time in milliseconds.
- **[`args`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fcore%2Fturn.ts#L371)**: (Optional, array of strings) Additional command-line arguments to pass to the command.
- **[`env`](%2Fgoogle-gemini%2Fgemini-cli%2Fscripts%2Flint.js#L121)**: (Optional, object) Environment variables to set for the command's process.
- **[`cwd`](%2Fgoogle-gemini%2Fgemini-cli%2Fscripts%2Fstart.js#L32)**: (Optional, string) The working directory for the command.

### Examples for Each Top-Level Key

Here are examples demonstrating how to use each top-level hook event in your [`settings.json`](%2Fgoogle-gemini%2Fgemini-cli%2FREADME.md#L321) file.

#### 1. [`SessionStart`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L29) Hook

Triggers at the beginning of a CLI session. Useful for setting up the environment, logging session start, or initializing resources.

**Example:** Log session start and ensure a temporary directory exists.

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo \"CLI session started at $(date)\" >> ~/.gemini_session.log"
          },
          {
            "type": "command",
            "command": "mkdir -p /tmp/gemini_session_data"
          }
        ]
      }
    ]
  }
}
```

#### 2. [`SessionEnd`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L30) Hook

Triggers when a CLI session ends. Ideal for cleanup, logging session duration, or persisting session-specific data.

**Example:** Clean up temporary files created during the session.

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "rm -rf /tmp/gemini_session_data"
          }
        ]
      }
    ]
  }
}
```

#### 3. [`BeforeTool`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L24) Hook

Executes _before_ a tool call is made. This is excellent for validating tool arguments, logging tool usage, or preventing certain actions.

**Example:** Validate [`run_shell_command`](%2Fgoogle-gemini%2Fgemini-cli%2Fdocs%2Ftools%2Fshell.md#L1) usage to ensure no sensitive files are accessed, and restrict [`write_file`](%2Fgoogle-gemini%2Fgemini-cli%2Fdocs%2Findex.md#L61) to specific directories.

```json
{
  "hooks": {
    "BeforeTool": [
      {
        "matcher": "run_shell_command",
        "hooks": [
          {
            "type": "command",
            "command": "./hooks/pre_shell_check.js",
            "timeout": 5000,
            "env": {
              "BLOCKED_PATTERNS": "rm -rf,sudo"
            }
          }
        ]
      },
      {
        "matcher": "write_file",
        "hooks": [
          {
            "type": "command",
            "command": "./hooks/restrict_write.py",
            "timeout": 3000,
            "args": ["--allowed-dir", "/app/src"]
          }
        ]
      }
    ]
  }
}
```

#### 4. [`AfterTool`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L25) Hook

Executes _after_ a tool call has completed (successfully or not). Useful for processing tool output, logging results, or triggering follow-up actions.

**Example:** Process [`read_file`](%2Fgoogle-gemini%2Fgemini-cli%2Fdocs%2Ftools%2Ffile-system.md#L36) output for sensitive information and notify if [`run_shell_command`](%2Fgoogle-gemini%2Fgemini-cli%2Fdocs%2Ftools%2Fshell.md#L1) failed.

```json
{
  "hooks": {
    "AfterTool": [
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "./hooks/scan_file_content.sh",
            "args": ["--sensitive-keywords", "API_KEY,PASSWORD"]
          }
        ]
      },
      {
        "matcher": "run_shell_command",
        "hooks": [
          {
            "type": "command",
            "command": "node ./hooks/log_shell_result.js"
          }
        ]
      }
    ]
  }
}
```

#### 5. [`BeforeModel`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L32) Hook

Executes _before_ a generative model request is sent. This allows for modifying the prompt, injecting context, or transforming the model configuration.

**Example:** Inject dynamic context into the prompt or adjust model temperature based on session state.

```json
{
  "hooks": {
    "BeforeModel": [
      {
        "sequential": true,
        "hooks": [
          {
            "type": "command",
            "command": "./hooks/add_dynamic_context.py"
          },
          {
            "type": "command",
            "command": "./hooks/adjust_model_params.sh",
            "args": ["--session-complexity", "$SESSION_COMPLEXITY_SCORE"]
          }
        ]
      }
    ]
  }
}
```

#### 6. [`AfterModel`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L33) Hook

Executes _after_ the generative model returns a response. Ideal for post-processing model output, extracting information, or logging model interactions.

**Example:** Analyze model response for sentiment or extract key entities.

```json
{
  "hooks": {
    "AfterModel": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python ./hooks/analyze_model_response.py",
            "cwd": "./analysis_scripts"
          }
        ]
      }
    ]
  }
}
```

#### 7. [`Notification`](%2Fgoogle-gemini%2Fgemini-cli%2Fpackages%2Fcore%2Fsrc%2Fhooks%2Ftypes.ts#L27) Hook

Executes when the CLI generates a user-facing notification. This can be used to intercept, log, or even suppress certain UI messages.

**Example:** Log all warning messages to a file.

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "warning",
        "hooks": [
          {
            "type": "command",
            "command": "logger --tag gemini-cli-warning",
            "args": ["$NOTIFICATION_MESSAGE"]
          }
        ]
      }
    ]
  }
}
```

This comprehensive setup allows you to tailor the Gemini CLI's behavior precisely to your development workflow and security requirements. The interaction between the hook system and the Large Language Model (LLM) components is facilitated by a translation layer, ensuring compatibility even if underlying LLM SDK types change, as mentioned in [Extensible Command-Line Hooks System](#gemini-cli-tools-and-extensions-extensible-command-line-hooks-system).
