from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class JanelaPrincipal(QMainWindow):
  def __init__(self, *args, **kwargs):
    super(JanelaPrincipal, self).__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("https://www.google.com"))
    self.setCentralWidget(self.browser)
    self.show()

app = QApplication(['', '--no-sandbox'])
window = JanelaPrincipal()
app.exec_()
