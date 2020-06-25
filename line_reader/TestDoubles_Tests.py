#!/usr/bin/env python3
from LineReader import readFromFile
from unittest.mock import MagicMock

def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    result = readFromFile("file")
    mock_open.assert_called_once_with("file", "r")
    assert result == "test line"
