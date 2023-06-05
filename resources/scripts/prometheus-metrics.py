import requests
import json

def get_prometheus_metrics(url):
    # Tworzenie zapytania do Prometheus API
    response = requests.get(url)
    data = response.json()

    # Przetwarzanie danych odpowiedzi
    metrics = []
    for result in data['data']['result']:
        metric = result['metric']
        value = result['value']
        metrics.append({
            'metric': metric,
            'value': value
        })

    return metrics

def save_metrics_to_file(metrics, file_path):
    # Zapisywanie metryk do pliku
    with open(file_path, 'w') as file:
        json.dump(metrics, file)

# Ustawienia Prometheus i pliku
query_name = 'kafka_topic_partitions'
prometheus_url = f'http://localhost:9090/api/v1/query?query={query_name}'
output_file = '../scripts/prometheus_metrics.json'

# Pobieranie metryk z Prometheus i zapisywanie ich do pliku
metrics = get_prometheus_metrics(prometheus_url)
save_metrics_to_file(metrics, output_file)

print('Metryki zostały zapisane w pliku:', output_file)
