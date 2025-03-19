import pandas as pd
import datetime

# Charger les données
def load_data_from_csv(file_path):
    df = pd.read_csv(file_path, sep=',', header=0)
    df.columns = ['timestamp', 'USD/GBP','USD/CAD','USD/EUR','USD/AUD','GBP/USD','GBP/CAD','GBP/EUR','GBP/AUD',
                  'CAD/USD','CAD/GBP','CAD/EUR','CAD/AUD','EUR/USD','EUR/GBP','EUR/CAD','EUR/AUD',
                  'AUD/USD','AUD/GBP','AUD/CAD','AUD/EUR']
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

# Charger les données
data = load_data_from_csv('/home/azureuser/scraping_dir/data/exchange_rates.csv')

# Filtrer les données de la journée
today = datetime.datetime.now().date()
daily_data = data[data['timestamp'].dt.date == today]

# Calculer les statistiques
report = {}
for pair in data.columns[1:]:
    report[pair] = {
        "High": round(daily_data[pair].max(), 4),
        "Low": round(daily_data[pair].min(), 4),
        "Volatility": round(daily_data[pair].std(), 4),
        "Return": round((daily_data[pair].iloc[-1] - daily_data[pair].iloc[0]) / daily_data[pair].iloc[0] * 100, 4)
    }

# Sauvegarder le rapport sous forme de fichier texte
report_filename = f"/home/azureuser/scraping_dir/reports/report_{today}.txt"
with open(report_filename, "w") as file:
    file.write(f"📊 FX Exchange Rates Report - {today}\n")
    file.write("="*40 + "\n")
    for pair, stats in report.items():
        file.write(f"{pair}\n")
        file.write(f" High: {stats['High']}\n")
        file.write(f" Low: {stats['Low']}\n")
        file.write(f" Volatility: {stats['Volatility']}\n")
        file.write(f" Return (24h): {stats['Return']}%\n")
        file.write("-"*40 + "\n")

print(f"✅ Rapport quotidien généré : {report_filename}")

