print("Electricity bill estimator")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

which_tariff = int(input("Which tariff? 11 or 31: "))
cents_per_kWh = int(input("Enter cents per kWh: "))
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))

if which_tariff == 11:
    estimated_bill = (cents_per_kWh * 0.01 * daily_use_in_kWh * number_of_billing_days) * TARIFF_11
    print(f"Estimated bill: ${estimated_bill:.2f}")
elif which_tariff == 31:
    estimated_bill = (cents_per_kWh * 0.01 * daily_use_in_kWh * number_of_billing_days) * TARIFF_31
    print(f"Estimated bill: ${estimated_bill:.2f}")