import sys
import networkx as nx


from simpleperf_report_lib import ReportLib

thread_cache = []

class LibSet(object):
    """ Collection of shared libraries used in perf.data. """

    def __init__(self):
        self.lib_name_to_id: Dict[str, int] = {}
        self.libs: List[LibInfo] = []

    def get_lib_id(self, lib_name: str) -> Optional[int]:
        return self.lib_name_to_id.get(lib_name)

    def add_lib(self, lib_name: str, build_id: str) -> int:
        """ Return lib_id of the newly added lib. """
        lib_id = len(self.libs)
        self.libs.append(LibInfo(lib_name, build_id))
        self.lib_name_to_id[lib_name] = lib_id
        return lib_id

    def get_lib(self, lib_id: int) -> LibInfo:
        return self.libs[lib_id]


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
    callstack = []
    while True:
        sample = lib.GetNextSample()
        if sample is None:
            lib.Close()
            break
        event = lib.GetEventOfCurrentSample()
        symbol = lib.GetSymbolOfCurrentSample()
        callchain = lib.GetCallChainOfCurrentSample()
        symbols = []
        # symbol_name replace for chain.nr entries[i].symbol
        # thread_cache .tid
        for i in range(callchain.nr):
            entry = callchain.entries[i]
            symbols.append(callchain.entries[i].symbol)
            callstack.append((lib_id, func_id, symbol.vaddr_in_file))

        thread.add_callstack(raw_sample.period, callstack, self.build_addr_hit_map)
    pass

if __name__ == "__main__":
    record_file = sys.argv[1]
    output_path = sys.argv[2]
    #binary_cache
    symfs_dir = None
    get_data(record_file, symfs_dir)



