from typing import Dict
from .exceptions import ThermodynamicViolationError

class LipidExtractor:
    """Models the thermodynamic trap of thermally drying microalgae for biofuel."""
    
    LATENT_HEAT_VAPORIZATION_WATER_MJ_KG = 2.26  # MJ/kg at 100C
    LIPID_LHV_MJ_KG = 37.0  # MJ/kg (biodiesel precursor)
    
    def __init__(self, biomass_kg: float, solid_fraction: float, lipid_fraction_dry: float):
        if not (0.0 < solid_fraction <= 1.0):
            raise ValueError("Solid fraction must be between 0 and 1.")
        if not (0.0 <= lipid_fraction_dry <= 1.0):
            raise ValueError("Lipid fraction must be between 0 and 1.")
            
        self.biomass_kg = biomass_kg
        self.solid_fraction = solid_fraction
        self.lipid_fraction_dry = lipid_fraction_dry
        
    def evaluate_thermal_drying(self) -> Dict[str, float]:
        """
        Evaluates if the energy required to evaporate the water exceeds the energy in the extracted lipids.
        """
        water_kg = self.biomass_kg * (1.0 - self.solid_fraction)
        dry_biomass_kg = self.biomass_kg * self.solid_fraction
        
        drying_energy_mj = water_kg * self.LATENT_HEAT_VAPORIZATION_WATER_MJ_KG
        
        lipid_kg = dry_biomass_kg * self.lipid_fraction_dry
        lipid_energy_mj = lipid_kg * self.LIPID_LHV_MJ_KG
        
        net_energy_mj = lipid_energy_mj - drying_energy_mj
        
        if net_energy_mj <= 0:
            raise ThermodynamicViolationError(
                f"Thermal drying is a net-energy sink! "
                f"Evaporating {water_kg:.1f}kg water requires {drying_energy_mj:.1f} MJ, "
                f"but {lipid_kg:.1f}kg of lipids only contain {lipid_energy_mj:.1f} MJ."
            )
            
        return {
            "water_evaporated_kg": round(water_kg, 2),
            "drying_energy_mj": round(drying_energy_mj, 2),
            "lipid_yield_kg": round(lipid_kg, 2),
            "lipid_energy_mj": round(lipid_energy_mj, 2),
            "net_energy_mj": round(net_energy_mj, 2),
            "eroi": round(lipid_energy_mj / max(drying_energy_mj, 0.001), 2)
        }
