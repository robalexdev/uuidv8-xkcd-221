import subprocess


def test_main():
    assert subprocess.check_output(["uuidv8-xkcd-221"], text=True) == "00000000-0000-8000-8000-000000000004\n"
