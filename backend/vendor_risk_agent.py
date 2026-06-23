def calculate_vendor_risk(vendor_id):

    high_risk_vendors = [
        "52923",
        "57133",
        "59935"
    ]

    if str(vendor_id) in high_risk_vendors:

        return {
            "vendor_risk": "HIGH",
            "score": 80
        }

    return {
        "vendor_risk": "LOW",
        "score": 20
    }