# Copyright (c) The SkillPedia under Apache License 2.0 (see LICENSE.txt).
# Source for "Build a Large Language Model From Scratch"
#  
# Code: https://github.com/Sangwan70/Building-an-LLM-From-Scratch
#
# File for internal use (unit tests)

from python_environment_check import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "FAIL" not in captured.out
