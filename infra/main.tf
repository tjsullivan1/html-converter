terraform {
  backend "remote" {
    organization = "tjssullivanent"

    workspaces {
      name = "html-converter"
    }
  }
}

# Configure the Azure provider
provider "azurerm" {
  version = "= 2.13.0"
  features {}
}

module "webserver" {
  source = "git::https://github.com/tjsullivan1/terraforming.git//modules/services/az-function?ref=v0.2.0"

  env                 = "d"
  name                = "htmlconv"
  resource_group_name = "rg-html-converter-d"
  os                  = "linux"
}