class MultiDict(dict):
    """
    Input should be dict with tuple as keys
    also, case insensitive
    """

    def __getitem__(self, item):
        if type(item) is tuple:
            return super().__getitem__(item)
        for key, d_item in self.items():
            key = list(map(str.lower, key))
            if item.lower() in key:
                return d_item
        else:
            raise KeyError("No such key '{}'".format(item))

    def __setitem__(self, key, value):
        if type(key) is tuple:
            super().__setitem__(key, value)
        else:
            for d_key, d_item in self.items():
                keys = list(map(str.lower, d_key))
                if key.lower() in keys:
                    super().__setitem__(d_key, value)

    def __contains__(self, item):
        if type(item) is tuple or type(item) is list:
            for i_key in item:
                for key, d_item in self.items():
                    key = list(map(str.lower, key))
                    if i_key.lower() in key:
                        return True
            return True
        for key, d_item in self.items():
            key = list(map(str.lower, key))
            if item.lower() in key:
                return True
        else:
            return False
