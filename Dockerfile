FROM python:3.11-slim

ARG PORT=9000

WORKDIR /mm-mcp

# Install uv
RUN pip install uv

# Copy the MCP server files
COPY . .

# Create and activate venv, install dependencies from pyproject.toml
RUN python -m venv venv \
    && . venv/bin/activate \
    && uv pip install .

ENV PATH="/mm-mcp/venv/bin:$PATH"
ENV VIRTUAL_ENV="/mm-mcp/venv"

EXPOSE ${PORT}

# Command to run the MCP server
CMD ["mcp", "run", "server/mm.py"]