import json
import subprocess
from pathlib import Path

mcp_path = Path(".cursor/rules/mcp.json")

if not mcp_path.exists():
    print(f"File {mcp_path} not found")
    exit(1)

with open(mcp_path, "r", encoding="utf-8") as f:
    mcp = json.load(f)

servers = mcp.get("mcpServers", {})
if not servers:
    print("No mcpServers found in mcp.json")
    exit(1)

name, config = next(iter(servers.items()))
cmd = config.get("command")
args = config.get("args", [])

if not cmd:
    print("No command found in mcp.json")
    exit(1)

full_cmd = [cmd] + args
print(f"Running: {' '.join(full_cmd)}")
subprocess.run(full_cmd)
