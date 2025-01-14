import os
import time
import pandas as pd
from joblib import load

# Proje kök dizinini tanımlayın
os.chdir("/home/selcuk1453/RANDOM-FOREST-TABANLI-IDS")
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Script çalıştırılırsa
except NameError:
    BASE_DIR = os.getcwd()  # Jupyter Notebook'ta çalıştırılırsa
# MODEL ve MODEL_HASSAS klasörlerini tanımlayın
MODEL_DIR = os.path.join(BASE_DIR, "MODEL")
MODEL_HASSAS_DIR = os.path.join(BASE_DIR, "MODEL_HASSAS")

# Modellerin yollarını dinamik olarak ayarlayın
models = {
    'BOTNET': load(os.path.join(MODEL_DIR, "BOTNET_random_forest_model3.pkl")),
    'GOLDENEYE': load(os.path.join(MODEL_DIR, "GOLDENEYE2_random_forest_model7.pkl")),
    'LOIC': load(os.path.join(MODEL_DIR, "loıc_random_forest_model6.pkl")),
    'HOIC': load(os.path.join(MODEL_DIR, "HOİC_random_forest_model6.pkl")),
    'HULK': load(os.path.join(MODEL_DIR, "hulk1_random_forest_model6.pkl")),
    'SLOWLORIS': load(os.path.join(MODEL_DIR, "SLOWLORIS_random_forest_model7.pkl")),
    'SSH': load(os.path.join(MODEL_DIR, "SSS_random_forest_model1.pkl"))
}

sensitive_models = {
    'HULK': load(os.path.join(MODEL_HASSAS_DIR, "hulk1_random_forest_model.pkl")),
    'BOTNET': load(os.path.join(MODEL_HASSAS_DIR, "botnet1_random_forest_model.pkl")),
    'GOLDENEYE': load(os.path.join(MODEL_HASSAS_DIR, "golden1_random_forest_model.pkl")),
    'LOIC': load(os.path.join(MODEL_HASSAS_DIR, "loic1_random_forest_model.pkl")),
    'HOIC': load(os.path.join(MODEL_HASSAS_DIR, "hoic1_random_forest_model.pkl")),
    'SLOWLORIS': load(os.path.join(MODEL_HASSAS_DIR, "slow1_random_forest_model.pkl")),
    'SSH': load(os.path.join(MODEL_DIR, "SSS_random_forest_model1.pkl"))
}

features = {
    'BOTNET': load(os.path.join(MODEL_DIR, "BOTNET_selected_features3.pkl")),
    'GOLDENEYE': load(os.path.join(MODEL_DIR, "GOLDENEYE2_selected_features7.pkl")),
    'LOIC': load(os.path.join(MODEL_DIR, "loic_selected_features6.pkl")),
    'HOIC': load(os.path.join(MODEL_DIR, "HOİC_selected_features6.pkl")),
    'HULK': load(os.path.join(MODEL_DIR, "hulk1_selected_features6.pkl")),
    'SLOWLORIS': load(os.path.join(MODEL_DIR, "SLOWLORIS_selected_features7.pkl")),
    'SSH': load(os.path.join(MODEL_DIR, "SSH_selected_features1.pkl"))
}

sensitive_features = {
    'HULK': load(os.path.join(MODEL_HASSAS_DIR, "hulk1_selected_features.pkl")),
    'BOTNET': load(os.path.join(MODEL_HASSAS_DIR, "botnet1_selected_features.pkl")),
    'GOLDENEYE': load(os.path.join(MODEL_HASSAS_DIR, "golden1_selected_features.pkl")),
    'LOIC': load(os.path.join(MODEL_HASSAS_DIR, "loic1_selected_features.pkl")),
    'HOIC': load(os.path.join(MODEL_HASSAS_DIR, "hoic1_selected_features.pkl")),
    'SLOWLORIS': load(os.path.join(MODEL_HASSAS_DIR, "slow1_selected_features.pkl")),
    'SSH': load(os.path.join(MODEL_DIR, "SSH_selected_features1.pkl"))
}

thresholds = {
    'BOTNET': 0.85,
    'GOLDENEYE': 0.9,
    'LOIC': 0.9,
    'HOIC': 0.9,
    'HULK': 0.5,
    'SLOWLORIS': 0.6,
    'SSH': 0.5
}

