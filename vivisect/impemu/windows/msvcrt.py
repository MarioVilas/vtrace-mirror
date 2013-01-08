
import vivisect.impemu.emufunc as emufunc
from vivisect.impemu.impmagic import *
import ntdll

class malloc(emufunc.EmuFunc):
    __callconv__ = "cdecl"
    __argt__ = [ntdll.DWORD,]
    __argn__ = ["dwSize",]

    def __call__(self, emu):
        size = self.getArgs(emu)[0]
        r = HeapChunk(size)
        ret = emu.setMagic(r)
        self.setReturn(emu, ret)

#EMUFUNC:_CIacos
class _CIacos(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIasin
class _CIasin(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIatan
class _CIatan(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIatan2
class _CIatan2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIcos
class _CIcos(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIcosh
class _CIcosh(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIexp
class _CIexp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIfmod
class _CIfmod(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIlog
class _CIlog(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIlog10
class _CIlog10(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIpow
class _CIpow(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIsin
class _CIsin(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIsinh
class _CIsinh(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CIsqrt
class _CIsqrt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CItan
class _CItan(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CItanh
class _CItanh(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_CxxThrowException
class _CxxThrowException(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_EH_prolog
class _EH_prolog(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_Getdays
class _Getdays(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_Getmonths
class _Getmonths(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_Gettnames
class _Gettnames(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_Strftime
class _Strftime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_XcptFilter
class _XcptFilter(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__CxxCallUnwindDtor
class __CxxCallUnwindDtor(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__CxxDetectRethrow
class __CxxDetectRethrow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__CxxExceptionFilter
class __CxxExceptionFilter(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__CxxFrameHandler
class __CxxFrameHandler(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__CxxLongjmpUnwind
class __CxxLongjmpUnwind(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__CxxQueryExceptionSize
class __CxxQueryExceptionSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__CxxRegisterExceptionObject
class __CxxRegisterExceptionObject(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__CxxUnregisterExceptionObject
class __CxxUnregisterExceptionObject(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__DestructExceptionObject
class __DestructExceptionObject(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__RTCastToVoid
class __RTCastToVoid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__RTDynamicCast
class __RTDynamicCast(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__RTtypeid
class __RTtypeid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__STRINGTOLD
class __STRINGTOLD(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:___lc_codepage_func
class ___lc_codepage_func(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:___lc_handle_func
class ___lc_handle_func(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:___mb_cur_max_func
class ___mb_cur_max_func(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:___setlc_active_func
class ___setlc_active_func(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:___unguarded_readlc_active_add_func
class ___unguarded_readlc_active_add_func(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__crtCompareStringA
class __crtCompareStringA(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__crtCompareStringW
class __crtCompareStringW(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__crtGetLocaleInfoW
class __crtGetLocaleInfoW(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__crtGetStringTypeW
class __crtGetStringTypeW(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__crtLCMapStringA
class __crtLCMapStringA(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__crtLCMapStringW
class __crtLCMapStringW(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__dllonexit
class __dllonexit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__doserrno
class __doserrno(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__fpecode
class __fpecode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__getmainargs
class __getmainargs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__iob_func
class __iob_func(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__isascii
class __isascii(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__iscsym
class __iscsym(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__iscsymf
class __iscsymf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__lconv_init
class __lconv_init(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p___argc
class __p___argc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p___argv
class __p___argv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p___initenv
class __p___initenv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p___mb_cur_max
class __p___mb_cur_max(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p___wargv
class __p___wargv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p___winitenv
class __p___winitenv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__acmdln
class __p__acmdln(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__amblksiz
class __p__amblksiz(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__commode
class __p__commode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__daylight
class __p__daylight(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__dstbias
class __p__dstbias(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__environ
class __p__environ(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__fileinfo
class __p__fileinfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__fmode
class __p__fmode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__iob
class __p__iob(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__mbcasemap
class __p__mbcasemap(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__mbctype
class __p__mbctype(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__osver
class __p__osver(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__pctype
class __p__pctype(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__pgmptr
class __p__pgmptr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__pwctype
class __p__pwctype(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__timezone
class __p__timezone(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__tzname
class __p__tzname(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__wcmdln
class __p__wcmdln(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__wenviron
class __p__wenviron(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__winmajor
class __p__winmajor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__winminor
class __p__winminor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__winver
class __p__winver(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__p__wpgmptr
class __p__wpgmptr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__pctype_func
class __pctype_func(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__pxcptinfoptrs
class __pxcptinfoptrs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__set_app_type
class __set_app_type(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__setusermatherr
class __setusermatherr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__threadhandle
class __threadhandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__threadid
class __threadid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__toascii
class __toascii(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__unDName
class __unDName(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__unDNameEx
class __unDNameEx(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__uncaught_exception
class __uncaught_exception(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:__wcserror
class __wcserror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:__wgetmainargs
class __wgetmainargs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_abnormal_termination
class _abnormal_termination(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_access
class _access(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_adj_fdiv_m16i
class _adj_fdiv_m16i(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_adj_fdiv_m32
class _adj_fdiv_m32(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_adj_fdiv_m32i
class _adj_fdiv_m32i(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_adj_fdiv_m64
class _adj_fdiv_m64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_adj_fdiv_r
class _adj_fdiv_r(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_adj_fdivr_m16i
class _adj_fdivr_m16i(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_adj_fdivr_m32
class _adj_fdivr_m32(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_adj_fdivr_m32i
class _adj_fdivr_m32i(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_adj_fdivr_m64
class _adj_fdivr_m64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_adj_fpatan
class _adj_fpatan(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_adj_fprem
class _adj_fprem(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_adj_fprem1
class _adj_fprem1(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_adj_fptan
class _adj_fptan(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_aligned_free
class _aligned_free(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_aligned_malloc
class _aligned_malloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_aligned_offset_malloc
class _aligned_offset_malloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_aligned_offset_realloc
class _aligned_offset_realloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_aligned_realloc
class _aligned_realloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_amsg_exit
class _amsg_exit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_assert
class _assert(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_atodbl
class _atodbl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_atoi64
class _atoi64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_atoldbl
class _atoldbl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_beep
class _beep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_beginthread
class _beginthread(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = ["start_address", "stack_size", "arglist"]
    __argt__ = [FUNCPTR, UINT32, Pointer, ]
#EMUFUNCDONE
        
#EMUFUNC:_beginthreadex
class _beginthreadex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = ["security", "stack_size", "start_address", "arglist", "initflag", "thrdaddr"]
    __argt__ = [Pointer, UINT32, FUNCPTR, Pointer, UINT32, UINT32, ]
#EMUFUNCDONE

#EMUFUNC:_c_exit
class _c_exit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_cabs
class _cabs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_callnewh
class _callnewh(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cexit
class _cexit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_cgets
class _cgets(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cgetws
class _cgetws(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_chdir
class _chdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_chdrive
class _chdrive(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_chgsign
class _chgsign(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_chkesp
class _chkesp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_chmod
class _chmod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_chsize
class _chsize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_clearfp
class _clearfp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_close
class _close(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_commit
class _commit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_control87
class _control87(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_controlfp
class _controlfp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_copysign
class _copysign(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cprintf
class _cprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cputs
class _cputs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cputws
class _cputws(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_creat
class _creat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cscanf
class _cscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ctime64
class _ctime64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cwait
class _cwait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cwprintf
class _cwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_cwscanf
class _cwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_dup
class _dup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_dup2
class _dup2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ecvt
class _ecvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_endthread
class _endthread(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_endthreadex
class _endthreadex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_eof
class _eof(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_errno
class _errno(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_except_handler2
class _except_handler2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_except_handler3
class _except_handler3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_execl
class _execl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_execle
class _execle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_execlp
class _execlp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_execlpe
class _execlpe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_execv
class _execv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_execve
class _execve(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_execvp
class _execvp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_execvpe
class _execvpe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_exit
class _exit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_expand
class _expand(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fcloseall
class _fcloseall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_fcvt
class _fcvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fdopen
class _fdopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fgetchar
class _fgetchar(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_fgetwchar
class _fgetwchar(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_filbuf
class _filbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_filelength
class _filelength(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_filelengthi64
class _filelengthi64(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fileno
class _fileno(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_findclose
class _findclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_findfirst
class _findfirst(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_findfirst64
class _findfirst64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_findfirsti64
class _findfirsti64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_findnext
class _findnext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_findnext64
class _findnext64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_findnexti64
class _findnexti64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_finite
class _finite(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_flsbuf
class _flsbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_flushall
class _flushall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_fpclass
class _fpclass(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fpieee_flt
class _fpieee_flt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fpreset
class _fpreset(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_fputchar
class _fputchar(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fputwchar
class _fputwchar(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fsopen
class _fsopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fstat
class _fstat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fstat64
class _fstat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_fstati64
class _fstati64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ftime
class _ftime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ftime64
class _ftime64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ftol
class _ftol(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_fullpath
class _fullpath(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_futime
class _futime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_futime64
class _futime64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_gcvt
class _gcvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_get_heap_handle
class _get_heap_handle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_get_osfhandle
class _get_osfhandle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_get_sbh_threshold
class _get_sbh_threshold(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getch
class _getch(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getche
class _getche(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getcwd
class _getcwd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_getdcwd
class _getdcwd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_getdiskfree
class _getdiskfree(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_getdllprocaddr
class _getdllprocaddr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_getdrive
class _getdrive(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getdrives
class _getdrives(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getmaxstdio
class _getmaxstdio(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getmbcp
class _getmbcp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getpid
class _getpid(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getsystime
class _getsystime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_getw
class _getw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_getwch
class _getwch(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getwche
class _getwche(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_getws
class _getws(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_global_unwind2
class _global_unwind2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_gmtime64
class _gmtime64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_heapadd
class _heapadd(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_heapchk
class _heapchk(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_heapmin
class _heapmin(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_heapset
class _heapset(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_heapused
class _heapused(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_heapwalk
class _heapwalk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_hypot
class _hypot(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_i64toa
class _i64toa(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_i64tow
class _i64tow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_initterm
class _initterm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_inp
class _inp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_inpd
class _inpd(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_inpw
class _inpw(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_isatty
class _isatty(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_isctype
class _isctype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbalnum
class _ismbbalnum(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbalpha
class _ismbbalpha(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbgraph
class _ismbbgraph(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbkalnum
class _ismbbkalnum(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbkana
class _ismbbkana(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbkprint
class _ismbbkprint(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbkpunct
class _ismbbkpunct(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbblead
class _ismbblead(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbprint
class _ismbbprint(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbpunct
class _ismbbpunct(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbbtrail
class _ismbbtrail(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcalnum
class _ismbcalnum(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcalpha
class _ismbcalpha(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcdigit
class _ismbcdigit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcgraph
class _ismbcgraph(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbchira
class _ismbchira(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbckata
class _ismbckata(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcl0
class _ismbcl0(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcl1
class _ismbcl1(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcl2
class _ismbcl2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbclegal
class _ismbclegal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbclower
class _ismbclower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcprint
class _ismbcprint(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcpunct
class _ismbcpunct(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcspace
class _ismbcspace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcsymbol
class _ismbcsymbol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbcupper
class _ismbcupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbslead
class _ismbslead(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ismbstrail
class _ismbstrail(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_isnan
class _isnan(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_itoa
class _itoa(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_itow
class _itow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_j0
class _j0(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_j1
class _j1(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_jn
class _jn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_kbhit
class _kbhit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_lfind
class _lfind(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_loaddll
class _loaddll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_local_unwind2
class _local_unwind2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_localtime64
class _localtime64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_lock
class _lock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_locking
class _locking(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_logb
class _logb(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_longjmpex
class _longjmpex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_lrotl
class _lrotl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_lrotr
class _lrotr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_lsearch
class _lsearch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_lseek
class _lseek(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_lseeki64
class _lseeki64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ltoa
class _ltoa(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ltow
class _ltow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_makepath
class _makepath(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbbtombc
class _mbbtombc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbbtype
class _mbbtype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbccpy
class _mbccpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbcjistojms
class _mbcjistojms(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbcjmstojis
class _mbcjmstojis(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbclen
class _mbclen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbctohira
class _mbctohira(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbctokata
class _mbctokata(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbctolower
class _mbctolower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbctombb
class _mbctombb(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbctoupper
class _mbctoupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsbtype
class _mbsbtype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbscat
class _mbscat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbschr
class _mbschr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbscmp
class _mbscmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbscoll
class _mbscoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbscpy
class _mbscpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbscspn
class _mbscspn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsdec
class _mbsdec(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsdup
class _mbsdup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsicmp
class _mbsicmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsicoll
class _mbsicoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsinc
class _mbsinc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbslen
class _mbslen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbslwr
class _mbslwr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnbcat
class _mbsnbcat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnbcmp
class _mbsnbcmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnbcnt
class _mbsnbcnt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnbcoll
class _mbsnbcoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnbcpy
class _mbsnbcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnbicmp
class _mbsnbicmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnbicoll
class _mbsnbicoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnbset
class _mbsnbset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsncat
class _mbsncat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnccnt
class _mbsnccnt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsncmp
class _mbsncmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsncoll
class _mbsncoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsncpy
class _mbsncpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnextc
class _mbsnextc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnicmp
class _mbsnicmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnicoll
class _mbsnicoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsninc
class _mbsninc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsnset
class _mbsnset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbspbrk
class _mbspbrk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsrchr
class _mbsrchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsrev
class _mbsrev(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsset
class _mbsset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsspn
class _mbsspn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsspnp
class _mbsspnp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsstr
class _mbsstr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbstok
class _mbstok(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbstrlen
class _mbstrlen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mbsupr
class _mbsupr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_memccpy
class _memccpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_memicmp
class _memicmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mkdir
class _mkdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mktemp
class _mktemp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_mktime64
class _mktime64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_msize
class _msize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_nextafter
class _nextafter(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_onexit
class _onexit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_open
class _open(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_open_osfhandle
class _open_osfhandle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_outp
class _outp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_outpd
class _outpd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_outpw
class _outpw(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_pclose
class _pclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_pipe
class _pipe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_popen
class _popen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_purecall
class _purecall(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_putch
class _putch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_putenv
class _putenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_putw
class _putw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_putwch
class _putwch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_putws
class _putws(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_read
class _read(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_resetstkoflw
class _resetstkoflw(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_rmdir
class _rmdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_rmtmp
class _rmtmp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_rotl
class _rotl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_rotr
class _rotr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_safe_fdiv
class _safe_fdiv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_safe_fdivr
class _safe_fdivr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_safe_fprem
class _safe_fprem(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_safe_fprem1
class _safe_fprem1(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_scalb
class _scalb(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_scprintf
class _scprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_scwprintf
class _scwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_searchenv
class _searchenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_seh_longjmp_unwind
class _seh_longjmp_unwind(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_set_SSE2_enable
class _set_SSE2_enable(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_set_error_mode
class _set_error_mode(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_set_sbh_threshold
class _set_sbh_threshold(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_seterrormode
class _seterrormode(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_setjmp
class _setjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_setjmp3
class _setjmp3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_setmaxstdio
class _setmaxstdio(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_setmbcp
class _setmbcp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_setmode
class _setmode(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_setsystime
class _setsystime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_sleep
class _sleep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_snprintf
class _snprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_snscanf
class _snscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_snwprintf
class _snwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_snwscanf
class _snwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_sopen
class _sopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_spawnl
class _spawnl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_spawnle
class _spawnle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_spawnlp
class _spawnlp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_spawnlpe
class _spawnlpe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_spawnv
class _spawnv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_spawnve
class _spawnve(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_spawnvp
class _spawnvp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_spawnvpe
class _spawnvpe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_splitpath
class _splitpath(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_stat
class _stat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_stat64
class _stat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_stati64
class _stati64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_statusfp
class _statusfp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_strcmpi
class _strcmpi(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strdate
class _strdate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strdup
class _strdup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strerror
class _strerror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_stricmp
class _stricmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_stricoll
class _stricoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strlwr
class _strlwr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strncoll
class _strncoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strnicmp
class _strnicmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strnicoll
class _strnicoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strnset
class _strnset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strrev
class _strrev(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strset
class _strset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strtime
class _strtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strtoi64
class _strtoi64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strtoui64
class _strtoui64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_strupr
class _strupr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_swab
class _swab(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_tell
class _tell(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_telli64
class _telli64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_tempnam
class _tempnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_time64
class _time64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_tolower
class _tolower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_toupper
class _toupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_tzset
class _tzset(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:_ui64toa
class _ui64toa(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ui64tow
class _ui64tow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ultoa
class _ultoa(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ultow
class _ultow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_umask
class _umask(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ungetch
class _ungetch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_ungetwch
class _ungetwch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_unlink
class _unlink(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_unloaddll
class _unloaddll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_unlock
class _unlock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_utime
class _utime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_utime64
class _utime64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_vscprintf
class _vscprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_vscwprintf
class _vscwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_vsnprintf
class _vsnprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_vsnwprintf
class _vsnwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_waccess
class _waccess(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wasctime
class _wasctime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wchdir
class _wchdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wchmod
class _wchmod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcreat
class _wcreat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsdup
class _wcsdup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcserror
class _wcserror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsicmp
class _wcsicmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsicoll
class _wcsicoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcslwr
class _wcslwr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsncoll
class _wcsncoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsnicmp
class _wcsnicmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsnicoll
class _wcsnicoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsnset
class _wcsnset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsrev
class _wcsrev(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsset
class _wcsset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcstoi64
class _wcstoi64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcstoui64
class _wcstoui64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wcsupr
class _wcsupr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wctime
class _wctime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wctime64
class _wctime64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wexecl
class _wexecl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wexecle
class _wexecle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wexeclp
class _wexeclp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wexeclpe
class _wexeclpe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wexecv
class _wexecv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wexecve
class _wexecve(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wexecvp
class _wexecvp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wexecvpe
class _wexecvpe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfdopen
class _wfdopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfindfirst
class _wfindfirst(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfindfirst64
class _wfindfirst64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfindfirsti64
class _wfindfirsti64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfindnext
class _wfindnext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfindnext64
class _wfindnext64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfindnexti64
class _wfindnexti64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfopen
class _wfopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfreopen
class _wfreopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfsopen
class _wfsopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wfullpath
class _wfullpath(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wgetcwd
class _wgetcwd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wgetdcwd
class _wgetdcwd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wgetenv
class _wgetenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wmakepath
class _wmakepath(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wmkdir
class _wmkdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wmktemp
class _wmktemp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wopen
class _wopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wperror
class _wperror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wpopen
class _wpopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wputenv
class _wputenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wremove
class _wremove(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wrename
class _wrename(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_write
class _write(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wrmdir
class _wrmdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wsearchenv
class _wsearchenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wsetlocale
class _wsetlocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wsopen
class _wsopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wspawnl
class _wspawnl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wspawnle
class _wspawnle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wspawnlp
class _wspawnlp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wspawnlpe
class _wspawnlpe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wspawnv
class _wspawnv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wspawnve
class _wspawnve(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wspawnvp
class _wspawnvp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wspawnvpe
class _wspawnvpe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wsplitpath
class _wsplitpath(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wstat
class _wstat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wstat64
class _wstat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wstati64
class _wstati64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wstrdate
class _wstrdate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wstrtime
class _wstrtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wsystem
class _wsystem(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wtempnam
class _wtempnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wtmpnam
class _wtmpnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wtof
class _wtof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wtoi
class _wtoi(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wtoi64
class _wtoi64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wtol
class _wtol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wunlink
class _wunlink(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wutime
class _wutime(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_wutime64
class _wutime64(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_y0
class _y0(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_y1
class _y1(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:_yn
class _yn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:acos
class acos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:asctime
class asctime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:asin
class asin(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:atan
class atan(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:atan2
class atan2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:atexit
class atexit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:atof
class atof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:atoi
class atoi(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:atol
class atol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:bsearch
class bsearch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:calloc
class calloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ceil
class ceil(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:clearerr
class clearerr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:clock
class clock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:cos
class cos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:cosh
class cosh(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ctime
class ctime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:difftime
class difftime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:div
class div(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:exp
class exp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fabs
class fabs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fclose
class fclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:feof
class feof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ferror
class ferror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fflush
class fflush(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fgetc
class fgetc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fgetpos
class fgetpos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fgets
class fgets(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fgetwc
class fgetwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fgetws
class fgetws(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:floor
class floor(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fmod
class fmod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fopen
class fopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fprintf
class fprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fputc
class fputc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fputs
class fputs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fputwc
class fputwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fputws
class fputws(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fread
class fread(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:free
class free(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:freopen
class freopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:frexp
class frexp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fscanf
class fscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fseek
class fseek(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fsetpos
class fsetpos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ftell
class ftell(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fwprintf
class fwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fwrite
class fwrite(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:fwscanf
class fwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getc
class getc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getchar
class getchar(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:getenv
class getenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:gets
class gets(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getwc
class getwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:getwchar
class getwchar(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:gmtime
class gmtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:is_wctype
class is_wctype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isalnum
class isalnum(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isalpha
class isalpha(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iscntrl
class iscntrl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isdigit
class isdigit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isgraph
class isgraph(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isleadbyte
class isleadbyte(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:islower
class islower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isprint
class isprint(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ispunct
class ispunct(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isspace
class isspace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isupper
class isupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswalnum
class iswalnum(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswalpha
class iswalpha(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswascii
class iswascii(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:iswcntrl
class iswcntrl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswctype
class iswctype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswdigit
class iswdigit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswgraph
class iswgraph(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswlower
class iswlower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswprint
class iswprint(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswpunct
class iswpunct(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswspace
class iswspace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswupper
class iswupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:iswxdigit
class iswxdigit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:isxdigit
class isxdigit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ldexp
class ldexp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ldiv
class ldiv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:localeconv
class localeconv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:localtime
class localtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:log
class log(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:log10
class log10(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:main_entry
class main_entry(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:malloc
class malloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:mblen
class mblen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:mbstowcs
class mbstowcs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:mbtowc
class mbtowc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:memchr
class memchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:memcmp
class memcmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:memcpy
class memcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:memmove
class memmove(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:memset
class memset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:mktime
class mktime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:modf
class modf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:perror
class perror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:pow
class pow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:printf
class printf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:putc
class putc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:putchar
class putchar(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:puts
class puts(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:putwc
class putwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:putwchar
class putwchar(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:qsort
class qsort(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:raise
class _raise(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:rand
class rand(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:realloc
class realloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:remove
class remove(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:rename
class rename(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:rewind
class rewind(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:scanf
class scanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:setbuf
class setbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:setlocale
class setlocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:setvbuf
class setvbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:signal
class signal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:sin
class sin(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:sinh
class sinh(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:sprintf
class sprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:sqrt
class sqrt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:srand
class srand(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:sscanf
class sscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strcat
class strcat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strchr
class strchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strcmp
class strcmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strcoll
class strcoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strcpy
class strcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strcspn
class strcspn(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strerror
class strerror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strftime
class strftime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strlen
class strlen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strncat
class strncat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strncmp
class strncmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strncpy
class strncpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strpbrk
class strpbrk(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strrchr
class strrchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strspn
class strspn(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strstr
class strstr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strtod
class strtod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strtok
class strtok(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strtol
class strtol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strtoul
class strtoul(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:strxfrm
class strxfrm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:swprintf
class swprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:swscanf
class swscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:system
class system(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:tan
class tan(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:tanh
class tanh(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:time
class time(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:tmpfile
class tmpfile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:tmpnam
class tmpnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:tolower
class tolower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:toupper
class toupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:towlower
class towlower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:towupper
class towupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ungetc
class ungetc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ungetwc
class ungetwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:vfprintf
class vfprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:vfwprintf
class vfwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:vprintf
class vprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:vsprintf
class vsprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:vswprintf
class vswprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:vwprintf
class vwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcscat
class wcscat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcschr
class wcschr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcscmp
class wcscmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcscoll
class wcscoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcscpy
class wcscpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcscspn
class wcscspn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcsftime
class wcsftime(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcslen
class wcslen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcsncat
class wcsncat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcsncmp
class wcsncmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcsncpy
class wcsncpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcspbrk
class wcspbrk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcsrchr
class wcsrchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcsspn
class wcsspn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcsstr
class wcsstr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcstod
class wcstod(emufunc.EmuFunc):
    __callconv__ = 'unknown'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcstok
class wcstok(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcstol
class wcstol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcstombs
class wcstombs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcstoul
class wcstoul(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wcsxfrm
class wcsxfrm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wctomb
class wctomb(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wprintf
class wprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:wscanf
class wscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

