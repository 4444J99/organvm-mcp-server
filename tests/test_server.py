"""Tests for MCP server dispatch and tool registration."""

import asyncio
from unittest.mock import patch

import pytest

from organvm_mcp.server import _DISPATCH, TOOLS, call_tool, main


class TestServerRegistration:
    def test_tools_count(self):
        assert len(TOOLS) == 142

    def test_dispatch_covers_all_tools(self):
        tool_names = {t.name for t in TOOLS}
        dispatch_names = set(_DISPATCH.keys())
        assert tool_names == dispatch_names

    def test_tool_names_prefixed(self):
        for tool in TOOLS:
            assert tool.name.startswith("organvm_"), f"{tool.name} missing prefix"

    def test_call_tool_unknown(self):
        result = asyncio.run(call_tool("nonexistent_tool", {}))
        assert len(result) == 1
        assert "Unknown tool" in result[0].text


class TestServerCLI:
    @pytest.mark.parametrize("flag", ["--verify", "--check", "--version", "-v"])
    def test_main_verify_flags(self, flag, capsys):
        with patch("sys.argv", ["organvm-mcp", flag]), pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "organvm-mcp v0.1.0:" in captured.out
        assert "142 tools registered successfully." in captured.out
