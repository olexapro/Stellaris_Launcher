import sys
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from otherClasses import Table, TableData, Mod


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # elements
        self.table = Table()
        self.table_dt = TableData(self)
        self.mod_list = []

        play_button = QtWidgets.QPushButton('Play')
        play_button.setFlat(True)
        # play_button.clicked.connect()

        load_btn = QtWidgets.QPushButton('Load')
        load_btn.setFlat(True)
        load_btn.clicked.connect(self.table_dt.fill_data)
        settings = QtWidgets.QPushButton('settings')
        settings.setFlat(True)

        # window proprieties
        self.setMinimumSize(QtCore.QSize(self.width(), self.height()))
        self.setWindowIcon(QtGui.QIcon('img\\ico1.png'))
        self.setWindowTitle('Stellaris Launcher 2.4 by yohko')

        vbox = QtWidgets.QVBoxLayout()
        wdg = QtWidgets.QWidget()

        vbox.addWidget(self.table)
        vbox.addWidget(load_btn)
        vbox.addWidget(play_button)
        vbox.addWidget(settings)
        wdg.setLayout(vbox)

        self.setCentralWidget(wdg)
        self.mods_registry = self.load_fd('mods_registry.json')
        self.mod_list = self.get_md()
        self.table_dt.fill_data()

    @staticmethod
    def load_fd(name, dir=r'Stellaris Launcher/'):
        with open(dir+name, 'r', encoding='utf_8') as data:
            b = json.load(data)
            # print(b)
        return b

    # def get_md(self):
    #     mod_list = []
    #     for mod_hash, data in self.mods_registry.items():
    #         print(mod_hash, data)
    #         mod_l = ['mod_hash', 'gameRegistryId', 'source', 'steamId', 'displayName', 'tags', 'requiredVersion',
    #                  'archivePath', 'status', 'Mid', 'timeUpdated', 'thumbnailUrl', 'dirPath', 'thumbnailPath']
    #         # mod_list.append(mod)
    #
    #         for j in data:
    #             for i in mod_l:
    #                 a = self.pack_u(mod_l[i], data[j])
    #                 a.append(a)
    #     return mod_list

    @staticmethod
    def pack_u(par, data):
        try:
            par = data[str(f'{par}')]
        except KeyError:
            par = ' - '
        return par


#  на случай если программа запускается из оболочки
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
