from bs4 import BeautifulSoup

def run_bs4_demo():
    # Парсинг та очищення текстового вмісту з HTML коду
    raw_html = "<div class='content'><p>Студент виконав роботу успішно.</p></div>"
    soup = BeautifulSoup(raw_html, "html.parser")
    return f"[beautifulsoup4] Знайдено чистий текст у тегах HTML: '{soup.find('p').text}'"
