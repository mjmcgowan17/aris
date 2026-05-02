# AGENTS.md

## Cursor Cloud specific instructions

### Overview
This is a single-file Python application (`agent.py`) that builds an AI research assistant using the Claude Agents SDK + Composio. The agent uses Composio's `WebSearch` and `WebFetch` tools via an MCP server to search the web.

### Running the application
```bash
source .venv/bin/activate
python agent.py
```

### Required environment variables
- `COMPOSIO_API_KEY` — Composio API key (required for Composio tool routing)
- `ANTHROPIC_API_KEY` — Anthropic API key (required by the Claude Agents SDK for LLM calls)

Both must be set before running `agent.py`. Without them, the app exits immediately with an `ApiKeyNotProvidedError` (Composio) or auth error (Anthropic).

### Dependencies
All Python dependencies are installed via `pip install composio-claude-agent-sdk`, which pulls in `composio`, `claude-agent-sdk`, and transitive deps. The virtual environment lives at `.venv/`.

### Gotchas
- `python3.12-venv` system package is required to create the venv on Ubuntu; the update script handles venv creation.
- The `claude-agent-sdk` wheel is ~60 MB because it bundles the Claude Code CLI binary.
- There are no tests, no linter config, and no build step in this repo — the entire app is a single `agent.py`.
