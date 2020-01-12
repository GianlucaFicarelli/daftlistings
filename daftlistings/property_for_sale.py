from daftlistings.listing import Listing


class PropertyForSale(Listing):
    def __init__(self, data_from_search=None, url=None, debug=False):
        super().__init__(data_from_search, url, debug)

    @property
    def formalised_address(self):
        if self.data_from_search:
            t = self.data_from_search.find(
                "a", {"class": "PropertyInformationCommonStyles__addressCopy--link"}
            )
            address = t.text
        else:
            address = self._ad_page_content.find(
                "h1", {"class": "PropertyMainInformation__address"}
            ).text.strip()

        s = address.split("-")
        a = s[0].strip()
        if "SALE AGREED" in a:
            a = a.split()
            a = a[3:]
            a = " ".join([str(x) for x in a])
        return a.lower().title().strip()

    @property
    def price(self):
        if self.data_from_search:
            price = self.data_from_search.find(
                "strong", {"class": "PropertyInformationCommonStyles__costAmountCopy"}
            ).text
        else:
            price = self._ad_page_content.find(
                "strong", {"class": "PropertyInformationCommonStyles__costAmountCopy"}
            ).text

        price = price[1:]
        price = price.replace(",", "")
        price = price.split()
        price = price[0]
        return int(price)
