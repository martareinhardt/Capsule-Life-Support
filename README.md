# 🚀 Capsule Life Support: Proven Viability for 10G Travel

[![Build Status](https://github.com/martareinhardt/Capsule-Life-Support/actions/workflows/run_g_force.yml/badge.svg)](https://github.com/martareinhardt/Capsule-Life-Support/actions)
[![Language](https://img.shields.io/badge/Language-Python%203.x-blue)](https://www.python.org/)
[![Viability Status](https://img.shields.io/badge/Viability-SUCCESS-brightgreen)](./Simulations/README.md)
[![License](https://img.shields.io/badge/License-MIT-gray)](https://opensource.org/licenses/MIT)

## 🎯 Executive Summary and Viability Status

This project demonstrates the engineering viability of a Multi-Layer Adaptive Capsule designed to protect an astronaut under extreme conditions, including **10G** acceleration.

The engineering simulations were validated via GitHub Actions, confirming **SUCCESS** in all critical life support aspects:

| Risk Area | Initial Condition | Final Result | Status |
| :--- | :--- | :--- | :--- |
| **G-Force** | 10.0 G | 1.75 G | ✅ SUCCESS |
| **Radiation** | 500 mSv | 47.50 mSv | ✅ SUCCESS |
| **Thermal** | 80.0 °C (External) | 3.28 °C (Internal) | ✅ SUCCESS |

---

## 🔬 Visual Proof of Viability

The following charts visually confirm that the final simulated values are well within the required safety limits for each system.

### 1. G-Force: Reduction from 10G to 1.75G

The damping system successfully reduces the G-Force to 1.75 G, significantly below the tolerable limit of 5G.

**[Gráfico G-Force](https://github.com/martareinhardt/Capsule-Life-Support/blob/main/Visualizations/g_force_reduction_chart.png?raw=true)**
![](https://raw.githubusercontent.com/martareinhardt/Capsule-Life-Support/main/Visualizations/g_force_reduction_chart.png)

### 2. Radiation: Below the Safety Limit

The shield reduces the absorbed dose to 47.50 mSv, maintaining safety well under the NASA limit of 50 mSv.

**[Gráfico Radiação](https://github.com/martareinhardt/Capsule-Life-Support/blob/main/Visualizations/radiation_viability_chart.png?raw=true)**
![](https://raw.githubusercontent.com/martareinhardt/Capsule-Life-Support/main/Visualizations/radiation_viability_chart.png)

### 3. Thermal Stability: Maintained within Cryogenic Range

The capsule's 99% insulation maintains the internal temperature at 3.28 °C, confirming successful cryo-stability.

**[Gráfico Térmico](https://github.com/martareinhardt/Capsule-Life-Support/blob/main/Visualizations/thermal_viability_chart.png?raw=true)**
![](https://raw.githubusercontent.com/martareinhardt/Capsule-Life-Support/main/Visualizations/thermal_viability_chart.png)

---

## ⚙️ Project Architecture and Automation

The project follows an automated, best-practice engineering workflow:

* **Detailed Technical Reports:** Find all engineering premises, equations, and numerical results in the **[Simulations/README.md](./Simulations/README.md)** file.
* **Source Code Locations:**
    * **Calculations:** `Simulations/`
    * **Visualizations:** `Visualizations/`
* **Automation:** The **`.github/workflows/run_g_force.yml`** workflow ensures all simulations and charts are executed and validated automatically upon every code change.
