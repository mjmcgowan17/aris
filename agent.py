# agent.py — Claude Agents SDK + Composio

import asyncio
from composio import Composio
from composio_claude_agent_sdk import ClaudeAgentSDKProvider
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, create_sdk_mcp_server

composio = Composio(provider=ClaudeAgentSDKProvider())
user_id = "user_8pbwb"

# Create a tool router session
session = composio.create(user_id=user_id)
tools = session.tools()
print(f"[composio] {len(tools)} tools: {[t.name for t in tools][:10]}")
custom_server = create_sdk_mcp_server(name="composio", version="1.0.0", tools=tools)

async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are a helpful assistant",
        permission_mode="bypassPermissions",
        mcp_servers={
            "composio": custom_server,
        },
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query("Search my Notion workspace for pages about 'quarterly planning' and summarize the top 3.")
        async for msg in client.receive_response():
            print(msg)

asyncio.run(main())
