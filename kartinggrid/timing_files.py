from pandas import read_html


class TimingFileInterface:

    def __init__(self, file=None):
        self.source_file = file
        self.data = self.build_data()
        pass

    def build_data(self):
        pass


class BasicTimingFile(TimingFileInterface):

    def __init__(self, file=None):
        super().__init__(file)

    def build_data(self):
        return 1


class HTMLTimingFile(TimingFileInterface):

    def __init__(self, file):
        super().__init__(file)

    def build_data():
        read_html(super().source_file)
