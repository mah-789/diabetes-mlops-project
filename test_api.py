import requests

def main() -> None:
    url = "http://127.0.0.1:8000/predict"
    payload = {
        "age": 45,
        "urea": 4.2,
        "cr": 0.8,
        "hba1c": 5.7,
        "chol": 4.5,
        "tg": 1.2,
        "hdl": 1.1,
        "ldl": 2.8,
        "vldl": 0.5,
        "bmi": 24.5,
        "gender": "F",
    }

    response = requests.post(url, json=payload, timeout=10)
    print(response.status_code, response.text)


if __name__ == "__main__":
    main()
