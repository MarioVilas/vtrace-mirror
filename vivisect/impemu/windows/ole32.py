from vivisect.impemu.impmagic import *
import vivisect.impemu.emufunc as emufunc

import ntdll

#EMUFUNC:BindMoniker
class BindMoniker(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CLIPFORMAT_UserFree
class CLIPFORMAT_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLIPFORMAT_UserMarshal
class CLIPFORMAT_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLIPFORMAT_UserSize
class CLIPFORMAT_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLIPFORMAT_UserUnmarshal
class CLIPFORMAT_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLSIDFromOle1Class
class CLSIDFromOle1Class(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLSIDFromProgID
class CLSIDFromProgID(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CLSIDFromProgIDEx
class CLSIDFromProgIDEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLSIDFromString
class CLSIDFromString(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoAddRefServerProcess
class CoAddRefServerProcess(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoAllowSetForegroundWindow
class CoAllowSetForegroundWindow(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoBuildVersion
class CoBuildVersion(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoCancelCall
class CoCancelCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoCopyProxy
class CoCopyProxy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoCreateFreeThreadedMarshaler
class CoCreateFreeThreadedMarshaler(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoCreateGuid
class CoCreateGuid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoCreateInstance
class CoCreateInstance(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ["rclsid", "pUnkOuter", "dsClsContext", "riid", "ppv"]
    __argt__ = [ntdll.CLSID, Pointer, ntdll.DWORD, ntdll.IID, Pointer, ]
#EMUFUNCDONE

    #def __call__(self, emu):

#EMUFUNC:CoCreateInstanceEx
class CoCreateInstanceEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoCreateObjectInContext
class CoCreateObjectInContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoDeactivateObject
class CoDeactivateObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoDisableCallCancellation
class CoDisableCallCancellation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoDisconnectObject
class CoDisconnectObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoDosDateTimeToFileTime
class CoDosDateTimeToFileTime(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoEnableCallCancellation
class CoEnableCallCancellation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoFileTimeNow
class CoFileTimeNow(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoFileTimeToDosDateTime
class CoFileTimeToDosDateTime(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoFreeAllLibraries
class CoFreeAllLibraries(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoFreeUnusedLibraries
class CoFreeUnusedLibraries(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoFreeUnusedLibrariesEx
class CoFreeUnusedLibrariesEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetApartmentID
class CoGetApartmentID(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetCallContext
class CoGetCallContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetCallerTID
class CoGetCallerTID(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetCancelObject
class CoGetCancelObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetClassObject
class CoGetClassObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetClassVersion
class CoGetClassVersion(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetComCatalog
class CoGetComCatalog(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetContextToken
class CoGetContextToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetCurrentLogicalThreadId
class CoGetCurrentLogicalThreadId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetCurrentProcess
class CoGetCurrentProcess(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoGetDefaultContext
class CoGetDefaultContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetInstanceFromFile
class CoGetInstanceFromFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetInstanceFromIStorage
class CoGetInstanceFromIStorage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetInterceptor
class CoGetInterceptor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetInterceptorFromTypeInfo
class CoGetInterceptorFromTypeInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetInterfaceAndReleaseStream
class CoGetInterfaceAndReleaseStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetMalloc
class CoGetMalloc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetMarshalSizeMax
class CoGetMarshalSizeMax(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetObject
class CoGetObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetObjectContext
class CoGetObjectContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetPSClsid
class CoGetPSClsid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetProcessIdentifier
class CoGetProcessIdentifier(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetStandardMarshal
class CoGetStandardMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetState
class CoGetState(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetStdMarshalEx
class CoGetStdMarshalEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoGetSystemSecurityPermissions
class CoGetSystemSecurityPermissions(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoGetTreatAsClass
class CoGetTreatAsClass(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoImpersonateClient
class CoImpersonateClient(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoInitialize
class CoInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoInitializeEx
class CoInitializeEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoInitializeSecurity
class CoInitializeSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'dwAllocFlags', None, None, None, None, None, None, None]
    __argt__ = [Pointer, ntdll.DWORD, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoInitializeWOW
class CoInitializeWOW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoInstall
class CoInstall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoInvalidateRemoteMachineBindings
class CoInvalidateRemoteMachineBindings(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoIsHandlerConnected
class CoIsHandlerConnected(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoIsOle1Class
class CoIsOle1Class(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoLoadLibrary
class CoLoadLibrary(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoLockObjectExternal
class CoLockObjectExternal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoMarshalHresult
class CoMarshalHresult(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoMarshalInterThreadInterfaceInStream
class CoMarshalInterThreadInterfaceInStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoMarshalInterface
class CoMarshalInterface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoPopServiceDomain
class CoPopServiceDomain(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoPushServiceDomain
class CoPushServiceDomain(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoQueryAuthenticationServices
class CoQueryAuthenticationServices(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoQueryClientBlanket
class CoQueryClientBlanket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoQueryProxyBlanket
class CoQueryProxyBlanket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoQueryReleaseObject
class CoQueryReleaseObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoReactivateObject
class CoReactivateObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRegisterChannelHook
class CoRegisterChannelHook(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRegisterClassObject
class CoRegisterClassObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRegisterInitializeSpy
class CoRegisterInitializeSpy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRegisterMallocSpy
class CoRegisterMallocSpy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRegisterMessageFilter
class CoRegisterMessageFilter(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRegisterPSClsid
class CoRegisterPSClsid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRegisterSurrogate
class CoRegisterSurrogate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRegisterSurrogateEx
class CoRegisterSurrogateEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoReleaseMarshalData
class CoReleaseMarshalData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoReleaseServerProcess
class CoReleaseServerProcess(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoResumeClassObjects
class CoResumeClassObjects(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoRetireServer
class CoRetireServer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRevertToSelf
class CoRevertToSelf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoRevokeClassObject
class CoRevokeClassObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRevokeInitializeSpy
class CoRevokeInitializeSpy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoRevokeMallocSpy
class CoRevokeMallocSpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoSetCancelObject
class CoSetCancelObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoSetProxyBlanket
class CoSetProxyBlanket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoSetState
class CoSetState(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoSuspendClassObjects
class CoSuspendClassObjects(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoSwitchCallContext
class CoSwitchCallContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoTaskMemAlloc
class CoTaskMemAlloc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoTaskMemFree
class CoTaskMemFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoTaskMemRealloc
class CoTaskMemRealloc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoTestCancel
class CoTestCancel(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoTreatAsClass
class CoTreatAsClass(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoUninitialize
class CoUninitialize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CoUnloadingWOW
class CoUnloadingWOW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoUnmarshalHresult
class CoUnmarshalHresult(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CoUnmarshalInterface
class CoUnmarshalInterface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CoWaitForMultipleHandles
class CoWaitForMultipleHandles(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_AddRef
class ComPs_CStdStubBuffer_AddRef(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_Connect
class ComPs_CStdStubBuffer_Connect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_CountRefs
class ComPs_CStdStubBuffer_CountRefs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_DebugServerQueryInterface
class ComPs_CStdStubBuffer_DebugServerQueryInterface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_DebugServerRelease
class ComPs_CStdStubBuffer_DebugServerRelease(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_Disconnect
class ComPs_CStdStubBuffer_Disconnect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_Invoke
class ComPs_CStdStubBuffer_Invoke(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_IsIIDSupported
class ComPs_CStdStubBuffer_IsIIDSupported(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_CStdStubBuffer_QueryInterface
class ComPs_CStdStubBuffer_QueryInterface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrCStdStubBuffer2_Release
class ComPs_NdrCStdStubBuffer2_Release(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrCStdStubBuffer_Release
class ComPs_NdrCStdStubBuffer_Release(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrClientCall2
class ComPs_NdrClientCall2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrClientCall2_va
class ComPs_NdrClientCall2_va(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrDllCanUnloadNow
class ComPs_NdrDllCanUnloadNow(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrDllGetClassObject
class ComPs_NdrDllGetClassObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrDllRegisterProxy
class ComPs_NdrDllRegisterProxy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrDllUnregisterProxy
class ComPs_NdrDllUnregisterProxy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrStubCall2
class ComPs_NdrStubCall2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComPs_NdrStubForwardingFunction
class ComPs_NdrStubForwardingFunction(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateAntiMoniker
class CreateAntiMoniker(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateBindCtx
class CreateBindCtx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CreateClassMoniker
class CreateClassMoniker(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDataAdviseHolder
class CreateDataAdviseHolder(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDataCache
class CreateDataCache(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateErrorInfo
class CreateErrorInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateFileMoniker
class CreateFileMoniker(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CreateGenericComposite
class CreateGenericComposite(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CreateILockBytesOnHGlobal
class CreateILockBytesOnHGlobal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CreateItemMoniker
class CreateItemMoniker(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CreateObjrefMoniker
class CreateObjrefMoniker(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateOleAdviseHolder
class CreateOleAdviseHolder(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePointerMoniker
class CreatePointerMoniker(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateStdProgressIndicator
class CreateStdProgressIndicator(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateStreamOnHGlobal
class CreateStreamOnHGlobal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:DcomChannelSetHResult
class DcomChannelSetHResult(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DllDebugObjectRPCHook
class DllDebugObjectRPCHook(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DllGetClassObject
class DllGetClassObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:DllGetClassObjectWOW
class DllGetClassObjectWOW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:DllRegisterServer
class DllRegisterServer(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:DoDragDrop
class DoDragDrop(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnableHookObject
class EnableHookObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FmtIdToPropStgName
class FmtIdToPropStgName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FreePropVariantArray
class FreePropVariantArray(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetClassFile
class GetClassFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetConvertStg
class GetConvertStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetDocumentBitStg
class GetDocumentBitStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetErrorInfo
class GetErrorInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetHGlobalFromILockBytes
class GetHGlobalFromILockBytes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetHGlobalFromStream
class GetHGlobalFromStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetHookInterface
class GetHookInterface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetRunningObjectTable
class GetRunningObjectTable(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:HACCEL_UserFree
class HACCEL_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HACCEL_UserMarshal
class HACCEL_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HACCEL_UserSize
class HACCEL_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HACCEL_UserUnmarshal
class HACCEL_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HBITMAP_UserFree
class HBITMAP_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HBITMAP_UserMarshal
class HBITMAP_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HBITMAP_UserSize
class HBITMAP_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HBITMAP_UserUnmarshal
class HBITMAP_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HBRUSH_UserFree
class HBRUSH_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HBRUSH_UserMarshal
class HBRUSH_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HBRUSH_UserSize
class HBRUSH_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HBRUSH_UserUnmarshal
class HBRUSH_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HDC_UserFree
class HDC_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HDC_UserMarshal
class HDC_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HDC_UserSize
class HDC_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HDC_UserUnmarshal
class HDC_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HENHMETAFILE_UserFree
class HENHMETAFILE_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HENHMETAFILE_UserMarshal
class HENHMETAFILE_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HENHMETAFILE_UserSize
class HENHMETAFILE_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HENHMETAFILE_UserUnmarshal
class HENHMETAFILE_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HGLOBAL_UserFree
class HGLOBAL_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HGLOBAL_UserMarshal
class HGLOBAL_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HGLOBAL_UserSize
class HGLOBAL_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HGLOBAL_UserUnmarshal
class HGLOBAL_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HICON_UserFree
class HICON_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HICON_UserMarshal
class HICON_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HICON_UserSize
class HICON_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HICON_UserUnmarshal
class HICON_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMENU_UserFree
class HMENU_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMENU_UserMarshal
class HMENU_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMENU_UserSize
class HMENU_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMENU_UserUnmarshal
class HMENU_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMETAFILEPICT_UserFree
class HMETAFILEPICT_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMETAFILEPICT_UserMarshal
class HMETAFILEPICT_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMETAFILEPICT_UserSize
class HMETAFILEPICT_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMETAFILEPICT_UserUnmarshal
class HMETAFILEPICT_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMETAFILE_UserFree
class HMETAFILE_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMETAFILE_UserMarshal
class HMETAFILE_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMETAFILE_UserSize
class HMETAFILE_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HMETAFILE_UserUnmarshal
class HMETAFILE_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HPALETTE_UserFree
class HPALETTE_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HPALETTE_UserMarshal
class HPALETTE_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HPALETTE_UserSize
class HPALETTE_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HPALETTE_UserUnmarshal
class HPALETTE_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HWND_UserFree
class HWND_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HWND_UserMarshal
class HWND_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HWND_UserSize
class HWND_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HWND_UserUnmarshal
class HWND_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HkOleRegisterObject
class HkOleRegisterObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IIDFromString
class IIDFromString(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsAccelerator
class IsAccelerator(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsEqualGUID
class IsEqualGUID(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidIid
class IsValidIid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidInterface
class IsValidInterface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidPtrIn
class IsValidPtrIn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidPtrOut
class IsValidPtrOut(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MkParseDisplayName
class MkParseDisplayName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MonikerCommonPrefixWith
class MonikerCommonPrefixWith(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MonikerRelativePathTo
class MonikerRelativePathTo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleBuildVersion
class OleBuildVersion(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:OleConvertIStorageToOLESTREAM
class OleConvertIStorageToOLESTREAM(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleConvertIStorageToOLESTREAMEx
class OleConvertIStorageToOLESTREAMEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, 'dwSize', None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ntdll.DWORD, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleConvertOLESTREAMToIStorage
class OleConvertOLESTREAMToIStorage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleConvertOLESTREAMToIStorageEx
class OleConvertOLESTREAMToIStorageEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleCreate
class OleCreate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateDefaultHandler
class OleCreateDefaultHandler(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateEmbeddingHelper
class OleCreateEmbeddingHelper(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateEx
class OleCreateEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateFromData
class OleCreateFromData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateFromDataEx
class OleCreateFromDataEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateFromFile
class OleCreateFromFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateFromFileEx
class OleCreateFromFileEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateLink
class OleCreateLink(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateLinkEx
class OleCreateLinkEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateLinkFromData
class OleCreateLinkFromData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateLinkFromDataEx
class OleCreateLinkFromDataEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateLinkToFile
class OleCreateLinkToFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateLinkToFileEx
class OleCreateLinkToFileEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateMenuDescriptor
class OleCreateMenuDescriptor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleCreateStaticFromData
class OleCreateStaticFromData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleDestroyMenuDescriptor
class OleDestroyMenuDescriptor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleDoAutoConvert
class OleDoAutoConvert(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleDraw
class OleDraw(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleDuplicateData
class OleDuplicateData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleFlushClipboard
class OleFlushClipboard(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:OleGetAutoConvert
class OleGetAutoConvert(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleGetClipboard
class OleGetClipboard(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleGetIconOfClass
class OleGetIconOfClass(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleGetIconOfFile
class OleGetIconOfFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleInitialize
class OleInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleInitializeWOW
class OleInitializeWOW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleIsCurrentClipboard
class OleIsCurrentClipboard(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleIsRunning
class OleIsRunning(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleLoad
class OleLoad(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleLoadFromStream
class OleLoadFromStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleLockRunning
class OleLockRunning(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleMetafilePictFromIconAndLabel
class OleMetafilePictFromIconAndLabel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleNoteObjectVisible
class OleNoteObjectVisible(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleQueryCreateFromData
class OleQueryCreateFromData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleQueryLinkFromData
class OleQueryLinkFromData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleRegEnumFormatEtc
class OleRegEnumFormatEtc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleRegEnumVerbs
class OleRegEnumVerbs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleRegGetMiscStatus
class OleRegGetMiscStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleRegGetUserType
class OleRegGetUserType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OleRun
class OleRun(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleSave
class OleSave(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleSaveToStream
class OleSaveToStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleSetAutoConvert
class OleSetAutoConvert(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleSetClipboard
class OleSetClipboard(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleSetContainedObject
class OleSetContainedObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleSetMenuDescriptor
class OleSetMenuDescriptor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleTranslateAccelerator
class OleTranslateAccelerator(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OleUninitialize
class OleUninitialize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:OpenOrCreateStream
class OpenOrCreateStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ProgIDFromCLSID
class ProgIDFromCLSID(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:PropStgNameToFmtId
class PropStgNameToFmtId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PropSysAllocString
class PropSysAllocString(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PropSysFreeString
class PropSysFreeString(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PropVariantChangeType
class PropVariantChangeType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PropVariantClear
class PropVariantClear(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:PropVariantCopy
class PropVariantCopy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ReadClassStg
class ReadClassStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ReadClassStm
class ReadClassStm(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ReadFmtUserTypeStg
class ReadFmtUserTypeStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ReadOleStg
class ReadOleStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ReadStringStream
class ReadStringStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegisterDragDrop
class RegisterDragDrop(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ReleaseStgMedium
class ReleaseStgMedium(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RevokeDragDrop
class RevokeDragDrop(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SNB_UserFree
class SNB_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SNB_UserMarshal
class SNB_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SNB_UserSize
class SNB_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SNB_UserUnmarshal
class SNB_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:STGMEDIUM_UserFree
class STGMEDIUM_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:STGMEDIUM_UserMarshal
class STGMEDIUM_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:STGMEDIUM_UserSize
class STGMEDIUM_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:STGMEDIUM_UserUnmarshal
class STGMEDIUM_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetConvertStg
class SetConvertStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetDocumentBitStg
class SetDocumentBitStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetErrorInfo
class SetErrorInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgConvertPropertyToVariant
class StgConvertPropertyToVariant(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgConvertVariantToProperty
class StgConvertVariantToProperty(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgCreateDocfile
class StgCreateDocfile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgCreateDocfileOnILockBytes
class StgCreateDocfileOnILockBytes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:StgCreatePropSetStg
class StgCreatePropSetStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgCreatePropStg
class StgCreatePropStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgCreateStorageEx
class StgCreateStorageEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgGetIFillLockBytesOnFile
class StgGetIFillLockBytesOnFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgGetIFillLockBytesOnILockBytes
class StgGetIFillLockBytesOnILockBytes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgIsStorageFile
class StgIsStorageFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgIsStorageILockBytes
class StgIsStorageILockBytes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgOpenAsyncDocfileOnIFillLockBytes
class StgOpenAsyncDocfileOnIFillLockBytes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgOpenPropStg
class StgOpenPropStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgOpenStorage
class StgOpenStorage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:StgOpenStorageEx
class StgOpenStorageEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgOpenStorageOnHandle
class StgOpenStorageOnHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgOpenStorageOnILockBytes
class StgOpenStorageOnILockBytes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:StgPropertyLengthAsVariant
class StgPropertyLengthAsVariant(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StgSetTimes
class StgSetTimes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StringFromCLSID
class StringFromCLSID(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:StringFromGUID2
class StringFromGUID2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StringFromIID
class StringFromIID(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UpdateDCOMSettings
class UpdateDCOMSettings(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:UtConvertDvtd16toDvtd32
class UtConvertDvtd16toDvtd32(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UtConvertDvtd32toDvtd16
class UtConvertDvtd32toDvtd16(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UtGetDvtd16Info
class UtGetDvtd16Info(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:UtGetDvtd32Info
class UtGetDvtd32Info(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WdtpInterfacePointer_UserFree
class WdtpInterfacePointer_UserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WdtpInterfacePointer_UserMarshal
class WdtpInterfacePointer_UserMarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WdtpInterfacePointer_UserSize
class WdtpInterfacePointer_UserSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WdtpInterfacePointer_UserUnmarshal
class WdtpInterfacePointer_UserUnmarshal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WriteClassStg
class WriteClassStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WriteClassStm
class WriteClassStm(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WriteFmtUserTypeStg
class WriteFmtUserTypeStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WriteOleStg
class WriteOleStg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WriteStringStream
class WriteStringStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:main_entry
class main_entry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

