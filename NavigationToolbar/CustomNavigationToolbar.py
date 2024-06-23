# 改写NavigationToolbar，使得可以保存高清图片
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QFileDialog


class CustomNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas, parent):
        super().__init__(canvas, parent)

    def save_figure(self, *args):
        # 默认保存的文件格式和 DPI
        default_format = 'png'
        default_dpi = 300

        # 打开文件对话框
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   f"Images (*.{default_format});;All Files (*)")

        if file_path:
            if not file_path.endswith(f".{default_format}"):
                file_path += f".{default_format}"
            self.canvas.figure.savefig(file_path, format=default_format, dpi=default_dpi)
            print(f"Image saved to {file_path}")
