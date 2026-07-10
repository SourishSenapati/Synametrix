from typing import Dict

class StruviteReactor:
    """Models the chemical OPEX vs Fertilizer Revenue for Struvite precipitation."""
    
    NAOH_COST_PER_KG = 0.50  # EUR/kg
    STRUVITE_VALUE_PER_KG = 0.12  # EUR/kg (120 EUR/tonne)
    
    def __init__(self, flow_m3_day: float, tan_mg_l: float, po4_mg_l: float, alkalinity_meq_l: float):
        if flow_m3_day <= 0 or alkalinity_meq_l < 0:
            raise ValueError("Flow and alkalinity must be positive.")
        self.flow_m3_day = flow_m3_day
        self.tan_mg_l = tan_mg_l
        self.po4_mg_l = po4_mg_l
        self.alkalinity_meq_l = alkalinity_meq_l
        
    def evaluate_economics(self, target_ph: float = 8.5, current_ph: float = 7.5) -> Dict[str, float]:
        """
        Calculates the NaOH required to overcome buffer capacity and compares it to struvite revenue.
        """
        if target_ph <= current_ph:
            return {"net_profit_eur_day": 0.0, "status": "No pH adjustment needed", "is_profitable": True}
            
        # Simplified titration: meq/L of base needed is roughly proportional to alkalinity and delta pH
        meq_base_needed_per_l = self.alkalinity_meq_l * 0.4 * (target_ph - current_ph) 
        
        # 1 meq NaOH = 40 mg NaOH
        naoh_mg_l = meq_base_needed_per_l * 40.0
        naoh_kg_day = (naoh_mg_l * self.flow_m3_day * 1000) / 1e6
        naoh_cost_day = naoh_kg_day * self.NAOH_COST_PER_KG
        
        # Struvite produced (assuming P is the limiting reagent)
        # Stoichiometric mass ratio: 245.4 / 30.97 = 7.92 kg struvite per kg P.
        p_kg_day = (self.po4_mg_l * self.flow_m3_day * 1000) / 1e6
        struvite_kg_day = p_kg_day * 7.92
        struvite_revenue_day = struvite_kg_day * self.STRUVITE_VALUE_PER_KG
        
        net_profit = struvite_revenue_day - naoh_cost_day
        
        return {
            "naoh_demand_kg_day": round(naoh_kg_day, 2),
            "naoh_cost_eur_day": round(naoh_cost_day, 2),
            "struvite_yield_kg_day": round(struvite_kg_day, 2),
            "struvite_revenue_eur_day": round(struvite_revenue_day, 2),
            "net_profit_eur_day": round(net_profit, 2),
            "is_profitable": net_profit > 0
        }
