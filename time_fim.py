import sys
import networkx as nx


from simpleperf_report_lib import ReportLib


class LibtSet(object):
    def __init__(self):
        self.name = {}
        self.t1 = []
    
    def ppp(self):
        pass

def get_data(record_file, symfs_dir):
    print(record_file)
    lib = ReportLib()
    lib.SetRecordFile(record_file)
    lib.ShowIpForUnknownSymbol()
    lib.ShowArtFrames()
    if symfs_dir:
        lib.SetSymfs(symfs_dir)
    libs = LibtSet()

    print(lib.MetaInfo())
    print(lib.GetRecordCmd())
    print(lib.GetArch())
    call_stakk = []
    while True:
        current_sample = lib.GetNextSample()
        if not current_sample:
            break



    pass

if __name__ == "__main__":
    record_file = sys.argv[1]
    output_path = sys.argv[2]
    #binary_cache
    symfs_dir = None
    get_data(record_file, symfs_dir)



