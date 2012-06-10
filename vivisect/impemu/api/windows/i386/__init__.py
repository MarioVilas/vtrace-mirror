
import ntdll
import kernel32

api_defs = {}
api_defs.update(ntdll.api_defs)
api_defs.update(kernel32.api_defs)

def getImportApi(impname):
    impname = impname.lower()
    return api_defs.get(impname)

