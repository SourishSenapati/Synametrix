import pytest
from syntrodynamatrix.models.lipid import LipidExtractor
from syntrodynamatrix.models.exceptions import ThermodynamicViolationError

def test_lipid_extraction_thermal_trap():
    # 1000kg of wet algae (1% solids) with 40% lipids
    extractor = LipidExtractor(biomass_kg=1000.0, solid_fraction=0.01, lipid_fraction_dry=0.4)
    with pytest.raises(ThermodynamicViolationError):
        extractor.evaluate_thermal_drying()

def test_lipid_extraction_viable_htl():
    # After extreme dewatering (e.g. 25% solids)
    extractor = LipidExtractor(biomass_kg=1000.0, solid_fraction=0.25, lipid_fraction_dry=0.4)
    res = extractor.evaluate_thermal_drying()
    assert res["net_energy_mj"] > 0
