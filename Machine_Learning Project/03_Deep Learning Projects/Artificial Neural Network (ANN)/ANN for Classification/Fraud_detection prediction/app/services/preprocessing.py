def encode_device_type(device_type_status):
        return {"device_type_Mobile": 1 if device_type_status == "Mobile" else 0,
                "device_type_Tablet": 1 if device_type_status == "Tablet" else 0}


def encode_device_ip_reputation(device_ip_reputation_status):
        return {"device_ip_reputation_Good": 1 if device_ip_reputation_status == "Good" else 0,
                "device_ip_reputation_Suspicious": 1 if device_ip_reputation_status == "Suspicious" else 0}


def encode_browser(browser_status):
        return {"browser_Edge": 1 if browser_status == "Edge" else 0,
                "browser_Firefox": 1 if browser_status == "Firefox" else 0,
                "browser_Opera": 1 if browser_status == "Opera" else 0,
                "browser_Safari": 1 if browser_status == "Safari" else 0}


def encode_operating_system(operating_system_status):
        return {"operating_system_Linux": 1 if operating_system_status == "Linux" else 0,
                "operating_system_Windows": 1 if operating_system_status == "Windows" else 0,
                "operating_system_iOS": 1 if operating_system_status == "iOS" else 0,
                "operating_system_macOS": 1 if operating_system_status == "macOS" else 0}


def encode_ad_position(ad_position_status):
        return {"ad_position_Side": 1 if ad_position_status == "Side" else 0,
                "ad_position_Top": 1 if ad_position_status == "Top" else 0}
