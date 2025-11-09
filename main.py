# Dummy PT project file
import json
import subprocess
from pathlib import Path

mcp_path = Path(".cursor/mcp.json")

if not mcp_path.exists():
    print("File .well-known/mcp.json not found")
    exit(1)

with open(mcp_path, "r", encoding="utf-8") as f:
    mcp = json.load(f)

cmd = None

if "command" in mcp:
    cmd = mcp["command"]
elif "entry" in mcp:
    entry = mcp["entry"]
    runtime = mcp.get("runtime", "")
    if runtime:
        cmd = f"{runtime} {entry}"
    else:
        if entry.endswith(".js"):
            cmd = f"node {entry}"
        elif entry.endswith(".py"):
            cmd = f"python {entry}"
        else:
            cmd = entry

if not cmd:
    print("mcp.json missing 'command' or 'entry'")
    exit(1)

print(f"Running: {cmd}")
subprocess.run(cmd, shell=True)