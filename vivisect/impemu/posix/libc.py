
from vivisect.const import *
from vivisect.impemu.impmagic import *
import vivisect.impemu.emufunc as emufunc

#EMUFUNC:__strspn_c1
class __strspn_c1(emufunc.EmuFunc):
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


#EMUFUNC:__gethostname_chk
class __gethostname_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strspn_c2
class __strspn_c2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setrpcent
class setrpcent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstod_l
class __wcstod_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strspn_c3
class __strspn_c3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sched_get_priority_min
class sched_get_priority_min(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:epoll_create
class epoll_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:klogctl
class klogctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__tolower_l
class __tolower_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dprintf
class dprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcscoll_l
class __wcscoll_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setuid
class setuid(emufunc.EmuFunc):
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


#EMUFUNC:__gettimeofday
class __gettimeofday(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__internal_endnetgrent
class __internal_endnetgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:chroot
class chroot(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_setbuf
class _IO_file_setbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getdate
class getdate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vswprintf_chk
class __vswprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_fopen
class _IO_file_fopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_cond_signal
class pthread_cond_signal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtoull_l
class strtoull_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_short
class xdr_short(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_padn
class _IO_padn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lfind
class lfind(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:strcasestr
class strcasestr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_fork
class __libc_fork(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdr_int64_t
class xdr_int64_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstod_l
class wcstod_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:socket
class socket(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:key_encryptsession_pk
class key_encryptsession_pk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_create
class argz_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strpbrk_g
class __strpbrk_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putchar_unlocked
class putchar_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_pmaplist
class xdr_pmaplist(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__res_init
class __res_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__xpg_basename
class __xpg_basename(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__stpcpy_chk
class __stpcpy_chk(emufunc.EmuFunc):
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


#EMUFUNC:_IO_wdefault_xsputn
class _IO_wdefault_xsputn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcpncpy
class wcpncpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mkdtemp
class mkdtemp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:srand48_r
class srand48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sighold
class sighold(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__default_morecore
class __default_morecore(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sched_getparam
class __sched_getparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iruserok
class iruserok(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:cuserid
class cuserid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:isnan
class isnan(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setstate_r
class setstate_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wmemset
class wmemset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__register_frame_info_bases
class __register_frame_info_bases(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_stat
class _IO_file_stat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:argz_replace
class argz_replace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:globfree64
class globfree64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argp_usage
class argp_usage(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_next
class argz_next(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getspnam_r
class getspnam_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fork
class __fork(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__sched_yield
class __sched_yield(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:res_init
class res_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__gmtime_r
class __gmtime_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:l64a
class l64a(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_attach
class _IO_file_attach(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strstr_g
class __strstr_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsftime_l
class wcsftime_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gets
class gets(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:putc_unlocked
class putc_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getrpcbyname
class getrpcbyname(emufunc.EmuFunc):
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


#EMUFUNC:_authenticate
class _authenticate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:a64l
class a64l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:hcreate
class hcreate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strcpy
class strcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__libc_init_first
class __libc_init_first(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdr_long
class xdr_long(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:shmget
class shmget(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigsuspend
class sigsuspend(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wdo_write
class _IO_wdo_write(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getw
class getw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gethostid
class gethostid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:flockfile
class flockfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__rawmemchr
class __rawmemchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsncasecmp_l
class wcsncasecmp_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_add
class argz_add(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__backtrace_symbols
class __backtrace_symbols(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strncpy_byn
class __strncpy_byn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vasprintf
class vasprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_un_link
class _IO_un_link(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_mcount
class _mcount(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__wcstod_internal
class __wcstod_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:authunix_create
class authunix_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wmemcmp
class wmemcmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gmtime_r
class gmtime_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fchmod
class fchmod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__printf_chk
class __printf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:obstack_vprintf
class obstack_vprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strspn_cg
class __strspn_cg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fgetws_chk
class __fgetws_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__register_atfork
class __register_atfork(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setgrent
class setgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:sigwait
class sigwait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswctype_l
class iswctype_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wctrans
class wctrans(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_vfprintf
class _IO_vfprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:acct
class acct(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:exit
class exit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:htonl
class htonl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:execl
class execl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:re_set_syntax
class re_set_syntax(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endprotoent
class endprotoent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wordexp
class wordexp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getprotobynumber_r
class getprotobynumber_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__assert
class __assert(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isinf
class isinf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clearerr_unlocked
class clearerr_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_keybuf
class xdr_keybuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fnmatch
class fnmatch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__islower_l
class __islower_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gnu_dev_major
class gnu_dev_major(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:htons
class htons(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_uint32_t
class xdr_uint32_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:readdir
class readdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:seed48_r
class seed48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigrelse
class sigrelse(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pathconf
class pathconf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__nss_hostname_digits_dots
class __nss_hostname_digits_dots(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:execv
class execv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sprintf
class sprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_putc
class _IO_putc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:nfsservctl
class nfsservctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:envz_merge
class envz_merge(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setlocale
class setlocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:strftime_l
class strftime_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:memfrob
class memfrob(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mbrtowc
class mbrtowc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getutid_r
class getutid_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:srand
class srand(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswcntrl_l
class iswcntrl_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_pthread_init
class __libc_pthread_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:iswblank
class iswblank(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tr_break
class tr_break(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__write
class __write(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__select
class __select(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:towlower
class towlower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vfwprintf_chk
class __vfwprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fgetws_unlocked
class fgetws_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:ttyname_r
class ttyname_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fopen
class fopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gai_strerror
class gai_strerror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsncpy
class wcsncpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetspent
class fgetspent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strsignal
class strsignal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strncmp
class strncmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnetbyname_r
class getnetbyname_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:svcfd_create
class svcfd_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getprotoent_r
class getprotoent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftruncate
class ftruncate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strncpy_gg
class __strncpy_gg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_unixcred
class xdr_unixcred(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:dcngettext
class dcngettext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_rmtcallres
class xdr_rmtcallres(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_puts
class _IO_puts(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet_nsap_addr
class inet_nsap_addr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet_aton
class inet_aton(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wordfree
class wordfree(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ttyslot
class ttyslot(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:posix_spawn_file_actions_addclose
class posix_spawn_file_actions_addclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_unsave_markers
class _IO_unsave_markers(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getdirentries
class getdirentries(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_default_uflow
class _IO_default_uflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcpcpy_chk
class __wcpcpy_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtold_internal
class __strtold_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcpy_small
class __strcpy_small(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:erand48
class erand48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstoul_l
class wcstoul_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:modify_ldt
class modify_ldt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_memalign
class __libc_memalign(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isfdtype
class isfdtype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcspn_c1
class __strcspn_c1(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getfsfile
class getfsfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcspn_c2
class __strcspn_c2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lcong48
class lcong48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpwent
class getpwent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__strcspn_c3
class __strcspn_c3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:re_match_2
class re_match_2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putgrent
class putgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:argz_stringify
class argz_stringify(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getservent_r
class getservent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:open_wmemstream
class open_wmemstream(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_opt_append
class inet6_opt_append(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strrchr
class strrchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setservent
class setservent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_openpt
class posix_openpt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcerr_systemerr
class svcerr_systemerr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fflush_unlocked
class fflush_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isgraph_l
class __isgraph_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_setschedpolicy
class posix_spawnattr_setschedpolicy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setbuffer
class setbuffer(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wait
class wait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vwprintf
class vwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_memalign
class posix_memalign(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getipv4sourcefilter
class getipv4sourcefilter(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcpy_g
class __strcpy_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vwprintf_chk
class __vwprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:tempnam
class tempnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isalpha
class isalpha(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtof_l
class strtof_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:regexec
class regexec(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:llseek
class llseek(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:revoke
class revoke(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:re_match
class re_match(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tdelete
class tdelete(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:readlinkat
class readlinkat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pipe
class pipe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__wctomb_chk
class __wctomb_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:get_avphys_pages
class get_avphys_pages(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:authunix_create_default
class authunix_create_default(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_ferror
class _IO_ferror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getrpcbynumber
class getrpcbynumber(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_count
class argz_count(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strdup
class __strdup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sysconf
class __sysconf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__readlink_chk
class __readlink_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setregid
class setregid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__res_ninit
class __res_ninit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tcdrain
class tcdrain(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setipv4sourcefilter
class setipv4sourcefilter(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:cfmakeraw
class cfmakeraw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstold
class wcstold(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sbrk
class __sbrk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_proc_open
class _IO_proc_open(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:shmat
class shmat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:perror
class perror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_str_pbackfail
class _IO_str_pbackfail(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rpmatch
class rpmatch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:statvfs64
class statvfs64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_sscanf
class __isoc99_sscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__getlogin_r_chk
class __getlogin_r_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fprintf
class _IO_fprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pvalloc
class pvalloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dcgettext
class dcgettext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:registerrpc
class registerrpc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wfile_overflow
class _IO_wfile_overflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstoll
class wcstoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_setpgroup
class posix_spawnattr_setpgroup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:qecvt_r
class qecvt_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_do_write
class _IO_do_write(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ecvt_r
class ecvt_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_switch_to_get_mode
class _IO_switch_to_get_mode(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcscat
class wcscat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getutxid
class getutxid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcrtomb
class wcrtomb(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__signbitf
class __signbitf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sync_file_range
class sync_file_range(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnetbyaddr
class getnetbyaddr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:connect
class connect(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wcspbrk
class wcspbrk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__open64_2
class __open64_2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isnan
class __isnan(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcspn_cg
class __strcspn_cg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:envz_remove
class envz_remove(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_longjmp
class _longjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ngettext
class ngettext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ldexpf
class ldexpf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fileno_unlocked
class fileno_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__signbitl
class __signbitl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lutimes
class lutimes(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dl_iterate_phdr
class dl_iterate_phdr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [FUNCPTR, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:key_get_conv
class key_get_conv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:munlock
class munlock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpwuid
class getpwuid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:stpncpy
class stpncpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftruncate64
class ftruncate64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sendfile
class sendfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mmap64
class mmap64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__nss_disable_nscd
class __nss_disable_nscd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getpwent_r
class getpwent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_rth_init
class inet6_rth_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_allocate_rtsig_private
class __libc_allocate_rtsig_private(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ldexpl
class ldexpl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:inet6_opt_next
class inet6_opt_next(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ecb_crypt
class ecb_crypt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ungetwc
class ungetwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:versionsort
class versionsort(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_longlong_t
class xdr_longlong_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstof_l
class __wcstof_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tfind
class tfind(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:_IO_printf
class _IO_printf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__argz_next
class __argz_next(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wmemcpy
class wmemcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_init
class posix_spawnattr_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__fxstatat64
class __fxstatat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sigismember
class __sigismember(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memcpy_by2
class __memcpy_by2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:get_current_dir_name
class get_current_dir_name(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:semctl
class semctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fputc_unlocked
class fputc_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:mbsrtowcs
class mbsrtowcs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__memcpy_by4
class __memcpy_by4(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:verr
class verr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getprotobynumber
class getprotobynumber(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:unlinkat
class unlinkat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isalnum_l
class isalnum_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getsecretkey
class getsecretkey(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_thread_freeres
class __libc_thread_freeres(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdr_authdes_verf
class xdr_authdes_verf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtof_internal
class __strtof_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:closedir
class closedir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:initgroups
class initgroups(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet_ntoa
class inet_ntoa(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstof_l
class wcstof_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__freelocale
class __freelocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:glob64
class glob64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fwprintf_chk
class __fwprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pmap_rmtcall
class pmap_rmtcall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putc
class putc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:nanosleep
class nanosleep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fchdir
class fchdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_char
class xdr_char(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setspent
class setspent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:fopencookie
class fopencookie(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isinf
class __isinf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__mempcpy_chk
class __mempcpy_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wdefault_pbackfail
class _IO_wdefault_pbackfail(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endaliasent
class endaliasent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:ftrylockfile
class ftrylockfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstoll_l
class wcstoll_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isalpha_l
class isalpha_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:feof_unlocked
class feof_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isblank
class isblank(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:re_search_2
class re_search_2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svc_sendreply
class svc_sendreply(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:uselocale
class uselocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getusershell
class getusershell(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:siginterrupt
class siginterrupt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getgrgid
class getgrgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:epoll_wait
class epoll_wait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:error
class error(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fputwc
class fputwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:mkfifoat
class mkfifoat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getrpcent_r
class getrpcent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:get_kernel_syms
class get_kernel_syms(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftell
class ftell(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_scanf
class __isoc99_scanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__read_chk
class __read_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet_ntop
class inet_ntop(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strncpy
class strncpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:signal
class signal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getdomainname
class getdomainname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fgetws_unlocked_chk
class __fgetws_unlocked_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__res_nclose
class __res_nclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:personality
class personality(emufunc.EmuFunc):
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


#EMUFUNC:__iswupper_l
class __iswupper_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vsprintf_chk
class __vsprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:mbstowcs
class mbstowcs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__newlocale
class __newlocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getpriority
class getpriority(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getsubopt
class getsubopt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tcgetsid
class tcgetsid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fork
class fork(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:putw
class putw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:warnx
class warnx(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ioperm
class ioperm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_setvbuf
class _IO_setvbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pmap_unset
class pmap_unset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_dl_mcount_wrapper_check
class _dl_mcount_wrapper_check(emufunc.EmuFunc):
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


#EMUFUNC:isastream
class isastream(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vwscanf
class vwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigprocmask
class sigprocmask(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_sputbackc
class _IO_sputbackc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fputws
class fputws(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:strtoul_l
class strtoul_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:listxattr
class listxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strchr_c
class __strchr_c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lcong48_r
class lcong48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:regfree
class regfree(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet_netof
class inet_netof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sched_getparam
class sched_getparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gettext
class gettext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:waitid
class waitid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigfillset
class sigfillset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_init_wmarker
class _IO_init_wmarker(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:futimes
class futimes(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:callrpc
class callrpc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strchr_g
class __strchr_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gtty
class gtty(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:time
class time(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__libc_malloc
class __libc_malloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getgrent
class getgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:ntp_adjtime
class ntp_adjtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:setreuid
class setreuid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigorset
class sigorset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_flush_all
class _IO_flush_all(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:readdir_r
class readdir_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:drand48_r
class drand48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:memalign
class memalign(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vfscanf
class vfscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fsetpos64
class fsetpos64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endnetent
class endnetent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:hsearch_r
class hsearch_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcscasecmp
class wcscasecmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:daemon
class daemon(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_feof
class _IO_feof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:key_setsecret
class key_setsecret(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__lxstat
class __lxstat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:svc_run
class svc_run(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_wdefault_finish
class _IO_wdefault_finish(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:shmctl
class shmctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstoul_l
class __wcstoul_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inotify_rm_watch
class inotify_rm_watch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_quad_t
class xdr_quad_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fflush
class _IO_fflush(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__mbrtowc
class __mbrtowc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:unlink
class unlink(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putchar
class putchar(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdrmem_create
class xdrmem_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_mutex_lock
class pthread_mutex_lock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgets_unlocked
class fgets_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putspent
class putspent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:listen
class listen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdr_int32_t
class xdr_int32_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:msgrcv
class msgrcv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__ivaliduser
class __ivaliduser(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getrpcent
class getrpcent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:select
class select(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__send
class __send(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:iswprint
class iswprint(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mkdir
class mkdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswalnum_l
class __iswalnum_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ispunct_l
class ispunct_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_fatal
class __libc_fatal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sched_cpualloc
class __sched_cpualloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:shmdt
class shmdt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:realloc
class realloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__pwrite64
class __pwrite64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setstate
class setstate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fstatfs
class fstatfs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:if_nameindex
class if_nameindex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:btowc
class btowc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__argz_stringify
class __argz_stringify(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_ungetc
class _IO_ungetc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memset_cc
class __memset_cc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rewinddir
class rewinddir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_adjust_wcolumn
class _IO_adjust_wcolumn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtold
class strtold(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswalpha_l
class __iswalpha_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_key_netstres
class xdr_key_netstres(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getaliasent_r
class getaliasent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fsync
class fsync(emufunc.EmuFunc):
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


#EMUFUNC:__memset_cg
class __memset_cg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putmsg
class putmsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_replymsg
class xdr_replymsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:sockatmark
class sockatmark(emufunc.EmuFunc):
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


#EMUFUNC:abort
class abort(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdr_u_short
class xdr_u_short(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_flush_all_linebuffered
class _IO_flush_all_linebuffered(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:strtoll
class strtoll(emufunc.EmuFunc):
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


#EMUFUNC:wcstoumax
class wcstoumax(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svc_getreq_common
class svc_getreq_common(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vsprintf
class vsprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigwaitinfo
class sigwaitinfo(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:moncontrol
class moncontrol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:socketpair
class socketpair(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__res_iclose
class __res_iclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:div
class div(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:memchr
class memchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtod_l
class __strtod_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strpbrk
class strpbrk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ether_aton
class ether_aton(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:memrchr
class memrchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__read
class __read(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:hdestroy
class hdestroy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__register_frame_info_table
class __register_frame_info_table(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:cfree
class cfree(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_tolower
class _tolower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ruserok_af
class ruserok_af(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:step
class step(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__dcgettext
class __dcgettext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:towctrans
class towctrans(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lsetxattr
class lsetxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setttyent
class setttyent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__isoc99_swscanf
class __isoc99_swscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__open64
class __open64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__bsd_getpgrp
class __bsd_getpgrp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpid
class getpid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getcontext
class getcontext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:kill
class kill(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strspn
class strspn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_condattr_init
class pthread_condattr_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_vfwscanf
class __isoc99_vfwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:imaxdiv
class imaxdiv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_fallocate64
class posix_fallocate64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcraw_create
class svcraw_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__sched_get_priority_max
class __sched_get_priority_max(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_extract
class argz_extract(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:bind_textdomain_codeset
class bind_textdomain_codeset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetpos
class fgetpos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fgetpos64
class _IO_fgetpos64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strdup
class strdup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:creat64
class creat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getc_unlocked
class getc_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svc_exit
class svc_exit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:strftime
class strftime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet_pton
class inet_pton(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__strncat_g
class __strncat_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__flbf
class __flbf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lockf64
class lockf64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_switch_to_main_wget_area
class _IO_switch_to_main_wget_area(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xencrypt
class xencrypt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putpmsg
class putpmsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_system
class __libc_system(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_uint16_t
class xdr_uint16_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_mallopt
class __libc_mallopt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sysv_signal
class sysv_signal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtoll_l
class strtoll_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sched_cpufree
class __sched_cpufree(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_getschedparam
class pthread_attr_getschedparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__dup2
class __dup2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_mutex_destroy
class pthread_mutex_destroy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetwc
class fgetwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:vlimit
class vlimit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:chmod
class chmod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sbrk
class sbrk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__assert_fail
class __assert_fail(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clntunix_create
class clntunix_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strrchr_c
class __strrchr_c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__toascii_l
class __toascii_l(emufunc.EmuFunc):
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


#EMUFUNC:finite
class finite(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ether_ntoa_r
class ether_ntoa_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__getmntent_r
class __getmntent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:printf
class printf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isalnum_l
class __isalnum_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__connect
class __connect(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getnetbyname
class getnetbyname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mkstemp
class mkstemp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__strrchr_g
class __strrchr_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:statvfs
class statvfs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:flock
class flock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:error_at_line
class error_at_line(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rewind
class rewind(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:llabs
class llabs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strcoll_l
class strcoll_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:localtime_r
class localtime_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wcscspn
class wcscspn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vtimes
class vtimes(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:copysign
class copysign(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__stpncpy
class __stpncpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_opt_finish
class inet6_opt_finish(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__nanosleep
class __nanosleep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:modff
class modff(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswlower
class iswlower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtod
class strtod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setjmp
class setjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__poll
class __poll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isspace
class isspace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tmpnam_r
class tmpnam_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__wctype_l
class __wctype_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetws
class fgetws(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:setutxent
class setutxent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__isalpha_l
class __isalpha_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtof
class strtof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstoll_l
class __wcstoll_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswdigit_l
class iswdigit_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_msgsnd
class __libc_msgsnd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gmtime
class gmtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__uselocale
class __uselocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ffs
class ffs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdr_opaque_auth
class xdr_opaque_auth(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__ctype_get_mb_cur_max
class __ctype_get_mb_cur_max(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__iswlower_l
class __iswlower_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:modfl
class modfl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:envz_add
class envz_add(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:strtok
class strtok(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpt
class getpt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:sigqueue
class sigqueue(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtol
class strtol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endpwent
class endpwent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_fopen
class _IO_fopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strstr_cg
class __strstr_cg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isatty
class isatty(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fts_close
class fts_close(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lchown
class lchown(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setmntent
class setmntent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:mmap
class mmap(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endnetgrent
class endnetgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_file_read
class _IO_file_read(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setsourcefilter
class setsourcefilter(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__register_frame
class __register_frame(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpw
class getpw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetspent_r
class fgetspent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:sched_yield
class sched_yield(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:strtoq
class strtoq(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:glob_pattern_p
class glob_pattern_p(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strsep_1c
class __strsep_1c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsncasecmp
class wcsncasecmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getgrnam_r
class getgrnam_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:ctime_r
class ctime_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:xdr_u_quad_t
class xdr_u_quad_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clearenv
class clearenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wctype_l
class wctype_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fstatvfs
class fstatvfs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigblock
class sigblock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_sa_len
class __libc_sa_len(emufunc.EmuFunc):
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


#EMUFUNC:svcudp_create
class svcudp_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswxdigit_l
class iswxdigit_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_setscope
class pthread_attr_setscope(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strchrnul
class strchrnul(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:swapoff
class swapoff(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:syslog
class syslog(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtoul_l
class __strtoul_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_destroy
class posix_spawnattr_destroy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__fread_unlocked_chk
class __fread_unlocked_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fsetpos
class fsetpos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pread64
class pread64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:eaccess
class eaccess(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_option_alloc
class inet6_option_alloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dysize
class dysize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:symlink
class symlink(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wdefault_uflow
class _IO_wdefault_uflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getspent
class getspent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:pthread_attr_setdetachstate
class pthread_attr_setdetachstate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetxattr
class fgetxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:srandom_r
class srandom_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:truncate
class truncate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_calloc
class __libc_calloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isprint
class isprint(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_fadvise
class posix_fadvise(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:memccpy
class memccpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:execle
class execle(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getloadavg
class getloadavg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsftime
class wcsftime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:cfsetispeed
class cfsetispeed(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__nss_configure_lookup
class __nss_configure_lookup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ldiv
class ldiv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_void
class xdr_void(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:ether_ntoa
class ether_ntoa(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:parse_printf_format
class parse_printf_format(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetc
class fgetc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tee
class tee(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_key_netstarg
class xdr_key_netstarg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strfry
class strfry(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_vsprintf
class _IO_vsprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:reboot
class reboot(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getaliasbyname_r
class getaliasbyname_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:jrand48
class jrand48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gethostbyname_r
class gethostbyname_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:execlp
class execlp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:swab
class swab(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_funlockfile
class _IO_funlockfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_flockfile
class _IO_flockfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strsep_2c
class __strsep_2c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:seekdir
class seekdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isblank_l
class isblank_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isascii_l
class __isascii_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:alphasort64
class alphasort64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pmap_getport
class pmap_getport(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:makecontext
class makecontext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fdatasync
class fdatasync(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:authdes_getucred
class authdes_getucred(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:truncate64
class truncate64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswgraph_l
class __iswgraph_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__ispunct_l
class __ispunct_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtoumax
class strtoumax(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argp_failure
class argp_failure(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcasecmp
class __strcasecmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vfscanf
class __vfscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgets
class fgets(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__openat64_2
class __openat64_2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswctype
class __iswctype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnetent_r
class getnetent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_setflags
class posix_spawnattr_setflags(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sched_setaffinity
class sched_setaffinity(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vscanf
class vscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpwnam
class getpwnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:inet6_option_append
class inet6_option_append(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:calloc
class calloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtouq_internal
class __strtouq_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getppid
class getppid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getmsg
class getmsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_unsave_wmarkers
class _IO_unsave_wmarkers(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_dl_addr
class _dl_addr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:msync
class msync(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_init
class _IO_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__signbit
class __signbit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:futimens
class futimens(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:renameat
class renameat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:asctime_r
class asctime_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:freelocale
class freelocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strlen
class strlen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:initstate
class initstate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ungetc
class ungetc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcschr
class wcschr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isxdigit
class isxdigit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ether_line
class ether_line(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_init
class _IO_file_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__wuflow
class __wuflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:lockf
class lockf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_authdes_cred
class xdr_authdes_cred(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:iswctype
class iswctype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:qecvt
class qecvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memset_gg
class __memset_gg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tmpfile
class tmpfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__internal_setnetgrent
class __internal_setnetgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__mbrlen
class __mbrlen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:xdr_int8_t
class xdr_int8_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__towupper_l
class __towupper_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sprofil
class sprofil(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pivot_root
class pivot_root(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:envz_entry
class envz_entry(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xprt_unregister
class xprt_unregister(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:newlocale
class newlocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:rexec_af
class rexec_af(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tsearch
class tsearch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:getaliasbyname
class getaliasbyname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcerr_progvers
class svcerr_progvers(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isspace_l
class isspace_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_insert
class argz_insert(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__memcpy_c
class __memcpy_c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gsignal
class gsignal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_opt_get_val
class inet6_opt_get_val(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gethostbyname2_r
class gethostbyname2_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__cxa_atexit
class __cxa_atexit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawn_file_actions_init
class posix_spawn_file_actions_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:malloc_stats
class malloc_stats(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:prctl
class prctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fwriting
class __fwriting(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setlogmask
class setlogmask(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strsep_3c
class __strsep_3c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__towctrans_l
class __towctrans_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_enum
class xdr_enum(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fread_unlocked
class fread_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memcpy_g
class __memcpy_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:unshare
class unshare(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:brk
class brk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:send
class send(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:isprint_l
class isprint_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setitimer
class setitimer(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__towctrans
class __towctrans(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_vsscanf
class __isoc99_vsscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setcontext
class setcontext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:signalfd
class signalfd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_option_next
class inet6_option_next(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigemptyset
class sigemptyset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswupper_l
class iswupper_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_dl_sym
class _dl_sym(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:openlog
class openlog(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getaddrinfo
class getaddrinfo(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_init_marker
class _IO_init_marker(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getchar_unlocked
class getchar_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__res_maybe_init
class __res_maybe_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dirname
class dirname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__gconv_get_alias_db
class __gconv_get_alias_db(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:memset
class memset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:localeconv
class localeconv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:cfgetospeed
class cfgetospeed(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memset_ccn_by2
class __memset_ccn_by2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:writev
class writev(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_default_xsgetn
class _IO_default_xsgetn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isalnum
class isalnum(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memset_ccn_by4
class __memset_ccn_by4(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setutent
class setutent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_seterr_reply
class _seterr_reply(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_switch_to_wget_mode
class _IO_switch_to_wget_mode(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_rth_add
class inet6_rth_add(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetc_unlocked
class fgetc_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:swprintf
class swprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getchar
class getchar(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getutid
class getutid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__gconv_get_cache
class __gconv_get_cache(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:glob
class glob(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:strstr
class strstr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:semtimedop
class semtimedop(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__secure_getenv
class __secure_getenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsnlen
class wcsnlen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstof_internal
class __wcstof_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strcspn
class strcspn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tcsendbreak
class tcsendbreak(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:telldir
class telldir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:islower
class islower(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:utimensat
class utimensat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fcvt
class fcvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtof_l
class __strtof_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rmdir
class rmdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_setbuffer
class _IO_setbuffer(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_iter_file
class _IO_iter_file(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:bind
class bind(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__strtoll_l
class __strtoll_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tcsetattr
class tcsetattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fseek
class fseek(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_float
class xdr_float(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:confstr
class confstr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:chdir
class chdir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:open64
class open64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_rth_segments
class inet6_rth_segments(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:read
class read(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:muntrace
class muntrace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getwchar
class getwchar(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:memcmp
class memcmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnameinfo
class getnameinfo(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpagesize
class getpagesize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdr_sizeof
class xdr_sizeof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [FUNCPTR, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__moddi3
class __moddi3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dgettext
class dgettext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__strlen_g
class __strlen_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_ftell
class _IO_ftell(emufunc.EmuFunc):
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


#EMUFUNC:getrpcport
class getrpcport(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_list_lock
class _IO_list_lock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_sprintf
class _IO_sprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__pread_chk
class __pread_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mlock
class mlock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endgrent
class endgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:strndup
class strndup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:init_module
class init_module(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__syslog_chk
class __syslog_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:asctime
class asctime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clnt_sperrno
class clnt_sperrno(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdrrec_skiprecord
class xdrrec_skiprecord(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mbsnrtowcs
class mbsnrtowcs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__strcoll_l
class __strcoll_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__gai_sigqueue
class __gai_sigqueue(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:toupper
class toupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setprotoent
class setprotoent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__getpid
class __getpid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:mbtowc
class mbtowc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:eventfd
class eventfd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__register_frame_info_table_bases
class __register_frame_info_table_bases(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:netname2user
class netname2user(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_toupper
class _toupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getsockopt
class getsockopt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:svctcp_create
class svctcp_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wsetb
class _IO_wsetb(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getdelim
class getdelim(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setgroups
class setgroups(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clnt_perrno
class clnt_perrno(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setxattr
class setxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_Unwind_Find_FDE
class _Unwind_Find_FDE(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:erand48_r
class erand48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:lrand48
class lrand48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_doallocbuf
class _IO_doallocbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ttyname
class ttyname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:grantpt
class grantpt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_init
class pthread_attr_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mempcpy
class mempcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:herror
class herror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getopt
class getopt(emufunc.EmuFunc):
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


#EMUFUNC:__fgets_unlocked_chk
class __fgets_unlocked_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:utmpname
class utmpname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getlogin_r
class getlogin_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isdigit_l
class isdigit_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vfwprintf
class vfwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__setmntent
class __setmntent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_seekoff
class _IO_seekoff(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tcflow
class tcflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:hcreate_r
class hcreate_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstouq
class wcstouq(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wdoallocbuf
class _IO_wdoallocbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rexec
class rexec(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:msgget
class msgget(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fwscanf
class fwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_int16_t
class xdr_int16_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__getcwd_chk
class __getcwd_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fchmodat
class fchmodat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:envz_strip
class envz_strip(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dup2
class dup2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clearerr
class clearerr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rcmd_af
class rcmd_af(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__rpc_thread_svc_max_pollfd
class __rpc_thread_svc_max_pollfd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:unsetenv
class unsetenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:rand_r
class rand_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:atexit
class atexit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_str_init_static
class _IO_str_init_static(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__finite
class __finite(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:timelocal
class timelocal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:argz_add_sep
class argz_add_sep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_pointer
class xdr_pointer(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:wctob
class wctob(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:longjmp
class longjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fxstat64
class __fxstat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:strptime
class strptime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_xsputn
class _IO_file_xsputn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clnt_sperror
class clnt_sperror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vprintf_chk
class __vprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__adjtimex
class __adjtimex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:shutdown
class shutdown(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:fattach
class fattach(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_setjmp
class _setjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:vsnprintf
class vsnprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:poll
class poll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:malloc_get_state
class malloc_get_state(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getpmsg
class getpmsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_getline
class _IO_getline(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ptsname
class ptsname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fexecve
class fexecve(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:re_comp
class re_comp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:clnt_perror
class clnt_perror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:qgcvt
class qgcvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:svcerr_noproc
class svcerr_noproc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstol_internal
class __wcstol_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_marker_difference
class _IO_marker_difference(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fprintf_chk
class __fprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strncasecmp_l
class __strncasecmp_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigaddset
class sigaddset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_sscanf
class _IO_sscanf(emufunc.EmuFunc):
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


#EMUFUNC:__frame_state_for
class __frame_state_for(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswupper
class iswupper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcerr_noprog
class svcerr_noprog(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_iter_end
class _IO_iter_end(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getgrnam
class getgrnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:adjtimex
class adjtimex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:pthread_mutex_unlock
class pthread_mutex_unlock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sethostname
class sethostname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_setb
class _IO_setb(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__pread64
class __pread64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mcheck
class mcheck(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isblank_l
class __isblank_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_reference
class xdr_reference(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:getpwuid_r
class getpwuid_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:endrpcent
class endrpcent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:netname2host
class netname2host(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet_network
class inet_network(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putenv
class putenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wcswidth
class wcswidth(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isctype
class isctype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pmap_set
class pmap_set(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_cond_broadcast
class pthread_cond_broadcast(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fchown
class fchown(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:catopen
class catopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstoull_l
class __wcstoull_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_netobj
class xdr_netobj(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftok
class ftok(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_link_in
class _IO_link_in(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:register_printf_function
class register_printf_function(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sigsetjmp
class __sigsetjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_wscanf
class __isoc99_wscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__ffs
class __ffs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getttyent
class getttyent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:inet_makeaddr
class inet_makeaddr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gethostbyaddr
class gethostbyaddr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_popen
class _IO_popen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:get_phys_pages
class get_phys_pages(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:argp_help
class argp_help(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fputc
class fputc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:gethostent_r
class gethostent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_seekmark
class _IO_seekmark(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__towlower_l
class __towlower_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:frexp
class frexp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:psignal
class psignal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:verrx
class verrx(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:setlogin
class setlogin(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__internal_getnetgrent_r
class __internal_getnetgrent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fseeko64
class fseeko64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:versionsort64
class versionsort64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fremovexattr
class fremovexattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_valloc
class __libc_valloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_fscanf
class __isoc99_fscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_sungetc
class _IO_sungetc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:recv
class recv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_rpc_dtablesize
class _rpc_dtablesize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:create_module
class create_module(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getsid
class getsid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mktemp
class mktemp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:inet_addr
class inet_addr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getrusage
class getrusage(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_peekc_locked
class _IO_peekc_locked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_remove_marker
class _IO_remove_marker(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isspace_l
class __isspace_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fts_read
class fts_read(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswlower_l
class iswlower_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswgraph
class iswgraph(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getfsspec
class getfsspec(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtoll_internal
class __strtoll_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ualarm
class ualarm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fputs
class fputs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:query_module
class query_module(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawn_file_actions_destroy
class posix_spawn_file_actions_destroy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtok_r
class strtok_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endhostent
class endhostent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__isprint_l
class __isprint_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_cond_wait
class pthread_cond_wait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_delete
class argz_delete(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__woverflow
class __woverflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_u_long
class xdr_u_long(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fpathconf
class fpathconf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iscntrl_l
class iscntrl_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:regerror
class regerror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strnlen
class strnlen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:nrand48
class nrand48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getspent_r
class getspent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wmempcpy
class wmempcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lseek
class lseek(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setresgid
class setresgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigaltstack
class sigaltstack(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strncmp_g
class __strncmp_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_string
class xdr_string(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftime
class ftime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:memcpy
class memcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getwc
class getwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:mbrlen
class mbrlen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:endusershell
class endusershell(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getwd
class getwd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sched_get_priority_min
class __sched_get_priority_min(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:freopen64
class freopen64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fclose
class fclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getdate_r
class getdate_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_setschedparam
class posix_spawnattr_setschedparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_seekwmark
class _IO_seekwmark(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_adjust_column
class _IO_adjust_column(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:euidaccess
class euidaccess(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sigpause
class __sigpause(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:symlinkat
class symlinkat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:rand
class rand(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:pselect
class pselect(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:pthread_setcanceltype
class pthread_setcanceltype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tcsetpgrp
class tcsetpgrp(emufunc.EmuFunc):
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


#EMUFUNC:__memmove_chk
class __memmove_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:nftw64
class nftw64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mprotect
class mprotect(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__getwd_chk
class __getwd_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcat_c
class __strcat_c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__nss_lookup_function
class __nss_lookup_function(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:ffsl
class ffsl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getmntent
class getmntent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_dl_error_tsd
class __libc_dl_error_tsd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__wcscasecmp_l
class __wcscasecmp_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtol_internal
class __strtol_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vsnprintf_chk
class __vsnprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__strcat_g
class __strcat_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mkostemp64
class mkostemp64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcsftime_l
class __wcsftime_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_doallocate
class _IO_file_doallocate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtoul
class strtoul(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fmemopen
class fmemopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_setschedparam
class pthread_setschedparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:hdestroy_r
class hdestroy_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endspent
class endspent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:munlockall
class munlockall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:sigpause
class sigpause(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_u_int
class xdr_u_int(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:vprintf
class vprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getutmpx
class getutmpx(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getutmp
class getutmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:setsockopt
class setsockopt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:malloc
class malloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_default_xsputn
class _IO_default_xsputn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:eventfd_read
class eventfd_read(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:remap_file_pages
class remap_file_pages(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:siglongjmp
class siglongjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpass
class getpass(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtouq
class strtouq(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_keystatus
class xdr_keystatus(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:uselib
class uselib(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigisemptyset
class sigisemptyset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strspn_g
class __strspn_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:killpg
class killpg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strfmon
class strfmon(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:duplocale
class duplocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strcat
class strcat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_int
class xdr_int(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:umask
class umask(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strcasecmp
class strcasecmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_vswscanf
class __isoc99_vswscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fdopendir
class fdopendir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftello64
class ftello64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_getschedpolicy
class pthread_attr_getschedpolicy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:realpath
class realpath(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:timegm
class timegm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftello
class ftello(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:modf
class modf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__libc_dlclose
class __libc_dlclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_mallinfo
class __libc_mallinfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:raise
class Raise(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setegid
class setegid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:malloc_usable_size
class malloc_usable_size(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isdigit_l
class __isdigit_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setfsgid
class setfsgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wdefault_doallocate
class _IO_wdefault_doallocate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_vfscanf
class _IO_vfscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:remove
class remove(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sched_setscheduler
class sched_setscheduler(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstold_l
class wcstold_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setpgid
class setpgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__openat_2
class __openat_2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpeername
class getpeername(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wcscasecmp_l
class wcscasecmp_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memset_gcn_by2
class __memset_gcn_by2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fgets_chk
class __fgets_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strverscmp
class __strverscmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__res_state
class __res_state(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:pmap_getmaps
class pmap_getmaps(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:frexpf
class frexpf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strndup
class __strndup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memset_gcn_by4
class __memset_gcn_by4(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_flushlbf
class _flushlbf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:mbsinit
class mbsinit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:towupper_l
class towupper_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strncpy_chk
class __strncpy_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getgid
class getgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__register_frame_table
class __register_frame_table(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:re_compile_pattern
class re_compile_pattern(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:asprintf
class asprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tzset
class tzset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__libc_pwrite
class __libc_pwrite(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__lxstat64
class __lxstat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:frexpl
class frexpl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdrrec_eof
class xdrrec_eof(emufunc.EmuFunc):
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


#EMUFUNC:vsyslog
class vsyslog(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__umoddi3
class __umoddi3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcudp_bufcreate
class svcudp_bufcreate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strerror_r
class __strerror_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:finitef
class finitef(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fstatfs64
class fstatfs64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getutline
class getutline(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__nss_services_lookup
class __nss_services_lookup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__uflow
class __uflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__mempcpy
class __mempcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtol_l
class strtol_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isnanf
class __isnanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__nl_langinfo_l
class __nl_langinfo_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svc_getreq_poll
class svc_getreq_poll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:finitel
class finitel(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sched_cpucount
class __sched_cpucount(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_setinheritsched
class pthread_attr_setinheritsched(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vsnprintf
class __vsnprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:nl_langinfo
class nl_langinfo(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setfsent
class setfsent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:hasmntopt
class hasmntopt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__isnanl
class __isnanl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_current_sigrtmax
class __libc_current_sigrtmax(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:opendir
class opendir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnetbyaddr_r
class getnetbyaddr_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wcsncat
class wcsncat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:scalbln
class scalbln(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:gethostent
class gethostent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_fgets
class _IO_fgets(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:bzero
class bzero(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clnt_broadcast
class clnt_broadcast(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, FUNCPTR, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:__sigaddset
class __sigaddset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isinff
class __isinff(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mcheck_check_all
class mcheck_check_all(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getspnam
class getspnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_condattr_destroy
class pthread_condattr_destroy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__statfs
class __statfs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__xstat64
class __xstat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fgetgrent_r
class fgetgrent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:inet6_option_space
class inet6_option_space(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clone
class clone(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswpunct_l
class __iswpunct_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getenv
class getenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__ctype_b_loc
class __ctype_b_loc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__isinfl
class __isinfl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sched_getaffinity
class sched_getaffinity(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__xpg_sigpause
class __xpg_sigpause(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:profil
class profil(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sscanf
class sscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__deregister_frame_info
class __deregister_frame_info(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__open_2
class __open_2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setresuid
class setresuid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:jrand48_r
class jrand48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:recvfrom
class recvfrom(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__mempcpy_by2
class __mempcpy_by2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__profile_frequency
class __profile_frequency(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wcsnrtombs
class wcsnrtombs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__mempcpy_by4
class __mempcpy_by4(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ruserok
class ruserok(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_obstack_allocated_p
class _obstack_allocated_p(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fts_set
class fts_set(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_u_longlong_t
class xdr_u_longlong_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:nice
class nice(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:regcomp
class regcomp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdecrypt
class xdecrypt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__open
class __open(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getitimer
class getitimer(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isgraph
class isgraph(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:catclose
class catclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clntudp_bufcreate
class clntudp_bufcreate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getservbyname
class getservbyname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__freading
class __freading(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcwidth
class wcwidth(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:msgctl
class msgctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet_lnaof
class inet_lnaof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigdelset
class sigdelset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gnu_get_libc_release
class gnu_get_libc_release(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:ioctl
class ioctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fchownat
class fchownat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:alarm
class alarm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_sputbackwc
class _IO_sputbackwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_pvalloc
class __libc_pvalloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:system
class system(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_getcredres
class xdr_getcredres(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__wcstol_l
class __wcstol_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vfwscanf
class vfwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inotify_init
class inotify_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:chflags
class chflags(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:err
class err(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getservbyname_r
class getservbyname_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:xdr_bool
class xdr_bool(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:ffsll
class ffsll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isctype
class __isctype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setrlimit64
class setrlimit64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:group_member
class group_member(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sched_getcpu
class sched_getcpu(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_fgetpos
class _IO_fgetpos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_free_backup_area
class _IO_free_backup_area(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:munmap
class munmap(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_setsigdefault
class posix_spawnattr_setsigdefault(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_obstack_begin_1
class _obstack_begin_1(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, FUNCPTR, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_nss_files_parse_pwent
class _nss_files_parse_pwent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wait3
class wait3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wait4
class wait4(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_obstack_newchunk
class _obstack_newchunk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__stpcpy_g
class __stpcpy_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:advance
class advance(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_opt_init
class inet6_opt_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__register_frame_info
class __register_frame_info(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gethostbyname
class gethostbyname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__lseek
class __lseek(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawn_file_actions_adddup2
class posix_spawn_file_actions_adddup2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstol_l
class wcstol_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iscntrl_l
class __iscntrl_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mkdirat
class mkdirat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:seteuid
class seteuid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcscpy
class wcscpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mrand48_r
class mrand48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:setfsuid
class setfsuid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dup
class dup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memset_chk
class __memset_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_exit
class pthread_exit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_u_char
class xdr_u_char(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getwchar_unlocked
class getwchar_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:pututxline
class pututxline(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:msgsnd
class msgsnd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getlogin
class getlogin(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:fchflags
class fchflags(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigandset
class sigandset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:scalbnf
class scalbnf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:sched_rr_get_interval
class sched_rr_get_interval(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_finish
class _IO_file_finish(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__sysctl
class __sysctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_double
class xdr_double(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getgroups
class getgroups(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:scalbnl
class scalbnl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:readv
class readv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getuid
class getuid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:rcmd
class rcmd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:readlink
class readlink(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lsearch
class lsearch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:iruserok_af
class iruserok_af(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fscanf
class fscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ether_aton_r
class ether_aton_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__printf_fp
class __printf_fp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mremap
class mremap(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:readahead
class readahead(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:host2netname
class host2netname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:removexattr
class removexattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_switch_to_wbackup_area
class _IO_switch_to_wbackup_area(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_pmap
class xdr_pmap(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__mempcpy_byn
class __mempcpy_byn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getprotoent
class getprotoent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_wfile_sync
class _IO_wfile_sync(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_opaque
class xdr_opaque(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getegid
class getegid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:setrlimit
class setrlimit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getopt_long
class getopt_long(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_open
class _IO_file_open(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:settimeofday
class settimeofday(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:open_memstream
class open_memstream(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:sstk
class sstk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_dl_vsym
class _dl_vsym(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fpurge
class __fpurge(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:utmpxname
class utmpxname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getpgid
class getpgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_current_sigrtmax_private
class __libc_current_sigrtmax_private(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:strtold_l
class strtold_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strncat_chk
class __strncat_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_madvise
class posix_madvise(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_getpgroup
class posix_spawnattr_getpgroup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vwarnx
class vwarnx(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__mempcpy_small
class __mempcpy_small(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetpos64
class fgetpos64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:index
class index(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_getdetachstate
class pthread_attr_getdetachstate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wfile_xsputn
class _IO_wfile_xsputn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:execvp
class execvp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mincore
class mincore(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mallinfo
class mallinfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:malloc_trim
class malloc_trim(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_str_underflow
class _IO_str_underflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:freeifaddrs
class freeifaddrs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcudp_enablecache
class svcudp_enablecache(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__duplocale
class __duplocale(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcsncasecmp_l
class __wcsncasecmp_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:linkat
class linkat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_default_pbackfail
class _IO_default_pbackfail(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_rth_space
class inet6_rth_space(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_free_wbackup_area
class _IO_free_wbackup_area(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_cond_timedwait
class pthread_cond_timedwait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpwnam_r
class getpwnam_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fsetpos
class _IO_fsetpos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:freopen
class freopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:backtrace_symbols_fd
class backtrace_symbols_fd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strncasecmp
class strncasecmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__xmknod
class __xmknod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wfile_seekoff
class _IO_wfile_seekoff(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ptrace
class ptrace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_rth_reverse
class inet6_rth_reverse(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:remque
class remque(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getifaddrs
class getifaddrs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:towlower_l
class towlower_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putwc_unlocked
class putwc_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:printf_size_info
class printf_size_info(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:scalbn
class scalbn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__wcstold_l
class __wcstold_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:if_nametoindex
class if_nametoindex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:scalblnf
class scalblnf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__wcstoll_internal
class __wcstoll_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:creat
class creat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fxstat
class __fxstat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_close_it
class _IO_file_close_it(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:scalblnl
class scalblnl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_file_close
class _IO_file_close(emufunc.EmuFunc):
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


#EMUFUNC:key_decryptsession_pk
class key_decryptsession_pk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sendfile64
class sendfile64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sendmsg
class sendmsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__backtrace_symbols_fd
class __backtrace_symbols_fd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstoimax
class wcstoimax(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtoull
class strtoull(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strsep_g
class __strsep_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wunderflow
class __wunderflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__udivdi3
class __udivdi3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fclose
class _IO_fclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fwritable
class __fwritable(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sysv_signal
class __sysv_signal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ulimit
class ulimit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:obstack_printf
class obstack_printf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wfile_underflow
class _IO_wfile_underflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fputwc_unlocked
class fputwc_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_getsigmask
class posix_spawnattr_getsigmask(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__nss_passwd_lookup
class __nss_passwd_lookup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:drand48
class drand48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdr_free
class xdr_free(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [FUNCPTR, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fileno
class fileno(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pclose
class pclose(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__bzero
class __bzero(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sethostent
class sethostent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isxdigit_l
class __isxdigit_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_rth_getaddr
class inet6_rth_getaddr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:re_search
class re_search(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__setpgid
class __setpgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gethostname
class gethostname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__dgettext
class __dgettext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:pthread_equal
class pthread_equal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sgetspent_r
class sgetspent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fstatvfs64
class fstatvfs64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:usleep
class usleep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_mutex_init
class pthread_mutex_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__clone
class __clone(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:utimes
class utimes(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigset
class sigset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__cmsg_nxthdr
class __cmsg_nxthdr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_obstack_memory_used
class _obstack_memory_used(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ustat
class ustat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:chown
class chown(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_realloc
class __libc_realloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:splice
class splice(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawn
class posix_spawn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswblank_l
class __iswblank_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_sungetwc
class _IO_sungetwc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getcwd
class getcwd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_vector
class xdr_vector(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:__getdelim
class __getdelim(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:eventfd_write
class eventfd_write(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:swapcontext
class swapcontext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__rpc_thread_svc_fdset
class __rpc_thread_svc_fdset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:lgetxattr
class lgetxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_uint8_t
class xdr_uint8_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__finitef
class __finitef(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsxfrm_l
class wcsxfrm_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:authdes_pk_create
class authdes_pk_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:if_indextoname
class if_indextoname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:vmsplice
class vmsplice(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:swscanf
class swscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcerr_decode
class svcerr_decode(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fwrite
class fwrite(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:updwtmpx
class updwtmpx(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gnu_get_libc_version
class gnu_get_libc_version(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__finitel
class __finitel(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:des_setparity
class des_setparity(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:copysignf
class copysignf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__cyg_profile_func_enter
class __cyg_profile_func_enter(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:fread
class fread(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getsourcefilter
class getsourcefilter(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isnanf
class isnanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:qfcvt_r
class qfcvt_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lrand48_r
class lrand48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fcvt_r
class fcvt_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gettimeofday
class gettimeofday(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:iswalnum_l
class iswalnum_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iconv_close
class iconv_close(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:adjtime
class adjtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnetgrent_r
class getnetgrent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigaction
class sigaction(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wmarker_delta
class _IO_wmarker_delta(emufunc.EmuFunc):
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


#EMUFUNC:copysignl
class copysignl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:seed48
class seed48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endttyent
class endttyent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:isnanl
class isnanl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_default_finish
class _IO_default_finish(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:rtime
class rtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getfsent
class getfsent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__isoc99_vwscanf
class __isoc99_vwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:epoll_ctl
class epoll_ctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswxdigit_l
class __iswxdigit_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fputs
class _IO_fputs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:madvise
class madvise(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_nss_files_parse_grent
class _nss_files_parse_grent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnetname
class getnetname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:passwd2des
class passwd2des(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_dl_mcount_wrapper
class _dl_mcount_wrapper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sigdelset
class __sigdelset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:scandir
class scandir(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, FUNCPTR, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:__stpcpy_small
class __stpcpy_small(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setnetent
class setnetent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mkstemp64
class mkstemp64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__libc_current_sigrtmin_private
class __libc_current_sigrtmin_private(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:gnu_dev_minor
class gnu_dev_minor(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isinff
class isinff(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getresgid
class getresgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_siglongjmp
class __libc_siglongjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:statfs
class statfs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:geteuid
class geteuid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:sched_setparam
class sched_setparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__memcpy_chk
class __memcpy_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ether_hostton
class ether_hostton(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswalpha_l
class iswalpha_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:quotactl
class quotactl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:srandom
class srandom(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswspace_l
class __iswspace_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getrpcbynumber_r
class getrpcbynumber_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:isinfl
class isinfl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_vfscanf
class __isoc99_vfscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:atof
class atof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getttynam
class getttynam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:re_set_registers
class re_set_registers(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__open_catalog
class __open_catalog(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigismember
class sigismember(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_setschedparam
class pthread_attr_setschedparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:bcopy
class bcopy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setlinebuf
class setlinebuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcswcs
class wcswcs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:atoi
class atoi(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__iswprint_l
class __iswprint_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtok_r_1c
class __strtok_r_1c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_hyper
class xdr_hyper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getdirentries64
class getdirentries64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:stime
class stime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:textdomain
class textdomain(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:sched_get_priority_max
class sched_get_priority_max(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:atol
class atol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:tcflush
class tcflush(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_getschedparam
class posix_spawnattr_getschedparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:inet6_opt_find
class inet6_opt_find(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstoull
class wcstoull(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ether_ntohost
class ether_ntohost(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mlockall
class mlockall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:stty
class stty(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswxdigit
class iswxdigit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftw64
class ftw64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:waitpid
class waitpid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fpending
class __fpending(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:close
class close(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:unlockpt
class unlockpt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_union
class xdr_union(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:backtrace
class backtrace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strverscmp
class strverscmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_getschedpolicy
class posix_spawnattr_getschedpolicy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:catgets
class catgets(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lldiv
class lldiv(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endutent
class endutent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:pthread_setcancelstate
class pthread_setcancelstate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tmpnam
class tmpnam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:inet_nsap_ntoa
class inet_nsap_ntoa(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strerror_l
class strerror_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:open
class open(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:twalk
class twalk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:srand48
class srand48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:toupper_l
class toupper_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcunixfd_create
class svcunixfd_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iopl
class iopl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ftw
class ftw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstoull_internal
class __wcstoull_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sgetspent
class sgetspent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:strerror_r
class strerror_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_iter_begin
class _IO_iter_begin(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:pthread_getschedparam
class pthread_getschedparam(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dngettext
class dngettext(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__rpc_thread_createerr
class __rpc_thread_createerr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:vhangup
class vhangup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:localtime
class localtime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:key_secretkey_is_set
class key_secretkey_is_set(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:difftime
class difftime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:swapon
class swapon(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endutxent
class endutxent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:lseek64
class lseek64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ferror_unlocked
class ferror_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:umount
class umount(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_Exit
class _Exit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:capset
class capset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strchr
class strchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wctrans_l
class wctrans_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:flistxattr
class flistxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clnt_spcreateerror
class clnt_spcreateerror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:obstack_free
class obstack_free(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_getscope
class pthread_attr_getscope(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getaliasent
class getaliasent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:sigignore
class sigignore(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigreturn
class sigreturn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:rresvport_af
class rresvport_af(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__monstartup
class __monstartup(emufunc.EmuFunc):
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


#EMUFUNC:svcerr_weakauth
class svcerr_weakauth(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fcloseall
class fcloseall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:iswcntrl
class iswcntrl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endmntent
class endmntent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:funlockfile
class funlockfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fprintf
class fprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getsockname
class getsockname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:utime
class utime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:scandir64
class scandir64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, FUNCPTR, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:hsearch
class hsearch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strpbrk_c2
class __strpbrk_c2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:abs
class abs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sendto
class sendto(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__strpbrk_c3
class __strpbrk_c3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:addmntent
class addmntent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswpunct_l
class iswpunct_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtold_l
class __strtold_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:updwtmp
class updwtmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_least_wmarker
class _IO_least_wmarker(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rindex
class rindex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vfork
class vfork(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getgrent_r
class getgrent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xprt_register
class xprt_register(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:addseverity
class addseverity(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vfprintf_chk
class __vfprintf_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mktime
class mktime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:key_gendes
class key_gendes(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mblen
class mblen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tdestroy
class tdestroy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:sysctl
class sysctl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clnt_create
class clnt_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:alphasort
class alphasort(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_rmtcall_args
class xdr_rmtcall_args(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__strtok_r
class __strtok_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mallopt
class mallopt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdrstdio_create
class xdrstdio_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtoimax
class strtoimax(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getline
class getline(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswdigit_l
class __iswdigit_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__stpcpy
class __stpcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iconv
class iconv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:get_myaddress
class get_myaddress(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getrpcbyname_r
class getrpcbyname_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:bdflush
class bdflush(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:imaxabs
class imaxabs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:re_compile_fastmap
class re_compile_fastmap(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lremovexattr
class lremovexattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fdopen
class fdopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_str_seekoff
class _IO_str_seekoff(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setusershell
class setusershell(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:readdir64
class readdir64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_callmsg
class xdr_callmsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:svcerr_auth
class svcerr_auth(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:qsort
class qsort(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:canonicalize_file_name
class canonicalize_file_name(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__getpgid
class __getpgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iconv_open
class iconv_open(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_sgetn
class _IO_sgetn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtod_internal
class __strtod_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fsetpos64
class _IO_fsetpos64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strfmon_l
class strfmon_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mrand48
class mrand48(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_getflags
class posix_spawnattr_getflags(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:accept
class accept(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wcstombs
class wcstombs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_free
class __libc_free(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:gethostbyname2
class gethostbyname2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:cbc_crypt
class cbc_crypt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__nss_hosts_lookup
class __nss_hosts_lookup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__strtoull_l
class __strtoull_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_netnamestr
class xdr_netnamestr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_str_overflow
class _IO_str_overflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argp_parse
class argp_parse(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_seekpos
class _IO_seekpos(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:envz_get
class envz_get(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcasestr
class __strcasestr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getresuid
class getresuid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_setsigmask
class posix_spawnattr_setsigmask(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:hstrerror
class hstrerror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vsyslog_chk
class __vsyslog_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inotify_add_watch
class inotify_add_watch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_proc_close
class _IO_proc_close(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tcgetattr
class tcgetattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:toascii
class toascii(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:statfs64
class statfs64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:authnone_create
class authnone_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__strcmp_gg
class __strcmp_gg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isupper_l
class isupper_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sethostid
class sethostid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getutxline
class getutxline(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tmpfile64
class tmpfile64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:sleep
class sleep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:times
class times(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_sync
class _IO_file_sync(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsxfrm
class wcsxfrm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcspn_g
class __strcspn_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strxfrm_l
class strxfrm_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_allocate_rtsig
class __libc_allocate_rtsig(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__ctype_toupper_loc
class __ctype_toupper_loc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:vm86
class vm86(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:insque
class insque(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clntraw_create
class clntraw_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:epoll_pwait
class epoll_pwait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__getpagesize
class __getpagesize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:valloc
class valloc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__ctype_tolower_loc
class __ctype_tolower_loc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getutxent
class getutxent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_list_unlock
class _IO_list_unlock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:fputws_unlocked
class fputws_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:xdr_array
class xdr_array(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:llistxattr
class llistxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__cxa_finalize
class __cxa_finalize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_current_sigrtmin
class __libc_current_sigrtmin(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:umount2
class umount2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:syscall
class syscall(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigpending
class sigpending(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:bsearch
class bsearch(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, FUNCPTR, ]
#EMUFUNCDONE


#EMUFUNC:__strpbrk_cg
class __strpbrk_cg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:freeaddrinfo
class freeaddrinfo(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strncasecmp_l
class strncasecmp_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__assert_perror_fail
class __assert_perror_fail(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:get_nprocs
class get_nprocs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getprotobyname_r
class getprotobyname_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__xpg_strerror_r
class __xpg_strerror_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setvbuf
class setvbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcsxfrm_l
class __wcsxfrm_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vsscanf
class vsscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__divdi3
class __divdi3(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetpwent
class fgetpwent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setaliasent
class setaliasent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__sigsuspend
class __sigsuspend(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:xdr_rejected_reply
class xdr_rejected_reply(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:capget
class capget(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:readdir64_r
class readdir64_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sched_setscheduler
class __sched_setscheduler(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpublickey
class getpublickey(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__rpc_thread_svc_pollfd
class __rpc_thread_svc_pollfd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:fts_open
class fts_open(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svc_unregister
class svc_unregister(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pututline
class pututline(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setsid
class setsid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getutent
class getutent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:posix_spawnattr_getsigdefault
class posix_spawnattr_getsigdefault(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:iswgraph_l
class iswgraph_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:printf_size
class printf_size(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_destroy
class pthread_attr_destroy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcscoll
class wcscoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__wcstoul_internal
class __wcstoul_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__deregister_frame
class __deregister_frame(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sigaction
class __sigaction(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:xdr_uint64_t
class xdr_uint64_t(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svcunix_create
class svcunix_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:nrand48_r
class nrand48_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:cfsetspeed
class cfsetspeed(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_nss_files_parse_spent
class _nss_files_parse_spent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_freeres
class __libc_freeres(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:fcntl
class fcntl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wctype
class wctype(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wcsspn
class wcsspn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getrlimit64
class getrlimit64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_option_init
class inet6_option_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__iswctype_l
class __iswctype_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ecvt
class ecvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rresvport
class rresvport(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:bindresvport
class bindresvport(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:cfsetospeed
class cfsetospeed(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__asprintf
class __asprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strcasecmp_l
class __strcasecmp_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fwide
class fwide(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getgrgid_r
class getgrgid_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:pthread_cond_init
class pthread_cond_init(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setpgrp
class setpgrp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wcsdup
class wcsdup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:cfgetispeed
class cfgetispeed(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:atoll
class atoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:bsd_signal
class bsd_signal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ptsname_r
class ptsname_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtol_l
class __strtol_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fsetxattr
class fsetxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__h_errno_location
class __h_errno_location(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdrrec_create
class xdrrec_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_seekoff
class _IO_file_seekoff(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_ftrylockfile
class _IO_ftrylockfile(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__close
class __close(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_iter_next
class _IO_iter_next(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getmntent_r
class getmntent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strchrnul_c
class __strchrnul_c(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:labs
class labs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:link
class link(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strftime_l
class __strftime_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_cryptkeyres
class xdr_cryptkeyres(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:futimesat
class futimesat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_wdefault_xsgetn
class _IO_wdefault_xsgetn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:innetgr
class innetgr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:openat
class openat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vswprintf
class vswprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__iswcntrl_l
class __iswcntrl_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vdprintf
class vdprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strchrnul_g
class __strchrnul_g(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clntudp_create
class clntudp_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:getprotobyname
class getprotobyname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__deregister_frame_info_bases
class __deregister_frame_info_bases(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_getline_info
class _IO_getline_info(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tolower_l
class tolower_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fsetlocking
class __fsetlocking(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strptime_l
class strptime_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_create_sep
class argz_create_sep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__xstat
class __xstat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wcscoll_l
class wcscoll_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__backtrace
class __backtrace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getrlimit
class getrlimit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigsetmask
class sigsetmask(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:key_encryptsession
class key_encryptsession(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isdigit
class isdigit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:scanf
class scanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getxattr
class getxattr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:lchmod
class lchmod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:iscntrl
class iscntrl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_msgrcv
class __libc_msgrcv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getdtablesize
class getdtablesize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:mount
class mount(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__toupper_l
class __toupper_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:random_r
class random_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:iswpunct
class iswpunct(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:errx
class errx(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strcasecmp_l
class strcasecmp_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wmemchr
class wmemchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:uname
class uname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:memmove
class memmove(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:key_setnet
class key_setnet(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_write
class _IO_file_write(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstod
class wcstod(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__chk_fail
class __chk_fail(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:svc_getreqset
class svc_getreqset(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:mcount
class mcount(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__isoc99_vscanf
class __isoc99_vscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mprobe
class mprobe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawnp
class posix_spawnp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstof
class wcstof(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_overflow
class _IO_file_overflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:backtrace_symbols
class backtrace_symbols(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_list_resetlock
class _IO_list_resetlock(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__modify_ldt
class __modify_ldt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_mcleanup
class _mcleanup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__wctrans_l
class __wctrans_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isxdigit_l
class isxdigit_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigtimedwait
class sigtimedwait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fwrite
class _IO_fwrite(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:ruserpass
class ruserpass(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstok
class wcstok(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_self
class pthread_self(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:svc_register
class svc_register(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__waitpid
class __waitpid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstol
class wcstol(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fopen64
class fopen64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_attr_setschedpolicy
class pthread_attr_setschedpolicy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vswscanf
class vswscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endservent
class endservent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__nss_group_lookup
class __nss_group_lookup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:pread
class pread(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ctermid
class ctermid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcschrnul
class wcschrnul(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_dlsym
class __libc_dlsym(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pwrite
class pwrite(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__endmntent
class __endmntent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstoq
class wcstoq(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sigstack
class sigstack(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__vfork
class __vfork(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:strsep
class strsep(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__freadable
class __freadable(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mkostemp
class mkostemp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswblank_l
class iswblank_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_obstack_begin
class _obstack_begin(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, FUNCPTR, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnetgrent
class getnetgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_underflow
class _IO_file_underflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:user2netname
class user2netname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__nss_next
class __nss_next(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsrtombs
class wcsrtombs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:bindtextdomain
class bindtextdomain(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:access
class access(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__sched_getscheduler
class __sched_getscheduler(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fmtmsg
class fmtmsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:qfcvt
class qfcvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtoq_internal
class __strtoq_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ntp_gettime
class ntp_gettime(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mcheck_pedantic
class mcheck_pedantic(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:mtrace
class mtrace(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_getc
class _IO_getc(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fxstatat
class __fxstatat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:memmem
class memmem(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fbufsize
class __fbufsize(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_marker_delta
class _IO_marker_delta(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:rawmemchr
class rawmemchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sync
class sync(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:sysinfo
class sysinfo(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getgrouplist
class getgrouplist(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:bcmp
class bcmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getwc_unlocked
class getwc_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:sigvec
class sigvec(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argz_append
class argz_append(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:svc_getreq
class svc_getreq(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setgid
class setgid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:malloc_set_state
class malloc_set_state(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__argz_count
class __argz_count(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wprintf
class wprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ulckpwdf
class ulckpwdf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:fts_children
class fts_children(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getservbyport_r
class getservbyport_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:mkfifo
class mkfifo(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strxfrm
class strxfrm(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:openat64
class openat64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sched_getscheduler
class sched_getscheduler(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:on_exit
class on_exit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:faccessat
class faccessat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__res_randomid
class __res_randomid(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:setbuf
class setbuf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_gets
class _IO_gets(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fwrite_unlocked
class fwrite_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:strcmp
class strcmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_longjmp
class __libc_longjmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtoull_internal
class __strtoull_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:iswspace_l
class iswspace_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:recvmsg
class recvmsg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:islower_l
class islower_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__underflow
class __underflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pwrite64
class pwrite64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strerror
class strerror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strfmon_l
class __strfmon_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_wrapstring
class xdr_wrapstring(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:tcgetpgrp
class tcgetpgrp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_start_main
class __libc_start_main(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [FUNCPTR, Unknown, Unknown, FUNCPTR, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:dirfd
class dirfd(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetwc_unlocked
class fgetwc_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:nftw
class nftw(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_des_block
class xdr_des_block(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_callhdr
class xdr_callhdr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:iswprint_l
class iswprint_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_cryptkeyarg2
class xdr_cryptkeyarg2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setpwent
class setpwent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:semop
class semop(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:endfsent
class endfsent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:__isupper_l
class __isupper_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wscanf
class wscanf(emufunc.EmuFunc):
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


#EMUFUNC:getutent_r
class getutent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:authdes_create
class authdes_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ppoll
class ppoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:stpcpy
class stpcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:pthread_cond_destroy
class pthread_cond_destroy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetpwent_r
class fgetpwent_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__strxfrm_l
class __strxfrm_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fdetach
class fdetach(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:ldexp
class ldexp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:gcvt
class gcvt(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wait
class __wait(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fwprintf
class fwprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_bytes
class xdr_bytes(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setenv
class setenv(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:nl_langinfo_l
class nl_langinfo_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setpriority
class setpriority(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_spawn_file_actions_addopen
class posix_spawn_file_actions_addopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__gconv_get_modules_db
class __gconv_get_modules_db(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:_IO_default_doallocate
class _IO_default_doallocate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__libc_dlopen_mode
class __libc_dlopen_mode(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fread
class _IO_fread(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fgetgrent
class fgetgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setdomainname
class setdomainname(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:write
class write(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getservbyport
class getservbyport(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:if_freenameindex
class if_freenameindex(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strtod_l
class strtod_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getnetent
class getnetent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getutline_r
class getutline_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wcslen
class wcslen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_fallocate
class posix_fallocate(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__pipe
class __pipe(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:lckpwdf
class lckpwdf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:xdrrec_endofrecord
class xdrrec_endofrecord(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:fseeko
class fseeko(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:towctrans_l
class towctrans_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:strcoll
class strcoll(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:inet6_opt_set_val
class inet6_opt_set_val(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ssignal
class ssignal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vfprintf
class vfprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:random
class random(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:globfree
class globfree(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:delete_module
class delete_module(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__wcstold_internal
class __wcstold_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:argp_state_help
class argp_state_help(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:basename
class basename(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ntohl
class ntohl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getpgrp
class getpgrp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:getopt_long_only
class getopt_long_only(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:closelog
class closelog(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wcsncmp
class wcsncmp(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:re_exec
class re_exec(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:isascii
class isascii(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:get_nprocs_conf
class get_nprocs_conf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:clnt_pcreateerror
class clnt_pcreateerror(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:monstartup
class monstartup(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__fcntl
class __fcntl(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:ntohs
class ntohs(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:snprintf
class snprintf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__isoc99_fwscanf
class __isoc99_fwscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__overflow
class __overflow(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strtoul_internal
class __strtoul_internal(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wmemmove
class wmemmove(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:posix_fadvise64
class posix_fadvise64(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_cryptkeyarg
class xdr_cryptkeyarg(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:sysconf
class sysconf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__gets_chk
class __gets_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_obstack_free
class _obstack_free(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gnu_dev_makedev
class gnu_dev_makedev(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_u_hyper
class xdr_u_hyper(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:setnetgrent
class setnetgrent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__xmknodat
class __xmknodat(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:_IO_fdopen
class _IO_fdopen(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:inet6_option_find
class inet6_option_find(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcstoull_l
class wcstoull_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:clnttcp_create
class clnttcp_create(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:isgraph_l
class isgraph_l(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:getservent
class getservent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:wctomb
class wctomb(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:fputs_unlocked
class fputs_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:siggetmask
class siggetmask(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:putpwent
class putpwent(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:putwchar_unlocked
class putwchar_unlocked(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strncpy_by2
class __strncpy_by2(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:semget
class semget(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_str_init_readonly
class _IO_str_init_readonly(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__strncpy_by4
class __strncpy_by4(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:initstate_r
class initstate_r(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:xdr_accepted_reply
class xdr_accepted_reply(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:__vsscanf
class __vsscanf(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:free
class free(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wcsstr
class wcsstr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:wcsrchr
class wcsrchr(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ispunct
class ispunct(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:_IO_file_seek
class _IO_file_seek(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__cyg_profile_func_exit
class __cyg_profile_func_exit(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE


#EMUFUNC:pthread_attr_getinheritsched
class pthread_attr_getinheritsched(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:__readlinkat_chk
class __readlinkat_chk(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:key_decryptsession
class key_decryptsession(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:vwarn
class vwarn(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:wcpcpy
class wcpcpy(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

