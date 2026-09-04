import requests

BASE_URL = "https://restful-booker.herokuapp.com/booking"

def run_tests():
    print("==========================================")
    print("   NUZUL HOSPITALITY - API VALIDATION TEST")
    print("==========================================")
    
    test_cases = [
        {
            "name": "TC-01: Inverted Check-in/Check-out Dates",
            "payload": {
                "firstname": "Fahad",
                "lastname": "Al-Otaibi",
                "totalprice": 250,
                "depositpaid": True,
                "bookingdates": {"checkin": "2026-08-15", "checkout": "2026-08-12"}
            }
        },
        {
            "name": "TC-02: Missing Guest Name",
            "payload": {
                "firstname": "",
                "lastname": "",
                "totalprice": 480,
                "depositpaid": False,
                "bookingdates": {"checkin": "2026-08-16", "checkout": "2026-08-19"}
            }
        },
        {
            "name": "TC-03: Zero Total Price",
            "payload": {
                "firstname": "Omar",
                "lastname": "Haddad",
                "totalprice": 0,
                "depositpaid": True,
                "bookingdates": {"checkin": "2026-08-19", "checkout": "2026-08-22"}
            }
        }
    ]

    failed_count = 0

    for test in test_cases:
        print(f"\nRunning: {test['name']}...")
        try:
            response = requests.post(BASE_URL, json=test['payload'], timeout=10)
            if response.status_code in [200, 201]:
                print(f"❌ FAIL: API accepted invalid payload! (HTTP {response.status_code})")
                failed_count += 1
            else:
                print(f"✅ PASS: API rejected invalid payload properly. (HTTP {response.status_code})")
        except Exception as e:
            print(f"⚠️ ERROR: Request failed due to: {e}")

    print("\n==========================================")
    print(f"TEST SUMMARY: {failed_count} critical issues detected.")
    print("==========================================")

if __name__ == "__main__":
    run_tests()