columns_and_types = {
    'Dst Port': 'int64', 'Protocol': 'int64', 'Flow Duration': 'int64',
    'Tot Fwd Pkts': 'int64', 'Tot Bwd Pkts': 'int64', 'TotLen Fwd Pkts': 'int64',
    'TotLen Bwd Pkts': 'int64', 'Fwd Pkt Len Max': 'int64', 'Fwd Pkt Len Min': 'int64',
    'Fwd Pkt Len Mean': 'float64', 'Fwd Pkt Len Std': 'float64', 'Bwd Pkt Len Max': 'int64',
    'Bwd Pkt Len Min': 'int64', 'Bwd Pkt Len Mean': 'float64', 'Bwd Pkt Len Std': 'float64',
    'Flow Byts/s': 'float64', 'Flow Pkts/s': 'float64', 'Flow IAT Mean': 'float64',
    'Flow IAT Std': 'float64', 'Flow IAT Max': 'int64', 'Flow IAT Min': 'int64',
    'Fwd IAT Tot': 'int64', 'Fwd IAT Mean': 'float64', 'Fwd IAT Std': 'float64',
    'Fwd IAT Max': 'int64', 'Fwd IAT Min': 'int64', 'Bwd IAT Tot': 'int64',
    'Bwd IAT Mean': 'float64', 'Bwd IAT Std': 'float64', 'Bwd IAT Max': 'int64',
    'Bwd IAT Min': 'int64', 'Fwd PSH Flags': 'int64', 'Bwd PSH Flags': 'int64',
    'Fwd URG Flags': 'int64', 'Bwd URG Flags': 'int64', 'Fwd Header Len': 'int64',
    'Bwd Header Len': 'int64', 'Fwd Pkts/s': 'float64', 'Bwd Pkts/s': 'float64',
    'Pkt Len Min': 'int64', 'Pkt Len Max': 'int64', 'Pkt Len Mean': 'float64',
    'Pkt Len Std': 'float64', 'Pkt Len Var': 'float64', 'FIN Flag Cnt': 'int64',
    'SYN Flag Cnt': 'int64', 'RST Flag Cnt': 'int64', 'PSH Flag Cnt': 'int64',
    'ACK Flag Cnt': 'int64', 'URG Flag Cnt': 'int64', 'CWE Flag Count': 'int64',
    'ECE Flag Cnt': 'int64', 'Down/Up Ratio': 'int64', 'Pkt Size Avg': 'float64',
    'Fwd Seg Size Avg': 'float64', 'Bwd Seg Size Avg': 'float64', 'Fwd Byts/b Avg': 'int64',
    'Fwd Pkts/b Avg': 'int64', 'Fwd Blk Rate Avg': 'int64', 'Bwd Byts/b Avg': 'int64',
    'Bwd Pkts/b Avg': 'int64', 'Bwd Blk Rate Avg': 'int64', 'Subflow Fwd Pkts': 'int64',
    'Subflow Fwd Byts': 'int64', 'Subflow Bwd Pkts': 'int64', 'Subflow Bwd Byts': 'int64',
    'Init Fwd Win Byts': 'int64', 'Init Bwd Win Byts': 'int64', 'Fwd Act Data Pkts': 'int64',
    'Fwd Seg Size Min': 'int64', 'Active Mean': 'float64', 'Active Std': 'float64',
    'Active Max': 'int64', 'Active Min': 'int64', 'Idle Mean': 'float64',
    'Idle Std': 'float64', 'Idle Max': 'int64', 'Idle Min': 'int64', 'Label': 'object'
}


def veri_temizleme(row):
    cleaned_row = row.replace([float('inf'), float('-inf')], pd.NA).fillna(0)
    cleaned_df = pd.DataFrame([cleaned_row], columns=cleaned_row.index)
    for column, dtype in columns_and_types.items():
        if column in cleaned_df.columns:
            cleaned_df[column] = cleaned_df[column].astype(dtype, errors='ignore')
    return cleaned_df


def model_tahmin(cleaned_df, row_num):
    tahmin_sonuclari = {}
    for attack_type, model in models.items():
        try:
            selected_features = features[attack_type]
            data_to_predict = cleaned_df[selected_features]
            y_proba = model.predict_proba(data_to_predict)
            # Probability that this is an attack = 1 - P(Benign)
            attack_prob = 1 - y_proba[0, model.classes_.tolist().index('Benign')]
            tahmin_sonuclari[attack_type] = attack_prob
        except:
            tahmin_sonuclari[attack_type] = 0

    esik_gecenler = {k: v for k, v in tahmin_sonuclari.items() if v >= thresholds[k]}
    if esik_gecenler:
        print(f"{row_num}: " + ", ".join([f"{k}: {v:.2f}" for k, v in esik_gecenler.items()]))
    else:
        print(f"{row_num}: Benign")

    return tahmin_sonuclari


