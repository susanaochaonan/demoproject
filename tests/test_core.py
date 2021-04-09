

def test_version():
    from demo import __version__
    assert isinstance(__version__,str)