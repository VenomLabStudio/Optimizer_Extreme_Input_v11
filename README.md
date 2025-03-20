# Optimizer_Extreme_Input_v11
Prepared and developcalculation by VenomLab Studio

# 2-Hop Arbitrage Formula 📈💰

## Overview  
This formula calculates the **optimal input amount (x\*)** to maximize profit when swapping tokens through **two liquidity pools** using a **Uniswap V2-style AMM (Automated Market Maker)**.

Arbitrage process:

x → R1,in → R1,out → R2,in → R2,out → y

Where:
- **x** = amount put into the first pool  
- **y** = final amount received  
- **R1,in**, **R1,out** = reserves of the first pool  
- **R2,in**, **R2,out** = reserves of the second pool  
- **n = 1000**, **s = 3** (for Uniswap V2, representing a 0.3% swap fee)  

## Formula for Optimal `x*`  
The **optimal input amount (`x*`)** is calculated using the quadratic formula:

\[
x^* = \frac{-b + \sqrt{b^2 - 4ac}}{2a}
\]

Where:

- \( a = k^2 \)
- \( b = 2 n^2 R_{1,in} R_{2,in} k \)
- \( c = n^4 R_{1,in}^2 R_{2,in}^2 - (n-s)^2 n^2 R_{1,in} R_{2,in} R_{1,out} R_{2,out} \)
- \( k = (n-s) n R_{2,in} + (n-s)^2 R_{1,out} \)

## Example Calculation  
Suppose there's a **2x price difference** between the two pools:

n = 1000 s = 3 R1,in = 100 * 10^18 R1,out = 1000 * 10^18 R2,in = 1000 * 10^18 R2,out = 200 * 10^18


By applying the formula, the optimal input amount `x*` is:

x* ≈ 20.5911 × 10^18


And the expected arbitrage profit is:
```
Profit ≈ 8.44176 × 10^18
```


## Validation  
The formula has been **validated using Desmos** and matches expected arbitrage profits, confirming its correctness.

## Next Steps 🚀  
# 2-Hop Arbitrage Formula

## Overview
This document explains the process of executing a 2-hop arbitrage trade, where a token is swapped through two liquidity pools to maximize profit. The goal is to determine the optimal input amount `x` for maximum profit.

### Swap Path:
x → R1,in → R1,out → R2,in → R2,out → y

Where:
- `x` is the initial input amount.
- `y` is the final output amount after swapping through both pools.

---

## Variable Definitions

| Variable  | Description |
|-----------|-------------|
| `x`       | Amount of tokens input into the first pool |
| `y1`      | Amount of tokens received from the first pool |
| `y2`      | Amount of tokens received from the second pool |
| `n`       | 1000 (constant for Uniswap V2) |
| `s`       | 3 (constant for Uniswap V2) |
| `R1,in`   | Reserve of input token in the first pool |
| `R1,out`  | Reserve of output token in the first pool |
| `R2,in`   | Reserve of input token in the second pool |
| `R2,out`  | Reserve of output token in the second pool |

---

## Formula Derivation

# Arbitrage Calculation Formula

## First Pool Swap
$$ y_1 = \frac{(n - s) R_{1,\text{out}} \cdot x}{n R_{1,\text{in}} + (n - s) x} $$

## Second Pool Swap
$$ y_2 = \frac{(n - s) R_{2,\text{out}} \cdot y_1}{n R_{2,\text{in}} + (n - s) y_1} $$

## Expanding \( y_2 \)
$$ y_2 = \frac{(n - s)^2 R_{1,\text{out}} R_{2,\text{out}} \cdot x}{n^2 R_{1,\text{in}} R_{2,\text{in}} + x(n - s)n R_{2,\text{in}} + (n - s)^2 R_{1,\text{out}} x} $$

## Profit Function:

$$ F(x) = y_2 - x $$

To maximize profit, we differentiate \( F(x) \):

$$ F'(x) = y_1' - 1 $$

