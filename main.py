import requests


def  get_data():
     headers = {
       "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
     }

     for i in range(1, 49):
        url = f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            print(f"Downloaded {i} of 48")

def main():
    get_data()

if __name__=='--main--':
  main()


    