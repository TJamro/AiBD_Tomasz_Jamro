from app import sorting

def test_sorting() :
    got = sorting(["t","testing","tes","te","test","tes"])
    want = ["t","te","tes","tes","test","testing"]

    assert got == want