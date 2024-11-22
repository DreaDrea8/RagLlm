import dropbox
import pdfplumber
import os

# Token Dropbox
DROPBOX_TOKEN = "sl.CBOrH5I-Z0DmGTM12cP7gtAlmqKcv69DAHku226rKsMnJgd9gbUeZVoPRrPLYLZMDoS5ssKyCPg07ECzrhWGTXvGhXsFi3pT0XBG54GT8kDZmytzZVU2vx1UumEPpWhBknVGA6Ymkhdv"
DROPBOX_FILE_PATH = "/chatbot_docs/29-Le-Petit-Prince-Puisque-cest-ma-rose.pdf"  # Chemin du fichier dans Dropbox
LOCAL_TEMP_FILE = "temp.pdf"  # Fichier temporaire local
TEXT_FILE = "./petitprince.txt"  # Fichier texte généré

def download_file_from_dropbox(token, dropbox_path, local_path):
    """Télécharge un fichier depuis Dropbox."""
    try:
        dbx = dropbox.Dropbox(token)
        metadata, res = dbx.files_download(path=dropbox_path)
        with open(local_path, "wb") as f:
            f.write(res.content)
        print(f"Fichier téléchargé avec succès : {local_path}")
    except dropbox.exceptions.ApiError as e:
        print(f"Erreur lors du téléchargement depuis Dropbox : {e}")

def extract_text_from_pdf(pdf_path, txt_path):
    """Extrait le texte d'un fichier PDF et le sauvegarde dans un fichier texte."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                for page in pdf.pages:
                    txt_file.write(page.extract_text() + '\n')
        print("Le texte a été extrait et sauvegardé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'extraction de texte : {e}")

def main():
    # Télécharger le fichier PDF depuis Dropbox
    download_file_from_dropbox(DROPBOX_TOKEN, DROPBOX_FILE_PATH, LOCAL_TEMP_FILE)
    
    # Extraire le texte et le sauvegarder
    extract_text_from_pdf(LOCAL_TEMP_FILE, TEXT_FILE)
    
    # Supprimer le fichier temporaire
    if os.path.exists(LOCAL_TEMP_FILE):
        os.remove(LOCAL_TEMP_FILE)
        print("Fichier temporaire supprimé.")

if __name__ == "__main__":
    main()
