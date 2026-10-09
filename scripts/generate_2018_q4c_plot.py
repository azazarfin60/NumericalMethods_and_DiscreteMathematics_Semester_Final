#!/usr/bin/env python3
"""Generate high-resolution plot for 2018 Q.4(c) linear regression."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def generate():
    v_data = np.array([2, 3, 4, 5, 7, 10], dtype=float)
    i_data = np.array([5.2, 7.8, 10.7, 13.0, 19.3, 27.5], dtype=float)

    # Fitted parameters
    b = 2.808171
    a = -0.592218
    v_line = np.linspace(0, 11, 200)
    i_line = a + b * v_line

    # Predicted point
    v_pred = 3.5
    i_pred = a + b * v_pred

    # Plot setup
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("#fafafa")

    # Grid
    ax.grid(True, linestyle="--", alpha=0.5, color="#cccccc", zorder=0)

    # Fitted line
    ax.plot(v_line, i_line, color="#1f77b4", linewidth=2.0, label="Fitted line: $i = -0.5922 + 2.8082\\,v$", zorder=2)

    # Measured data points
    ax.scatter(v_data, i_data, color="#d62728", s=60, edgecolor="black", linewidth=0.8, zorder=4, label="Measured data points")

    # Predicted point
    ax.scatter([v_pred], [i_pred], color="#2ca02c", s=80, marker="D", edgecolor="black", linewidth=1.0, zorder=5, label=f"Interpolated point at $3.5\\text{{ V}}$: $i = {i_pred:.4f}\\text{{ A}}$")

    # Dashed projection lines for v = 3.5 V
    ax.plot([v_pred, v_pred], [0, i_pred], color="#2ca02c", linestyle=":", linewidth=1.2, zorder=3)
    ax.plot([0, v_pred], [i_pred, i_pred], color="#2ca02c", linestyle=":", linewidth=1.2, zorder=3)

    # Data point labels
    for v, i in zip(v_data, i_data):
        ax.annotate(f"({v:g}, {i:.1f})", (v, i), textcoords="offset points", xytext=(-10, 8), fontsize=8.5, color="#222222")

    # Annotation for evaluated point
    ax.annotate(f"(3.5 V, {i_pred:.2f} A)", (v_pred, i_pred), textcoords="offset points", xytext=(15, -12), fontsize=9, color="#1b781b", weight="bold",
                arrowprops=dict(arrowstyle="->", color="#2ca02c", lw=1.2))

    # Labels and title
    ax.set_xlabel("Voltage $v$ (V)", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_ylabel("Current $i$ (A)", fontsize=11, fontweight="bold", labelpad=8)
    ax.set_title("Linear Regression: Current vs. Imposed Voltage [2018 Q.4(c)]", fontsize=12, fontweight="bold", pad=12)

    # Limits
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 30)

    # Legend
    ax.legend(loc="upper left", frameon=True, framealpha=0.92, edgecolor="#bbbbbb", fontsize=9.5)

    # Metrics box
    stats_text = (
        "Linear Regression Fit\n"
        "$i = a + b\\,v$\n"
        "$b = 2.8082\\text{ A/V}$\n"
        "$a = -0.5922\\text{ A}$\n"
        "$r = 0.9996\\ (r^2 = 0.9991)$\n"
        "$i(3.5\\text{ V}) = 9.2364\\text{ A}$"
    )
    ax.text(0.96, 0.06, stats_text, transform=ax.transAxes, fontsize=9,
            verticalalignment="bottom", horizontalalignment="right",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#ffffff", edgecolor="#cccccc", alpha=0.95))

    plt.tight_layout()

    # Paths to save
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    destinations = [
        os.path.join(root, "answers_exam_style", "diagrams", "2018_Q4c_regression.jpg"),
        os.path.join(root, "answers_exam_style", "diagrams", "2018_Q4c_regression.png"),
        os.path.join(root, "topicwise_answers_exam_style", "diagrams", "2018_Q4c_regression.jpg"),
        os.path.join(root, "topicwise_answers_exam_style", "diagrams", "2018_Q4c_regression.png"),
        os.path.join(root, "PreviousYearQuestions", "diagrams", "2018_Q4c_regression.jpg"),
        os.path.join(root, "PreviousYearQuestions", "diagrams", "2018_Q4c_regression.png")
    ]

    for d in destinations:
        os.makedirs(os.path.dirname(d), exist_ok=True)
        plt.savefig(d, dpi=300)
        print("Saved:", d)

if __name__ == "__main__":
    generate()
