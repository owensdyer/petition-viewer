import requests
import json

def get_petition(petition_id):
    url = "https://petition.parliament.uk/petitions/" + str(petition_id) + ".json"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)


def main() -> None:
    data = get_petition(700143)
    print(data['data']['attributes']['action'])

if __name__ == '__main__':
    main()