from vivisect.impemu.impmagic import *
import vivisect.impemu.emufunc as emufunc

#EMUFUNC:AcceptSecurityContext
class AcceptSecurityContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AcquireCredentialsHandleA
class AcquireCredentialsHandleA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AcquireCredentialsHandleW
class AcquireCredentialsHandleW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddCredentialsA
class AddCredentialsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddCredentialsW
class AddCredentialsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddSecurityPackageA
class AddSecurityPackageA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddSecurityPackageW
class AddSecurityPackageW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ApplyControlToken
class ApplyControlToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CompleteAuthToken
class CompleteAuthToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredMarshalTargetInfo
class CredMarshalTargetInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CredUnmarshalTargetInfo
class CredUnmarshalTargetInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DecryptMessage
class DecryptMessage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteSecurityContext
class DeleteSecurityContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteSecurityPackageA
class DeleteSecurityPackageA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteSecurityPackageW
class DeleteSecurityPackageW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EncryptMessage
class EncryptMessage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumerateSecurityPackagesA
class EnumerateSecurityPackagesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumerateSecurityPackagesW
class EnumerateSecurityPackagesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ExportSecurityContext
class ExportSecurityContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FreeContextBuffer
class FreeContextBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FreeCredentialsHandle
class FreeCredentialsHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetComputerObjectNameA
class GetComputerObjectNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetComputerObjectNameW
class GetComputerObjectNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSecurityUserInfo
class GetSecurityUserInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUserNameExA
class GetUserNameExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUserNameExW
class GetUserNameExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ImpersonateSecurityContext
class ImpersonateSecurityContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ImportSecurityContextA
class ImportSecurityContextA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ImportSecurityContextW
class ImportSecurityContextW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitSecurityInterfaceA
class InitSecurityInterfaceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:InitSecurityInterfaceW
class InitSecurityInterfaceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:InitializeSecurityContextA
class InitializeSecurityContextA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InitializeSecurityContextW
class InitializeSecurityContextW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaCallAuthenticationPackage
class LsaCallAuthenticationPackage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaConnectUntrusted
class LsaConnectUntrusted(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaDeregisterLogonProcess
class LsaDeregisterLogonProcess(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaEnumerateLogonSessions
class LsaEnumerateLogonSessions(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaFreeReturnBuffer
class LsaFreeReturnBuffer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaGetLogonSessionData
class LsaGetLogonSessionData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaLogonUser
class LsaLogonUser(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaLookupAuthenticationPackage
class LsaLookupAuthenticationPackage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaRegisterLogonProcess
class LsaRegisterLogonProcess(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaRegisterPolicyChangeNotification
class LsaRegisterPolicyChangeNotification(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LsaUnregisterPolicyChangeNotification
class LsaUnregisterPolicyChangeNotification(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MakeSignature
class MakeSignature(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryContextAttributesA
class QueryContextAttributesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryContextAttributesW
class QueryContextAttributesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryCredentialsAttributesA
class QueryCredentialsAttributesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryCredentialsAttributesW
class QueryCredentialsAttributesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QuerySecurityContextToken
class QuerySecurityContextToken(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QuerySecurityPackageInfoA
class QuerySecurityPackageInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QuerySecurityPackageInfoW
class QuerySecurityPackageInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RevertSecurityContext
class RevertSecurityContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslAcceptSecurityContext
class SaslAcceptSecurityContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslEnumerateProfilesA
class SaslEnumerateProfilesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslEnumerateProfilesW
class SaslEnumerateProfilesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslGetProfilePackageA
class SaslGetProfilePackageA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslGetProfilePackageW
class SaslGetProfilePackageW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslIdentifyPackageA
class SaslIdentifyPackageA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslIdentifyPackageW
class SaslIdentifyPackageW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslInitializeSecurityContextA
class SaslInitializeSecurityContextA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaslInitializeSecurityContextW
class SaslInitializeSecurityContextW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SealMessage
class SealMessage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SecCacheSspiPackages
class SecCacheSspiPackages(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:SecDeleteUserModeContext
class SecDeleteUserModeContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SecGetLocaleSpecificEncryptionRules
class SecGetLocaleSpecificEncryptionRules(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SecInitUserModeContext
class SecInitUserModeContext(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SecpFreeMemory
class SecpFreeMemory(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:SecpTranslateName
class SecpTranslateName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SecpTranslateNameEx
class SecpTranslateNameEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetContextAttributesA
class SetContextAttributesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetContextAttributesW
class SetContextAttributesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TranslateNameA
class TranslateNameA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TranslateNameW
class TranslateNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnsealMessage
class UnsealMessage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:VerifySignature
class VerifySignature(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:main_entry
class main_entry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

