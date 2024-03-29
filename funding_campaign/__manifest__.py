# Copyright 2024 Elabore ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "funding_campaign",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Stéphan Sainléger",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Create and manage your funding campaigns",
    # any module necessary for this one to work correctly
    "depends": [
        "account",
        "base",
        "crm",
        "product",
        "sale",
        "sale_crm",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/crm_lead.xml",
        "views/sale_order.xml",
        "views/account_move.xml",
        "views/funding_campaign.xml",
        "views/ir_actions_act_window_records.xml",
        "views/ir_ui_menu_records.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}