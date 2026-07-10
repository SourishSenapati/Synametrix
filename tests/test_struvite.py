import pytest
from synametrix.models.struvite import StruviteReactor

def test_struvite_economic_trap():
    reactor = StruviteReactor(flow_m3_day=1000.0, tan_mg_l=800.0, po4_mg_l=80.0, alkalinity_meq_l=100.0)
    res = reactor.evaluate_economics(target_ph=8.5, current_ph=7.5)
    assert not res["is_profitable"], "High alkalinity digestate should not be profitable with pure NaOH."
    assert res["net_profit_eur_day"] < 0
