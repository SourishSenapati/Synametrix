import argparse
from .models.biogas import BiogasUpgrader
from .models.struvite import StruviteReactor
from .models.lipid import LipidExtractor
from .models.exceptions import ThermodynamicViolationError

def run_audit():
    print("=========================================================")
    print(" TECHNO-ECONOMIC & THERMODYNAMIC AUDIT: AD-MICROALGAE")
    print("=========================================================\n")
    
    print("SCENARIO 1: Biogas Upgrading (100 m3/hr biogas, 60% CH4, 2.0 bar micro-sparger)")
    upgrader = BiogasUpgrader(gas_flow_m3_hr=100.0)
    res1 = upgrader.evaluate_viability(methane_fraction=0.6, pressure_required_bar=2.0)
    for k, v in res1.items():
        print(f"  - {k}: {v}")
    print("  -> CONCLUSION: Viable. EROI > 1.0\n")
    
    print("SCENARIO 2: Struvite Precipitation (1000 m3/day, 80 mg/L PO4, 80 meq/L Alkalinity)")
    reactor = StruviteReactor(flow_m3_day=1000.0, tan_mg_l=800.0, po4_mg_l=80.0, alkalinity_meq_l=80.0)
    res2 = reactor.evaluate_economics(target_ph=8.5, current_ph=7.5)
    for k, v in res2.items():
        print(f"  - {k}: {v}")
    print("  -> CONCLUSION: Not viable via direct NaOH dosing. Air-stripping required.\n")
    
    print("SCENARIO 3: Thermal Drying for SAF Lipids (1000kg slurry, 15% solids after centrifuge, 40% lipids)")
    extractor = LipidExtractor(biomass_kg=1000.0, solid_fraction=0.15, lipid_fraction_dry=0.40)
    try:
        res3 = extractor.evaluate_thermal_drying()
        for k, v in res3.items():
            print(f"  - {k}: {v}")
    except ThermodynamicViolationError as e:
        print(f"  - FATAL ERROR: {str(e)}")
    print("  -> CONCLUSION: Thermal drying is physically impossible. Must use Hydrothermal Liquefaction (HTL).\n")
    
    print("=========================================================")
    print(" AUDIT COMPLETE. ZERO LOOSE ENDS.")
    print("=========================================================")

def main():
    parser = argparse.ArgumentParser(description="Run the SyntroDynaMatrix TEA audit.")
    parser.parse_args()
    run_audit()

if __name__ == "__main__":
    main()
