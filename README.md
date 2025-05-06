## ModelManager MCP Server

This is a ModelManager MCP server that provides a REST API for ModelManager tools.

### Configuration

```json
{
  "mcpServers": {
    "mm-mcp": {
      "command": "mm-mcp/.venv/bin/mcp",
      "args": ["run", "mm-mcp/server/mm.py"]
    },
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
        "mm-mcp"
      ],
      "env": {
        "SECRET_KEY": "your-secret-key",
        "MM_API_BASE_URL": "your-api-base-url"
      }
    }
  }
}
```
