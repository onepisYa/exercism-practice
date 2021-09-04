def distance(strand_a, strand_b):
    # if len(strand_a) != len(strand_b):
    #     raise ValueError("Lengths don't match")
    assert len(strand_a) == len(strand_b), "Lengths don't match"
    return sum(1 for a, b in zip(strand_a, strand_b) if a != b)
