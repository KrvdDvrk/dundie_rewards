import pytest

from KrvdDvrkDundie.core import load

from .constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_3_people(request):
    """Test function load function."""
    assert len(load(PEOPLE_FILE)) == 3


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    """Test function load function."""
    assert load(PEOPLE_FILE)[0]["name"] == "Jim Halpert"


# No unit uma boa prática: Sempre manter um único assert dentro de cada teste
