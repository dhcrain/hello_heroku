from hashids import Hashids


def make_short_link(url):
    hashids = Hashids(salt="yabbadabbadooo")
    return hashids.encode(id(url))
