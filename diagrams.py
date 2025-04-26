import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)
y = x**2 * np.sin(x)
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = x^2 \cdot \sin(x)$')
plt.title('Графік функції f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

np.random.seed(0) 
normal_data = np.random.normal(loc=5, scale=2, size=1000)
plt.figure(figsize=(8, 5))
plt.hist(normal_data, bins=30, color='skyblue', edgecolor='black')
plt.title('Гістограма нормального розподілу (μ=5, σ=2)')
plt.xlabel('Значення')
plt.ylabel('Кількість')
plt.grid(True)
plt.show()

hobbies = ['Читання', 'Музика',  'Подорожі', 'Cон']
percentages = [25, 55, 5, 15]
plt.figure(figsize=(7, 7))
plt.pie(percentages, labels=hobbies, autopct='%1.1f%%', startangle=140)
plt.title('Мої улюблені хобі')
plt.show()

np.random.seed(1)
fruits = ['Яблука', 'Банани', 'Апельсини', 'Груші']
apple_weights = np.random.normal(loc=150, scale=15, size=100)
banana_weights = np.random.normal(loc=120, scale=10, size=100)
orange_weights = np.random.normal(loc=130, scale=12, size=100)
pear_weights = np.random.normal(loc=140, scale=18, size=100)
data = [apple_weights, banana_weights, orange_weights, pear_weights]
plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=fruits)
plt.title('Вага фруктів')
plt.ylabel('Вага (г)')
plt.grid(True)
plt.show()