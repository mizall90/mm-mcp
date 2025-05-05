from mcp.server.fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass
from dotenv import load_dotenv
import httpx
import asyncio
import os

load_dotenv()

@dataclass
class MMContext:
    """Context for the MM MCP server."""
    secret_key: str
    api_base_url: str

@asynccontextmanager
async def mm_lifespan(server: FastMCP) -> AsyncIterator[MMContext]:
    """
    Manages the MM API config lifecycle.
    """
    secret_key = os.getenv("SECRET_KEY") or "07d03abbb611d7aee3d26a0bdbf30fa5e9b41a4b"
    api_base_url = os.getenv("MM_API_BASE_URL") or "http://127.0.0.1:8000/api/mcp-usecase-detail/get_usecase_data/"
    ctx = MMContext(secret_key=secret_key, api_base_url=api_base_url)
    try:
        yield ctx
    finally:
        pass  # Add cleanup if needed

mcp = FastMCP(
    "mm-mcp",
    description="MCP server for MM usecase data retrieval",
    lifespan=mm_lifespan,
    host=os.getenv("HOST", "0.0.0.0"),
    port=os.getenv("PORT", "9000")
)

@mcp.tool()
async def get_usecase_data(ctx: Context) -> str:
    """
    Get the usecase data from the MM API.
    Args:
        ctx: The MCP server provided context which includes MM API config.
    Returns:
        str: The usecase data.
    """
    api_base_url = ctx.request_context.lifespan_context.api_base_url
    secret_key = ctx.request_context.lifespan_context.secret_key
    headers = {"Authorization": f"secret-key {secret_key}", "Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        response = await client.get(api_base_url, headers=headers)
        response.raise_for_status()
        data = response.json()
    # Return the whole results for all usecases
    return str(data)

async def main():
    await mcp.run_sse_async()

if __name__ == "__main__":
    asyncio.run(main())