Expanding further, we arrive at the quadratic equation:

$$ a x^2 + b x + c = 0 $$

Where:

$$ a = k^2 $$

$$ b = 2 n^2 R_{1,\text{in}} R_{2,\text{in}} k $$

$$ c = n^4 R_{1,\text{in}}^2 R_{2,\text{in}}^2 - (n - s)^2 n^2 R_{1,\text{in}} R_{2,\text{in}} R_{1,\text{out}} R_{2,\text{out}} $$


## Solving for \( x^* \):

$$ x^* = \frac{-b + \sqrt{b^2 - 4ac}}{2a} $$


---

## Formula Validation

To validate the formula, consider a scenario where there is a **2x price difference** between the two pools.

### Example Variables:

n = 1000 s = 3 R1,in = 100 × 10^18 R1,out = 1000 × 10^18 R2,in = 1000 × 10^18 R2,out = 200 × 10^18


### Expected Results:
- **Optimal Input (`x*`)** = `20.5911 × 10^18`
- **Max Profit (`F(x*)`)** = `8.44176 × 10^18`

These values match the results derived from the quadratic formula, confirming its accuracy.

---

## Graphical Representation

The formula and expected values can be visualized using Desmos or similar graphing tools.

---

## Conclusion

This formula allows traders to compute the optimal input amount for **2-hop arbitrage**, ensuring maximum profit by leveraging price differences between two pools.

## Simplifying

The equation is given by:

$$
y_1 = (n - s) R_{1,\text{out}} \frac{x}{n R_{1,\text{in}} + (n - s)x}
$$

Similarly, for \( y_2 \):

$$
y_2 = (n - s) R_{2,\text{out}} \frac{y_1}{n R_{2,\text{in}} + (n - s) y_1}
$$

Further simplification leads to:

$$
y_2 = \frac{(n - s)^2 R_{1,\text{out}} R_{2,\text{out}} x}{n^2 R_{1,\text{in}} R_{2,\text{in}} + (n - s)n R_{2,\text{in}} x + (n - s)^2 R_{1,\text{out}} x}
$$

Finally, solving for \( x^* \):

$$
x^* = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

where:
$$
a = k^2, \quad b = 2 n^2 R_{1,\text{in}} R_{2,\text{in}} k, \quad c = (n^2 R_{1,\text{in}} R_{2,\text{in}})^2 - (n - s)^2 n^2 R_{1,\text{in}} R_{2,\text{in}} R_{1,\text{out}} R_{2,\text{out}}
$$


Below is the most works for my mev style with different strategy :
===================================================================

## Simplify to extreme style venomlab studio 

Simplifying