def yeniden_degerlendirme(chunk, max_attack_type, output_file):
    with open(output_file, 'a') as f:
        for idx, row in chunk.iterrows():
            cleaned_df = veri_temizleme(row)

            # Hassas model tahmini
            try:
                sensitive_model = sensitive_models[max_attack_type]
                sensitive_features_list = sensitive_features[max_attack_type]
                sensitive_data = cleaned_df[sensitive_features_list]
                y_proba = sensitive_model.predict_proba(sensitive_data)
                sensitive_prob = 1 - y_proba[0, sensitive_model.classes_.tolist().index('Benign')]
            except Exception as e:
                sensitive_prob = "Hata"
                print(f"Hassas model tahmini hatası (satır {idx}): {e}")

            tahmin_sonuclari = {}
            for attack_type, model in models.items():
                if attack_type == max_attack_type:
                    continue
                try:
                    selected_features = features[attack_type]
                    data_to_predict = cleaned_df[selected_features]
                    y_proba = model.predict_proba(data_to_predict)
                    attack_prob = 1 - y_proba[0, model.classes_.tolist().index('Benign')]
                    tahmin_sonuclari[attack_type] = attack_prob
                except:
                    tahmin_sonuclari[attack_type] = 0

            sensitive_prob_str = f"{sensitive_prob:.2f}" if isinstance(sensitive_prob, float) else sensitive_prob
            esik_gecenler = [f"{k}: {v:.2f}" for k, v in tahmin_sonuclari.items() if v >= thresholds[k]]
            f.write(f"{idx}: {max_attack_type} Hassas ({sensitive_prob_str}) | {', '.join(esik_gecenler)}\n")


def watch_for_changes(file_to_watch, output_file, chunk_size=100):
    print("Trafik dinleniyor...")
    last_processed_line = 0
    columns = None

    # Hem saldırıları hem de benign satırları sayabilmek için
    attack_counts = {}
    benign_count = 0  

    # buffer_df: 500 satırı tam yakalamak için tutulan gerçek veriler
    buffer_df = pd.DataFrame()

    while True:
        if not os.path.exists(file_to_watch):
            print("Dosya bulunamadı, yeniden kontrol ediliyor...")
            time.sleep(0.5)
            continue

        try:
            # CSV'deki kolon isimlerini henüz bilmiyorsak ilk satırdan çek
            if columns is None:
                temp_df = pd.read_csv(file_to_watch, nrows=1)
                columns = temp_df.columns.tolist()

            # Her seferinde chunk_size kadar satır oku
            new_data = pd.read_csv(
                file_to_watch,
                header=0,
                names=columns,
                skiprows=range(1, last_processed_line + 1),
                nrows=chunk_size
            )

            if new_data.empty:
                time.sleep(0.1)
                continue

            new_index_start = last_processed_line + 1
            new_index_end = last_processed_line + len(new_data)
            new_data.index = range(new_index_start, new_index_end + 1)
            last_processed_line += len(new_data)

            # Tampon DataFrame'e ekle
            buffer_df = pd.concat([buffer_df, new_data], ignore_index=False)

            # Satır bazında analiz
            for idx, row in new_data.iterrows():
                cleaned_df = veri_temizleme(row)
                tahmin_sonuclari = model_tahmin(cleaned_df, idx)
                max_attack_type = max(tahmin_sonuclari, key=tahmin_sonuclari.get)
                max_prob = tahmin_sonuclari[max_attack_type]

                if max_prob >= thresholds[max_attack_type]:
                    attack_counts[max_attack_type] = attack_counts.get(max_attack_type, 0) + 1
                else:
                    benign_count += 1

                # Şu anki **toplam satır** sayısı = saldırıların toplamı + benign_count
                total_lines = sum(attack_counts.values()) + benign_count

                # 500'e tam ulaşınca blok işlemini yap
                if total_lines == 500:
                    block = buffer_df.iloc[:500].copy()

                    with open(output_file, 'a') as f:
                        f.write("---------\n")
                        f.write(f"Toplam 500 satır incelendi.\n")
                        f.write("Saldırı sayıları:\n")
                        for attack, count in attack_counts.items():
                            f.write(f"- {attack}: {count} kez\n")
                        f.write(f"Benign: {benign_count} kez\n")
                        f.write("---------\n")

                    # En çok tespit edilen saldırı
                    if attack_counts:
                        most_detected_attack = max(attack_counts, key=attack_counts.get)
                        yeniden_degerlendirme(block, most_detected_attack, output_file)

                    # İlk 500 satırı buffer_df’ten at
                    buffer_df = buffer_df.iloc[500:].copy()

                    # Sayaçları sıfırla
                    attack_counts = {}
                    benign_count = 0

        except pd.errors.EmptyDataError:
            time.sleep(0.1)
        except Exception as e:
            print(f"Hata: {e}")
            time.sleep(0.1)


file_to_watch = os.path.join(BASE_DIR, "attack.csv")
output_file = os.path.join(BASE_DIR, "output.txt")
watch_for_changes(file_to_watch, output_file, chunk_size=100)
