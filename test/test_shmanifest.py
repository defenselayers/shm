import pytest
from click.testing import CliRunner
from shmanifest import cli


@pytest.mark.cli
def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['-v', '--user', 'test', '--passwd', 'test'])
    assert result.exit_code == 0
    assert 'Registry:' in result.output
    assert 'https://registry.defenselayers.com/' in result.output
    assert 'ERROR: wrong response from registry' in result.output
