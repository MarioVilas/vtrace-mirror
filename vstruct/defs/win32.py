
# FIXME this is named wrong!

import vstruct
from vstruct.primitives import *

@vstruct.structbuilder
def CLIENT_ID():
    x = vstruct.VStruct("CLIENT_ID")
    x.UniqueProcess = v_ptr()
    x.UniqueThread = v_ptr()
    return x

@vstruct.structbuilder
def EXCEPTION_RECORD():
    x = vstruct.VStruct("EXCEPTION_RECORD")
    x.ExceptionCode = v_uint32()
    x.ExceptionFlags = v_uint32()
    x.ExceptionRecord = v_ptr()
    x.ExceptionAddress = v_ptr()
    x.NumberParameters = v_uint32()
    return x

@vstruct.structbuilder
def EXCEPTION_REGISTRATION():
    x = vstruct.VStruct("EXCEPTION_REGISTRATION")
    x.prev = v_ptr()
    x.handler = v_ptr()
    return x

@vstruct.structbuilder
def HEAP():
    x = vstruct.VStruct("HEAP")
    x.Entry = HEAP_ENTRY()
    x.Signature = v_uint32()
    x.Flags = v_uint32()
    x.ForceFlags = v_uint32()
    x.VirtualMemoryThreshold = v_uint32()
    x.SegmentReserve = v_uint32()
    x.SegmentCommit = v_uint32()
    x.DeCommitFreeBlockThreshold = v_uint32()
    x.DeCommitTotalFreeThreshold = v_uint32()
    x.TotalFreeSize = v_uint32()
    x.MaximumAllocationSize = v_uint32()
    x.ProcessHeapsListIndex = v_uint16()
    x.HeaderValidateLength = v_uint16()
    x.HeaderValidateCopy = v_ptr()
    x.NextAvailableTagIndex = v_uint16()
    x.MaximumTagIndex = v_uint16()
    x.TagEntries = v_ptr()
    x.UCRSegments = v_ptr()
    x.UnusedUnCommittedRanges = v_ptr()
    x.AlignRound = v_uint32()
    x.AlignMask = v_uint32()
    x.VirtualAllocBlocks = ListEntry()
    x.Segments = vstruct.VArray([v_uint32() for i in range(64)])
    x.u = vstruct.VArray([v_uint8() for i in range(16)])
    x.u2 = vstruct.VArray([v_uint8() for i in range(2)])
    x.AllocatorBackTraceIndex = v_uint16()
    x.NonDedicatedListLength = v_uint32()
    x.LargeBlocksIndex = v_ptr()
    x.PseudoTagEntries = v_ptr()
    x.FreeLists = vstruct.VArray([ListEntry() for i in range(128)])
    x.LockVariable = v_uint32()
    x.CommitRoutine = v_ptr()
    x.FrontEndHeap = v_ptr()
    x.FrontEndHeapLockCount = v_uint16()
    x.FrontEndHeapType = v_uint8()
    x.LastSegmentIndex = v_uint8()
    return x

@vstruct.structbuilder
def HEAP_SEGMENT():
    x = vstruct.VStruct("HEAP_SEGMENT")
    x.Entry = HEAP_ENTRY()
    x.SegmentSignature = v_uint32()
    x.SegmentFlags = v_uint32()
    x.Heap = v_ptr()
    x.LargestUncommitedRange = v_uint32()
    x.BaseAddress = v_ptr()
    x.NumberOfPages = v_uint32()
    x.FirstEntry = v_ptr()
    x.LastValidEntry = v_ptr()
    x.NumberOfUnCommittedPages = v_uint32()
    x.NumberOfUnCommittedRanges = v_uint32()
    x.UncommittedRanges = v_ptr()
    x.SegmentAllocatorBackTraceIndex = v_uint16()
    x.Reserved = v_uint16()
    x.LastEntryInSegment = v_ptr()
    return x

@vstruct.structbuilder
def HEAP_ENTRY():
    x = vstruct.VStruct("HEAP_ENTRY")
    x.Size = v_uint16()
    x.PrevSize = v_uint16()
    x.SegmentIndex = v_uint8()
    x.Flags = v_uint8()
    x.Unused = v_uint8()
    x.TagIndex = v_uint8()
    return x

@vstruct.structbuilder
def ListEntry():
    x = vstruct.VStruct("ListEntry")
    x.Flink = v_ptr()
    x.Blink = v_ptr()
    return x

@vstruct.structbuilder
def NT_TIB():
    x = vstruct.VStruct("NT_TIB")
    x.ExceptionList = v_ptr()
    x.StackBase = v_ptr()
    x.StackLimit = v_ptr()
    x.SubSystemTib = v_ptr()
    x.FiberData = v_ptr()
    #x.Version = v_ptr() # This is a union field
    x.ArbitraryUserPtr = v_ptr()
    x.Self = v_ptr()
    return x

