"""Modelos."""

class Votante:
    """Clase votante."""
    def __init__(self, address, name, email, locality, center):
        """Init method."""
        self.address = address
        self.name = name
        self.email = email
        self.locality = locality
        self.center = center

    def __str__(self):
        """String method."""
        return f"{self.name}: {self.address}"

    def __repr__(self):
        """Representation method."""
        return repr(str(self))

class Candidato:
    """Clase candidato."""
    def __init__(self, votante, index):
        """Init method."""
        self.votante = votante
        self.index = index

    def __str__(self):
        """String method."""
        return f"{str(self.votante)}: {self.index}"

    def __repr__(self):
        """Representation method."""
        return repr(str(self))
