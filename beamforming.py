import numpy as np
import matplotlib.pyplot as plt

N = 8
theta = np.linspace(-90, 90, 1000)
theta_rad = np.radians(theta)

steer_angle = 30
d = 0.5

beta = -2*np.pi*d*np.sin(np.radians(steer_angle))

AF = np.zeros(len(theta_rad), dtype=complex)

for n in range(N):
    AF += np.exp(
        1j*n*(2*np.pi*d*np.sin(theta_rad)+beta)
    )

AF = np.abs(AF)
AF = AF / np.max(AF)

plt.plot(theta,20*np.log10(AF))
plt.title("5G Beamforming Pattern")
plt.xlabel("Angle")
plt.ylabel("Gain (dB)")
plt.grid()

plt.savefig("beamforming_pattern.png")

plt.show()