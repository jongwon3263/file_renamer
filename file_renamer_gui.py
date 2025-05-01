import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QListWidget, QMessageBox
)

class FileRenamer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('폴더 기반 파일 이름 변경기')
        self.setGeometry(300, 300, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel('변경할 폴더를 선택하세요.')
        layout.addWidget(self.label)

        self.btn_select_folder = QPushButton('폴더 선택')
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)

        self.btn_rename = QPushButton('이름 변경 실행')
        self.btn_rename.clicked.connect(self.rename_files)
        self.btn_rename.setEnabled(False)
        layout.addWidget(self.btn_rename)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "폴더 선택", os.getcwd())
        if folder:
            self.directory = folder
            self.label.setText(f"선택된 폴더: {folder}")
            self.btn_rename.setEnabled(True)

    def rename_files(self):
        self.list_widget.clear()
        if hasattr(self, 'directory'):
            try:
                for filename in os.listdir(self.directory):
                    parts = filename.split("_")
                    if len(parts) >= 3:
                        ext = os.path.splitext(filename)[1]
                        new_name = parts[-2] + ext
                        old_path = os.path.join(self.directory, filename)
                        new_path = os.path.join(self.directory, new_name)
                        os.rename(old_path, new_path)
                        self.list_widget.addItem(f"{filename} → {new_name}")
                QMessageBox.information(self, "완료", "파일 이름 변경이 완료되었습니다.")
            except Exception as e:
                QMessageBox.critical(self, "오류 발생", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileRenamer()
    ex.show()
    sys.exit(app.exec_())