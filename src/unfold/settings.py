from django.conf import settings

CONFIG_DEFAULTS = {
    "SITE_TITLE": None,
    "SITE_HEADER": None,
    "SITE_URL": "/",
    "SITE_ICON": None,
    "SITE_SYMBOL": None,
    "SITE_LOGO": None,
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "FIELDSET_CLASSES": ['tab'],
    "IS_SHOW_INLINES_IN_TAB": True,
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "DASHBOARD_CALLBACK": None,
    "ENVIRONMENT": None,
    "STYLES": [],
    "SCRIPTS": [],
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": {},
    },
    "TABS": [],
    "LOGIN": {
        "image": None,
        "redirect_after": None,
    },
    "EXTENSIONS": {"modeltranslation": {"flags": {}}},
}


def get_config(settings_name=None):
    if settings_name is None:
        settings_name = "UNFOLD"

    return {**CONFIG_DEFAULTS, **getattr(settings, settings_name, {})}
