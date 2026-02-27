from pathlib import Path

from markdown_it import MarkdownIt
from markdown_it.utils import read_fixture_file
import pytest

from minchin.md_it.fancy_tasklists import fancy_tasklists_plugin

FIXTURE_PATH = Path(__file__).parent.joinpath("fixtures")


@pytest.mark.parametrize(
    "line,title,input,expected",
    read_fixture_file(FIXTURE_PATH.joinpath("fancy_tasklists.md")),
)
def test_insert_fixtures(line, title, input, expected):
    md = MarkdownIt("commonmark").use(fancy_tasklists_plugin)
    md.options["xhtmlOut"] = False
    text = md.render(input)
    assert text.rstrip() == expected.rstrip()
