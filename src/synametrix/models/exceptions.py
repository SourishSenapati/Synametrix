class ThermodynamicViolationError(Exception):
    """Raised when a process violates the laws of thermodynamics (e.g., energy out > energy in)."""
    pass
