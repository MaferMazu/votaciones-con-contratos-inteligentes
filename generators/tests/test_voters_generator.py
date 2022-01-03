from pathlib import Path

from generators.voters_generator import voters_generator

LOCATION = Path(__file__).absolute().parent.parent

def test_voters_generator():
    """Test voters generator."""
    file_path = 'file_examples/sample_localities.txt'
    voters = voters_generator(file_path)
    assert len(voters) == 70
    del voters
