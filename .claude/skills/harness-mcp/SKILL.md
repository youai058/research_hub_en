---
name: harness-mcp
description: "Register / toggle / debug MCP servers. .mcp.json (repo) + ~/.claude.json (user), stdio/sse/http, settings.json flags enableAllProjectMcpServers / disabled / enabled. Triggers: 'add MCP server', 'connect external tool', '.mcp.json', 'disable MCP', 'stdio server', 'http MCP'."
---

# Harness MCP Manager

MCP is the protocol that exposes external tool servers to Claude Code as **tools**. Manage registration and toggling separately.

## Registration locations

| File | Scope | Note |
|---|---|---|
| `{project}/.mcp.json` | project | git-committable; team-shared servers |
| `~/.claude.json` | user global | personal servers (project-independent) |

## Server types

### stdio (local process)

```json
{
  "mcpServers": {
    "my-server": {
      "type": "stdio",
      "command": "/usr/bin/node",
      "args": ["/path/to/server.js"],
      "env": {"API_KEY": "xxx"}
    }
  }
}
```

- Most common. Server speaks JSON-RPC over stdin/stdout.
- Do not put secrets here; put only the env-var name in `env` and the real value in `settings.local.json` or a host env var.

### SSE (remote)

```json
{
  "mcpServers": {
    "remote-sse": {
      "type": "sse",
      "url": "https://example.com/mcp"
    }
  }
}
```

### HTTP (remote)

```json
{
  "mcpServers": {
    "remote-http": {
      "type": "http",
      "url": "https://example.com/mcp"
    }
  }
}
```

## Toggle — settings.json

Registering in `.mcp.json` and enabling it are separate. In settings.json:

```json
{
  "enableAllProjectMcpServers": true,
  "disabledMcpjsonServers": ["my-server"],
  "enabledMcpjsonServers": []
}
```

- `enableAllProjectMcpServers`: permit every server in `.mcp.json` by default. For security, **keep the default false** and opt in explicitly.
- `disabledMcpjsonServers` / `enabledMcpjsonServers`: per-server toggles.

## Authoring steps

1. **Secret scan**: check the server config to be added for plaintext secrets; if present, extract to an env var
2. Read `.mcp.json` → add the new server to the `mcpServers` object → revalidate JSON
3. If needed, edit the settings.json toggle via the `harness-settings` skill
4. Check git status: if `.mcp.json` is already tracked, review the commit scope and re-verify no secret leakage
5. Tell the user: "server registered; restart the session and verify with `/mcp`"

## Debugging

- Server missing from the list → verify `.mcp.json` JSON parses; verify settings toggle
- Server listed but tool calls fail → check the stdio server's stderr logs; verify `env` var propagation
- Permission prompt every time → add the MCP tool to `permissions.allow` in settings.json

## Security principles

- `.mcp.json` contains **executable command paths**. When committed to the repo, teammates will run the same path — consider that
- Untrusted MCP servers: set `enableAllProjectMcpServers: false` and permit explicitly
- Never put API keys / tokens in plaintext in `.mcp.json`. Use `env` + `settings.local.json` combination

## Checklist

- [ ] `.mcp.json` JSON is valid
- [ ] Server type specified (`stdio` / `sse` / `http`)
- [ ] No plaintext secrets
- [ ] git status checked (notify user if committable)
- [ ] settings.json toggle policy decided
- [ ] After registration, advise user to verify with `/mcp`