- $y_1 = \frac{(n - s)R_{1, out}x}{nR_{1, in} + (n - s)x}$
- $y_2 = \frac{(n - s)R_{2, out}y_1}{nR_{2, in} + (n - s)y_1}$
- $y_2 = 	\{ (n - s)R_{2, out} \times \frac{(n - s)R_{1, out}x}{nR_{1, in} + (n - s)x} \} \div \{ nR_{2, in} + (n - s) \frac{(n - s)R_{1, out}x}{nR_{1, in} + (n - s)x} \}$
- $y_2 = 	\{ (n - s)R_{2, out} \times (n - s)R_{1, out}x \} \div [ nR_{2, in} \{ nR_{1, in} + (n - s)x \} + (n - s) (n - s)R_{1, out}x ]$
- $y_2 = 	\{ (n - s)^2R_{1, out}R_{2, out}x \} \div \{ n^2R_{1, in}R_{2, in} + (n - s)nR_{2, in}x + (n - s)^2R_{1, out}x \}$
- $y_2 =  \frac	{(n - s)^2R_{1, out}R_{2, out}x} {n^2R_{1, in}R_{2, in} + x \{ (n - s)nR_{2, in} + (n - s)^2R_{1, out} \}}$
- $F(x) = y_2 - x$
- $F^{\prime}(x) = y^{\prime}_1 - 1$
- $f = (n - s)^2R_{1, out}R_{2, out}x$
- $g = n^2R_{1, in}R_{2, in} + x \{ (n - s)nR_{2, in} + (n - s)^2R_{1, out} \}$
- $y^{\prime}_1 = \frac {f^{\prime}g - fg^{\prime}} {g^2}$
- $g^2 = f^{\prime}g - fg^{\prime}$
- $f^{\prime}g - fg^{\prime} = (n - s)^2R_{1, out}R_{2, out} [ n^2R_{1, in}R_{2, in} + x \{ (n - s)nR_{2, in} + (n - s)^2R_{1, out} \} ] - (n - s)^2R_{1, out}R_{2, out}x \{ (n - s)nR_{2, in} + (n - s)^2R_{1, out} \}$
- $f^{\prime}g - fg^{\prime} = (n - s)^2R_{1, out}R_{2, out} \{ n^2R_{1, in}R_{2, in} + (n - s)nR_{2, in} x \} + (n - s)^4R^2_{1, out}R_{2, out} x - (n - s)^3nR_{2, in}R_{1, out}R_{2, out}x - (n - s)^4R^2_{1, out}R_{2, out}x$
- $f^{\prime}g - fg^{\prime} = (n - s)^2R_{1, out}R_{2, out} \{ n^2R_{1, in}R_{2, in} + (n - s)nR_{2, in} x \} - (n - s)^3nR_{2, in}R_{1, out}R_{2, out}x$
- $f^{\prime}g - fg^{\prime} = (n - s)^2n^2R_{1, in}R_{2, in}R_{1, out}R_{2, out}$
- $g^2 = [ n^2R_{1, in}R_{2, in} + x \{ (n - s)nR_{2, in} + (n - s)^2R_{1, out} \}]^2$
- $k = (n - s)nR_{2, in} + (n - s)^2R_{1, out}$
- $g^2 = (n^2R_{1, in}R_{2, in} + kx)^2$
- $g^2 = (n^2R_{1, in}R_{2, in})^2 + 2n^2R_{1, in}R_{2, in} kx + (kx)^2$
- $(n^2R_{1, in}R_{2, in})^2 + 2n^2R_{1, in}R_{2, in} kx + (kx)^2 = (n - s)^2n^2R_{1, in}R_{2, in}R_{1, out}R_{2, out}$
- $k^2x^2 + 2n^2R_{1, in}R_{2, in} kx + (n^2R_{1, in}R_{2, in})^2 - (n - s)^2n^2R_{1, in}R_{2, in}R_{1, out}R_{2, out} = 0$
- $a = k^2$
- $b = 2n^2R_{1, in}R_{2, in} k$
- $c = (n^2R_{1, in}R_{2, in})^2 - (n - s)^2n^2R_{1, in}R_{2, in}R_{1, out}R_{2, out}$
- $x^* = \frac {-b + \sqrt {b^2 - 4ac}} {2a}$


Validate the formula

- The formula expanded above is validated.
  - Consider a situation where there is a 2x price difference between the two pools.
  - Variable
    - $n = 1000$
    - $s = 3$
    - $R_{1, in}=100 * 10^{18}$
    - $R_{1, out}=1000 * 10^{18}$
    - $R_{2, in}=1000 * 10^{18}$
    - $R_{2, out}=200 * 10^{18}$
  - [Calculate and graph on desmos](https://www.desmos.com/calculator/ltanp7fyvt)
    - In the graph below, we can see that the expected value of the arbitrage profit is $8.44176 \times 10^{18}$. We can also see that the quantity of tokens that should be put into the first pool to get the maximum profit is $20.5911 \times 10^{18}$. These values are consistent with the results derived from the root formula, so we can say that the formula is validated.

![](images/2-hop-arbitrage-formula.png)

<br>
 This example below showing you how to get:

 ```
 Optimal Input Amount (x*): 2.059111e+19
Expected Arbitrage Profit: -1.656784e+19
```

```python
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
```
