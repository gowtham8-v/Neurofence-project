import sys
import time

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox
)

from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class NeuroFenceGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NeuroFence")
        self.resize(1100, 700)

        self.setup_ui()

    def setup_ui(self):

        main_layout = QVBoxLayout()

        # -----------------------------
        # Title
        # -----------------------------
        title = QLabel("🛡 NeuroFence AI Security Scanner")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        main_layout.addWidget(title)

        # -----------------------------
        # Model Selection
        # -----------------------------
        model_layout = QHBoxLayout()

        model_label = QLabel("Model :")

        self.model_box = QComboBox()
        self.model_box.addItem("DistilGPT2")

        model_layout.addWidget(model_label)
        model_layout.addWidget(self.model_box)
        model_layout.addStretch()

        main_layout.addLayout(model_layout)

        # -----------------------------
        # Prompt Panel
        # -----------------------------
        prompt_layout = QVBoxLayout()

        prompt_title = QLabel("Prompt")

        self.prompt_box = QTextEdit()
        self.prompt_box.setPlaceholderText(
            "Enter your prompt here..."
        )

        prompt_layout.addWidget(prompt_title)
        prompt_layout.addWidget(self.prompt_box)

        # -----------------------------
        # Response Panel
        # -----------------------------
        response_layout = QVBoxLayout()

        response_title = QLabel("Generated Response")

        self.response_box = QTextEdit()
        self.response_box.setReadOnly(True)

        response_layout.addWidget(response_title)
        response_layout.addWidget(self.response_box)

        # -----------------------------
        # Two Panel Layout
        # -----------------------------
        panels = QHBoxLayout()

        panels.addLayout(prompt_layout)
        panels.addLayout(response_layout)

        main_layout.addLayout(panels)

        # -----------------------------
        # Scan Button
        # -----------------------------
        self.scan_button = QPushButton("🔍 Scan Prompt")
        self.scan_button.clicked.connect(self.fake_scan)

        main_layout.addWidget(self.scan_button)

        # -----------------------------
        # Status
        # -----------------------------
        self.status_label = QLabel("Status : Ready")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

    def fake_scan(self):

        self.status_label.setText("Status : Scanning...")
        QApplication.processEvents()

        time.sleep(1)

        self.response_box.setPlainText(
            "Scanner module will be implemented in the next commit."
        )

        self.status_label.setText("Status : Ready")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = NeuroFenceGUI()
    window.show()

    sys.exit(app.exec())