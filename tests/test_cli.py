import sys

from sandhi import cli


def test_cli_basic_output(capsys):
    """CLI prints sandhi result and returns success."""
    exit_code = cli.main(["ते", "अपि"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "तेऽपि" in captured.out


def test_cli_quiet_output(capsys):
    """CLI --quiet prints only forms."""
    exit_code = cli.main(["--quiet", "ते", "अपि"])
    captured = capsys.readouterr()

    assert exit_code == 0
    # In quiet mode we expect just the form, without numbering or separators.
    lines = [line for line in captured.out.splitlines() if line.strip()]
    assert "तेऽपि" in lines[0]
    assert "|" not in lines[0]

