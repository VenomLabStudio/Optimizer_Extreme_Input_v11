import math

def calculate_optimal_x(n, s, R1_in, R1_out, R2_in, R2_out):
    # Step 1: Compute k
    k = (n - s) * n * R2_in + (n - s)**2 * R1_out
    
    # Step 2: Compute coefficients a, b, c
    a = k**2
    b = 2 * n**2 * R1_in * R2_in * k
    c = (n**4 * R1_in**2 * R2_in**2) - ((n - s)**2 * n**2 * R1_in * R2_in * R1_out * R2_out)
    
    # Step 3: Compute discriminant
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        raise ValueError("Discriminant is negative. No real solution exists.")
    
    # Step 4: Compute optimal x*
    x_star = (-b + math.sqrt(discriminant)) / (2 * a)
    
    # Step 5: Compute expected profit
    y = (n - s) * R2_out * x_star / (n * R2_in + (n - s) * x_star)
    profit = y - x_star

    return x_star, profit

# Example scenario values
n = 1000
s = 3
R1_in = 100 * 10**18
R1_out = 1000 * 10**18
R2_in = 1000 * 10**18
R2_out = 200 * 10**18

# Run calculation
x_star, profit = calculate_optimal_x(n, s, R1_in, R1_out, R2_in, R2_out)

# Print results
print(f"Optimal Input Amount (x*): {x_star:.6e}")
print(f"Expected Arbitrage Profit: {profit:.6e}")
