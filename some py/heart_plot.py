import numpy as np
import matplotlib.pyplot as plt

# x от -2 до 2 (иначе под корнем будет отрицательное)
x = np.linspace(-2, 2, 10000)

# x^(2/3) в реальных числах: |x|**(2/3)
x_pow = np.abs(x) ** (2/3)

y = (x_pow + np.sin(100 * x)) * np.sqrt(4 - x**2) * 0.9 - 2

plt.figure(figsize=(6, 6))

# красная «сердечная» кривая
plt.plot(x, y, color='red', linewidth=0.7)

# оси как на скрине
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)

# сетка можно оставить – будет похоже на Mathway
plt.grid(True, linestyle='--', linewidth=0.3)

# ВАЖНО: не ставим set_aspect('equal'), чтобы форма была такой же вытянутой
plt.show()
