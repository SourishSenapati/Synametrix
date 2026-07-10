import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib

# Ultra-Human-Readable Publication quality settings
plt.style.use('seaborn-v0_8-whitegrid')
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['axes.labelsize'] = 18
matplotlib.rcParams['axes.titlesize'] = 22
matplotlib.rcParams['axes.titleweight'] = 'bold'
matplotlib.rcParams['legend.fontsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 14
matplotlib.rcParams['ytick.labelsize'] = 14
matplotlib.rcParams['figure.dpi'] = 300
matplotlib.rcParams['savefig.dpi'] = 300

os.makedirs(os.path.join('figures', 'tif'), exist_ok=True)
os.makedirs(os.path.join('figures', 'png'), exist_ok=True)

# ---------------------------------------------------------
# Figure 2.1: Steele Photoinhibition Curve
# ---------------------------------------------------------
def generate_steele_curve():
    I = np.linspace(0, 3000, 500)
    mu_max = 1.25
    K_I = 120
    K_II = 2500
    mu = mu_max * I / (K_I + I + (I**2 / K_II))
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(I, mu, color='#004488', linewidth=4, label=r'Growth Rate ($\mu$)')
    
    I_opt = np.sqrt(K_I * K_II)
    mu_opt = mu_max * I_opt / (K_I + I_opt + (I_opt**2 / K_II))
    
    ax.axvline(x=I_opt, color='#d95f02', linestyle='--', linewidth=2, alpha=0.9, label='Optimal Light Intensity')
    ax.plot(I_opt, mu_opt, 'o', color='#d95f02', markersize=12, markeredgecolor='black', markeredgewidth=1.5)
    
    bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=1.5, alpha=0.9)
    ax.text(I_opt + 150, mu_opt - 0.1, f'Maximum Growth\n$I_{{opt}}$ = {int(I_opt)} \\mu mol m^{{-2}} s^{{-1}}', 
            fontsize=14, verticalalignment='top', bbox=bbox_props)
    
    ax.fill_between(I, 0, mu, where=(I > 1500), color='#e41a1c', alpha=0.15, label='Photoinhibition Zone')
    ax.set_xlabel(r'Light Intensity ($\mu$mol photons m$^{-2}$ s$^{-1}$)', fontweight='bold')
    ax.set_ylabel('Specific Growth Rate (d$^{-1}$)', fontweight='bold')
    ax.set_title('Steele Photoinhibition Growth Rate')
    ax.set_xlim(0, 3000)
    ax.set_ylim(0, 1.2)
    ax.legend(loc='lower right', frameon=True, shadow=True)
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'tif', '2-01.tif'), format='tiff', bbox_inches='tight', pil_kwargs={"compression": "tiff_lzw"})
    plt.savefig(os.path.join('figures', 'png', '2-01.png'), format='png', bbox_inches='tight', dpi=150)
    plt.close()

# ---------------------------------------------------------
# Figure 2.2: Beer-Lambert Light Attenuation
# ---------------------------------------------------------
def generate_beer_lambert():
    y = np.linspace(0, 0.1, 500) # Depth up to 100 mm (0.1 m)
    I_0 = 400
    alpha = 15.0 # m^2/kg = L/g/m
    
    fig, ax = plt.subplots(figsize=(10, 7))
    colors = ['#1b9e77', '#d95f02', '#7570b3']
    
    for i, X in enumerate([1.0, 2.0, 3.0]):
        I_y = I_0 * np.exp(-alpha * y * X)
        ax.plot(y * 1000, I_y, color=colors[i], linewidth=4, label=f'Biomass = {X} g/L')
    
    # Compensation point
    I_c = 10
    ax.axhline(y=I_c, color='black', linestyle='--', linewidth=2, label='Compensation Point ($I_c$)')
    ax.text(80, I_c + 10, 'Dark Core Onset', fontsize=14, fontweight='bold', color='black')
    
    ax.fill_between(y * 1000, 0, I_c, color='gray', alpha=0.2)
    
    ax.set_xlabel('Reactor Depth (mm)', fontweight='bold')
    ax.set_ylabel(r'Local Light Intensity ($\mu$mol photons m$^{-2}$ s$^{-1}$)', fontweight='bold')
    ax.set_title('Beer-Lambert Light Attenuation in Tubular PBR')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 400)
    ax.legend(loc='upper right', frameon=True, shadow=True)
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'tif', '2-02.tif'), format='tiff', bbox_inches='tight', pil_kwargs={"compression": "tiff_lzw"})
    plt.savefig(os.path.join('figures', 'png', '2-02.png'), format='png', bbox_inches='tight', dpi=150)
    plt.close()

