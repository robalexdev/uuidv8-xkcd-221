from uuidv8_xkcd_221 import generate


def test_generate():
    assert str(generate()) == "00000000-0000-8000-8000-000000000004"
