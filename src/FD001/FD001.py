from pathlib import Path
import pandas as pd

RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
DATA_DIR = RAIZ_PROYECTO / "data"

# Toda la informacon la podras encontrar en el zip de la pagina
# https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data

index_cols = ["unit", "cycle"]
setting_cols = ["op_setting_1", "op_setting_2", "op_setting_3"]
sensor_cols = [
    "T2", "T24", "T30", "T50",       # temperaturas: fan inlet, LPC, HPC, LPT outlet
    "P2", "P15", "P30",              # presiones: fan inlet, bypass, HPC outlet
    "Nf", "Nc",                      # velocidad física del fan y del core
    "epr", "Ps30", "phi",            # relación de presiones, presión estática HPC, flujo combustible/Ps30
    "NRf", "NRc", "BPR", "farB",     # velocidades corregidas, bypass ratio, relación combustible-aire
    "htBleed", "Nf_dmd", "PCNfR_dmd",
    "W31", "W32",                    # sangrado de enfriamiento HPT y LPT
]
columnas = index_cols + setting_cols + sensor_cols

train = pd.read_csv(r"C:\CMAPSS_Jet_Engine\data\train_FD001.txt", sep=r"\s+", header=None, names=columnas)
print(train.shape)
print(train.head())