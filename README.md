# brownian-motion-candlestick-price-simulator
# 📈 Reflected Geometric Brownian Motion (RGBM) Price Sequence Generator

This simple code simulates intra-candle price movements for an asset based on provided OHLC (Open, High, Low, Close) prices using a **Reflected Geometric Brownian Motion (RGBM)** approach.

The simulation generates a realistic and smoothly interpolated price path that stays within the candle bounds (`phigh` and `plow`) while respecting the opening and closing prices.

---

## ✨ Features

- Simulates realistic intra-minute price movements based on OHLC data.
- Ensures that generated prices never exceed the provided high/low bounds.
- Smoothly interpolates between open and close prices.
- Easy to modify for different use cases like trading bots, backtesting, synthetic data generation, etc.

---

## 🧪 Example Results

| Bullish Example | Bearish Example |
|:---------------:|:---------------:|
| ![Bullish Example](https://github.com/user-attachments/assets/2e67b99b-fd7c-4ca0-96dc-77e2ea5bb4d7) | ![Bearish Example](https://github.com/user-attachments/assets/296b33eb-5494-4d0c-b996-138bccf0c0dd) |
