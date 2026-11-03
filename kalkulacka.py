def pamet_gb(parametry, bity):
    """Paměť vah modelu v GB."""
    return parametry * bity / 8 / 1e9


def export_csv(radky, soubor):
    """Uloží výsledky do CSV souboru."""
    with open(soubor, "w") as f:
        f.write("model;bity;pamet_gb\n")
        for model, bity, gb in radky:
            f.write(f"{model};{bity};{gb}\n")

if __name__ == "__main__":
    print(f"7B v INT4: {pamet_gb(7e9, 4):.1f} GB")
