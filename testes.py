import pandas as pd

# Créer des données fictives
data = {
    "Mot": ["Bonjour", "Hello", "Hola", "Ciao", "Danke", "Grazie"],
    "Langue": ["Français", "Anglais", "Espagnol", "Italien", "Allemand", "Italien"],
    "Code Langue": ["fr", "en", "es", "it", "de", "it"],
    "Prononciation (audio)": ["audio_bonjour.mp3", "audio_hello.mp3", "audio_hola.mp3", "audio_ciao.mp3", "audio_danke.mp3", "audio_grazie.mp3"],
    "Image (illustrative)": ["image_bonjour.jpg", "image_hello.jpg", "image_hola.jpg", "image_ciao.jpg", "image_danke.jpg", "image_grazie.jpg"]
}

# Créer un DataFrame
df = pd.DataFrame(data)

# Enregistrer dans un fichier Excel
df.to_excel("mots_fictifs.xlsx", index=False)
