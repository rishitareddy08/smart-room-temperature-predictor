# SMART ROOM TEMPERATURE PREDICTOR

A modern engineering dashboard for simulating indoor temperature, HVAC response, building insulation effects, numerical root-finding, and error analysis.

## Project Overview

This project models a room as a simplified thermal system and uses numerical methods to predict temperature evolution, estimate the time required to reach a target temperature, and compare analytical and numerical approaches.

## Problem Statement

Buildings rarely operate in a perfectly steady environment. Outdoor conditions, solar gains, internal occupancy heat, insulation quality, and HVAC control all affect indoor temperature. Engineers need a practical model to estimate how long it takes a room to cool or heat to a target setpoint and how different design choices affect comfort.

## Objectives

- Simulate indoor temperature evolution for a room or multiple rooms.
- Apply Newton's law of cooling and a lumped thermal model.
- Compare analytical and numerical solutions.
- Solve target-time estimation with the Bisection and Newton-Raphson methods.
- Analyze insulation and HVAC behavior.
- Compare actual temperatures from a CSV against predicted values.
- Generate a readable engineering report.

## Features

- Dark-themed scientific dashboard with Plotly charts.
- Temperature simulator with outdoor variation modes.
- HVAC thermostat logic and thermal influence model.
- Bisection and Newton-Raphson implementations.
- Euler and RK4 comparison against the analytical solution.
- Multi-room simulation.
- CSV validation and actual-vs-predicted analysis.
- Downloadable report and dataset.

## Technology Stack

- Python 3.11+
- Streamlit
- NumPy
- Pandas
- Plotly
- Pytest

## Architecture

The project is separated into focused modules for:

- Physical model: thermal behavior and building assumptions
- Numerical algorithms: Bisection, Newton-Raphson, ODE solvers
- Simulation logic: room and multi-room analysis
- Utilities: validation, metrics, styling, constants
- UI pages: dashboard, simulator, reports, analysis, about page

## Mathematical Model

### Newton's Law of Cooling

`dT/dt = -k(T - T_out)`

Analytical solution:

`T(t) = T_out + (T_0 - T_out)e^(-kt)`

### Simplified Building Thermal Model

`C dT/dt = UA(T_out - T) - Q_HVAC + Q_internal + Q_solar`

Where:

- `C` = thermal capacitance
- `U` = heat-transfer coefficient
- `A` = exposed area
- `T` = indoor temperature
- `T_out` = outdoor temperature
- `Q_HVAC` = HVAC thermal contribution
- `Q_internal` = internal heat gain
- `Q_solar` = solar heat gain

## Numerical Methods

- Bisection Method
- Newton-Raphson Method
- Euler Method
- Fourth-order Runge-Kutta (RK4)

## Syllabus Mapping

- Unit II: Bisection method, Newton-Raphson method
- Unit IV: First-order ODE, exponential decay, Newton's law of cooling
- Unit V: Higher-order ODE extension, homogeneous and non-homogeneous concepts

## Installation

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

## Test

```bash
pytest
```

## Sample Input

- Initial indoor temperature: 32°C
- Outdoor temperature: 38°C
- Target temperature: 24°C
- Insulation: Medium
- HVAC: Automatic
- Duration: 24 hours

## Expected Output

- Temperature trend chart
- Target-time estimate
- Bisection and Newton-Raphson results
- HVAC status graph
- Error metrics and reports

## Limitations

This project uses a simplified lumped thermal model. It is educational and not a substitute for full building energy modeling software.

## Future Scope

- Real-time sensor integration
- More realistic weather profiles
- Multi-zone airflow and occupancy modeling
- Detailed energy optimization

## Repository Structure

```text
smart-room-temperature-predictor/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── thermal_model.py
│   │   ├── building.py
│   │   └── hvac.py
│   ├── numerical/
│   │   ├── __init__.py
│   │   ├── bisection.py
│   │   ├── newton_raphson.py
│   │   └── ode_solver.py
│   ├── simulation/
│   │   ├── __init__.py
│   │   ├── simulator.py
│   │   └── multi_room.py
│   └── utils/
│       ├── __init__.py
│       ├── validation.py
│       ├── metrics.py
│       ├── constants.py
│       └── styling.py
├── pages/
│   ├── home.py
│   ├── dashboard.py
│   ├── simulator.py
│   ├── numerical_methods.py
│   ├── building_analysis.py
│   ├── multi_room.py
│   ├── data_analysis.py
│   ├── reports.py
│   └── about.py
├── data/
│   └── sample_temperature.csv
├── tests/
│   ├── test_bisection.py
│   ├── test_newton_raphson.py
│   ├── test_thermal_model.py
│   └── test_validation.py
├── assets/
│   └── logo.svg
└── .venv/
```

## Authoring Note

The project is designed as a polished numerical methods mini-project for engineering demonstration, presentation, and viva.
