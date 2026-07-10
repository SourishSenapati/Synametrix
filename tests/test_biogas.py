import pytest
from syntrodynamatrix.models.biogas import BiogasUpgrader
from syntrodynamatrix.models.exceptions import ThermodynamicViolationError

def test_biogas_upgrader_violation():
    upgrader = BiogasUpgrader(gas_flow_m3_hr=100.0)
    with pytest.raises(ThermodynamicViolationError):
        # High pressure compression on poor biogas
        upgrader.evaluate_viability(methane_fraction=0.4, pressure_required_bar=10.0)

def test_biogas_upgrader_viable():
    upgrader = BiogasUpgrader(gas_flow_m3_hr=100.0)
    res = upgrader.evaluate_viability(methane_fraction=0.6, pressure_required_bar=2.0)
    assert res["energy_return_on_investment_eroi"] > 1.0
