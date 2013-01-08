
from vivisect.impemu.impmagic import *
import vivisect.impemu.emufunc as emufunc

import ntdll

#EMUFUNC:CommitUrlCacheEntryA
class CommitUrlCacheEntryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'ptr', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CommitUrlCacheEntryW
class CommitUrlCacheEntryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'ptr']
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:CreateMD5SSOHash
class CreateMD5SSOHash(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateUrlCacheContainerA
class CreateUrlCacheContainerA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateUrlCacheContainerW
class CreateUrlCacheContainerW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateUrlCacheEntryA
class CreateUrlCacheEntryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateUrlCacheEntryW
class CreateUrlCacheEntryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateUrlCacheGroup
class CreateUrlCacheGroup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteIE3Cache
class DeleteIE3Cache(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteUrlCacheContainerA
class DeleteUrlCacheContainerA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteUrlCacheContainerW
class DeleteUrlCacheContainerW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteUrlCacheEntry
class DeleteUrlCacheEntry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteUrlCacheEntryA
class DeleteUrlCacheEntryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteUrlCacheEntryW
class DeleteUrlCacheEntryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:DeleteUrlCacheGroup
class DeleteUrlCacheGroup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteWpadCacheForNetworks
class DeleteWpadCacheForNetworks(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DetectAutoProxyUrl
class DetectAutoProxyUrl(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'ptr', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DispatchAPICall
class DispatchAPICall(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DllInstall
class DllInstall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindCloseUrlCache
class FindCloseUrlCache(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindFirstUrlCacheContainerA
class FindFirstUrlCacheContainerA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindFirstUrlCacheContainerW
class FindFirstUrlCacheContainerW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindFirstUrlCacheEntryA
class FindFirstUrlCacheEntryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FindFirstUrlCacheEntryExA
class FindFirstUrlCacheEntryExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'ptr', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindFirstUrlCacheEntryExW
class FindFirstUrlCacheEntryExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn', 'unkn', 'unkn', 'ptr', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindFirstUrlCacheEntryW
class FindFirstUrlCacheEntryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindFirstUrlCacheGroup
class FindFirstUrlCacheGroup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindNextUrlCacheContainerA
class FindNextUrlCacheContainerA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FindNextUrlCacheContainerW
class FindNextUrlCacheContainerW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindNextUrlCacheEntryA
class FindNextUrlCacheEntryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FindNextUrlCacheEntryExA
class FindNextUrlCacheEntryExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindNextUrlCacheEntryExW
class FindNextUrlCacheEntryExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindNextUrlCacheEntryW
class FindNextUrlCacheEntryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FindNextUrlCacheGroup
class FindNextUrlCacheGroup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ForceNexusLookup
class ForceNexusLookup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:ForceNexusLookupExW
class ForceNexusLookupExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FreeUrlCacheSpaceA
class FreeUrlCacheSpaceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FreeUrlCacheSpaceW
class FreeUrlCacheSpaceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpCommandA
class FtpCommandA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpCommandW
class FtpCommandW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpCreateDirectoryA
class FtpCreateDirectoryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FtpCreateDirectoryW
class FtpCreateDirectoryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpDeleteFileA
class FtpDeleteFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FtpDeleteFileW
class FtpDeleteFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpFindFirstFileA
class FtpFindFirstFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'lpBuffer', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, StringA, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpFindFirstFileW
class FtpFindFirstFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpGetCurrentDirectoryA
class FtpGetCurrentDirectoryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'ptr']
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FtpGetCurrentDirectoryW
class FtpGetCurrentDirectoryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpGetFileA
class FtpGetFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['obj', 'unkn', 'unkn', 'unkn', 'unkn', 'dwSize', 'unkn']
    __argt__ = [ObjectRef, Unknown, Unknown, Unknown, Unknown, ntdll.DWORD, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpGetFileEx
class FtpGetFileEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['obj', 'unkn', 'lpFileName', 'unkn', 'unkn', 'dwSize', 'unkn']
    __argt__ = [ObjectRef, Unknown, StringW, Unknown, Unknown, ntdll.DWORD, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpGetFileSize
class FtpGetFileSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpGetFileW
class FtpGetFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['obj', 'unkn', 'lpFileName', 'unkn', 'unkn', 'dwSize', 'unkn']
    __argt__ = [ObjectRef, Unknown, StringW, Unknown, Unknown, ntdll.DWORD, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpOpenFileA
class FtpOpenFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpOpenFileW
class FtpOpenFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpPutFileA
class FtpPutFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['obj', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpPutFileEx
class FtpPutFileEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['obj', 'lpFileName', 'unkn', 'unkn', 'unkn']
    __argt__ = [ObjectRef, StringW, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpPutFileW
class FtpPutFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['obj', 'lpFileName', 'unkn', 'unkn', 'unkn']
    __argt__ = [ObjectRef, StringW, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpRemoveDirectoryA
class FtpRemoveDirectoryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FtpRemoveDirectoryW
class FtpRemoveDirectoryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpRenameFileA
class FtpRenameFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'ptr']
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FtpRenameFileW
class FtpRenameFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FtpSetCurrentDirectoryA
class FtpSetCurrentDirectoryA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:FtpSetCurrentDirectoryW
class FtpSetCurrentDirectoryW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheConfigInfoA
class GetUrlCacheConfigInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheConfigInfoW
class GetUrlCacheConfigInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheEntryInfoA
class GetUrlCacheEntryInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'ptr']
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheEntryInfoExA
class GetUrlCacheEntryInfoExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'ptr', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheEntryInfoExW
class GetUrlCacheEntryInfoExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheEntryInfoW
class GetUrlCacheEntryInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheGroupAttributeA
class GetUrlCacheGroupAttributeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheGroupAttributeW
class GetUrlCacheGroupAttributeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetUrlCacheHeaderData
class GetUrlCacheHeaderData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GopherCreateLocatorA
class GopherCreateLocatorA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherCreateLocatorW
class GopherCreateLocatorW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherFindFirstFileA
class GopherFindFirstFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherFindFirstFileW
class GopherFindFirstFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherGetAttributeA
class GopherGetAttributeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherGetAttributeW
class GopherGetAttributeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherGetLocatorTypeA
class GopherGetLocatorTypeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherGetLocatorTypeW
class GopherGetLocatorTypeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherOpenFileA
class GopherOpenFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GopherOpenFileW
class GopherOpenFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpAddRequestHeadersA
class HttpAddRequestHeadersA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'obj', 'unkn', 'unkn']
    __argt__ = [Unknown, ObjectRef, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpAddRequestHeadersW
class HttpAddRequestHeadersW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpCheckDavCompliance
class HttpCheckDavCompliance(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'ptr', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpEndRequestA
class HttpEndRequestA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpEndRequestW
class HttpEndRequestW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpOpenRequestA
class HttpOpenRequestA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'ptr', 'ptr', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpOpenRequestW
class HttpOpenRequestW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpQueryInfoA
class HttpQueryInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'obj', 'ptr', 'ptr']
    __argt__ = [Unknown, Unknown, ObjectRef, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:HttpQueryInfoW
class HttpQueryInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'obj', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, ObjectRef, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:HttpSendRequestA
class HttpSendRequestA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'obj', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, ObjectRef, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpSendRequestExA
class HttpSendRequestExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpSendRequestExW
class HttpSendRequestExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HttpSendRequestW
class HttpSendRequestW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IncrementUrlCacheHeaderData
class IncrementUrlCacheHeaderData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetAlgIdToStringA
class InternetAlgIdToStringA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetAlgIdToStringW
class InternetAlgIdToStringW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetAttemptConnect
class InternetAttemptConnect(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn']
    __argt__ = [ObjectRef, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetAutodial
class InternetAutodial(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetAutodialCallback
class InternetAutodialCallback(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetAutodialHangup
class InternetAutodialHangup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetCanonicalizeUrlA
class InternetCanonicalizeUrlA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr', 'unkn']
    __argt__ = [Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetCanonicalizeUrlW
class InternetCanonicalizeUrlW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetCheckConnectionA
class InternetCheckConnectionA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'ptr', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetCheckConnectionW
class InternetCheckConnectionW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetClearAllPerSiteCookieDecisions
class InternetClearAllPerSiteCookieDecisions(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:InternetCloseHandle
class InternetCloseHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetCombineUrlA
class InternetCombineUrlA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetCombineUrlW
class InternetCombineUrlW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetConfirmZoneCrossing
class InternetConfirmZoneCrossing(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'obj', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, ObjectRef, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetConfirmZoneCrossingA
class InternetConfirmZoneCrossingA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'obj', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, ObjectRef, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetConfirmZoneCrossingW
class InternetConfirmZoneCrossingW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetConnectA
class InternetConnectA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['obj', 'ptr', 'unkn', 'ptr', 'ptr', 'unkn', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Pointer, Unknown, Pointer, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetConnectW
class InternetConnectW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'obj', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ObjectRef, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetCrackUrlA
class InternetCrackUrlA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'ptr', 'unkn', 'unkn', 'ptr']
    __argt__ = [ObjectRef, Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetCrackUrlW
class InternetCrackUrlW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetCreateUrlA
class InternetCreateUrlA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr', 'ptr']
    __argt__ = [Pointer, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetCreateUrlW
class InternetCreateUrlW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetDial
class InternetDial(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetDialA
class InternetDialA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetDialW
class InternetDialW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetEnumPerSiteCookieDecisionA
class InternetEnumPerSiteCookieDecisionA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'ptr', 'unkn']
    __argt__ = [Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetEnumPerSiteCookieDecisionW
class InternetEnumPerSiteCookieDecisionW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'ptr', 'unkn']
    __argt__ = [Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetErrorDlg
class InternetErrorDlg(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetFindNextFileA
class InternetFindNextFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'lpBuffer']
    __argt__ = [Unknown, StringA, ]
#EMUFUNCDONE

#EMUFUNC:InternetFindNextFileW
class InternetFindNextFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetFortezzaCommand
class InternetFortezzaCommand(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetCertByURL
class InternetGetCertByURL(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetCertByURLA
class InternetGetCertByURLA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetConnectedState
class InternetGetConnectedState(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetConnectedStateEx
class InternetGetConnectedStateEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetConnectedStateExA
class InternetGetConnectedStateExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetConnectedStateExW
class InternetGetConnectedStateExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetCookieA
class InternetGetCookieA(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'ptr', 'unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetCookieExA
class InternetGetCookieExA(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ptr', 'edx', 'ptr', 'ptr', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Pointer, Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetCookieExW
class InternetGetCookieExW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'ptr', 'unkn', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetCookieW
class InternetGetCookieW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'ptr', 'unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetLastResponseInfoA
class InternetGetLastResponseInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr']
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetLastResponseInfoW
class InternetGetLastResponseInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetPerSiteCookieDecisionA
class InternetGetPerSiteCookieDecisionA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetPerSiteCookieDecisionW
class InternetGetPerSiteCookieDecisionW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetSecurityInfoByURL
class InternetGetSecurityInfoByURL(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'ptr', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetSecurityInfoByURLA
class InternetGetSecurityInfoByURLA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'ptr', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGetSecurityInfoByURLW
class InternetGetSecurityInfoByURLW(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'ptr', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGoOnline
class InternetGoOnline(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGoOnlineA
class InternetGoOnlineA(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetGoOnlineW
class InternetGoOnlineW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetHangUp
class InternetHangUp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetInitializeAutoProxyDll
class InternetInitializeAutoProxyDll(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn']
    __argt__ = [ObjectRef, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetLockRequestFile
class InternetLockRequestFile(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'obj', 'ptr']
    __argt__ = [ObjectRef, ObjectRef, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetOpenA
class InternetOpenA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'ptr', 'unkn', 'ptr', 'ptr', 'unkn']
    __argt__ = [ObjectRef, Pointer, Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetOpenUrlA
class InternetOpenUrlA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'ptr', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetOpenUrlW
class InternetOpenUrlW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetOpenW
class InternetOpenW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetQueryDataAvailable
class InternetQueryDataAvailable(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetQueryFortezzaStatus
class InternetQueryFortezzaStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetQueryOptionA
class InternetQueryOptionA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'obj', 'unkn', 'obj', 'ptr']
    __argt__ = [ObjectRef, ObjectRef, Unknown, ObjectRef, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetQueryOptionW
class InternetQueryOptionW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'obj', 'unkn', 'obj', 'ptr']
    __argt__ = [Unknown, Unknown, ObjectRef, Unknown, ObjectRef, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetReadFile
class InternetReadFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'lpBuffer', 'nNumberOfBytesToRead', 'ptr']
    __argt__ = [Unknown, StringA, ntdll.DWORD, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetReadFileExA
class InternetReadFileExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetReadFileExW
class InternetReadFileExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSecurityProtocolToStringA
class InternetSecurityProtocolToStringA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSecurityProtocolToStringW
class InternetSecurityProtocolToStringW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetCookieA
class InternetSetCookieA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr']
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetCookieExA
class InternetSetCookieExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetCookieExW
class InternetSetCookieExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetCookieW
class InternetSetCookieW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetDialState
class InternetSetDialState(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetDialStateA
class InternetSetDialStateA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetDialStateW
class InternetSetDialStateW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetFilePointer
class InternetSetFilePointer(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetOptionA
class InternetSetOptionA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'obj', 'unkn', 'ptr', 'unkn']
    __argt__ = [ObjectRef, ObjectRef, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetOptionExA
class InternetSetOptionExA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'obj', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [ObjectRef, ObjectRef, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetOptionExW
class InternetSetOptionExW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'obj', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ObjectRef, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetOptionW
class InternetSetOptionW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'obj', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, ObjectRef, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetPerSiteCookieDecisionA
class InternetSetPerSiteCookieDecisionA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetPerSiteCookieDecisionW
class InternetSetPerSiteCookieDecisionW(emufunc.EmuFunc):
    __callconv__ = 'msfastcall'
    __argn__ = ['ecx', 'edx', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetStatusCallback
class InternetSetStatusCallback(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetStatusCallbackA
class InternetSetStatusCallbackA(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetSetStatusCallbackW
class InternetSetStatusCallbackW(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'unkn']
    __argt__ = [ObjectRef, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetShowSecurityInfoByURL
class InternetShowSecurityInfoByURL(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetShowSecurityInfoByURLA
class InternetShowSecurityInfoByURLA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetShowSecurityInfoByURLW
class InternetShowSecurityInfoByURLW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetTimeFromSystemTime
class InternetTimeFromSystemTime(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr', 'unkn']
    __argt__ = [Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetTimeFromSystemTimeA
class InternetTimeFromSystemTimeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr', 'unkn']
    __argt__ = [Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetTimeFromSystemTimeW
class InternetTimeFromSystemTimeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn', 'dwSize']
    __argt__ = [Pointer, Unknown, Unknown, ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:InternetTimeToSystemTime
class InternetTimeToSystemTime(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetTimeToSystemTimeA
class InternetTimeToSystemTimeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetTimeToSystemTimeW
class InternetTimeToSystemTimeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetUnlockRequestFile
class InternetUnlockRequestFile(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'lpVoid']
    __argt__ = [ObjectRef, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:InternetWriteFile
class InternetWriteFile(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'lpSrc', 'dwSize', 'lpNumberOfBytesWritten']
    __argt__ = [ObjectRef, Unknown, Pointer, ntdll.DWORD, ntdll.DWORD_P, ]
#EMUFUNCDONE

#EMUFUNC:InternetWriteFileExA
class InternetWriteFileExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InternetWriteFileExW
class InternetWriteFileExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsHostInProxyBypassList
class IsHostInProxyBypassList(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = ['obj', 'unkn', 'ptr', 'unkn']
    __argt__ = [ObjectRef, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsUrlCacheEntryExpiredA
class IsUrlCacheEntryExpiredA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsUrlCacheEntryExpiredW
class IsUrlCacheEntryExpiredW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LoadUrlCacheContent
class LoadUrlCacheContent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:ParseX509EncodedCertificateForListBoxEntry
class ParseX509EncodedCertificateForListBoxEntry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PrivacyGetZonePreferenceW
class PrivacyGetZonePreferenceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:PrivacySetZonePreferenceW
class PrivacySetZonePreferenceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'ptr']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ReadUrlCacheEntryStream
class ReadUrlCacheEntryStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'lpBuffer', 'lpNumberOfBytesRead', 'unkn']
    __argt__ = [Unknown, Unknown, StringA, ntdll.DWORD_P, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ReadUrlCacheEntryStreamEx
class ReadUrlCacheEntryStreamEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'lpBuffer', 'lpNumberOfBytesRead']
    __argt__ = [Unknown, Unknown, Unknown, StringA, ntdll.DWORD_P, ]
#EMUFUNCDONE

#EMUFUNC:RegisterUrlCacheNotification
class RegisterUrlCacheNotification(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ResumeSuspendedDownload
class ResumeSuspendedDownload(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RetrieveUrlCacheEntryFileA
class RetrieveUrlCacheEntryFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RetrieveUrlCacheEntryFileW
class RetrieveUrlCacheEntryFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RetrieveUrlCacheEntryStreamA
class RetrieveUrlCacheEntryStreamA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'ptr', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RetrieveUrlCacheEntryStreamW
class RetrieveUrlCacheEntryStreamW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RunOnceUrlCache
class RunOnceUrlCache(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheConfigInfoA
class SetUrlCacheConfigInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheConfigInfoW
class SetUrlCacheConfigInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheEntryGroup
class SetUrlCacheEntryGroup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheEntryGroupA
class SetUrlCacheEntryGroupA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheEntryGroupW
class SetUrlCacheEntryGroupW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheEntryInfoA
class SetUrlCacheEntryInfoA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'ptr', 'unkn']
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheEntryInfoW
class SetUrlCacheEntryInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn', 'unkn']
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheGroupAttributeA
class SetUrlCacheGroupAttributeA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheGroupAttributeW
class SetUrlCacheGroupAttributeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn', 'unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetUrlCacheHeaderData
class SetUrlCacheHeaderData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ShowCertificate
class ShowCertificate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ShowClientAuthCerts
class ShowClientAuthCerts(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn']
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ShowSecurityInfo
class ShowSecurityInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'ptr']
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:ShowX509EncodedCertificate
class ShowX509EncodedCertificate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnlockUrlCacheEntryFile
class UnlockUrlCacheEntryFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnlockUrlCacheEntryFileA
class UnlockUrlCacheEntryFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnlockUrlCacheEntryFileW
class UnlockUrlCacheEntryFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['ptr', 'unkn']
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnlockUrlCacheEntryStream
class UnlockUrlCacheEntryStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn']
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UpdateUrlCacheContentPath
class UpdateUrlCacheContentPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpFileName']
    __argt__ = [StringA, ]
#EMUFUNCDONE

#EMUFUNC:UrlZonesDetach
class UrlZonesDetach(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_GetFileExtensionFromUrl
class _GetFileExtensionFromUrl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'ptr', 'unkn']
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:main_entry
class main_entry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['unkn', 'unkn', 'unkn']
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