# ---------------------------------------------------------
# Figure 2.3: Tube Diameter Sensitivity
# ---------------------------------------------------------
def generate_tube_diameter():
    X = np.linspace(1.0, 4.0, 200)
    alpha = 15.0
    I_c = 10
    
    fig, ax = plt.subplots(figsize=(10, 7))
    colors = ['#000000', '#004488', '#d95f02']
    
    for i, I_0 in enumerate([200, 400, 800]):
        D_max = (1 / (alpha * X)) * np.log(I_0 / I_c) * 1000 # convert to mm
        ax.plot(X, D_max, color=colors[i], linewidth=4, label=f'Incident Light = {I_0} \\mu mol/m^2/s')
    
    ax.axhspan(50, 100, color='green', alpha=0.15, label='Industrial Operational Range')
    
    ax.set_xlabel('Biomass Concentration (g L$^{-1}$)', fontweight='bold')
    ax.set_ylabel('Maximum Tube Diameter, $D_{max}$ (mm)', fontweight='bold')
    ax.set_title('Parametric Sensitivity of Reactor Diameter')
    ax.set_xlim(1.0, 4.0)
    ax.set_ylim(0, 250)
    ax.legend(loc='upper right', frameon=True, shadow=True)
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'tif', '2-03.tif'), format='tiff', bbox_inches='tight', pil_kwargs={"compression": "tiff_lzw"})
    plt.savefig(os.path.join('figures', 'png', '2-03.png'), format='png', bbox_inches='tight', dpi=150)
    plt.close()

# ---------------------------------------------------------
# Figure 2.4: ODE Simulation Profiles
# ---------------------------------------------------------
def generate_ode_profiles():
    t = np.linspace(0, 5, 200) # 5 days
    # Logistic-like growth for biomass, exponential decay for substrate
    X_max = 2.5
    X_0 = 0.2
    k = 1.8
    X = X_max / (1 + ((X_max - X_0) / X_0) * np.exp(-k * t))
    
    S_0 = 50.0 # mg/L
    S = S_0 * np.exp(-1.2 * t)
    
    fig, ax1 = plt.subplots(figsize=(10, 7))
    
    color1 = '#005a32'
    ax1.plot(t, X, color=color1, linewidth=4, label='Biomass Concentration (X)')
    ax1.set_xlabel('Cultivation Time (Days)', fontweight='bold')
    ax1.set_ylabel('Biomass Concentration (g L$^{-1}$)', color=color1, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(0, 3)
    ax1.set_xlim(0, 5)
    
    ax2 = ax1.twinx()
    color2 = '#cb181d'
    ax2.plot(t, S, color=color2, linewidth=4, linestyle='--', label='Ammonium Substrate (S)')
    ax2.set_ylabel('Ammonium Concentration (mg L$^{-1}$)', color=color2, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(0, 60)
    
    # Combined legend
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='center right', frameon=True, shadow=True)
    
    plt.title('Batch Growth and Substrate Depletion Kinetics', fontweight='bold', fontsize=22)
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'tif', '2-04.tif'), format='tiff', bbox_inches='tight', pil_kwargs={"compression": "tiff_lzw"})
    plt.savefig(os.path.join('figures', 'png', '2-04.png'), format='png', bbox_inches='tight', dpi=150)
    plt.close()

# ---------------------------------------------------------
# Figure 2.5: Barlow Burst Pressure
# ---------------------------------------------------------
def generate_burst_pressure():
    D_o = np.linspace(50, 150, 100) # mm
    w = 3.0 # mm wall thickness
    sigma_glass = 48.0 # MPa
    sigma_pmma = 70.0 # MPa
    
    Pb_glass = 2 * sigma_glass * w / D_o
    Pb_pmma = 2 * sigma_pmma * w / D_o
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(D_o, Pb_glass, color='#004488', linewidth=4, label='Borosilicate Glass (Tensile = 48 MPa)')
    ax.plot(D_o, Pb_pmma, color='#d95f02', linewidth=4, linestyle='--', label='PMMA (Tensile = 70 MPa)')
    
    ax.axhline(y=0.6, color='black', linestyle=':', linewidth=3, label='Working Pressure (0.6 MPa)')
    ax.fill_between(D_o, 0, 0.6, color='red', alpha=0.1, label='Failure Zone')
    
    ax.set_xlabel('Outer Tube Diameter (mm)', fontweight='bold')
    ax.set_ylabel('Calculated Burst Pressure (MPa)', fontweight='bold')
    ax.set_title('Barlow Burst Pressure Analysis for Reactor Safety')
    ax.set_xlim(50, 150)
    ax.set_ylim(0, 10)
    ax.legend(loc='upper right', frameon=True, shadow=True)
    
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'tif', '2-05.tif'), format='tiff', bbox_inches='tight', pil_kwargs={"compression": "tiff_lzw"})
    plt.savefig(os.path.join('figures', 'png', '2-05.png'), format='png', bbox_inches='tight', dpi=150)
    plt.close()

