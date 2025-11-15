# AGENTS.md - Project Overview

This document provides a comprehensive overview of the `cdn` project, which serves as a knowledge base and configuration hub for a suite of AI agents. The repository contains a collection of markdown files that define the behavior, rules, and operational guidelines for these agents.

## Directory Overview

The project is structured to provide contextual information to agents, ensuring they perform tasks according to predefined standards and instructions. It is not a traditional software project with source code, but rather a configuration and documentation repository.

## Key Files and Directories

- **`INDEX.md`**: This is the central index for the repository. It provides a high-level overview of all the important documents and explains when each should be used by an agent.

- **`agents/`**: This directory contains the core instructional documents for the different AI agent personas:
  - `developer.md`: Defines the behavior, principles, and workflow for the full-stack developer agent.
  - `code-reviewer.md`: Outlines the principles, process, and standards for the code reviewer agent, with a strong emphasis on security and simplicity.
  - `researcher.md`: Describes the capabilities and methodology for the research agent, focusing on gathering and synthesizing technical information.

- **`rules/`**: This directory establishes the standards and conventions that the agents should follow:
  - `code-quality-standards.md`: Defines the standards for writing clean, readable, and maintainable code.
  - `commit-standards.md`: Specifies the format for commit messages.
  - Other files in this directory provide further rules on design principles, security, and research methodology.

- **`guides/`**: This directory contains specific guides for various technologies and tasks that the agents might encounter, such as working with React, shell tools, or ffmpeg.

- **`schema/`**:
  - `gemini-cli.json`: This file contains the JSON schema for the Gemini CLI's settings, defining the structure and available options for configuring the tool.

## Usage

The files in this repository are intended to be used as context for the Gemini CLI. When the CLI is running in this directory, it will use the information in these files to inform the behavior of the AI agents. This allows for a high degree of customization and ensures that the agents' outputs are consistent with the project's standards and goals.