@vstruct.structbuilder
def PEB():
    x = vstruct.VStruct("PEB")
    x.InheritedAddressSpace = v_uint8()
    x.ReadImageFileExecOptions = v_uint8()
    x.BeingDebugged = v_uint8()
    x.SpareBool = v_uint8()
    x.Mutant = v_ptr()
    x.ImageBaseAddress = v_ptr()
    x.Ldr = v_ptr()
    x.ProcessParameters = v_ptr()
    x.SubSystemData = v_ptr()
    x.ProcessHeap = v_ptr()
    x.FastPebLock = v_ptr()
    x.FastPebLockRoutine = v_ptr()
    x.FastPebUnlockRoutine = v_ptr()
    x.EnvironmentUpdateCount = v_uint32()
    x.KernelCallbackTable = v_ptr()
    x.SystemReserved = v_uint32()
    x.AtlThunkSListPtr32 = v_ptr()
    x.FreeList = v_ptr()
    x.TlsExpansionCounter = v_uint32()
    x.TlsBitmap = v_ptr()
    x.TlsBitmapBits = vstruct.VArray([v_uint32() for i in range(2)])
    x.ReadOnlySharedMemoryBase = v_ptr()
    x.ReadOnlySharedMemoryHeap = v_ptr()
    x.ReadOnlyStaticServerData = v_ptr()
    x.AnsiCodePageData = v_ptr()
    x.OemCodePageData = v_ptr()
    x.UnicodeCaseTableData = v_ptr()
    x.NumberOfProcessors = v_uint32()
    x.NtGlobalFlag = v_uint64()
    x.CriticalSectionTimeout = v_uint64()
    x.HeapSegmentReserve = v_uint32()
    x.HeapSegmentCommit = v_uint32()
    x.HeapDeCommitTotalFreeThreshold = v_uint32()
    x.HeapDeCommitFreeBlockThreshold = v_uint32()
    x.NumberOfHeaps = v_uint32()
    x.MaximumNumberOfHeaps = v_uint32()
    x.ProcessHeaps = v_ptr()
    x.GdiSharedHandleTable = v_ptr()
    x.ProcessStarterHelper = v_ptr()
    x.GdiDCAttributeList = v_uint32()
    x.LoaderLock = v_ptr()
    x.OSMajorVersion = v_uint32()
    x.OSMinorVersion = v_uint32()
    x.OSBuildNumber = v_uint16()
    x.OSCSDVersion = v_uint16()
    x.OSPlatformId = v_uint32()
    x.ImageSubsystem = v_uint32()
    x.ImageSubsystemMajorVersion = v_uint32()
    x.ImageSubsystemMinorVersion = v_uint32()
    x.ImageProcessAffinityMask = v_uint32()
    x.GdiHandleBuffer = vstruct.VArray([v_ptr() for i in range(34)])
    x.PostProcessInitRoutine = v_ptr()
    x.TlsExpansionBitmap = v_ptr()
    x.TlsExpansionBitmapBits = vstruct.VArray([v_uint32() for i in range(32)])
    x.SessionId = v_uint32()
    x.AppCompatFlags = v_uint64()
    x.AppCompatFlagsUser = v_uint64()
    x.pShimData = v_ptr()
    x.AppCompatInfo = v_ptr()
    x.CSDVersion = v_ptr()
    x.UNKNOWN = v_uint32()
    x.ActivationContextData = v_ptr()
    x.ProcessAssemblyStorageMap = v_ptr()
    x.SystemDefaultActivationContextData = v_ptr()
    x.SystemAssemblyStorageMap = v_ptr()
    x.MinimumStackCommit = v_uint32()
    return x

@vstruct.structbuilder
def SEH3_SCOPETABLE():
    x = vstruct.VStruct("SEH3_SCOPETABLE")
    x.EnclosingLevel = v_int32()
    x.FilterFunction = v_ptr()
    x.HandlerFunction = v_ptr()
    return x

@vstruct.structbuilder
def SEH4_SCOPETABLE():
    x = vstruct.VStruct("SEH4_SCOPETABLE")
    x.GSCookieOffset = v_int32()
    x.GSCookieXOROffset = v_int32()
    x.EHCookieOffset = v_int32()
    x.EHCookieXOROffset = v_int32()
    x.EnclosingLevel = v_int32()
    x.FilterFunction = v_ptr()
    x.HandlerFunction = v_ptr()
    return x

@vstruct.structbuilder
def TEB():
    x = vstruct.VStruct("TEB")
    x.TIB = NT_TIB()
    x.EnvironmentPointer = v_ptr()
    x.ClientId = CLIENT_ID()
    x.ActiveRpcHandle = v_ptr()
    x.ThreadLocalStorage = v_ptr()
    x.ProcessEnvironmentBlock = v_ptr()
    x.LastErrorValue = v_uint32()
    x.CountOfOwnedCriticalSections = v_uint32()
    x.CsrClientThread = v_ptr()
    x.Win32ThreadInfo = v_ptr()
    x.User32Reserved = vstruct.VArray([v_uint32() for i in range(26)])
    x.UserReserved = vstruct.VArray([v_uint32() for i in range(5)])
    x.WOW32Reserved = v_ptr()
    x.CurrentLocale = v_uint32()
    x.FpSoftwareStatusRegister = v_uint32()
    return x

@vstruct.structbuilder
def CLSID():
    x = vstruct.VStruct("CLSID")
    x.uuid = GUID()
    return x

@vstruct.structbuilder
def IID():
    x = vstruct.VStruct("IID")
    x.uuid = GUID()
    return x

