import sys
import networkx as nx


from simpleperf_report_lib import ReportLib


class LibtSet(object):
    def __init__(self):
        self.name = {}
        self.t1 = []
    
    def ppp(self):
        pass

def get_data(record_file, binary_cache):
    lib = ReportLib()
    lib.SetRecordFile(record_file)
    lib.ShowIpForUnknownSymbol()
    lib.ShowArtFrames()
    lib.SetSymfs()
    libs = LibtSet()

    lib.MetaInfo()
    lib.GetRecordCmd()
    lib.GetArch()

    pass

if __name__ == "main":
    record_file = sys.argv[0]
    output_path = sys.argv[1]
    #binary_cache
    binary_cache = ''
    get_data(record_file, binary_cache)



