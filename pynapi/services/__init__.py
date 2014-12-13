class serviceBase(object):
    """ base class for all services - to make your own, just inherit from this one """
    def __init__(self, *args, **kwargs):
        object.__init__(self)

    def get(self, *args, **kwargs):
        pass
