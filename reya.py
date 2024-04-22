import requests

def parse_data(wallet_address):
    url = f"https://api.reya.xyz/api/xp/xp-profile/{wallet_address}"
    try:
        response = requests.get(url)
        data = response.json()
        deposited_value = data.get("deposited")
        xp_data = data.get("xp", {})
        xp_value = xp_data.get("value")
        boost_value = data.get("currentBoost")
        if deposited_value is not None:
            return deposited_value, xp_value, boost_value
        else:
            return "Value not found"
    except Exception as e:
        return f"Error: {e}"

def main():
    # Чтение списка кошельков из файла
    with open("wallets.txt", "r") as file:
        wallets = file.read().splitlines()

    # Парсинг значений для каждого кошелька
    for wallet_address in wallets:
        parsed_data = parse_data(wallet_address)
        if isinstance(parsed_data, tuple):
            deposited, value, currentBoost = parsed_data
            print(f"Wallet: {wallet_address}, Deposited: {deposited}, XP: {value}, Boost: {currentBoost}")
        else:
            print(parsed_data)

if __name__ == "__main__":
    main()
