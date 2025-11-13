import math

v = 500      # velocity in m/s
angle = 10   # degrees
g = 9.81

theta = math.radians(angle)

for t in range(0, 5):   # 0 to 4 seconds
    y = v * math.sin(theta) * t - 0.5 * g * t * t
    print(f"t={t}s height={y:.2f}m")
