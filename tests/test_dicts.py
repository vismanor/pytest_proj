from utils import dicts


def test_get_val():
    assert dicts.get_val({'bye': 'beast'}, 'bye', 'git') == 'beast'
    assert dicts.get_val({'bye': 'beast'}, 'saddy', 'git') == 'git'
    assert dicts.get_val({'bye': 'beast'}, 'bye', 24) == 'beast'
    assert dicts.get_val({'bye': 'beast'}, 1, 24) == 24
