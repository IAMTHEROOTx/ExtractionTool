import requests

nameofthefile = input("How you want to call your file: ")
url = input("Paste the website url here: ")

website_response = requests.get(url)

if website_response.status_code == 200:
    file_name = nameofthefile
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(website_response.text)
    
    print(f"Le contenu du site a été sauvegardé dans le fichier {file_name}.")
else:
    print(f"Erreur lors du téléchargement du site : {response.status_code}")