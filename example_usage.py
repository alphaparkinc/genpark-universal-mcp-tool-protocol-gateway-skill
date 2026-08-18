from client import UniversalMcpToolProtocolGatewayClient

def main():
    client = UniversalMcpToolProtocolGatewayClient()
    tool_def = {"name": "query_database", "description": "Execute read-only SQL queries"}
    res = client.wrap_tool_as_mcp(tool_def)
    print(f"Gateway Active: {res['gateway_active']}")
    print(f"Tools Exposed: {res['exposed_tools_count']}")
    print("MCP Server Config:")
    print(res["mcp_server_config_json"])

if __name__ == "__main__":
    main()
