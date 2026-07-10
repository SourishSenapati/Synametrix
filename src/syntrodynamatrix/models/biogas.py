from typing import Dict
from .exceptions import ThermodynamicViolationError

class BiogasUpgrader:
    """Models the energetic viability of upgrading biogas via microalgal sparging."""
    
    # Constants
    METHANE_LHV_MJ_PER_KG = 50.0  # Lower Heating Value of Methane (MJ/kg)
    METHANE_DENSITY_KG_PER_M3 = 0.717  # at STP
    COMPRESSOR_EFFICIENCY = 0.65  # Isentropic efficiency of standard gas blowers
    
    def __init__(self, gas_flow_m3_hr: float, target_kla: float = 30.0):
        if gas_flow_m3_hr <= 0:
            raise ValueError("Gas flow must be strictly positive.")
        self.gas_flow_m3_hr = gas_flow_m3_hr
        self.target_kla = target_kla
        
    def calculate_compression_energy(self, pressure_bar: float) -> float:
        """
        Calculates the energy required (in kW) to compress the biogas to the target pressure.
        """
        if pressure_bar <= 1.0:
            return 0.0
            
        # Simplified for isothermal/adiabatic estimation for Roots blowers
        power_kw = (self.gas_flow_m3_hr * 0.015 * (pressure_bar - 1.0)) / self.COMPRESSOR_EFFICIENCY
        return power_kw
        
    def evaluate_viability(self, methane_fraction: float, pressure_required_bar: float) -> Dict[str, float]:
        """
        Evaluates if the energy spent on compression exceeds the energy gained in the purified methane.
        """
        if not (0.0 < methane_fraction <= 1.0):
            raise ValueError("Methane fraction must be between 0 and 1.")
            
        compression_power_kw = self.calculate_compression_energy(pressure_required_bar)
        compression_energy_mj_per_hr = compression_power_kw * 3.6  # 1 kWh = 3.6 MJ
        
        # Methane energy content
        methane_flow_m3_hr = self.gas_flow_m3_hr * methane_fraction
        methane_mass_kg_hr = methane_flow_m3_hr * self.METHANE_DENSITY_KG_PER_M3
        methane_energy_mj_per_hr = methane_mass_kg_hr * self.METHANE_LHV_MJ_PER_KG
        
        net_energy_mj_per_hr = methane_energy_mj_per_hr - compression_energy_mj_per_hr
        
        if net_energy_mj_per_hr <= 0:
            raise ThermodynamicViolationError(
                f"Net energy is negative ({net_energy_mj_per_hr:.2f} MJ/hr). "
                f"Compression requires more energy than the methane contains."
            )
            
        return {
            "compression_power_kw": round(compression_power_kw, 2),
            "compression_energy_mj_hr": round(compression_energy_mj_per_hr, 2),
            "methane_energy_mj_hr": round(methane_energy_mj_per_hr, 2),
            "net_energy_mj_hr": round(net_energy_mj_per_hr, 2),
            "energy_return_on_investment_eroi": round(methane_energy_mj_per_hr / max(compression_energy_mj_per_hr, 0.001), 2)
        }
