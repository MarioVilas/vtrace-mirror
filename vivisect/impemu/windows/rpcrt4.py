from vivisect.impemu.impmagic import *
import vivisect.impemu.emufunc as emufunc

import ntdll

#EMUFUNC:CStdStubBuffer_AddRef
class CStdStubBuffer_AddRef(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CStdStubBuffer_Connect
class CStdStubBuffer_Connect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CStdStubBuffer_CountRefs
class CStdStubBuffer_CountRefs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CStdStubBuffer_DebugServerQueryInterface
class CStdStubBuffer_DebugServerQueryInterface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CStdStubBuffer_DebugServerRelease
class CStdStubBuffer_DebugServerRelease(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CStdStubBuffer_Disconnect
class CStdStubBuffer_Disconnect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CStdStubBuffer_Invoke
class CStdStubBuffer_Invoke(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CStdStubBuffer_IsIIDSupported
class CStdStubBuffer_IsIIDSupported(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CStdStubBuffer_QueryInterface
class CStdStubBuffer_QueryInterface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CheckVerificationTrailer
class CheckVerificationTrailer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateProxyFromTypeInfo
class CreateProxyFromTypeInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateStubFromTypeInfo
class CreateStubFromTypeInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DceErrorInqTextA
class DceErrorInqTextA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DceErrorInqTextW
class DceErrorInqTextW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DllGetClassObject
class DllGetClassObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DllRegisterServer
class DllRegisterServer(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GlobalMutexClearExternal
class GlobalMutexClearExternal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GlobalMutexRequestExternal
class GlobalMutexRequestExternal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_RpcAllocate
class I_RpcAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['dwSize']
    __argt__ = [ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcAsyncAbortCall
class I_RpcAsyncAbortCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcAsyncSetHandle
class I_RpcAsyncSetHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBCacheAllocate
class I_RpcBCacheAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['dwSize']
    __argt__ = [ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBCacheFree
class I_RpcBCacheFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingCopy
class I_RpcBindingCopy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingHandleToAsyncHandle
class I_RpcBindingHandleToAsyncHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingInqConnId
class I_RpcBindingInqConnId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingInqDynamicEndpointA
class I_RpcBindingInqDynamicEndpointA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingInqDynamicEndpointW
class I_RpcBindingInqDynamicEndpointW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingInqLocalClientPID
class I_RpcBindingInqLocalClientPID(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingInqSecurityContext
class I_RpcBindingInqSecurityContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingInqTransportType
class I_RpcBindingInqTransportType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingInqWireIdForSnego
class I_RpcBindingInqWireIdForSnego(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingIsClientLocal
class I_RpcBindingIsClientLocal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcBindingToStaticStringBindingW
class I_RpcBindingToStaticStringBindingW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcConnectionInqSockBuffSize
class I_RpcConnectionInqSockBuffSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcConnectionSetSockBuffSize
class I_RpcConnectionSetSockBuffSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcDeleteMutex
class I_RpcDeleteMutex(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcEnableWmiTrace
class I_RpcEnableWmiTrace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcExceptionFilter
class I_RpcExceptionFilter(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcFree
class I_RpcFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcFreeBuffer
class I_RpcFreeBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcFreePipeBuffer
class I_RpcFreePipeBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcGetBuffer
class I_RpcGetBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcGetBufferWithObject
class I_RpcGetBufferWithObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcGetCurrentCallHandle
class I_RpcGetCurrentCallHandle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_RpcGetExtendedError
class I_RpcGetExtendedError(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_RpcIfInqTransferSyntaxes
class I_RpcIfInqTransferSyntaxes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcLogEvent
class I_RpcLogEvent(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcMapWin32Status
class I_RpcMapWin32Status(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcNegotiateTransferSyntax
class I_RpcNegotiateTransferSyntax(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcNsBindingSetEntryNameA
class I_RpcNsBindingSetEntryNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcNsBindingSetEntryNameW
class I_RpcNsBindingSetEntryNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcNsInterfaceExported
class I_RpcNsInterfaceExported(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcNsInterfaceUnexported
class I_RpcNsInterfaceUnexported(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcParseSecurity
class I_RpcParseSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcProxyNewConnection
class I_RpcProxyNewConnection(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcReallocPipeBuffer
class I_RpcReallocPipeBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcReceive
class I_RpcReceive(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcRequestMutex
class I_RpcRequestMutex(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcSend
class I_RpcSend(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcSendReceive
class I_RpcSendReceive(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerAllocateIpPort
class I_RpcServerAllocateIpPort(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerCheckClientRestriction
class I_RpcServerCheckClientRestriction(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerInqAddressChangeFn
class I_RpcServerInqAddressChangeFn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_RpcServerInqLocalConnAddress
class I_RpcServerInqLocalConnAddress(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerInqTransportType
class I_RpcServerInqTransportType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerRegisterForwardFunction
class I_RpcServerRegisterForwardFunction(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerSetAddressChangeFn
class I_RpcServerSetAddressChangeFn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerUseProtseq2A
class I_RpcServerUseProtseq2A(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerUseProtseq2W
class I_RpcServerUseProtseq2W(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerUseProtseqEp2A
class I_RpcServerUseProtseqEp2A(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcServerUseProtseqEp2W
class I_RpcServerUseProtseqEp2W(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcSessionStrictContextHandle
class I_RpcSessionStrictContextHandle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_RpcSsDontSerializeContext
class I_RpcSsDontSerializeContext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_RpcSystemFunction001
class I_RpcSystemFunction001(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTransConnectionAllocatePacket
class I_RpcTransConnectionAllocatePacket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'dwSize']
    __argt__ = [Unknown, ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTransConnectionFreePacket
class I_RpcTransConnectionFreePacket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'lpVoid']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTransConnectionReallocPacket
class I_RpcTransConnectionReallocPacket(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'dwSize']
    __argt__ = [Unknown, Unknown, Unknown, ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTransDatagramAllocate
class I_RpcTransDatagramAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTransDatagramAllocate2
class I_RpcTransDatagramAllocate2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTransDatagramFree
class I_RpcTransDatagramFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'lpVoid']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTransGetThreadEvent
class I_RpcTransGetThreadEvent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_RpcTransIoCancelled
class I_RpcTransIoCancelled(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTransServerNewConnection
class I_RpcTransServerNewConnection(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_RpcTurnOnEEInfoPropagation
class I_RpcTurnOnEEInfoPropagation(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_UuidCreate
class I_UuidCreate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MIDL_wchar_strcpy
class MIDL_wchar_strcpy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MIDL_wchar_strlen
class MIDL_wchar_strlen(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MesBufferHandleReset
class MesBufferHandleReset(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MesDecodeBufferHandleCreate
class MesDecodeBufferHandleCreate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MesDecodeIncrementalHandleCreate
class MesDecodeIncrementalHandleCreate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MesEncodeDynBufferHandleCreate
class MesEncodeDynBufferHandleCreate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MesEncodeFixedBufferHandleCreate
class MesEncodeFixedBufferHandleCreate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MesEncodeIncrementalHandleCreate
class MesEncodeIncrementalHandleCreate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MesHandleFree
class MesHandleFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MesIncrementalHandleReset
class MesIncrementalHandleReset(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MesInqProcEncodingId
class MesInqProcEncodingId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRCContextBinding
class NDRCContextBinding(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRCContextMarshall
class NDRCContextMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRCContextUnmarshall
class NDRCContextUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRSContextMarshall
class NDRSContextMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRSContextMarshall2
class NDRSContextMarshall2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRSContextMarshallEx
class NDRSContextMarshallEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRSContextUnmarshall
class NDRSContextUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRSContextUnmarshall2
class NDRSContextUnmarshall2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRSContextUnmarshallEx
class NDRSContextUnmarshallEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NDRcopy
class NDRcopy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrAllocate
class NdrAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrAsyncClientCall
class NdrAsyncClientCall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrAsyncServerCall
class NdrAsyncServerCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrByteCountPointerFree
class NdrByteCountPointerFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrCStdStubBuffer2_Release
class NdrCStdStubBuffer2_Release(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrCStdStubBuffer_Release
class NdrCStdStubBuffer_Release(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrClearOutParameters
class NdrClearOutParameters(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrClientCall
class NdrClientCall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrClientCall2
class NdrClientCall2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrClientContextMarshall
class NdrClientContextMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrClientContextUnmarshall
class NdrClientContextUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrClientInitialize
class NdrClientInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrClientInitializeNew
class NdrClientInitializeNew(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrComplexArrayBufferSize
class NdrComplexArrayBufferSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrComplexArrayFree
class NdrComplexArrayFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrComplexArrayMemorySize
class NdrComplexArrayMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrComplexStructBufferSize
class NdrComplexStructBufferSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrComplexStructFree
class NdrComplexStructFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrComplexStructMemorySize
class NdrComplexStructMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantArrayMemorySize
class NdrConformantArrayMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantStringMarshall
class NdrConformantStringMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantStringMemorySize
class NdrConformantStringMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantStringUnmarshall
class NdrConformantStringUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantStructFree
class NdrConformantStructFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantStructMemorySize
class NdrConformantStructMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantVaryingArrayMemorySize
class NdrConformantVaryingArrayMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantVaryingStructFree
class NdrConformantVaryingStructFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConformantVaryingStructMemorySize
class NdrConformantVaryingStructMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrContextHandleInitialize
class NdrContextHandleInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConvert
class NdrConvert(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrConvert2
class NdrConvert2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrCorrelationFree
class NdrCorrelationFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrCorrelationInitialize
class NdrCorrelationInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrCorrelationPass
class NdrCorrelationPass(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrCreateServerInterfaceFromStub
class NdrCreateServerInterfaceFromStub(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrDcomAsyncClientCall
class NdrDcomAsyncClientCall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrDcomAsyncStubCall
class NdrDcomAsyncStubCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrDllCanUnloadNow
class NdrDllCanUnloadNow(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrDllGetClassObject
class NdrDllGetClassObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrDllRegisterProxy
class NdrDllRegisterProxy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrDllUnregisterProxy
class NdrDllUnregisterProxy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrEncapsulatedUnionFree
class NdrEncapsulatedUnionFree(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrEncapsulatedUnionMemorySize
class NdrEncapsulatedUnionMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrFixedArrayFree
class NdrFixedArrayFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrFixedArrayMemorySize
class NdrFixedArrayMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrFreeBuffer
class NdrFreeBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrFullPointerFree
class NdrFullPointerFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrFullPointerInsertRefId
class NdrFullPointerInsertRefId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrFullPointerQueryPointer
class NdrFullPointerQueryPointer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrFullPointerQueryRefId
class NdrFullPointerQueryRefId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrFullPointerXlatFree
class NdrFullPointerXlatFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrFullPointerXlatInit
class NdrFullPointerXlatInit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['dwSize', None]
    __argt__ = [ntdll.DWORD, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrGetBuffer
class NdrGetBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrGetDcomProtocolVersion
class NdrGetDcomProtocolVersion(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrGetSimpleTypeBufferAlignment
class NdrGetSimpleTypeBufferAlignment(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrGetSimpleTypeBufferSize
class NdrGetSimpleTypeBufferSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrGetSimpleTypeMemorySize
class NdrGetSimpleTypeMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrGetTypeFlags
class NdrGetTypeFlags(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrGetUserMarshalInfo
class NdrGetUserMarshalInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrInterfacePointerBufferSize
class NdrInterfacePointerBufferSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrInterfacePointerMarshall
class NdrInterfacePointerMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrInterfacePointerMemorySize
class NdrInterfacePointerMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrInterfacePointerUnmarshall
class NdrInterfacePointerUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMapCommAndFaultStatus
class NdrMapCommAndFaultStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesProcEncodeDecode
class NdrMesProcEncodeDecode(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesProcEncodeDecode2
class NdrMesProcEncodeDecode2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesSimpleTypeAlignSize
class NdrMesSimpleTypeAlignSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesSimpleTypeDecode
class NdrMesSimpleTypeDecode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesSimpleTypeEncode
class NdrMesSimpleTypeEncode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesTypeAlignSize
class NdrMesTypeAlignSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesTypeAlignSize2
class NdrMesTypeAlignSize2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesTypeDecode
class NdrMesTypeDecode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesTypeDecode2
class NdrMesTypeDecode2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesTypeEncode
class NdrMesTypeEncode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesTypeEncode2
class NdrMesTypeEncode2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrMesTypeFree2
class NdrMesTypeFree2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrNonConformantStringMemorySize
class NdrNonConformantStringMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrNonEncapsulatedUnionFree
class NdrNonEncapsulatedUnionFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrNonEncapsulatedUnionMemorySize
class NdrNonEncapsulatedUnionMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrNsGetBuffer
class NdrNsGetBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrNsSendReceive
class NdrNsSendReceive(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrOleFree
class NdrOleFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrOutInit
class NdrOutInit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrPartialIgnoreClientBufferSize
class NdrPartialIgnoreClientBufferSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrPartialIgnoreClientMarshall
class NdrPartialIgnoreClientMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrPartialIgnoreServerInitialize
class NdrPartialIgnoreServerInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrPointerFree
class NdrPointerFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrPointerMemorySize
class NdrPointerMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrProxyErrorHandler
class NdrProxyErrorHandler(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrProxyFreeBuffer
class NdrProxyFreeBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrProxyGetBuffer
class NdrProxyGetBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrProxyInitialize
class NdrProxyInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrProxySendReceive
class NdrProxySendReceive(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrRangeUnmarshall
class NdrRangeUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrRpcSmClientFree
class NdrRpcSmClientFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrRpcSmSetClientToOsf
class NdrRpcSmSetClientToOsf(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrRpcSsDefaultAllocate
class NdrRpcSsDefaultAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['dwSize']
    __argt__ = [ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:NdrRpcSsDefaultFree
class NdrRpcSsDefaultFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrRpcSsDisableAllocate
class NdrRpcSsDisableAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrRpcSsEnableAllocate
class NdrRpcSsEnableAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrSendReceive
class NdrSendReceive(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerCall
class NdrServerCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerCall2
class NdrServerCall2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerContextMarshall
class NdrServerContextMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerContextNewMarshall
class NdrServerContextNewMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerContextNewUnmarshall
class NdrServerContextNewUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerInitialize
class NdrServerInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerInitializeMarshall
class NdrServerInitializeMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerInitializeNew
class NdrServerInitializeNew(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerInitializePartial
class NdrServerInitializePartial(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerInitializeUnmarshall
class NdrServerInitializeUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerMarshall
class NdrServerMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrServerUnmarshall
class NdrServerUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrSimpleStructBufferSize
class NdrSimpleStructBufferSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrSimpleStructFree
class NdrSimpleStructFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrSimpleStructMarshall
class NdrSimpleStructMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrSimpleStructMemorySize
class NdrSimpleStructMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrSimpleStructUnmarshall
class NdrSimpleStructUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrSimpleTypeMarshall
class NdrSimpleTypeMarshall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrSimpleTypeUnmarshall
class NdrSimpleTypeUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrStubCall
class NdrStubCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrStubCall2
class NdrStubCall2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrStubGetBuffer
class NdrStubGetBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrStubInitialize
class NdrStubInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrStubInitializeMarshall
class NdrStubInitializeMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrTypeFlags
class NdrTypeFlags(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:NdrTypeFree
class NdrTypeFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrTypeMarshall
class NdrTypeMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrTypeSize
class NdrTypeSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrTypeUnmarshall
class NdrTypeUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrUnmarshallBasetypeInline
class NdrUnmarshallBasetypeInline(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrUserMarshalBufferSize
class NdrUserMarshalBufferSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrUserMarshalFree
class NdrUserMarshalFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrUserMarshalMarshall
class NdrUserMarshalMarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrUserMarshalMemorySize
class NdrUserMarshalMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrUserMarshalSimpleTypeConvert
class NdrUserMarshalSimpleTypeConvert(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrUserMarshalUnmarshall
class NdrUserMarshalUnmarshall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrVaryingArrayFree
class NdrVaryingArrayFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrVaryingArrayMemorySize
class NdrVaryingArrayMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrXmitOrRepAsFree
class NdrXmitOrRepAsFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrXmitOrRepAsMemorySize
class NdrXmitOrRepAsMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrpCreateProxy
class NdrpCreateProxy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrpCreateStub
class NdrpCreateStub(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrpGetProcFormatString
class NdrpGetProcFormatString(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrpGetTypeFormatString
class NdrpGetTypeFormatString(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrpGetTypeGenCookie
class NdrpGetTypeGenCookie(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrpMemoryIncrement
class NdrpMemoryIncrement(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrpReleaseTypeFormatString
class NdrpReleaseTypeFormatString(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NdrpReleaseTypeGenCookie
class NdrpReleaseTypeGenCookie(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrpSetRpcSsDefaults
class NdrpSetRpcSsDefaults(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NdrpVarVtOfTypeDesc
class NdrpVarVtOfTypeDesc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcAsyncAbortCall
class RpcAsyncAbortCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcAsyncCancelCall
class RpcAsyncCancelCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcAsyncCompleteCall
class RpcAsyncCompleteCall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcAsyncGetCallStatus
class RpcAsyncGetCallStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcAsyncInitializeHandle
class RpcAsyncInitializeHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcAsyncRegisterInfo
class RpcAsyncRegisterInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingCopy
class RpcBindingCopy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingFree
class RpcBindingFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingFromStringBindingA
class RpcBindingFromStringBindingA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingFromStringBindingW
class RpcBindingFromStringBindingW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqAuthClientA
class RpcBindingInqAuthClientA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqAuthClientExA
class RpcBindingInqAuthClientExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqAuthClientExW
class RpcBindingInqAuthClientExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqAuthClientW
class RpcBindingInqAuthClientW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqAuthInfoA
class RpcBindingInqAuthInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqAuthInfoExA
class RpcBindingInqAuthInfoExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqAuthInfoExW
class RpcBindingInqAuthInfoExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqAuthInfoW
class RpcBindingInqAuthInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqObject
class RpcBindingInqObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingInqOption
class RpcBindingInqOption(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingReset
class RpcBindingReset(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingServerFromClient
class RpcBindingServerFromClient(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingSetAuthInfoA
class RpcBindingSetAuthInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingSetAuthInfoExA
class RpcBindingSetAuthInfoExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingSetAuthInfoExW
class RpcBindingSetAuthInfoExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingSetAuthInfoW
class RpcBindingSetAuthInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingSetObject
class RpcBindingSetObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingSetOption
class RpcBindingSetOption(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingToStringBindingA
class RpcBindingToStringBindingA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingToStringBindingW
class RpcBindingToStringBindingW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcBindingVectorFree
class RpcBindingVectorFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcCancelThread
class RpcCancelThread(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcCancelThreadEx
class RpcCancelThreadEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcCertGeneratePrincipalNameA
class RpcCertGeneratePrincipalNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcCertGeneratePrincipalNameW
class RpcCertGeneratePrincipalNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcEpRegisterA
class RpcEpRegisterA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcEpRegisterNoReplaceA
class RpcEpRegisterNoReplaceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcEpRegisterNoReplaceW
class RpcEpRegisterNoReplaceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcEpRegisterW
class RpcEpRegisterW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcEpResolveBinding
class RpcEpResolveBinding(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcEpUnregister
class RpcEpUnregister(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcErrorAddRecord
class RpcErrorAddRecord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcErrorClearInformation
class RpcErrorClearInformation(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcErrorEndEnumeration
class RpcErrorEndEnumeration(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcErrorGetNextRecord
class RpcErrorGetNextRecord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcErrorGetNumberOfRecords
class RpcErrorGetNumberOfRecords(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcErrorLoadErrorInfo
class RpcErrorLoadErrorInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcErrorResetEnumeration
class RpcErrorResetEnumeration(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcErrorSaveErrorInfo
class RpcErrorSaveErrorInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcErrorStartEnumeration
class RpcErrorStartEnumeration(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcFreeAuthorizationContext
class RpcFreeAuthorizationContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcGetAuthorizationContextForClient
class RpcGetAuthorizationContextForClient(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcIfIdVectorFree
class RpcIfIdVectorFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcIfInqId
class RpcIfInqId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcImpersonateClient
class RpcImpersonateClient(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtEnableIdleCleanup
class RpcMgmtEnableIdleCleanup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcMgmtEpEltInqBegin
class RpcMgmtEpEltInqBegin(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtEpEltInqDone
class RpcMgmtEpEltInqDone(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtEpEltInqNextA
class RpcMgmtEpEltInqNextA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtEpEltInqNextW
class RpcMgmtEpEltInqNextW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'lpVoid', None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtEpUnregister
class RpcMgmtEpUnregister(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtInqComTimeout
class RpcMgmtInqComTimeout(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtInqDefaultProtectLevel
class RpcMgmtInqDefaultProtectLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtInqIfIds
class RpcMgmtInqIfIds(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtInqServerPrincNameA
class RpcMgmtInqServerPrincNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtInqServerPrincNameW
class RpcMgmtInqServerPrincNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtInqStats
class RpcMgmtInqStats(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtIsServerListening
class RpcMgmtIsServerListening(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtSetAuthorizationFn
class RpcMgmtSetAuthorizationFn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtSetCancelTimeout
class RpcMgmtSetCancelTimeout(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtSetComTimeout
class RpcMgmtSetComTimeout(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtSetServerStackSize
class RpcMgmtSetServerStackSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtStatsVectorFree
class RpcMgmtStatsVectorFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtStopServerListening
class RpcMgmtStopServerListening(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcMgmtWaitServerListen
class RpcMgmtWaitServerListen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcNetworkInqProtseqsA
class RpcNetworkInqProtseqsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcNetworkInqProtseqsW
class RpcNetworkInqProtseqsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcNetworkIsProtseqValidA
class RpcNetworkIsProtseqValidA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcNetworkIsProtseqValidW
class RpcNetworkIsProtseqValidW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcNsBindingInqEntryNameA
class RpcNsBindingInqEntryNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcNsBindingInqEntryNameW
class RpcNsBindingInqEntryNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcObjectInqType
class RpcObjectInqType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcObjectSetInqFn
class RpcObjectSetInqFn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcObjectSetType
class RpcObjectSetType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcProtseqVectorFreeA
class RpcProtseqVectorFreeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcProtseqVectorFreeW
class RpcProtseqVectorFreeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcRaiseException
class RpcRaiseException(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcRevertToSelf
class RpcRevertToSelf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcRevertToSelfEx
class RpcRevertToSelfEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerInqBindings
class RpcServerInqBindings(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerInqCallAttributesA
class RpcServerInqCallAttributesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerInqCallAttributesW
class RpcServerInqCallAttributesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerInqDefaultPrincNameA
class RpcServerInqDefaultPrincNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerInqDefaultPrincNameW
class RpcServerInqDefaultPrincNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerInqIf
class RpcServerInqIf(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerListen
class RpcServerListen(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerRegisterAuthInfoA
class RpcServerRegisterAuthInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerRegisterAuthInfoW
class RpcServerRegisterAuthInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerRegisterIf
class RpcServerRegisterIf(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerRegisterIf2
class RpcServerRegisterIf2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerRegisterIfEx
class RpcServerRegisterIfEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerTestCancel
class RpcServerTestCancel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUnregisterIf
class RpcServerUnregisterIf(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUnregisterIfEx
class RpcServerUnregisterIfEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseAllProtseqs
class RpcServerUseAllProtseqs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseAllProtseqsEx
class RpcServerUseAllProtseqsEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseAllProtseqsIf
class RpcServerUseAllProtseqsIf(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseAllProtseqsIfEx
class RpcServerUseAllProtseqsIfEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqA
class RpcServerUseProtseqA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqEpA
class RpcServerUseProtseqEpA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqEpExA
class RpcServerUseProtseqEpExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqEpExW
class RpcServerUseProtseqEpExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqEpW
class RpcServerUseProtseqEpW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqExA
class RpcServerUseProtseqExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqExW
class RpcServerUseProtseqExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqIfA
class RpcServerUseProtseqIfA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqIfExA
class RpcServerUseProtseqIfExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqIfExW
class RpcServerUseProtseqIfExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqIfW
class RpcServerUseProtseqIfW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerUseProtseqW
class RpcServerUseProtseqW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcServerYield
class RpcServerYield(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcSmAllocate
class RpcSmAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSmClientFree
class RpcSmClientFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSmDestroyClientContext
class RpcSmDestroyClientContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcSmDisableAllocate
class RpcSmDisableAllocate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcSmEnableAllocate
class RpcSmEnableAllocate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcSmFree
class RpcSmFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSmGetThreadHandle
class RpcSmGetThreadHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSmSetClientAllocFree
class RpcSmSetClientAllocFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSmSetThreadHandle
class RpcSmSetThreadHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSmSwapClientAllocFree
class RpcSmSwapClientAllocFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsAllocate
class RpcSsAllocate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsContextLockExclusive
class RpcSsContextLockExclusive(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsContextLockShared
class RpcSsContextLockShared(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsDestroyClientContext
class RpcSsDestroyClientContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsDisableAllocate
class RpcSsDisableAllocate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcSsEnableAllocate
class RpcSsEnableAllocate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcSsFree
class RpcSsFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsGetContextBinding
class RpcSsGetContextBinding(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsGetThreadHandle
class RpcSsGetThreadHandle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcSsSetClientAllocFree
class RpcSsSetClientAllocFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsSetThreadHandle
class RpcSsSetThreadHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcSsSwapClientAllocFree
class RpcSsSwapClientAllocFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcStringBindingComposeA
class RpcStringBindingComposeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcStringBindingComposeW
class RpcStringBindingComposeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcStringBindingParseA
class RpcStringBindingParseA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RpcStringBindingParseW
class RpcStringBindingParseW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcStringFreeA
class RpcStringFreeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcStringFreeW
class RpcStringFreeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RpcTestCancel
class RpcTestCancel(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RpcUserFree
class RpcUserFree(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SimpleTypeAlignment
class SimpleTypeAlignment(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SimpleTypeBufferSize
class SimpleTypeBufferSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SimpleTypeMemorySize
class SimpleTypeMemorySize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TowerConstruct
class TowerConstruct(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:TowerExplode
class TowerExplode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:UuidCompare
class UuidCompare(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UuidCreate
class UuidCreate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:UuidCreateNil
class UuidCreateNil(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UuidCreateSequential
class UuidCreateSequential(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UuidEqual
class UuidEqual(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UuidFromStringA
class UuidFromStringA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UuidFromStringW
class UuidFromStringW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UuidHash
class UuidHash(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UuidIsNil
class UuidIsNil(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:UuidToStringA
class UuidToStringA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UuidToStringW
class UuidToStringW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:char_array_from_ndr
class char_array_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:char_from_ndr
class char_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:data_from_ndr
class data_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:data_into_ndr
class data_into_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:data_size_ndr
class data_size_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:double_from_ndr
class double_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:enum_from_ndr
class enum_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:float_from_ndr
class float_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:long_array_from_ndr
class long_array_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:long_from_ndr
class long_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:long_from_ndr_temp
class long_from_ndr_temp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:main_entry
class main_entry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:short_array_from_ndr
class short_array_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:short_from_ndr
class short_from_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:short_from_ndr_temp
class short_from_ndr_temp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:tree_into_ndr
class tree_into_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:tree_peek_ndr
class tree_peek_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:tree_size_ndr
class tree_size_ndr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

