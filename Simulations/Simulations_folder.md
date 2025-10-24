# Capsule Viability Simulation Reports

This document summarizes the mathematical and engineering viability of the Multi-Layer Adaptive Capsule for 10G Travel, as validated by the Python scripts located in the `Simulations/` folder.

---

## 1. G-Force Reduction Simulation (Script: `g_force_calculator.py`)

This simulation validates whether the protective layers can reduce an extreme 10G acceleration (10 times Earth's gravity) to a level tolerable for the human body (typically below 5G).

| Parameter | Project Premise | Viable Result |
| :--- | :--- | :--- |
| **Initial Acceleration** | 10.0 G | 10.0 G |
| **Protective Layer Reduction** | 30% | 7.00 G |
| **Cryogenic Layer Reduction** | 75% (of remainder) | 1.75 G |
| **FINAL G-FORCE FELT** | N/A | **1.75 G** |
| **VIABILITY STATUS** | Below 5.0 G | **SUCCESS** |

**Conclusion:** The multi-layer protection system is highly effective, reducing the final G-Force to **1.75 G**.

## 2. Radiation Protection Simulation (Script: `radiation_shield.py`)

This simulation validates the effectiveness of the magnetic/graphene shield against long-duration mission radiation doses.

| Parameter | Project Premise | Viable Result |
| :--- | :--- | :--- |
| **Initial Space Dose** | 500 mSv | 500.00 mSv |
| **Deflection Efficiency** | 90% | 50.00 mSv (after deflection) |
| **Internal Absorption (Fluid)** | 5% (of remainder) | 47.50 mSv (output) |
| **FINAL DOSE ABSORBED** | N/A | **47.50 mSv** |
| **Safety Limit (NASA)** | 50 mSv | **SUCCESS** |

**Conclusion:** The final radiation dose absorbed by the astronaut is **47.50 mSv**, remaining within the safety limit.

## 3. Thermal Efficiency Simulation (Script: `thermal_simulator.py`)

This simulation evaluates the SiC aerogel's ability to maintain the cryogenic layer's temperature within the operational range of 0°C to 5°C, simulating a harsh external environment of 80°C.

| Parameter | Project Premise | Viable Result |
| :--- | :--- | :--- |
| **External Temperature** | 80.0 °C | 80.0 °C |
| **Insulation Efficiency** | 99% | 0.80 °C (heat leak) |
| **Internal Target Temp** | 2.5 °C (average) | 2.5 °C |
| **FINAL INTERNAL TEMP** | N/A | **3.28 °C** |
| **Safety Range** | 0°C to 5°C | **SUCCESS** |

**Conclusion:** The 99% insulation system is sufficient to maintain a stable temperature of **3.28 °C**.
