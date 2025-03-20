import math
import logging
from decimal import Decimal, getcontext

# Set Decimal precision for large BSC values
getcontext().prec = 50  

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def calculate_optimal_x(n, s, R1_in, R1_out, R2_in, R2_out):
    """Calculates the optimal swap input and expected profit with detailed logs."""
    
    try:
        logging.info("Starting calculation for optimal swap input and profit...")

        # Convert to Decimal for precision
        n, s, R1_in, R1_out, R2_in, R2_out = map(Decimal, (n, s, R1_in, R1_out, R2_in, R2_out))

        # Precompute values
        ns = n - s
        n2 = n * n
        ns2 = ns * ns
        k = ns * n * R2_in + ns2 * R1_out

        logging.info(f"Computed k = {k}")

        # Compute coefficients
        a = k * k
        b = 2 * n2 * R1_in * R2_in * k
        c = (n2 * R1_in * R2_in)**2 - (ns2 * n2 * R1_in * R2_in * R1_out * R2_out)

        logging.info(f"Coefficients calculated: a = {a}, b = {b}, c = {c}")

        # Compute discriminant
        discriminant = b * b - 4 * a * c
        logging.info(f"Discriminant = {discriminant}")

        if discriminant < 0:
            logging.error("Discriminant is negative. No real solution exists.")
            return None, None  # No valid solution

        # Compute square root of discriminant safely
        sqrt_discriminant = Decimal(math.sqrt(discriminant))

        # Compute optimal x*
        if a == 0:
            logging.warning("Coefficient 'a' is zero, returning x* = 0")
            x_star = Decimal(0)
        else:
            x_star = (-b + sqrt_discriminant) / (2 * a)

        logging.info(f"Optimal x* computed: {x_star}")

        # Compute expected profit
        denominator = n * R2_in + ns * x_star
        if denominator == 0:
            logging.warning("Denominator is zero, returning profit = 0")
            return float(x_star), 0.0

        y = (ns * R2_out * x_star) / denominator
        profit = y - x_star

        logging.info(f"Estimated Profit: {profit}")

        return float(x_star), float(profit)

    except Exception as e:
        logging.error(f"Error occurred during calculation: {e}")
        return None, None  # Return None in case of an error

# Example scenario values
n = 1000
s = 3
R1_in = 100 * 10**18
R1_out = 1000 * 10**18
R2_in = 1000 * 10**18
R2_out = 200 * 10**18

# Run calculation
x_star, profit = calculate_optimal_x(n, s, R1_in, R1_out, R2_in, R2_out)

# Print results if valid
if x_star is not None:
    print(f"✅ Optimal Input Amount (x*): {x_star:.6e}")
    print(f"💰 Expected Arbitrage Profit: {profit:.6e}")
else:
    print("❌ No valid solution found due to errors.")
