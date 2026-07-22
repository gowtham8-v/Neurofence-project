import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class NeuroFenceGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NeuroFence")
        self.resize(900, 600)

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout()

        # Title
        title = QLabel("🛡 NeuroFence")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        layout.addWidget(title)

        # Prompt label
        prompt_label = QLabel("Prompt")
        prompt_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        layout.addWidget(prompt_label)

        # Prompt input
        self.prompt_box = QTextEdit()
        self.prompt_box.setPlaceholderText(
            "Enter your prompt here..."
        )
        self.prompt_box.setMinimumHeight(250)
        layout.addWidget(self.prompt_box)

        # Scan button
        self.scan_button = QPushButton("🔍 Scan Prompt")
        self.scan_button.clicked.connect(self.fake_scan)
        layout.addWidget(self.scan_button)

        # Status label
        self.status_label = QLabel("Status : Ready")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def fake_scan(self):
        self.status_label.setText("Status : Scanning...")
        QApplication.processEvents()

        self.status_label.setText("Status : Ready")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = NeuroFenceGUI()
    window.show()

    sys.exit(app.exec())