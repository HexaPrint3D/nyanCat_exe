import webview # Installiere dies mit: pip install pywebview

def start_nyan():
    # Die offizielle Seite liefert Animation + Musik in einem Guss
    url = 'https://www.nyan.cat/index.php?cat=original'
    
    # Erstellt ein separates Fenster ohne Browser-Leisten
    window = webview.create_window(
        'Nyaning', 
        url, 
        width=800, 
        height=600, 
        resizable=True
    )
    webview.start()

if __name__ == '__main__':
    start_nyan()
