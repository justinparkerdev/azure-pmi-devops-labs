# ==============================================================================
# Azure & PMI Governance Automation Module
# Framework Standard: Cloud Adoption Framework (CAF)
# Reference: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/
# Architecture Prep: https://telegra.ph/AB-100-Exam-Value-Trends-and-Architecture-Prep-Guide-09-01
# ==============================================================================

resource "azurerm_resource_group" "pmi_governance_rg" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    Environment = "Production"
    ManagedBy   = "Terraform"
    Framework   = "PMI-DevOps-Standard"
  }
}

resource "azurerm_storage_account" "governance_logs" {
  name                     = "stpmigov${var.environment}${var.random_suffix}"
  resource_group_name      = azurerm_resource_group.pmi_governance_rg.name
  location                 = azurerm_resource_group.pmi_governance_rg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  blob_properties {
    versioning_enabled = true
  }

  tags = {
    Compliance = "PMI-Audit-Ready"
  }
}
