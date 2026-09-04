# Nuzul Booking API Safeguard Tool

## Why this tool?
This lightweight Python automation tool was built to prevent release regressions like ticket NZL-217. It targets the core Booking API layer by automatically validating payload integrity before bookings reach the Staff Console or central system.

## What problem does it solve?
It specifically catches bad date logic (inverted dates causing negative stay durations), missing mandatory parameters (empty guest names), and invalid pricing values (SAR 0 totals) by ensuring the API correctly responds with error status codes (e.g., HTTP 400) rather than processing broken requests.

## How to run:
1. Clone this repository:
 git clone https://github.com/wafaalzahrani371-hub/nuzul-qa-api-safeguard.git
   cd nuzul-qa-api-safeguard
