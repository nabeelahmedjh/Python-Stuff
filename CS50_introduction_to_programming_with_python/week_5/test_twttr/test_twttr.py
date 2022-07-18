from twttr import reduce


def main():
    return 0


def test_lowercase():
    assert reduce("twitter") == "twttr"
    assert reduce("mango") == "mng"
    assert reduce("facebook") == "fcbk"


def test_uppercase():
    assert reduce("TWITTER") == "TWTTR"
    assert reduce("MANGO") == "MNG"
    assert reduce("FACEBOOK") == "FCBK"


if __name__ == "__main__":
    main()
