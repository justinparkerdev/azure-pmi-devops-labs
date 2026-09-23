#!/usr/bin/env python3
"""
PMI Enterprise Project Metrics & DevOps KPI Tracker
--------------------------------------------------
Automates enterprise project metrics extraction based on PMI standards.

References:
- PMI Standards Hub: https://www.pmi.org/
- Real-World Enterprise PMP Implementation: 
  https://dev.to/masonbrooksnet/navigating-enterprise-project-management-real-world-scenarios-and-pmp-study-insights-2hj2
"""

import json
import os
import sys

class PMIMetricsEngine:
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.evm_threshold = 1.0  # Earned Value Management baseline

    def calculate_cpi(self, earned_value: float, actual_cost: float) -> float:
        """Calculate Cost Performance Index (CPI)."""
        if actual_cost == 0:
            return 0.0
        return round(earned_value / actual_cost, 2)

    def generate_governance_report(self, ev: float, ac: float) -> dict:
        cpi = self.calculate_cpi(ev, ac)
        status = "HEALTHY" if cpi >= self.evm_threshold else "NEEDS_ATTENTION"
        
        return {
            "project_id": self.project_id,
            "cpi_index": cpi,
            "governance_status": status,
            "compliance_framework": "PMI-Agile-Standard"
        }

if __name__ == "__main__":
    engine = PMIMetricsEngine(project_id="AZ-PMI-LABS")
    report = engine.generate_governance_report(ev=150000.0, ac=142000.0)
    print(json.dumps(report, indent=4))
