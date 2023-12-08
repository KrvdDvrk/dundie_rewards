from subprocess import CalledProcessError, check_output

import pytest
from click.testing import CliRunner

from dundie.cli import load, main

from .constants import PEOPLE_FILE

cmd = CliRunner()


@pytest.mark.integration
@pytest.mark.medium
def test_load_positive_call_load_command():
    """test command load"""
    out = check_output(["dundie", "load", "tests/assets/people.csv"]).decode("utf-8").split("\n")
    # breakpoint
    assert len(out) == 2
    out = cmd.invoke(load, PEOPLE_FILE)
    assert "Dunder Mifflin Associates" in out.output


@pytest.mark.integration
@pytest.mark.medium
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """test command load"""
    with pytest.raises(CalledProcessError) as error:
        check_output(["dundie", "wrong_command", "tests/assets/people.csv"]).decode("utf-8").split(
            "\n"
        )

    assert "status 2" in str(error.getrepr())
    out = cmd.invoke(main, wrong_command, PEOPLE_FILE)
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output
