# 第一个函数saveImage ————————————————————————————————————————————————————————————————————————————————————————————
def saveImage(self):
    current_index = self.tab_widget.currentIndex()
    if current_index != -1:
        figure = self.figures[current_index]
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;All Files (*)",
                                                   options=options)
        if file_name:
            try:
                figure.savefig(file_name)
                print(f"Image saved to {file_name}")
            except Exception as e:
                print(f"Error saving the image: {e}")


# 第二个函数updateTable ————————————————————————————————————————————————————————————————————————————————————————————
def updateTable(self, data, index):
    table_widget = self.table_widgets[index]
    table_widget.setRowCount(len(data))
    table_widget.setColumnCount(len(data[0]))
    table_widget.setHorizontalHeaderLabels(['W', 'L', 'Recip_Sqrt', 'Sig_Mis_Vtlin', 'Sig_Recip_Sqrt'])

    for row in data:
        for i in [2, 3, 4]:  # Format specific columns
            try:
                num = float(row[i])
                row[i] = f"{num:.3f}"
            except ValueError:
                continue

    for row in range(len(data)):
        for col in range(len(data[0])):
            table_widget.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    table_widget.resizeColumnsToContents()  # Auto-adjust column width

# 第三个函数copyAll  （for table widget）————————————————————————————————————————————————————————————————————————————————————————————
def copyAll(self):
    table = self.table_widgets[self.tab_widget.currentIndex()]
    copied_text = ""

    # Copy header
    header_labels = []
    for col in range(table.columnCount()):
        header_labels.append(table.horizontalHeaderItem(col).text())
    copied_text += "\t".join(header_labels) + "\n"

    # Copy all data
    for row in range(table.rowCount()):
        row_text = ""
        for col in range(table.columnCount()):
            item = table.item(row, col)
            if item is not None:
                row_text += item.text() + "\t"
            else:
                row_text += "\t"
        copied_text += row_text.strip() + "\n"

    QApplication.clipboard().setText(copied_text.strip())


# 第四个函数showContextMenu,通过右键实现copyAll ————————————————————————————————————————————————————————————————————————————————————————————
def showContextMenu(self, pos):
    table = self.table_widgets[self.tab_widget.currentIndex()]
    context_menu = QMenu(self)
    copy_action = QAction("Copy", self)
    copy_action.triggered.connect(self.copyAll)
    context_menu.addAction(copy_action)
    context_menu.exec_(table.viewport().mapToGlobal(pos))



