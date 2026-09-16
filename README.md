# Finance Issues & Quantitative Portfolio Modeling

A comprehensive repository dedicated to quantitative finance, financial economics, portfolio optimization, and stochastic Monte Carlo simulations. This project explores key concepts in Modern Portfolio Theory (MPT) alongside practical Monte Carlo experiments in Python.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Module Summaries](#module-summaries)
  - [1. Modern Portfolio Theory (MPT)](#1-modern-portfolio-theory-mpt)
  - [2. Roulette Monte Carlo Simulation](#2-roulette-monte-carlo-simulation)
  - [3. Stock Portfolio Monte Carlo Simulation](#3-stock-portfolio-monte-carlo-simulation)
- [Key Quantitative Concepts](#key-quantitative-concepts)
- [Installation & Requirements](#installation--requirements)
- [Usage Instructions](#usage-instructions)

---

## 🔍 Overview

This repository contains numerical implementations, Jupyter notebooks, and Python scripts focused on two main pillars of quantitative finance and probability theory:

1. **Modern Portfolio Theory (MPT)**: Mathematical optimization of asset allocation using Markowitz efficiency, Lagrange multipliers, Sharpe ratio maximization, risk aversion utilities, Capital Market Line (CML), and empirical stock data via `yfinance`.
2. **Monte Carlo Methods & Stochastic Simulation**: Empirical evaluation of law of large numbers, house edge dynamics across casino roulette variants (Fair, European, American), and stochastic portfolio modeling.

---

## 📂 Repository Structure

```directory
finance-issues/
├── modern_portfolio_theory/           # MPT, Efficient Frontier, CML, and yfinance Notebooks
│   ├── capital_market_line.ipynb      # CML derivation & Risk-Free asset allocation
│   ├── efficient_frontier.ipynb       # Markowitz Efficient Frontier construction
│   ├── efficient_frontier_harvard.ipynb # Alternative MPT & Efficient Frontier formulation
│   ├── markowitz_lagrange.ipynb       # Analytical optimization via Lagrange Multipliers
│   ├── optimal_portfolio_cml.ipynb    # Tangency Portfolio & CML optimal selection
│   ├── stock_diversification.ipynb    # Idiosyncratic risk reduction through diversification
│   ├── stock_portfalio_yfinance.ipynb # Live market data portfolio analysis (yfinance)
│   ├── stock_portfalio_yfinance_beta.ipynb # Beta estimation & CAPM analysis with real stock data
│   ├── stock_portfolio.ipynb          # Multi-asset portfolio return & covariance modeling
│   ├── surfaces_geometry.ipynb        # 3D visual geometry of mean-variance utility surfaces
│   └── utility_and_risk_aversion.ipynb# Investor risk aversion coefficients & utility curves
│
├── roulettes_monte_carlo/             # Object-Oriented Stochastic Roulette Simulation
│   ├── main.py                        # Simulation orchestrator & MIT experiment runner
│   ├── roulettes.py                   # OOP models for Fair, European, and American Roulettes
│   └── statistics.py                  # Statistical functions (Mean, Std Dev, 95% Confidence Interval)
│
└── stock_portfolio_monte_carlo/       # Stochastic Stock Trajectory & Return Simulations
    └── stock_portfolio.ipynb          # Monte Carlo path generation for stock portfolios
```

---

## 🛠️ Module Summaries

### 1. Modern Portfolio Theory (MPT)
Located in `modern_portfolio_theory/`

This collection of Jupyter Notebooks covers foundational and advanced portfolio theory:
- **Markowitz Optimization & Lagrange Multipliers**: Analytical and numerical solution techniques to minimize portfolio variance for a given expected return.
- **Efficient Frontier & Tangency Portfolio**: Computing the set of optimal portfolios offering the highest expected return for a given level of risk, as well as identifying the Maximum Sharpe Ratio portfolio.
- **Capital Market Line (CML)**: Integrating risk-free assets ($R_f$) to construct the CML and analyze optimal borrowing/lending positions.
- **Risk Aversion & Utility Functions**: Modeling investor utility $U = E(r) - \frac{1}{2} A \sigma^2$ under varying risk aversion levels ($A$).
- **Empirical Market Analysis (`yfinance`)**: Fetching historical market data, computing expected returns, asset covariance matrices, and individual asset Betas ($\beta$).

### 2. Roulette Monte Carlo Simulation
Located in `roulettes_monte_carlo/`

A Python module implementing object-oriented stochastic sampling inspired by MIT computational thinking principles:
- **`roulettes.py`**: Defines classes for `FairRoulette` (no house edge), `EuRoulette` (single zero `0`), and `AmRoulette` (double zero `00`).
- **`statistics.py`**: Computes sample mean, variance, standard deviation, and margin of error using the Empirical Rule for a 95% confidence level ($Z = 1.96$).
- **`main.py`**: Runs multi-trial stochastic simulations scaling sample sizes (100, 1,000, 100,000 spins) to illustrate convergence, regression to the mean, and the exact house edge.

### 3. Stock Portfolio Monte Carlo Simulation
Located in `stock_portfolio_monte_carlo/`

- **`stock_portfolio.ipynb`**: Utilizes Monte Carlo simulations to project portfolio return distributions and potential future asset price trajectories under uncertainty.

---

## 📐 Key Quantitative Concepts

- **Portfolio Expected Return & Variance**:
  $$\mathbb{E}(R_p) = \mathbf{w}^T \boldsymbol{\mu}, \quad \sigma_p^2 = \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}$$
- **Sharpe Ratio**:
  $$\text{Sharpe Ratio} = \frac{\mathbb{E}(R_p) - R_f}{\sigma_p}$$
- **Capital Market Line (CML)**:
  $$\mathbb{E}(R_p) = R_f + \left(\frac{\mathbb{E}(R_t) - R_f}{\sigma_t}\right) \sigma_p$$
- **Monte Carlo Confidence Interval (95%)**:
  $$\text{CI}_{95\%} = \bar{x} \pm 1.96 \cdot \sigma$$

---

## ⚡ Installation & Requirements

Ensure you have Python 3.8+ installed. You can set up the environment and install the required packages:

```bash
pip install numpy pandas matplotlib scipy yfinance plotly jupyter
```

---

## 🚀 Usage Instructions

### Running the Roulette Monte Carlo Experiment
Execute the Python script directly from your terminal:

```bash
python roulettes_monte_carlo/main.py
```

### Exploring Jupyter Notebooks
Launch Jupyter Notebook or Jupyter Lab to interact with the Modern Portfolio Theory notebooks:

```bash
jupyter notebook
```

Navigate to `modern_portfolio_theory/` or `stock_portfolio_monte_carlo/` to run and modify the analysis.

---

## 📄 License

This repository is maintained for educational and quantitative research purposes.