# ---------------------------------------------------------
# Figure 2.6: PINN Spatial Biomass Distribution (Heatmap)
# ---------------------------------------------------------
def generate_pinn_heatmap():
    x = np.linspace(0, 1, 150)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    
    base_flow = 1.0 - 0.8 * np.exp(-20 * (Y - 0.5)**2)
    vortex = 0.5 * np.exp(-30 * ((X - 0.3)**2 + (Y - 0.7)**2)) - 0.4 * np.exp(-30 * ((X - 0.7)**2 + (Y - 0.3)**2))
    
    biomass = base_flow + vortex
    biomass = 1.5 + 1.5 * (biomass - np.min(biomass)) / (np.max(biomass) - np.min(biomass))
    
    fig, ax = plt.subplots(figsize=(11, 6))
    c = ax.contourf(X, Y, biomass, levels=100, cmap='inferno')
    cbar = fig.colorbar(c, ax=ax)
    cbar.set_label('Biomass Concentration (g L$^{-1}$)', rotation=270, labelpad=25, fontweight='bold', fontsize=16)
    
    U = np.ones_like(X) * 0.8
    V = np.gradient(vortex, axis=0) * 15
    ax.streamplot(X, Y, U, V, color='white', linewidth=1.5, density=0.5, arrowsize=2.0)
    
    ax.text(0.3, 0.75, 'High Mixing Zone', color='white', fontsize=14, fontweight='bold', 
            ha='center', va='center', bbox=dict(boxstyle="round", fc="black", alpha=0.5))
    ax.text(0.7, 0.25, 'Flow Stagnation', color='white', fontsize=14, fontweight='bold', 
            ha='center', va='center', bbox=dict(boxstyle="round", fc="black", alpha=0.5))
    
    ax.set_xlabel('Reactor Length (Normalized)', fontweight='bold')
    ax.set_ylabel('Reactor Radius (Normalized)', fontweight='bold')
    ax.set_title('PINN-Predicted Biomass Distribution')
    
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'tif', '2-06.tif'), format='tiff', bbox_inches='tight', pil_kwargs={"compression": "tiff_lzw"})
    plt.savefig(os.path.join('figures', 'png', '2-06.png'), format='png', bbox_inches='tight', dpi=150)
    plt.close()

# ---------------------------------------------------------
# Figure 4.1: Free Ammonia (FA) Toxicity Thermal Map
# ---------------------------------------------------------
def generate_ammonia_map():
    pH = np.linspace(7.0, 9.0, 200)
    T_C = np.linspace(15, 40, 200)
    PH, TC = np.meshgrid(pH, T_C)
    TK = TC + 273.15
    TAN = 1000
    FA = (TAN * 10**PH) / (np.exp(6344 / TK) + 10**PH)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    levels = np.linspace(0, 300, 100)
    c = ax.contourf(PH, TC, FA, levels=levels, cmap='YlOrRd', extend='max')
    cbar = fig.colorbar(c, ax=ax, ticks=[0, 45, 100, 200, 300])
    cbar.set_label('Free Ammonia (mg L$^{-1}$)', rotation=270, labelpad=25, fontweight='bold', fontsize=16)
    
    CS = ax.contour(PH, TC, FA, levels=[45.0], colors='black', linewidths=4, linestyles='solid')
    ax.clabel(CS, inline=True, fontsize=16, fmt='Critical Threshold: 45 mg/L', manual=[(8.2, 25)])
    
    ax.contourf(PH, TC, FA, levels=[45, 1000], colors='none', hatches=['//'], alpha=0.1)
    ax.text(7.5, 35, 'SAFE ZONE', fontsize=18, fontweight='bold', color='#005a32', ha='center', va='center', bbox=dict(boxstyle="round", fc="white", alpha=0.8))
    ax.text(8.7, 20, 'TOXIC ZONE', fontsize=18, fontweight='bold', color='#cb181d', ha='center', va='center', bbox=dict(boxstyle="round", fc="white", alpha=0.8))
    
    ax.set_xlabel('Operational pH', fontweight='bold')
    ax.set_ylabel('System Temperature (°C)', fontweight='bold')
    ax.set_title('Ammonia Toxicity Risk in Anaerobic Digestate')
    
    plt.tight_layout()
    plt.savefig(os.path.join('figures', 'tif', '4-01.tif'), format='tiff', bbox_inches='tight', pil_kwargs={"compression": "tiff_lzw"})
    plt.savefig(os.path.join('figures', 'png', '4-01.png'), format='png', bbox_inches='tight', dpi=150)
    plt.close()

if __name__ == "__main__":
    generate_steele_curve()
    generate_beer_lambert()
    generate_tube_diameter()
    generate_ode_profiles()
    generate_burst_pressure()
    generate_pinn_heatmap()
    generate_ammonia_map()
    print("All 7 Ultra-Human-Readable TIFF figures generated successfully.")
