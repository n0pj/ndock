class BaseParser (object):  # pragma: no cover
    """
    A base parser class
    """

    def parse(self, content):
        """
        :param content: string config content
        :returns: a :class:`..nodes.Node` tree
        """
        return None

    def stringify(self, tree):
        """
        :param tree: a :class:`..nodes.Node` tree
        :returns: string config content
        """
        return None
