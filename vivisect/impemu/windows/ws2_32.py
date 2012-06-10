
import vivisect.impemu.emufunc as emufunc
from vivisect.impemu.impmagic import *

import ntdll

# FIXME make a unified socket thing

#EMUFUNC:FreeAddrInfoW
class FreeAddrInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetAddrInfoW
class GetAddrInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetNameInfoW
class GetNameInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WEP
class WEP(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WPUCompleteOverlappedRequest
class WPUCompleteOverlappedRequest(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAccept
class WSAAccept(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAddressToStringA
class WSAAddressToStringA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAddressToStringW
class WSAAddressToStringW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAsyncGetHostByAddr
class WSAAsyncGetHostByAddr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'dwSize', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ntdll.DWORD, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAsyncGetHostByName
class WSAAsyncGetHostByName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAsyncGetProtoByName
class WSAAsyncGetProtoByName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAsyncGetProtoByNumber
class WSAAsyncGetProtoByNumber(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAsyncGetServByName
class WSAAsyncGetServByName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAsyncGetServByPort
class WSAAsyncGetServByPort(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAAsyncSelect
class WSAAsyncSelect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSACancelAsyncRequest
class WSACancelAsyncRequest(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSACancelBlockingCall
class WSACancelBlockingCall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSACleanup
class WSACleanup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSACloseEvent
class WSACloseEvent(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['hObject']
    __argt__ = [HANDLE, ]
#EMUFUNCDONE

#EMUFUNC:WSAConnect
class WSAConnect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSACreateEvent
class WSACreateEvent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSADuplicateSocketA
class WSADuplicateSocketA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSADuplicateSocketW
class WSADuplicateSocketW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WSAEnumNameSpaceProvidersA
class WSAEnumNameSpaceProvidersA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAEnumNameSpaceProvidersW
class WSAEnumNameSpaceProvidersW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAEnumNetworkEvents
class WSAEnumNetworkEvents(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAEnumProtocolsA
class WSAEnumProtocolsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAEnumProtocolsW
class WSAEnumProtocolsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WSAEventSelect
class WSAEventSelect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAGetOverlappedResult
class WSAGetOverlappedResult(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAGetQOSByName
class WSAGetQOSByName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAGetServiceClassInfoA
class WSAGetServiceClassInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAGetServiceClassInfoW
class WSAGetServiceClassInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAGetServiceClassNameByClassIdA
class WSAGetServiceClassNameByClassIdA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAGetServiceClassNameByClassIdW
class WSAGetServiceClassNameByClassIdW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAHtonl
class WSAHtonl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAHtons
class WSAHtons(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAInstallServiceClassA
class WSAInstallServiceClassA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAInstallServiceClassW
class WSAInstallServiceClassW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAIoctl
class WSAIoctl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAIsBlocking
class WSAIsBlocking(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSAJoinLeaf
class WSAJoinLeaf(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSALookupServiceBeginA
class WSALookupServiceBeginA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WSALookupServiceBeginW
class WSALookupServiceBeginW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr']
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WSALookupServiceEnd
class WSALookupServiceEnd(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSALookupServiceNextA
class WSALookupServiceNextA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSALookupServiceNextW
class WSALookupServiceNextW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WSANSPIoctl
class WSANSPIoctl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['this', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSANtohl
class WSANtohl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSANtohs
class WSANtohs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAProviderConfigChange
class WSAProviderConfigChange(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSARecv
class WSARecv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSARecvDisconnect
class WSARecvDisconnect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSARecvFrom
class WSARecvFrom(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSARemoveServiceClass
class WSARemoveServiceClass(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAResetEvent
class WSAResetEvent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSASend
class WSASend(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSASendDisconnect
class WSASendDisconnect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSASendTo
class WSASendTo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSASetBlockingHook
class WSASetBlockingHook(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSASetEvent
class WSASetEvent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSASetLastError
class WSASetLastError(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSASetServiceA
class WSASetServiceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSASetServiceW
class WSASetServiceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSASocketA
class WSASocketA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSASocketW
class WSASocketW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAStartup
class WSAStartup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WSAStringToAddressA
class WSAStringToAddressA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSAStringToAddressW
class WSAStringToAddressW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr', 'ptr']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WSAUnhookBlockingHook
class WSAUnhookBlockingHook(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSAWaitForMultipleEvents
class WSAWaitForMultipleEvents(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:WSApSetPostRoutine
class WSApSetPostRoutine(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCDeinstallProvider
class WSCDeinstallProvider(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCEnableNSProvider
class WSCEnableNSProvider(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCEnumProtocols
class WSCEnumProtocols(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCGetProviderPath
class WSCGetProviderPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCInstallNameSpace
class WSCInstallNameSpace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCInstallProvider
class WSCInstallProvider(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCUnInstallNameSpace
class WSCUnInstallNameSpace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCUpdateProvider
class WSCUpdateProvider(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCWriteNameSpaceOrder
class WSCWriteNameSpaceOrder(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WSCWriteProviderOrder
class WSCWriteProviderOrder(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:accept
class accept(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:bind
class bind(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:closesocket
class closesocket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:connect
class connect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:freeaddrinfo
class freeaddrinfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:getaddrinfo
class getaddrinfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:gethostbyaddr
class gethostbyaddr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:gethostbyname
class gethostbyname(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:gethostname
class gethostname(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getnameinfo
class getnameinfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getpeername
class getpeername(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getprotobyname
class getprotobyname(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getprotobynumber
class getprotobynumber(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getservbyname
class getservbyname(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getservbyport
class getservbyport(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getsockname
class getsockname(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getsockopt
class getsockopt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:htonl
class htonl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:htons
class htons(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:inet_addr
class inet_addr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:inet_ntoa
class inet_ntoa(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ioctlsocket
class ioctlsocket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:listen
class listen(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:main_entry
class main_entry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ntohl
class ntohl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ntohs
class ntohs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:recv
class recv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:recvfrom
class recvfrom(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:select
class select(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:send
class send(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:sendto
class sendto(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:setsockopt
class setsockopt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:shutdown
class shutdown(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:socket
class socket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

