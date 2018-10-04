#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `P1` package."""

import pytest

from click.testing import CliRunner

from P1 import P1
from P1 import cli

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'P1.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

class Test_P1(unittest.TestCase):
	ini_position = P1.ini_position
        vel = P1.vel
        nt = P1.nt
        wall_size = P1.wall_size
        del_t = P1.del_t
        m = P1.m
        T = P1.T
        e = P1.e
        total_t = P1.total_T
	def test_move():
		[a,b,c] = P1.move()
		assert b[-1] == 0.0 or 5.0
		assert b[0] == 0
		assert a[0] == 0
		assert t > 0 and t < nt

	def test_run():
		[a,b] = P1.run()
		assert len(a) == 100
		assert b[1] != 0.0
		assert b[-1] == wall_size

