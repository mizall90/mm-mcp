## ModelManager MCP Server

This is a ModelManager MCP server that provides a REST API for ModelManager tools.

### Configuration For mcp integration on host (g: windsurf, vscode, claude desktop)

#### Local Configuration
```json
{
  "mcpServers": {
    "mm-mcp": {
      "command": "mm-mcp/.venv/bin/mcp",
      "args": ["run", "mm-mcp/server/mm.py"]
    }
  }
}
```

#### Docker Configuration
```json
{
  "mcpServers": {
    "mm-mcp-docker": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "--network=host",
        "-e",
        "SECRET_KEY",
        "-e",
        "MM_API_BASE_URL",
        "modelmanagerdev/mcp:v1"
      ],
      "env": {
        "SECRET_KEY": "your-secret-key",
        "MM_API_BASE_URL": "your-api-base-url"
      }
    }
  }
}
```
