import pytest
import favorites

def test_favorites():
    assert favorites.get_fav("color") == "red"
