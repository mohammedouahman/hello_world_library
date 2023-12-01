# Test the hellow_world function
from hello_world_library.hello_world import hello_world
def test_hellow_world():
    assert hello_world() == "Hello, World!"
    