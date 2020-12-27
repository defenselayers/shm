import os
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


@pytest.mark.registry
def test_registry():
    try:
        user = os.environ['TEST_DL_REGUSER']
        passwd = os.environ['TEST_DL_REGPASSWD']
    except KeyError:
        pytest.fail('missing TEST_DL_REGUSER or TEST_DL_REGPASSWD variables to run test')

    runner = CliRunner()
    result = runner.invoke(cli, ['-v', '--user', user, '--passwd', passwd])
    assert result.exit_code == 0
    assert 'Registry:' in result.output
    assert 'https://registry.defenselayers.com/' in result.output
    assert 'latest' in result.output
