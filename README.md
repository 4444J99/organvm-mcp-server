# ORGANVM MCP Server

[![CI](https://github.com/meta-organvm/organvm-mcp-server/actions/workflows/ci.yml/badge.svg)](https://github.com/meta-organvm/organvm-mcp-server/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Exposes the full ORGANVM system context, graph, metrics, and governance tools to any Claude Code session or Model Context Protocol (MCP) client.

## Overview

The `organvm-mcp-server` is a core system infrastructure component that allows AI assistants working in *any* repository (within or outside the 8-organ system) to query live metadata about the entire ecosystem via standard stdio JSON-RPC transport.

It provides a unified interface to:
- **Registry & Organs**: Repository metadata, status, promotion pipelines, and tier classifications.
- **Seeds & Edges**: Automation contracts, produces/consumes data edges, and event catalogs.
- **Dependency Graph**: Inter-organ relationships, unidirectional flow rules, and blast radius analysis.
- **System Health & Omega Criteria**: Real-time health metrics, CI status, and transition progress.
- **Context & Session Memory**: Working directory context, shared cross-agent memory, and SOP discovery.
- **Corpus & Ontologia**: Knowledge graph concepts, entity resolution, and structural registry.

---

## One-Command Verification

To verify that `organvm-mcp-server` is correctly installed and ready to serve tools:

```bash
organvm-mcp --verify
```

Expected output:
```text
organvm-mcp v0.1.0: 142 tools registered successfully.
```

---

## Installation

### Local / Editable Installation
```bash
git clone https://github.com/meta-organvm/organvm-mcp-server.git
cd organvm-mcp-server
pip install -e ".[dev]"
```

Or build and install wheel locally:
```bash
python -m build
pip install dist/organvm_mcp_server-0.1.0-py3-none-any.whl
```

---

## Endpoint & Authentication Setup

`organvm-mcp-server` operates locally using standard `stdio` transport. No external auth token or network port configuration is required for standard stdio usage.

### Claude Code Configuration

Add `organvm` to your `~/.claude/mcp.json` (or project `.claude/mcp.json`):

```json
{
  "mcpServers": {
    "organvm": {
      "command": "organvm-mcp",
      "args": []
    }
  }
}
```

If using a specific virtual environment, specify the full executable path:

```json
{
  "mcpServers": {
    "organvm": {
      "command": "/path/to/venv/bin/organvm-mcp",
      "args": []
    }
  }
}
```

### Cursor / Windsurf / Other MCP Clients

Configure as a stdio server:
- **Server Name**: `organvm`
- **Command**: `organvm-mcp`
- **Transport**: `stdio`

### Environment Variables (Optional)

| Variable | Description | Default |
|----------|-------------|---------|
| `ORGANVM_ROOT` | Path to the workspace root directory | Auto-detected from working directory |
| `ORGANVM_REGISTRY_PATH` | Path to `registry-v2.json` | Relative to workspace root |

---

## Tools Provided

142 total tools organized across domain modules:

- `organvm_get_context`: **Primary Context Tool** — Auto-detects working directory and returns repo, organ, edge, and governance details.
- `organvm_query_registry`: Search and filter repositories by organ, tier, or status.
- `organvm_get_repo`: Retrieve details for a specific repository.
- `organvm_list_organs`: Summary statistics for all 8 system organs.
- `organvm_get_seed` / `organvm_find_edges`: Read automation contracts and trace produces/consumes data streams.
- `organvm_trace_dependencies`: Upstream and downstream dependency graph traversal.
- `organvm_system_health` / `organvm_omega_status`: High-level system health metrics and transition progress.
- `organvm_governance_audit` / `organvm_check_dependency`: Enforce governance policies and unidirectional flow rules.
- `organvm_pulse_mood` / `organvm_pulse_briefing`: System sentiment and cross-session briefing.
- `organvm_sop_discover` / `organvm_sop_resolve`: Discover and resolve applicable SOPs.

---

## Development & Testing

Run unit tests and verification:

```bash
# Run pytest test suite
pytest tests/ -v

# Run lint checks
ruff check src/ tests/

# Run type checks
pyright src/

# Run via MCP inspector
mcp dev src/organvm_mcp/server.py
```

---

## License

[MIT](LICENSE)
