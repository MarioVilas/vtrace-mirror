
from vivisect.impemu.impmagic import *
import vivisect.impemu.emufunc as emufunc

import ntdll

#EMUFUNC:A_SHAFinal
class A_SHAFinal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:A_SHAInit
class A_SHAInit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:A_SHAUpdate
class A_SHAUpdate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AbortSystemShutdownA
class AbortSystemShutdownA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AbortSystemShutdownW
class AbortSystemShutdownW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheck
class AccessCheck(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckAndAuditAlarmA
class AccessCheckAndAuditAlarmA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckAndAuditAlarmW
class AccessCheckAndAuditAlarmW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckByType
class AccessCheckByType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckByTypeAndAuditAlarmA
class AccessCheckByTypeAndAuditAlarmA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckByTypeAndAuditAlarmW
class AccessCheckByTypeAndAuditAlarmW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckByTypeResultList
class AccessCheckByTypeResultList(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckByTypeResultListAndAuditAlarmA
class AccessCheckByTypeResultListAndAuditAlarmA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckByTypeResultListAndAuditAlarmByHandleA
class AccessCheckByTypeResultListAndAuditAlarmByHandleA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckByTypeResultListAndAuditAlarmByHandleW
class AccessCheckByTypeResultListAndAuditAlarmByHandleW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AccessCheckByTypeResultListAndAuditAlarmW
class AccessCheckByTypeResultListAndAuditAlarmW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAccessAllowedAce
class AddAccessAllowedAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAccessAllowedAceEx
class AddAccessAllowedAceEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:AddAccessAllowedObjectAce
class AddAccessAllowedObjectAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAccessDeniedAce
class AddAccessDeniedAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAccessDeniedAceEx
class AddAccessDeniedAceEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAccessDeniedObjectAce
class AddAccessDeniedObjectAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAce
class AddAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAuditAccessAce
class AddAuditAccessAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAuditAccessAceEx
class AddAuditAccessAceEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddAuditAccessObjectAce
class AddAuditAccessObjectAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddUsersToEncryptedFile
class AddUsersToEncryptedFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AdjustTokenGroups
class AdjustTokenGroups(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AdjustTokenPrivileges
class AdjustTokenPrivileges(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AllocateAndInitializeSid
class AllocateAndInitializeSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:AllocateLocallyUniqueId
class AllocateLocallyUniqueId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AreAllAccessesGranted
class AreAllAccessesGranted(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AreAnyAccessesGranted
class AreAnyAccessesGranted(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BackupEventLogA
class BackupEventLogA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BackupEventLogW
class BackupEventLogW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildExplicitAccessWithNameA
class BuildExplicitAccessWithNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildExplicitAccessWithNameW
class BuildExplicitAccessWithNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildImpersonateExplicitAccessWithNameA
class BuildImpersonateExplicitAccessWithNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildImpersonateExplicitAccessWithNameW
class BuildImpersonateExplicitAccessWithNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildImpersonateTrusteeA
class BuildImpersonateTrusteeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildImpersonateTrusteeW
class BuildImpersonateTrusteeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildSecurityDescriptorA
class BuildSecurityDescriptorA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildSecurityDescriptorW
class BuildSecurityDescriptorW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildTrusteeWithNameA
class BuildTrusteeWithNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildTrusteeWithNameW
class BuildTrusteeWithNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildTrusteeWithObjectsAndNameA
class BuildTrusteeWithObjectsAndNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildTrusteeWithObjectsAndNameW
class BuildTrusteeWithObjectsAndNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildTrusteeWithObjectsAndSidA
class BuildTrusteeWithObjectsAndSidA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildTrusteeWithObjectsAndSidW
class BuildTrusteeWithObjectsAndSidW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildTrusteeWithSidA
class BuildTrusteeWithSidA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BuildTrusteeWithSidW
class BuildTrusteeWithSidW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CancelOverlappedAccess
class CancelOverlappedAccess(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ChangeServiceConfig2A
class ChangeServiceConfig2A(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ChangeServiceConfig2W
class ChangeServiceConfig2W(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ChangeServiceConfigA
class ChangeServiceConfigA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ChangeServiceConfigW
class ChangeServiceConfigW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CheckTokenMembership
class CheckTokenMembership(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ClearEventLogA
class ClearEventLogA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ClearEventLogW
class ClearEventLogW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CloseCodeAuthzLevel
class CloseCodeAuthzLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CloseEncryptedFileRaw
class CloseEncryptedFileRaw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CloseEventLog
class CloseEventLog(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CloseServiceHandle
class CloseServiceHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CloseTrace
class CloseTrace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CommandLineFromMsiDescriptor
class CommandLineFromMsiDescriptor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ComputeAccessTokenFromCodeAuthzLevel
class ComputeAccessTokenFromCodeAuthzLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ControlService
class ControlService(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ControlTraceA
class ControlTraceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ControlTraceW
class ControlTraceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertAccessToSecurityDescriptorA
class ConvertAccessToSecurityDescriptorA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertAccessToSecurityDescriptorW
class ConvertAccessToSecurityDescriptorW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSDToStringSDRootDomainA
class ConvertSDToStringSDRootDomainA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSDToStringSDRootDomainW
class ConvertSDToStringSDRootDomainW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSecurityDescriptorToAccessA
class ConvertSecurityDescriptorToAccessA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'lpVoid', 'lpVoid', 'lpVoid', 'lpVoid']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSecurityDescriptorToAccessNamedA
class ConvertSecurityDescriptorToAccessNamedA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'lpVoid', 'lpVoid', 'lpVoid', 'lpVoid']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSecurityDescriptorToAccessNamedW
class ConvertSecurityDescriptorToAccessNamedW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSecurityDescriptorToAccessW
class ConvertSecurityDescriptorToAccessW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSecurityDescriptorToStringSecurityDescriptorA
class ConvertSecurityDescriptorToStringSecurityDescriptorA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSecurityDescriptorToStringSecurityDescriptorW
class ConvertSecurityDescriptorToStringSecurityDescriptorW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSidToStringSidA
class ConvertSidToStringSidA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertSidToStringSidW
class ConvertSidToStringSidW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ConvertStringSDToSDDomainA
class ConvertStringSDToSDDomainA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertStringSDToSDDomainW
class ConvertStringSDToSDDomainW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertStringSDToSDRootDomainA
class ConvertStringSDToSDRootDomainA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertStringSDToSDRootDomainW
class ConvertStringSDToSDRootDomainW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertStringSecurityDescriptorToSecurityDescriptorA
class ConvertStringSecurityDescriptorToSecurityDescriptorA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertStringSecurityDescriptorToSecurityDescriptorW
class ConvertStringSecurityDescriptorToSecurityDescriptorW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertStringSidToSidA
class ConvertStringSidToSidA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ConvertStringSidToSidW
class ConvertStringSidToSidW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ConvertToAutoInheritPrivateObjectSecurity
class ConvertToAutoInheritPrivateObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CopySid
class CopySid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateCodeAuthzLevel
class CreateCodeAuthzLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePrivateObjectSecurity
class CreatePrivateObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePrivateObjectSecurityEx
class CreatePrivateObjectSecurityEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CreatePrivateObjectSecurityWithMultipleInheritance
class CreatePrivateObjectSecurityWithMultipleInheritance(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateProcessAsUserA
class CreateProcessAsUserA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateProcessAsUserSecure
class CreateProcessAsUserSecure(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CreateProcessAsUserW
class CreateProcessAsUserW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateProcessWithLogonW
class CreateProcessWithLogonW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateRestrictedToken
class CreateRestrictedToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CreateServiceA
class CreateServiceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateServiceW
class CreateServiceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateTraceInstanceId
class CreateTraceInstanceId(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateWellKnownSid
class CreateWellKnownSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CredDeleteA
class CredDeleteA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredDeleteW
class CredDeleteW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredEnumerateA
class CredEnumerateA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredEnumerateW
class CredEnumerateW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredGetSessionTypes
class CredGetSessionTypes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredGetTargetInfoA
class CredGetTargetInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredGetTargetInfoW
class CredGetTargetInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredIsMarshaledCredentialA
class CredIsMarshaledCredentialA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CredIsMarshaledCredentialW
class CredIsMarshaledCredentialW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CredMarshalCredentialA
class CredMarshalCredentialA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'lpVoid', None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CredMarshalCredentialW
class CredMarshalCredentialW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredProfileLoaded
class CredProfileLoaded(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:CredReadA
class CredReadA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredReadDomainCredentialsA
class CredReadDomainCredentialsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredReadDomainCredentialsW
class CredReadDomainCredentialsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredReadW
class CredReadW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredRenameA
class CredRenameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredRenameW
class CredRenameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredUnmarshalCredentialA
class CredUnmarshalCredentialA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredUnmarshalCredentialW
class CredUnmarshalCredentialW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredWriteA
class CredWriteA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredWriteDomainCredentialsA
class CredWriteDomainCredentialsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredWriteDomainCredentialsW
class CredWriteDomainCredentialsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredWriteW
class CredWriteW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredpConvertCredential
class CredpConvertCredential(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CredpConvertTargetInfo
class CredpConvertTargetInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredpDecodeCredential
class CredpDecodeCredential(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredpEncodeCredential
class CredpEncodeCredential(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptAcquireContextA
class CryptAcquireContextA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptAcquireContextW
class CryptAcquireContextW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptContextAddRef
class CryptContextAddRef(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptCreateHash
class CryptCreateHash(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CryptDecrypt
class CryptDecrypt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptDeriveKey
class CryptDeriveKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptDestroyHash
class CryptDestroyHash(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CryptDestroyKey
class CryptDestroyKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CryptDuplicateHash
class CryptDuplicateHash(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptDuplicateKey
class CryptDuplicateKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptEncrypt
class CryptEncrypt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptEnumProviderTypesA
class CryptEnumProviderTypesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CryptEnumProviderTypesW
class CryptEnumProviderTypesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptEnumProvidersA
class CryptEnumProvidersA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CryptEnumProvidersW
class CryptEnumProvidersW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptExportKey
class CryptExportKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptGenKey
class CryptGenKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptGenRandom
class CryptGenRandom(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptGetDefaultProviderA
class CryptGetDefaultProviderA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CryptGetDefaultProviderW
class CryptGetDefaultProviderW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptGetHashParam
class CryptGetHashParam(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptGetKeyParam
class CryptGetKeyParam(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptGetProvParam
class CryptGetProvParam(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptGetUserKey
class CryptGetUserKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptHashData
class CryptHashData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptHashSessionKey
class CryptHashSessionKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptImportKey
class CryptImportKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptReleaseContext
class CryptReleaseContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSetHashParam
class CryptSetHashParam(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSetKeyParam
class CryptSetKeyParam(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSetProvParam
class CryptSetProvParam(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSetProviderA
class CryptSetProviderA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSetProviderExA
class CryptSetProviderExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSetProviderExW
class CryptSetProviderExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSetProviderW
class CryptSetProviderW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSignHashA
class CryptSignHashA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptSignHashW
class CryptSignHashW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptVerifySignatureA
class CryptVerifySignatureA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CryptVerifySignatureW
class CryptVerifySignatureW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DecryptFileA
class DecryptFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DecryptFileW
class DecryptFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteAce
class DeleteAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteService
class DeleteService(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeregisterEventSource
class DeregisterEventSource(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DestroyPrivateObjectSecurity
class DestroyPrivateObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:DuplicateEncryptionInfoFile
class DuplicateEncryptionInfoFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DuplicateToken
class DuplicateToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:DuplicateTokenEx
class DuplicateTokenEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ElfBackupEventLogFileA
class ElfBackupEventLogFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfBackupEventLogFileW
class ElfBackupEventLogFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ElfChangeNotify
class ElfChangeNotify(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfClearEventLogFileA
class ElfClearEventLogFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfClearEventLogFileW
class ElfClearEventLogFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ElfCloseEventLog
class ElfCloseEventLog(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfDeregisterEventSource
class ElfDeregisterEventSource(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfFlushEventLog
class ElfFlushEventLog(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfNumberOfRecords
class ElfNumberOfRecords(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfOldestRecord
class ElfOldestRecord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfOpenBackupEventLogA
class ElfOpenBackupEventLogA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfOpenBackupEventLogW
class ElfOpenBackupEventLogW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfOpenEventLogA
class ElfOpenEventLogA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfOpenEventLogW
class ElfOpenEventLogW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfReadEventLogA
class ElfReadEventLogA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfReadEventLogW
class ElfReadEventLogW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfRegisterEventSourceA
class ElfRegisterEventSourceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfRegisterEventSourceW
class ElfRegisterEventSourceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfReportEventA
class ElfReportEventA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ElfReportEventW
class ElfReportEventW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnableTrace
class EnableTrace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EncryptFileA
class EncryptFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EncryptFileW
class EncryptFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:EncryptedFileKeyInfo
class EncryptedFileKeyInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EncryptionDisable
class EncryptionDisable(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumDependentServicesA
class EnumDependentServicesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumDependentServicesW
class EnumDependentServicesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumServiceGroupW
class EnumServiceGroupW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumServicesStatusA
class EnumServicesStatusA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumServicesStatusExA
class EnumServicesStatusExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumServicesStatusExW
class EnumServicesStatusExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumServicesStatusW
class EnumServicesStatusW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumerateTraceGuids
class EnumerateTraceGuids(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EqualDomainSid
class EqualDomainSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EqualPrefixSid
class EqualPrefixSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EqualSid
class EqualSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FileEncryptionStatusA
class FileEncryptionStatusA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FileEncryptionStatusW
class FileEncryptionStatusW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindFirstFreeAce
class FindFirstFreeAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FlushTraceA
class FlushTraceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FlushTraceW
class FlushTraceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FreeEncryptedFileKeyInfo
class FreeEncryptedFileKeyInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FreeEncryptionCertificateHashList
class FreeEncryptionCertificateHashList(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FreeInheritedFromArray
class FreeInheritedFromArray(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetAccessPermissionsForObjectA
class GetAccessPermissionsForObjectA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetAccessPermissionsForObjectW
class GetAccessPermissionsForObjectW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetAce
class GetAce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetAclInformation
class GetAclInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetAuditedPermissionsFromAclA
class GetAuditedPermissionsFromAclA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetAuditedPermissionsFromAclW
class GetAuditedPermissionsFromAclW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCurrentHwProfileA
class GetCurrentHwProfileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCurrentHwProfileW
class GetCurrentHwProfileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetEffectiveRightsFromAclA
class GetEffectiveRightsFromAclA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEffectiveRightsFromAclW
class GetEffectiveRightsFromAclW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEventLogInformation
class GetEventLogInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetExplicitEntriesFromAclA
class GetExplicitEntriesFromAclA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetExplicitEntriesFromAclW
class GetExplicitEntriesFromAclW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetFileSecurityA
class GetFileSecurityA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetFileSecurityW
class GetFileSecurityW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetInformationCodeAuthzLevelW
class GetInformationCodeAuthzLevelW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetInformationCodeAuthzPolicyW
class GetInformationCodeAuthzPolicyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetInheritanceSourceA
class GetInheritanceSourceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetInheritanceSourceW
class GetInheritanceSourceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetKernelObjectSecurity
class GetKernelObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetLocalManagedApplicationData
class GetLocalManagedApplicationData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetLocalManagedApplications
class GetLocalManagedApplications(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetManagedApplicationCategories
class GetManagedApplicationCategories(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetManagedApplications
class GetManagedApplications(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMultipleTrusteeA
class GetMultipleTrusteeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMultipleTrusteeOperationA
class GetMultipleTrusteeOperationA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMultipleTrusteeOperationW
class GetMultipleTrusteeOperationW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMultipleTrusteeW
class GetMultipleTrusteeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetNamedSecurityInfoA
class GetNamedSecurityInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetNamedSecurityInfoExA
class GetNamedSecurityInfoExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetNamedSecurityInfoExW
class GetNamedSecurityInfoExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetNamedSecurityInfoW
class GetNamedSecurityInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetNumberOfEventLogRecords
class GetNumberOfEventLogRecords(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetOldestEventLogRecord
class GetOldestEventLogRecord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetOverlappedAccessResults
class GetOverlappedAccessResults(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetPrivateObjectSecurity
class GetPrivateObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityDescriptorControl
class GetSecurityDescriptorControl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityDescriptorDacl
class GetSecurityDescriptorDacl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityDescriptorGroup
class GetSecurityDescriptorGroup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityDescriptorOwner
class GetSecurityDescriptorOwner(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityDescriptorRMControl
class GetSecurityDescriptorRMControl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityDescriptorSacl
class GetSecurityDescriptorSacl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityInfo
class GetSecurityInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityInfoExA
class GetSecurityInfoExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityInfoExW
class GetSecurityInfoExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetServiceDisplayNameA
class GetServiceDisplayNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetServiceDisplayNameW
class GetServiceDisplayNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetServiceKeyNameA
class GetServiceKeyNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetServiceKeyNameW
class GetServiceKeyNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSidLengthRequired
class GetSidLengthRequired(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTokenInformation
class GetTokenInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetTraceEnableFlags
class GetTraceEnableFlags(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTraceEnableLevel
class GetTraceEnableLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTraceLoggerHandle
class GetTraceLoggerHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTrusteeFormA
class GetTrusteeFormA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTrusteeFormW
class GetTrusteeFormW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTrusteeNameA
class GetTrusteeNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTrusteeNameW
class GetTrusteeNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTrusteeTypeA
class GetTrusteeTypeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTrusteeTypeW
class GetTrusteeTypeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUserNameA
class GetUserNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUserNameW
class GetUserNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetWindowsAccountDomainSid
class GetWindowsAccountDomainSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:I_ScGetCurrentGroupStateW
class I_ScGetCurrentGroupStateW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_ScIsSecurityProcess
class I_ScIsSecurityProcess(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:I_ScPnPGetServiceName
class I_ScPnPGetServiceName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_ScSendTSMessage
class I_ScSendTSMessage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_ScSetServiceBitsA
class I_ScSetServiceBitsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:I_ScSetServiceBitsW
class I_ScSetServiceBitsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IdentifyCodeAuthzLevelW
class IdentifyCodeAuthzLevelW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ImpersonateAnonymousToken
class ImpersonateAnonymousToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ImpersonateLoggedOnUser
class ImpersonateLoggedOnUser(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ImpersonateNamedPipeClient
class ImpersonateNamedPipeClient(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ImpersonateSelf
class ImpersonateSelf(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitializeAcl
class InitializeAcl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitializeSecurityDescriptor
class InitializeSecurityDescriptor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitializeSid
class InitializeSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitiateSystemShutdownA
class InitiateSystemShutdownA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitiateSystemShutdownExA
class InitiateSystemShutdownExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitiateSystemShutdownExW
class InitiateSystemShutdownExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitiateSystemShutdownW
class InitiateSystemShutdownW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InstallApplication
class InstallApplication(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsTextUnicode
class IsTextUnicode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsTokenRestricted
class IsTokenRestricted(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsTokenUntrusted
class IsTokenUntrusted(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidAcl
class IsValidAcl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidSecurityDescriptor
class IsValidSecurityDescriptor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidSid
class IsValidSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsWellKnownSid
class IsWellKnownSid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LockServiceDatabase
class LockServiceDatabase(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LogonUserA
class LogonUserA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LogonUserExA
class LogonUserExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LogonUserExW
class LogonUserExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LogonUserW
class LogonUserW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupAccountNameA
class LookupAccountNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupAccountNameW
class LookupAccountNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupAccountSidA
class LookupAccountSidA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LookupAccountSidW
class LookupAccountSidW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LookupPrivilegeDisplayNameA
class LookupPrivilegeDisplayNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupPrivilegeDisplayNameW
class LookupPrivilegeDisplayNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupPrivilegeNameA
class LookupPrivilegeNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupPrivilegeNameW
class LookupPrivilegeNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupPrivilegeValueA
class LookupPrivilegeValueA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupPrivilegeValueW
class LookupPrivilegeValueW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupSecurityDescriptorPartsA
class LookupSecurityDescriptorPartsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LookupSecurityDescriptorPartsW
class LookupSecurityDescriptorPartsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaAddAccountRights
class LsaAddAccountRights(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaAddPrivilegesToAccount
class LsaAddPrivilegesToAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaClearAuditLog
class LsaClearAuditLog(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaClose
class LsaClose(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaCreateAccount
class LsaCreateAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaCreateSecret
class LsaCreateSecret(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaCreateTrustedDomain
class LsaCreateTrustedDomain(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaCreateTrustedDomainEx
class LsaCreateTrustedDomainEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaDelete
class LsaDelete(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaDeleteTrustedDomain
class LsaDeleteTrustedDomain(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaEnumerateAccountRights
class LsaEnumerateAccountRights(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaEnumerateAccounts
class LsaEnumerateAccounts(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaEnumerateAccountsWithUserRight
class LsaEnumerateAccountsWithUserRight(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaEnumeratePrivileges
class LsaEnumeratePrivileges(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaEnumeratePrivilegesOfAccount
class LsaEnumeratePrivilegesOfAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaEnumerateTrustedDomains
class LsaEnumerateTrustedDomains(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaEnumerateTrustedDomainsEx
class LsaEnumerateTrustedDomainsEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaFreeMemory
class LsaFreeMemory(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaGetQuotasForAccount
class LsaGetQuotasForAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaGetRemoteUserName
class LsaGetRemoteUserName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaGetSystemAccessAccount
class LsaGetSystemAccessAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaGetUserName
class LsaGetUserName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaICLookupNames
class LsaICLookupNames(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaICLookupNamesWithCreds
class LsaICLookupNamesWithCreds(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaICLookupSids
class LsaICLookupSids(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaICLookupSidsWithCreds
class LsaICLookupSidsWithCreds(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaLookupNames
class LsaLookupNames(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaLookupNames2
class LsaLookupNames2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaLookupPrivilegeDisplayName
class LsaLookupPrivilegeDisplayName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaLookupPrivilegeName
class LsaLookupPrivilegeName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaLookupPrivilegeValue
class LsaLookupPrivilegeValue(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaLookupSids
class LsaLookupSids(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaOpenAccount
class LsaOpenAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaOpenPolicy
class LsaOpenPolicy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaOpenPolicySce
class LsaOpenPolicySce(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaOpenSecret
class LsaOpenSecret(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaOpenTrustedDomain
class LsaOpenTrustedDomain(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaOpenTrustedDomainByName
class LsaOpenTrustedDomainByName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaQueryDomainInformationPolicy
class LsaQueryDomainInformationPolicy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaQueryForestTrustInformation
class LsaQueryForestTrustInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaQueryInfoTrustedDomain
class LsaQueryInfoTrustedDomain(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaQueryInformationPolicy
class LsaQueryInformationPolicy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaQuerySecret
class LsaQuerySecret(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaQuerySecurityObject
class LsaQuerySecurityObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaQueryTrustedDomainInfo
class LsaQueryTrustedDomainInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaQueryTrustedDomainInfoByName
class LsaQueryTrustedDomainInfoByName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaRemoveAccountRights
class LsaRemoveAccountRights(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaRemovePrivilegesFromAccount
class LsaRemovePrivilegesFromAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaRetrievePrivateData
class LsaRetrievePrivateData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetDomainInformationPolicy
class LsaSetDomainInformationPolicy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetForestTrustInformation
class LsaSetForestTrustInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetInformationPolicy
class LsaSetInformationPolicy(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetInformationTrustedDomain
class LsaSetInformationTrustedDomain(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetQuotasForAccount
class LsaSetQuotasForAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetSecret
class LsaSetSecret(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetSecurityObject
class LsaSetSecurityObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetSystemAccessAccount
class LsaSetSystemAccessAccount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetTrustedDomainInfoByName
class LsaSetTrustedDomainInfoByName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaSetTrustedDomainInformation
class LsaSetTrustedDomainInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaStorePrivateData
class LsaStorePrivateData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MD4Final
class MD4Final(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MD4Init
class MD4Init(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MD4Update
class MD4Update(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MD5Final
class MD5Final(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MD5Init
class MD5Init(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:MD5Update
class MD5Update(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MSChapSrvChangePassword
class MSChapSrvChangePassword(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MSChapSrvChangePassword2
class MSChapSrvChangePassword2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MakeAbsoluteSD
class MakeAbsoluteSD(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MakeAbsoluteSD2
class MakeAbsoluteSD2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MakeSelfRelativeSD
class MakeSelfRelativeSD(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:NotifyBootConfigStatus
class NotifyBootConfigStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NotifyChangeEventLog
class NotifyChangeEventLog(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ObjectCloseAuditAlarmA
class ObjectCloseAuditAlarmA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ObjectCloseAuditAlarmW
class ObjectCloseAuditAlarmW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ObjectDeleteAuditAlarmA
class ObjectDeleteAuditAlarmA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ObjectDeleteAuditAlarmW
class ObjectDeleteAuditAlarmW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ObjectOpenAuditAlarmA
class ObjectOpenAuditAlarmA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ObjectOpenAuditAlarmW
class ObjectOpenAuditAlarmW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ObjectPrivilegeAuditAlarmA
class ObjectPrivilegeAuditAlarmA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ObjectPrivilegeAuditAlarmW
class ObjectPrivilegeAuditAlarmW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenBackupEventLogA
class OpenBackupEventLogA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenBackupEventLogW
class OpenBackupEventLogW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenEncryptedFileRawA
class OpenEncryptedFileRawA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenEncryptedFileRawW
class OpenEncryptedFileRawW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenEventLogA
class OpenEventLogA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenEventLogW
class OpenEventLogW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenProcessToken
class OpenProcessToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OpenSCManagerA
class OpenSCManagerA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenSCManagerW
class OpenSCManagerW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenServiceA
class OpenServiceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenServiceW
class OpenServiceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenThreadToken
class OpenThreadToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:OpenTraceA
class OpenTraceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OpenTraceW
class OpenTraceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PrivilegeCheck
class PrivilegeCheck(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PrivilegedServiceAuditAlarmA
class PrivilegedServiceAuditAlarmA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PrivilegedServiceAuditAlarmW
class PrivilegedServiceAuditAlarmW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ProcessIdleTasks
class ProcessIdleTasks(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:ProcessTrace
class ProcessTrace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryAllTracesA
class QueryAllTracesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryAllTracesW
class QueryAllTracesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryRecoveryAgentsOnEncryptedFile
class QueryRecoveryAgentsOnEncryptedFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceConfig2A
class QueryServiceConfig2A(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceConfig2W
class QueryServiceConfig2W(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceConfigA
class QueryServiceConfigA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceConfigW
class QueryServiceConfigW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceLockStatusA
class QueryServiceLockStatusA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceLockStatusW
class QueryServiceLockStatusW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceObjectSecurity
class QueryServiceObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceStatus
class QueryServiceStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:QueryServiceStatusEx
class QueryServiceStatusEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryTraceA
class QueryTraceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryTraceW
class QueryTraceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:QueryUsersOnEncryptedFile
class QueryUsersOnEncryptedFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryWindows31FilesMigration
class QueryWindows31FilesMigration(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ReadEncryptedFileRaw
class ReadEncryptedFileRaw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:ReadEventLogA
class ReadEventLogA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ReadEventLogW
class ReadEventLogW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegCloseKey
class RegCloseKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegConnectRegistryA
class RegConnectRegistryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegConnectRegistryW
class RegConnectRegistryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegCreateKeyA
class RegCreateKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegCreateKeyExA
class RegCreateKeyExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegCreateKeyExW
class RegCreateKeyExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegCreateKeyW
class RegCreateKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegDeleteKeyA
class RegDeleteKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegDeleteKeyW
class RegDeleteKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegDeleteValueA
class RegDeleteValueA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegDeleteValueW
class RegDeleteValueW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegDisablePredefinedCache
class RegDisablePredefinedCache(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RegDisablePredefinedCacheEx
class RegDisablePredefinedCacheEx(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RegEnumKeyA
class RegEnumKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegEnumKeyExA
class RegEnumKeyExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegEnumKeyExW
class RegEnumKeyExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegEnumKeyW
class RegEnumKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegEnumValueA
class RegEnumValueA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegEnumValueW
class RegEnumValueW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegFlushKey
class RegFlushKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegGetKeySecurity
class RegGetKeySecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegLoadKeyA
class RegLoadKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegLoadKeyW
class RegLoadKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegNotifyChangeKeyValue
class RegNotifyChangeKeyValue(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegOpenCurrentUser
class RegOpenCurrentUser(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegOpenKeyA
class RegOpenKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegOpenKeyExA
class RegOpenKeyExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegOpenKeyExW
class RegOpenKeyExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegOpenKeyW
class RegOpenKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegOpenUserClassesRoot
class RegOpenUserClassesRoot(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegOverridePredefKey
class RegOverridePredefKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegQueryInfoKeyA
class RegQueryInfoKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, Pointer, Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegQueryInfoKeyW
class RegQueryInfoKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegQueryMultipleValuesA
class RegQueryMultipleValuesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegQueryMultipleValuesW
class RegQueryMultipleValuesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegQueryValueA
class RegQueryValueA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegQueryValueExA
class RegQueryValueExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegQueryValueExW
class RegQueryValueExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegQueryValueW
class RegQueryValueW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RegReplaceKeyA
class RegReplaceKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegReplaceKeyW
class RegReplaceKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegRestoreKeyA
class RegRestoreKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegRestoreKeyW
class RegRestoreKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSaveKeyA
class RegSaveKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSaveKeyExA
class RegSaveKeyExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSaveKeyExW
class RegSaveKeyExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSaveKeyW
class RegSaveKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSetKeySecurity
class RegSetKeySecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSetValueA
class RegSetValueA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSetValueExA
class RegSetValueExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSetValueExW
class RegSetValueExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegSetValueW
class RegSetValueW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegUnLoadKeyA
class RegUnLoadKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegUnLoadKeyW
class RegUnLoadKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterEventSourceA
class RegisterEventSourceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterEventSourceW
class RegisterEventSourceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterIdleTask
class RegisterIdleTask(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterServiceCtrlHandlerA
class RegisterServiceCtrlHandlerA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterServiceCtrlHandlerExA
class RegisterServiceCtrlHandlerExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterServiceCtrlHandlerExW
class RegisterServiceCtrlHandlerExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterServiceCtrlHandlerW
class RegisterServiceCtrlHandlerW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterTraceGuidsA
class RegisterTraceGuidsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RegisterTraceGuidsW
class RegisterTraceGuidsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RemoveTraceCallback
class RemoveTraceCallback(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RemoveUsersFromEncryptedFile
class RemoveUsersFromEncryptedFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ReportEventA
class ReportEventA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ReportEventW
class ReportEventW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:RevertToSelf
class RevertToSelf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:SaferCloseLevel
class SaferCloseLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferComputeTokenFromLevel
class SaferComputeTokenFromLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferCreateLevel
class SaferCreateLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferGetLevelInformation
class SaferGetLevelInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SaferGetPolicyInformation
class SaferGetPolicyInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferIdentifyLevel
class SaferIdentifyLevel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferRecordEventLogEntry
class SaferRecordEventLogEntry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferSetLevelInformation
class SaferSetLevelInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferSetPolicyInformation
class SaferSetPolicyInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferiChangeRegistryScope
class SaferiChangeRegistryScope(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferiCompareTokenLevels
class SaferiCompareTokenLevels(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferiIsExecutableFileType
class SaferiIsExecutableFileType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'dwSize']
    __argt__ = [Unknown, ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:SaferiPopulateDefaultsInRegistry
class SaferiPopulateDefaultsInRegistry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferiRecordEventLogEntry
class SaferiRecordEventLogEntry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferiReplaceProcessThreadTokens
class SaferiReplaceProcessThreadTokens(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaferiSearchMatchingHashRules
class SaferiSearchMatchingHashRules(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetAclInformation
class SetAclInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetEntriesInAccessListA
class SetEntriesInAccessListA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, 'lpVoid', None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetEntriesInAccessListW
class SetEntriesInAccessListW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetEntriesInAclA
class SetEntriesInAclA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SetEntriesInAclW
class SetEntriesInAclW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SetEntriesInAuditListA
class SetEntriesInAuditListA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, 'lpVoid', None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetEntriesInAuditListW
class SetEntriesInAuditListW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetFileSecurityA
class SetFileSecurityA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetFileSecurityW
class SetFileSecurityW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetInformationCodeAuthzLevelW
class SetInformationCodeAuthzLevelW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetInformationCodeAuthzPolicyW
class SetInformationCodeAuthzPolicyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetKernelObjectSecurity
class SetKernelObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SetNamedSecurityInfoA
class SetNamedSecurityInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid', None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetNamedSecurityInfoExA
class SetNamedSecurityInfoExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetNamedSecurityInfoExW
class SetNamedSecurityInfoExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetNamedSecurityInfoW
class SetNamedSecurityInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetPrivateObjectSecurity
class SetPrivateObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetPrivateObjectSecurityEx
class SetPrivateObjectSecurityEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityDescriptorControl
class SetSecurityDescriptorControl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityDescriptorDacl
class SetSecurityDescriptorDacl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityDescriptorGroup
class SetSecurityDescriptorGroup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityDescriptorOwner
class SetSecurityDescriptorOwner(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityDescriptorRMControl
class SetSecurityDescriptorRMControl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityDescriptorSacl
class SetSecurityDescriptorSacl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityInfo
class SetSecurityInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityInfoExA
class SetSecurityInfoExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSecurityInfoExW
class SetSecurityInfoExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetServiceBits
class SetServiceBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetServiceObjectSecurity
class SetServiceObjectSecurity(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetServiceStatus
class SetServiceStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetThreadToken
class SetThreadToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetTokenInformation
class SetTokenInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetTraceCallback
class SetTraceCallback(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUserFileEncryptionKey
class SetUserFileEncryptionKey(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartServiceA
class StartServiceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartServiceCtrlDispatcherA
class StartServiceCtrlDispatcherA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartServiceCtrlDispatcherW
class StartServiceCtrlDispatcherW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartServiceW
class StartServiceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartTraceA
class StartTraceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartTraceW
class StartTraceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:StopTraceA
class StopTraceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StopTraceW
class StopTraceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SynchronizeWindows31FilesAndWindowsNTRegistry
class SynchronizeWindows31FilesAndWindowsNTRegistry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction001
class SystemFunction001(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction002
class SystemFunction002(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction003
class SystemFunction003(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction004
class SystemFunction004(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction005
class SystemFunction005(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction006
class SystemFunction006(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction007
class SystemFunction007(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction008
class SystemFunction008(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction009
class SystemFunction009(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction010
class SystemFunction010(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction011
class SystemFunction011(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction012
class SystemFunction012(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction013
class SystemFunction013(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction014
class SystemFunction014(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction015
class SystemFunction015(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction016
class SystemFunction016(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction017
class SystemFunction017(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction018
class SystemFunction018(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction019
class SystemFunction019(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction020
class SystemFunction020(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction021
class SystemFunction021(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction022
class SystemFunction022(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction023
class SystemFunction023(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction024
class SystemFunction024(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction025
class SystemFunction025(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction026
class SystemFunction026(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction027
class SystemFunction027(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction028
class SystemFunction028(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction029
class SystemFunction029(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction030
class SystemFunction030(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction031
class SystemFunction031(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction032
class SystemFunction032(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction033
class SystemFunction033(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction034
class SystemFunction034(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction035
class SystemFunction035(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction036
class SystemFunction036(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction040
class SystemFunction040(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SystemFunction041
class SystemFunction041(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TraceEvent
class TraceEvent(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:TraceEventInstance
class TraceEventInstance(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TraceMessage
class TraceMessage(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TraceMessageVa
class TraceMessageVa(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TreeResetNamedSecurityInfoA
class TreeResetNamedSecurityInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TreeResetNamedSecurityInfoW
class TreeResetNamedSecurityInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TrusteeAccessToObjectA
class TrusteeAccessToObjectA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TrusteeAccessToObjectW
class TrusteeAccessToObjectW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UninstallApplication
class UninstallApplication(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnlockServiceDatabase
class UnlockServiceDatabase(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnregisterIdleTask
class UnregisterIdleTask(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'hObject', 'hObject']
    __argt__ = [Unknown, HANDLE, HANDLE, ]
#EMUFUNCDONE

#EMUFUNC:UnregisterTraceGuids
class UnregisterTraceGuids(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UpdateTraceA
class UpdateTraceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UpdateTraceW
class UpdateTraceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WdmWmiServiceMain
class WdmWmiServiceMain(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiCloseBlock
class WmiCloseBlock(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['hObject']
    __argt__ = [HANDLE, ]
#EMUFUNCDONE

#EMUFUNC:WmiCloseTraceWithCursor
class WmiCloseTraceWithCursor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiConvertTimestamp
class WmiConvertTimestamp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiDevInstToInstanceNameA
class WmiDevInstToInstanceNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiDevInstToInstanceNameW
class WmiDevInstToInstanceNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiEnumerateGuids
class WmiEnumerateGuids(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiExecuteMethodA
class WmiExecuteMethodA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiExecuteMethodW
class WmiExecuteMethodW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiFileHandleToInstanceNameA
class WmiFileHandleToInstanceNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiFileHandleToInstanceNameW
class WmiFileHandleToInstanceNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiFreeBuffer
class WmiFreeBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiGetFirstTraceOffset
class WmiGetFirstTraceOffset(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiGetNextEvent
class WmiGetNextEvent(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiGetTraceHeader
class WmiGetTraceHeader(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiMofEnumerateResourcesA
class WmiMofEnumerateResourcesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiMofEnumerateResourcesW
class WmiMofEnumerateResourcesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiNotificationRegistrationA
class WmiNotificationRegistrationA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiNotificationRegistrationW
class WmiNotificationRegistrationW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiOpenBlock
class WmiOpenBlock(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiOpenTraceWithCursor
class WmiOpenTraceWithCursor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiParseTraceEvent
class WmiParseTraceEvent(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiQueryAllDataA
class WmiQueryAllDataA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiQueryAllDataMultipleA
class WmiQueryAllDataMultipleA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiQueryAllDataMultipleW
class WmiQueryAllDataMultipleW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiQueryAllDataW
class WmiQueryAllDataW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiQueryGuidInformation
class WmiQueryGuidInformation(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiQuerySingleInstanceA
class WmiQuerySingleInstanceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiQuerySingleInstanceMultipleA
class WmiQuerySingleInstanceMultipleA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiQuerySingleInstanceMultipleW
class WmiQuerySingleInstanceMultipleW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:WmiQuerySingleInstanceW
class WmiQuerySingleInstanceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiReceiveNotificationsA
class WmiReceiveNotificationsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiReceiveNotificationsW
class WmiReceiveNotificationsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiSetSingleInstanceA
class WmiSetSingleInstanceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiSetSingleInstanceW
class WmiSetSingleInstanceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiSetSingleItemA
class WmiSetSingleItemA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WmiSetSingleItemW
class WmiSetSingleItemW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:Wow64Win32ApiEntry
class Wow64Win32ApiEntry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:WriteEncryptedFileRaw
class WriteEncryptedFileRaw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:main_entry
class main_entry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

