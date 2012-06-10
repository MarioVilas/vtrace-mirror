
from vivisect.impemu.impmagic import *
import vivisect.impemu.emufunc as emufunc

import ntdll

#EMUFUNC:AbortDoc
class AbortDoc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AbortPath
class AbortPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddFontMemResourceEx
class AddFontMemResourceEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddFontResourceA
class AddFontResourceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddFontResourceExA
class AddFontResourceExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddFontResourceExW
class AddFontResourceExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddFontResourceTracking
class AddFontResourceTracking(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AddFontResourceW
class AddFontResourceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AngleArc
class AngleArc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AnimatePalette
class AnimatePalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:AnyLinkedFonts
class AnyLinkedFonts(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:Arc
class Arc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ArcTo
class ArcTo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BRUSHOBJ_hGetColorTransform
class BRUSHOBJ_hGetColorTransform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BRUSHOBJ_pvAllocRbrush
class BRUSHOBJ_pvAllocRbrush(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BRUSHOBJ_pvGetRbrush
class BRUSHOBJ_pvGetRbrush(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BRUSHOBJ_ulGetBrushColor
class BRUSHOBJ_ulGetBrushColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BeginPath
class BeginPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:BitBlt
class BitBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLIPOBJ_bEnum
class CLIPOBJ_bEnum(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLIPOBJ_cEnumStart
class CLIPOBJ_cEnumStart(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CLIPOBJ_ppoGetPath
class CLIPOBJ_ppoGetPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CancelDC
class CancelDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CheckColorsInGamut
class CheckColorsInGamut(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ChoosePixelFormat
class ChoosePixelFormat(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:Chord
class Chord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ClearBitmapAttributes
class ClearBitmapAttributes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ClearBrushAttributes
class ClearBrushAttributes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CloseEnhMetaFile
class CloseEnhMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CloseFigure
class CloseFigure(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CloseMetaFile
class CloseMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ColorCorrectPalette
class ColorCorrectPalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ColorMatchToTarget
class ColorMatchToTarget(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CombineRgn
class CombineRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CombineTransform
class CombineTransform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CopyEnhMetaFileA
class CopyEnhMetaFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CopyEnhMetaFileW
class CopyEnhMetaFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CopyMetaFileA
class CopyMetaFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CopyMetaFileW
class CopyMetaFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateBitmap
class CreateBitmap(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateBitmapIndirect
class CreateBitmapIndirect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateBrushIndirect
class CreateBrushIndirect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateColorSpaceA
class CreateColorSpaceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateColorSpaceW
class CreateColorSpaceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:CreateCompatibleBitmap
class CreateCompatibleBitmap(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateCompatibleDC
class CreateCompatibleDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDCA
class CreateDCA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDCW
class CreateDCW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDIBPatternBrush
class CreateDIBPatternBrush(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDIBPatternBrushPt
class CreateDIBPatternBrushPt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDIBSection
class CreateDIBSection(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDIBitmap
class CreateDIBitmap(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateDiscardableBitmap
class CreateDiscardableBitmap(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateEllipticRgn
class CreateEllipticRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateEllipticRgnIndirect
class CreateEllipticRgnIndirect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateEnhMetaFileA
class CreateEnhMetaFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateEnhMetaFileW
class CreateEnhMetaFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateFontA
class CreateFontA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateFontIndirectA
class CreateFontIndirectA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateFontIndirectExA
class CreateFontIndirectExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateFontIndirectExW
class CreateFontIndirectExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateFontIndirectW
class CreateFontIndirectW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateFontW
class CreateFontW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateHalftonePalette
class CreateHalftonePalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateHatchBrush
class CreateHatchBrush(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateICA
class CreateICA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateICW
class CreateICW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateMetaFileA
class CreateMetaFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateMetaFileW
class CreateMetaFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePalette
class CreatePalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePatternBrush
class CreatePatternBrush(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePen
class CreatePen(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePenIndirect
class CreatePenIndirect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePolyPolygonRgn
class CreatePolyPolygonRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreatePolygonRgn
class CreatePolygonRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateRectRgn
class CreateRectRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateRectRgnIndirect
class CreateRectRgnIndirect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateRoundRectRgn
class CreateRoundRectRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateScalableFontResourceA
class CreateScalableFontResourceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:CreateScalableFontResourceW
class CreateScalableFontResourceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:CreateSolidBrush
class CreateSolidBrush(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DPtoLP
class DPtoLP(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry0
class DdEntry0(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry1
class DdEntry1(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry10
class DdEntry10(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry11
class DdEntry11(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry12
class DdEntry12(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry13
class DdEntry13(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry14
class DdEntry14(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry15
class DdEntry15(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry16
class DdEntry16(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry17
class DdEntry17(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry18
class DdEntry18(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry19
class DdEntry19(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry2
class DdEntry2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry20
class DdEntry20(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry21
class DdEntry21(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry22
class DdEntry22(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry23
class DdEntry23(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry24
class DdEntry24(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry25
class DdEntry25(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry26
class DdEntry26(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry27
class DdEntry27(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry28
class DdEntry28(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry29
class DdEntry29(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry3
class DdEntry3(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry30
class DdEntry30(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry31
class DdEntry31(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry32
class DdEntry32(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry33
class DdEntry33(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry34
class DdEntry34(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry35
class DdEntry35(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry36
class DdEntry36(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry37
class DdEntry37(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry38
class DdEntry38(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry39
class DdEntry39(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry4
class DdEntry4(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry40
class DdEntry40(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry41
class DdEntry41(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry42
class DdEntry42(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry43
class DdEntry43(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry44
class DdEntry44(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry45
class DdEntry45(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry46
class DdEntry46(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry47
class DdEntry47(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry48
class DdEntry48(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry49
class DdEntry49(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry5
class DdEntry5(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry50
class DdEntry50(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry51
class DdEntry51(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry52
class DdEntry52(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry53
class DdEntry53(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry54
class DdEntry54(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry55
class DdEntry55(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry56
class DdEntry56(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry6
class DdEntry6(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry7
class DdEntry7(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry8
class DdEntry8(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DdEntry9
class DdEntry9(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteColorSpace
class DeleteColorSpace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteDC
class DeleteDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteEnhMetaFile
class DeleteEnhMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteMetaFile
class DeleteMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeleteObject
class DeleteObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DescribePixelFormat
class DescribePixelFormat(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeviceCapabilitiesExA
class DeviceCapabilitiesExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DeviceCapabilitiesExW
class DeviceCapabilitiesExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:DrawEscape
class DrawEscape(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:Ellipse
class Ellipse(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnableEUDC
class EnableEUDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EndDoc
class EndDoc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EndFormPage
class EndFormPage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EndPage
class EndPage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EndPath
class EndPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngAcquireSemaphore
class EngAcquireSemaphore(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:EngAlphaBlend
class EngAlphaBlend(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngAssociateSurface
class EngAssociateSurface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngBitBlt
class EngBitBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngCheckAbort
class EngCheckAbort(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngComputeGlyphSet
class EngComputeGlyphSet(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngCopyBits
class EngCopyBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngCreateBitmap
class EngCreateBitmap(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngCreateClip
class EngCreateClip(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:EngCreateDeviceBitmap
class EngCreateDeviceBitmap(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngCreateDeviceSurface
class EngCreateDeviceSurface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngCreatePalette
class EngCreatePalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngCreateSemaphore
class EngCreateSemaphore(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:EngDeleteClip
class EngDeleteClip(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngDeletePalette
class EngDeletePalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngDeletePath
class EngDeletePath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngDeleteSemaphore
class EngDeleteSemaphore(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE

#EMUFUNC:EngDeleteSurface
class EngDeleteSurface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngEraseSurface
class EngEraseSurface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngFillPath
class EngFillPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngFindResource
class EngFindResource(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngFreeModule
class EngFreeModule(emufunc.EmuFunc):
    __callconv__ = 'cdecl'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE


#EMUFUNC:EngGetCurrentCodePage
class EngGetCurrentCodePage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngGetDriverName
class EngGetDriverName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngGetPrinterDataFileName
class EngGetPrinterDataFileName(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngGradientFill
class EngGradientFill(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngLineTo
class EngLineTo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngLoadModule
class EngLoadModule(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngLockSurface
class EngLockSurface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngMarkBandingSurface
class EngMarkBandingSurface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngMultiByteToUnicodeN
class EngMultiByteToUnicodeN(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngMultiByteToWideChar
class EngMultiByteToWideChar(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngPaint
class EngPaint(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngPlgBlt
class EngPlgBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngQueryEMFInfo
class EngQueryEMFInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngQueryLocalTime
class EngQueryLocalTime(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngReleaseSemaphore
class EngReleaseSemaphore(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:EngStretchBlt
class EngStretchBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngStretchBltROP
class EngStretchBltROP(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngStrokeAndFillPath
class EngStrokeAndFillPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngStrokePath
class EngStrokePath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngTextOut
class EngTextOut(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngTransparentBlt
class EngTransparentBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngUnicodeToMultiByteN
class EngUnicodeToMultiByteN(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngUnlockSurface
class EngUnlockSurface(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EngWideCharToMultiByte
class EngWideCharToMultiByte(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumEnhMetaFile
class EnumEnhMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumFontFamiliesA
class EnumFontFamiliesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumFontFamiliesExA
class EnumFontFamiliesExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumFontFamiliesExW
class EnumFontFamiliesExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumFontFamiliesW
class EnumFontFamiliesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumFontsA
class EnumFontsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumFontsW
class EnumFontsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumICMProfilesA
class EnumICMProfilesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:EnumICMProfilesW
class EnumICMProfilesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:EnumMetaFile
class EnumMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EnumObjects
class EnumObjects(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EqualRgn
class EqualRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:Escape
class Escape(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, 'dwSize', None, None]
    __argt__ = [Unknown, Unknown, ntdll.DWORD, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:EudcLoadLinkW
class EudcLoadLinkW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:EudcUnloadLinkW
class EudcUnloadLinkW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ExcludeClipRect
class ExcludeClipRect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ExtCreatePen
class ExtCreatePen(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ExtCreateRegion
class ExtCreateRegion(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ExtEscape
class ExtEscape(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, 'dwSize', None, None, None]
    __argt__ = [Unknown, Unknown, ntdll.DWORD, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ExtFloodFill
class ExtFloodFill(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ExtSelectClipRgn
class ExtSelectClipRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ExtTextOutA
class ExtTextOutA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, 'lpVoid', 'dwSize', None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ntdll.DWORD, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:ExtTextOutW
class ExtTextOutW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, 'lpVoid', None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FONTOBJ_cGetAllGlyphHandles
class FONTOBJ_cGetAllGlyphHandles(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FONTOBJ_cGetGlyphs
class FONTOBJ_cGetGlyphs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FONTOBJ_pQueryGlyphAttrs
class FONTOBJ_pQueryGlyphAttrs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FONTOBJ_pfdg
class FONTOBJ_pfdg(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FONTOBJ_pifi
class FONTOBJ_pifi(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FONTOBJ_pvTrueTypeFontFile
class FONTOBJ_pvTrueTypeFontFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FONTOBJ_pxoGetXform
class FONTOBJ_pxoGetXform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FONTOBJ_vGetInfo
class FONTOBJ_vGetInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FillPath
class FillPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FillRgn
class FillRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FixBrushOrgEx
class FixBrushOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FlattenPath
class FlattenPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FloodFill
class FloodFill(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FontIsLinked
class FontIsLinked(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:FrameRgn
class FrameRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiAddFontResourceW
class GdiAddFontResourceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiAddGlsBounds
class GdiAddGlsBounds(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GdiAddGlsRecord
class GdiAddGlsRecord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiAlphaBlend
class GdiAlphaBlend(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiArtificialDecrementDriver
class GdiArtificialDecrementDriver(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiCleanCacheDC
class GdiCleanCacheDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiComment
class GdiComment(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GdiConsoleTextOut
class GdiConsoleTextOut(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertAndCheckDC
class GdiConvertAndCheckDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertBitmap
class GdiConvertBitmap(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertBitmapV5
class GdiConvertBitmapV5(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertBrush
class GdiConvertBrush(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertDC
class GdiConvertDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertEnhMetaFile
class GdiConvertEnhMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertFont
class GdiConvertFont(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertMetaFilePict
class GdiConvertMetaFilePict(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertPalette
class GdiConvertPalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertRegion
class GdiConvertRegion(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiConvertToDevmodeW
class GdiConvertToDevmodeW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiCreateLocalEnhMetaFile
class GdiCreateLocalEnhMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiCreateLocalMetaFilePict
class GdiCreateLocalMetaFilePict(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiDeleteLocalDC
class GdiDeleteLocalDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiDeleteSpoolFileHandle
class GdiDeleteSpoolFileHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = ['lpVoid']
    __argt__ = [Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GdiDescribePixelFormat
class GdiDescribePixelFormat(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiDllInitialize
class GdiDllInitialize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiDrawStream
class GdiDrawStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GdiEndDocEMF
class GdiEndDocEMF(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEndPageEMF
class GdiEndPageEMF(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry1
class GdiEntry1(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry10
class GdiEntry10(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry11
class GdiEntry11(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry12
class GdiEntry12(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry13
class GdiEntry13(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GdiEntry14
class GdiEntry14(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry15
class GdiEntry15(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry16
class GdiEntry16(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry2
class GdiEntry2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry3
class GdiEntry3(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry4
class GdiEntry4(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry5
class GdiEntry5(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry6
class GdiEntry6(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry7
class GdiEntry7(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry8
class GdiEntry8(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiEntry9
class GdiEntry9(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiFixUpHandle
class GdiFixUpHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiFlush
class GdiFlush(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GdiFullscreenControl
class GdiFullscreenControl(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetBatchLimit
class GdiGetBatchLimit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GdiGetBitmapBitsSize
class GdiGetBitmapBitsSize(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetCharDimensions
class GdiGetCharDimensions(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetCodePage
class GdiGetCodePage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetDC
class GdiGetDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetDevmodeForPage
class GdiGetDevmodeForPage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetLocalBrush
class GdiGetLocalBrush(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetLocalDC
class GdiGetLocalDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetLocalFont
class GdiGetLocalFont(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetPageCount
class GdiGetPageCount(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetPageHandle
class GdiGetPageHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetSpoolFileHandle
class GdiGetSpoolFileHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGetSpoolMessage
class GdiGetSpoolMessage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiGradientFill
class GdiGradientFill(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiInitSpool
class GdiInitSpool(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GdiInitializeLanguagePack
class GdiInitializeLanguagePack(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiIsMetaFileDC
class GdiIsMetaFileDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiIsMetaPrintDC
class GdiIsMetaPrintDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiIsPlayMetafileDC
class GdiIsPlayMetafileDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiPlayDCScript
class GdiPlayDCScript(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiPlayEMF
class GdiPlayEMF(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'dwSize', None, None, None]
    __argt__ = [Unknown, ntdll.DWORD, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiPlayJournal
class GdiPlayJournal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiPlayPageEMF
class GdiPlayPageEMF(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiPlayPrivatePageEMF
class GdiPlayPrivatePageEMF(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiPlayScript
class GdiPlayScript(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiPrinterThunk
class GdiPrinterThunk(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiProcessSetup
class GdiProcessSetup(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GdiQueryFonts
class GdiQueryFonts(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiQueryTable
class GdiQueryTable(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GdiRealizationInfo
class GdiRealizationInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GdiReleaseDC
class GdiReleaseDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiReleaseLocalDC
class GdiReleaseLocalDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiResetDCEMF
class GdiResetDCEMF(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'dwSize']
    __argt__ = [Unknown, ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:GdiSetAttrs
class GdiSetAttrs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiSetBatchLimit
class GdiSetBatchLimit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiSetLastError
class GdiSetLastError(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiSetPixelFormat
class GdiSetPixelFormat(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiSetServerAttr
class GdiSetServerAttr(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiStartDocEMF
class GdiStartDocEMF(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:GdiStartPageEMF
class GdiStartPageEMF(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiSwapBuffers
class GdiSwapBuffers(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiTransparentBlt
class GdiTransparentBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GdiValidateHandle
class GdiValidateHandle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetArcDirection
class GetArcDirection(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetAspectRatioFilterEx
class GetAspectRatioFilterEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetBitmapAttributes
class GetBitmapAttributes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetBitmapBits
class GetBitmapBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetBitmapDimensionEx
class GetBitmapDimensionEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetBkColor
class GetBkColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetBkMode
class GetBkMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetBoundsRect
class GetBoundsRect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:GetBrushAttributes
class GetBrushAttributes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetBrushOrgEx
class GetBrushOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharABCWidthsA
class GetCharABCWidthsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharABCWidthsFloatA
class GetCharABCWidthsFloatA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharABCWidthsFloatW
class GetCharABCWidthsFloatW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharABCWidthsI
class GetCharABCWidthsI(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharABCWidthsW
class GetCharABCWidthsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharWidth32A
class GetCharWidth32A(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'lpVoid']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetCharWidth32W
class GetCharWidth32W(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharWidthA
class GetCharWidthA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'lpVoid']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetCharWidthFloatA
class GetCharWidthFloatA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'lpVoid']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE

#EMUFUNC:GetCharWidthFloatW
class GetCharWidthFloatW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharWidthI
class GetCharWidthI(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:GetCharWidthInfo
class GetCharWidthInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharWidthW
class GetCharWidthW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharacterPlacementA
class GetCharacterPlacementA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCharacterPlacementW
class GetCharacterPlacementW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:GetClipBox
class GetClipBox(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetClipRgn
class GetClipRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetColorAdjustment
class GetColorAdjustment(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetColorSpace
class GetColorSpace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCurrentObject
class GetCurrentObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetCurrentPositionEx
class GetCurrentPositionEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetDCBrushColor
class GetDCBrushColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetDCOrgEx
class GetDCOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetDCPenColor
class GetDCPenColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetDIBColorTable
class GetDIBColorTable(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetDIBits
class GetDIBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, 'lpVoid', None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetDeviceCaps
class GetDeviceCaps(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetDeviceGammaRamp
class GetDeviceGammaRamp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetETM
class GetETM(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEUDCTimeStamp
class GetEUDCTimeStamp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:GetEUDCTimeStampExW
class GetEUDCTimeStampExW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEnhMetaFileA
class GetEnhMetaFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEnhMetaFileBits
class GetEnhMetaFileBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEnhMetaFileDescriptionA
class GetEnhMetaFileDescriptionA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEnhMetaFileDescriptionW
class GetEnhMetaFileDescriptionW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEnhMetaFileHeader
class GetEnhMetaFileHeader(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEnhMetaFilePaletteEntries
class GetEnhMetaFilePaletteEntries(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEnhMetaFilePixelFormat
class GetEnhMetaFilePixelFormat(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetEnhMetaFileW
class GetEnhMetaFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetFontAssocStatus
class GetFontAssocStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetFontData
class GetFontData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetFontLanguageInfo
class GetFontLanguageInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetFontResourceInfoW
class GetFontResourceInfoW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetFontUnicodeRanges
class GetFontUnicodeRanges(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetGlyphIndicesA
class GetGlyphIndicesA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetGlyphIndicesW
class GetGlyphIndicesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetGlyphOutline
class GetGlyphOutline(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetGlyphOutlineA
class GetGlyphOutlineA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetGlyphOutlineW
class GetGlyphOutlineW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetGlyphOutlineWow
class GetGlyphOutlineWow(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetGraphicsMode
class GetGraphicsMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetHFONT
class GetHFONT(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetICMProfileA
class GetICMProfileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetICMProfileW
class GetICMProfileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetKerningPairs
class GetKerningPairs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetKerningPairsA
class GetKerningPairsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetKerningPairsW
class GetKerningPairsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetLayout
class GetLayout(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetLogColorSpaceA
class GetLogColorSpaceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetLogColorSpaceW
class GetLogColorSpaceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMapMode
class GetMapMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMetaFileA
class GetMetaFileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMetaFileBitsEx
class GetMetaFileBitsEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMetaFileW
class GetMetaFileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMetaRgn
class GetMetaRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetMiterLimit
class GetMiterLimit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetNearestColor
class GetNearestColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetNearestPaletteIndex
class GetNearestPaletteIndex(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetObjectA
class GetObjectA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GetObjectType
class GetObjectType(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetObjectW
class GetObjectW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetOutlineTextMetricsA
class GetOutlineTextMetricsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetOutlineTextMetricsW
class GetOutlineTextMetricsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetPaletteEntries
class GetPaletteEntries(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetPath
class GetPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetPixel
class GetPixel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetPixelFormat
class GetPixelFormat(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetPolyFillMode
class GetPolyFillMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetROP2
class GetROP2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetRandomRgn
class GetRandomRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetRasterizerCaps
class GetRasterizerCaps(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetRegionData
class GetRegionData(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetRelAbs
class GetRelAbs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetRgnBox
class GetRgnBox(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetStockObject
class GetStockObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetStretchBltMode
class GetStretchBltMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetStringBitmapA
class GetStringBitmapA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetStringBitmapW
class GetStringBitmapW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSystemPaletteEntries
class GetSystemPaletteEntries(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetSystemPaletteUse
class GetSystemPaletteUse(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextAlign
class GetTextAlign(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextCharacterExtra
class GetTextCharacterExtra(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextCharset
class GetTextCharset(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextCharsetInfo
class GetTextCharsetInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextColor
class GetTextColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextExtentExPointA
class GetTextExtentExPointA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GetTextExtentExPointI
class GetTextExtentExPointI(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GetTextExtentExPointW
class GetTextExtentExPointW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GetTextExtentExPointWPri
class GetTextExtentExPointWPri(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GetTextExtentPoint32A
class GetTextExtentPoint32A(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextExtentPoint32W
class GetTextExtentPoint32W(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextExtentPointA
class GetTextExtentPointA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextExtentPointI
class GetTextExtentPointI(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextExtentPointW
class GetTextExtentPointW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextFaceA
class GetTextFaceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextFaceAliasW
class GetTextFaceAliasW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextFaceW
class GetTextFaceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextMetricsA
class GetTextMetricsA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetTextMetricsW
class GetTextMetricsW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:GetTransform
class GetTransform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetViewportExtEx
class GetViewportExtEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetViewportOrgEx
class GetViewportOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetWinMetaFileBits
class GetWinMetaFileBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetWindowExtEx
class GetWindowExtEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetWindowOrgEx
class GetWindowOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:GetWorldTransform
class GetWorldTransform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HT_Get8BPPFormatPalette
class HT_Get8BPPFormatPalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:HT_Get8BPPMaskPalette
class HT_Get8BPPMaskPalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IntersectClipRect
class IntersectClipRect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:InvertRgn
class InvertRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidEnhMetaRecord
class IsValidEnhMetaRecord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:IsValidEnhMetaRecordOffExt
class IsValidEnhMetaRecordOffExt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LPtoDP
class LPtoDP(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LineDDA
class LineDDA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:LineTo
class LineTo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MaskBlt
class MaskBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:MirrorRgn
class MirrorRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ModifyWorldTransform
class ModifyWorldTransform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:MoveToEx
class MoveToEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:NamedEscape
class NamedEscape(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OffsetClipRgn
class OffsetClipRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OffsetRgn
class OffsetRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OffsetViewportOrgEx
class OffsetViewportOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:OffsetWindowOrgEx
class OffsetWindowOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PATHOBJ_bEnum
class PATHOBJ_bEnum(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PATHOBJ_bEnumClipLines
class PATHOBJ_bEnumClipLines(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PATHOBJ_vEnumStart
class PATHOBJ_vEnumStart(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PATHOBJ_vEnumStartClipLines
class PATHOBJ_vEnumStartClipLines(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PATHOBJ_vGetBounds
class PATHOBJ_vGetBounds(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PaintRgn
class PaintRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PatBlt
class PatBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PathToRegion
class PathToRegion(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:Pie
class Pie(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PlayEnhMetaFile
class PlayEnhMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PlayEnhMetaFileRecord
class PlayEnhMetaFileRecord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PlayMetaFile
class PlayMetaFile(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PlayMetaFileRecord
class PlayMetaFileRecord(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, 'lpSrc', None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:PlgBlt
class PlgBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolyBezier
class PolyBezier(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolyBezierTo
class PolyBezierTo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolyDraw
class PolyDraw(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolyPatBlt
class PolyPatBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolyPolygon
class PolyPolygon(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolyPolyline
class PolyPolyline(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolyTextOutA
class PolyTextOutA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolyTextOutW
class PolyTextOutW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:Polygon
class Polygon(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:Polyline
class Polyline(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PolylineTo
class PolylineTo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PtInRegion
class PtInRegion(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:PtVisible
class PtVisible(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:QueryFontAssocStatus
class QueryFontAssocStatus(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = []
    __argt__ = []
#EMUFUNCDONE

#EMUFUNC:RealizePalette
class RealizePalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RectInRegion
class RectInRegion(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RectVisible
class RectVisible(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:Rectangle
class Rectangle(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RemoveFontMemResourceEx
class RemoveFontMemResourceEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RemoveFontResourceA
class RemoveFontResourceA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RemoveFontResourceExA
class RemoveFontResourceExA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RemoveFontResourceExW
class RemoveFontResourceExW(emufunc.EmuFunc):
    __callconv__ = 'thiscall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RemoveFontResourceTracking
class RemoveFontResourceTracking(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RemoveFontResourceW
class RemoveFontResourceW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ResetDCA
class ResetDCA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ResetDCW
class ResetDCW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, 'dwSize']
    __argt__ = [Unknown, ntdll.DWORD, ]
#EMUFUNCDONE

#EMUFUNC:ResizePalette
class ResizePalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RestoreDC
class RestoreDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:RoundRect
class RoundRect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:STROBJ_bEnum
class STROBJ_bEnum(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:STROBJ_bEnumPositionsOnly
class STROBJ_bEnumPositionsOnly(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:STROBJ_bGetAdvanceWidths
class STROBJ_bGetAdvanceWidths(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:STROBJ_dwGetCodePage
class STROBJ_dwGetCodePage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:STROBJ_vEnumStart
class STROBJ_vEnumStart(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SaveDC
class SaveDC(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ScaleViewportExtEx
class ScaleViewportExtEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:ScaleWindowExtEx
class ScaleWindowExtEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SelectBrushLocal
class SelectBrushLocal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SelectClipPath
class SelectClipPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SelectClipRgn
class SelectClipRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SelectFontLocal
class SelectFontLocal(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SelectObject
class SelectObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SelectPalette
class SelectPalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetAbortProc
class SetAbortProc(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetArcDirection
class SetArcDirection(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetBitmapAttributes
class SetBitmapAttributes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetBitmapBits
class SetBitmapBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetBitmapDimensionEx
class SetBitmapDimensionEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetBkColor
class SetBkColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetBkMode
class SetBkMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetBoundsRect
class SetBoundsRect(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:SetBrushAttributes
class SetBrushAttributes(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetBrushOrgEx
class SetBrushOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetColorAdjustment
class SetColorAdjustment(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetColorSpace
class SetColorSpace(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetDCBrushColor
class SetDCBrushColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetDCPenColor
class SetDCPenColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetDIBColorTable
class SetDIBColorTable(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetDIBits
class SetDIBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, 'lpVoid', None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetDIBitsToDevice
class SetDIBitsToDevice(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, 'lpVoid', None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:SetDeviceGammaRamp
class SetDeviceGammaRamp(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetEnhMetaFileBits
class SetEnhMetaFileBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetFontEnumeration
class SetFontEnumeration(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetGraphicsMode
class SetGraphicsMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetICMMode
class SetICMMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetICMProfileA
class SetICMProfileA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetICMProfileW
class SetICMProfileW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Pointer, ]
#EMUFUNCDONE


#EMUFUNC:SetLayout
class SetLayout(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetLayoutWidth
class SetLayoutWidth(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetMagicColors
class SetMagicColors(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetMapMode
class SetMapMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetMapperFlags
class SetMapperFlags(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetMetaFileBitsEx
class SetMetaFileBitsEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetMetaRgn
class SetMetaRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetMiterLimit
class SetMiterLimit(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetPaletteEntries
class SetPaletteEntries(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetPixel
class SetPixel(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetPixelFormat
class SetPixelFormat(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetPixelV
class SetPixelV(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetPolyFillMode
class SetPolyFillMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetROP2
class SetROP2(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetRectRgn
class SetRectRgn(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetRelAbs
class SetRelAbs(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetStretchBltMode
class SetStretchBltMode(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetSystemPaletteUse
class SetSystemPaletteUse(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetTextAlign
class SetTextAlign(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetTextCharacterExtra
class SetTextCharacterExtra(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetTextColor
class SetTextColor(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetTextJustification
class SetTextJustification(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetViewportExtEx
class SetViewportExtEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetViewportOrgEx
class SetViewportOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetVirtualResolution
class SetVirtualResolution(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetWinMetaFileBits
class SetWinMetaFileBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetWindowExtEx
class SetWindowExtEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetWindowOrgEx
class SetWindowOrgEx(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SetWorldTransform
class SetWorldTransform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartDocA
class StartDocA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartDocW
class StartDocW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartFormPage
class StartFormPage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StartPage
class StartPage(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StretchBlt
class StretchBlt(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StretchDIBits
class StretchDIBits(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None, None, None, 'lpVoid', None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, Pointer, Pointer, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:StrokeAndFillPath
class StrokeAndFillPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:StrokePath
class StrokePath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:SwapBuffers
class SwapBuffers(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:TextOutA
class TextOutA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'lpVoid', 'dwSize']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ntdll.DWORD, ]
#EMUFUNCDONE


#EMUFUNC:TextOutW
class TextOutW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, 'lpVoid', 'dwSize']
    __argt__ = [Unknown, Unknown, Unknown, Pointer, ntdll.DWORD, ]
#EMUFUNCDONE


#EMUFUNC:TranslateCharsetInfo
class TranslateCharsetInfo(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnloadNetworkFonts
class UnloadNetworkFonts(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UnrealizeObject
class UnrealizeObject(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UpdateColors
class UpdateColors(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UpdateICMRegKeyA
class UpdateICMRegKeyA(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:UpdateICMRegKeyW
class UpdateICMRegKeyW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Pointer, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:WidenPath
class WidenPath(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:XFORMOBJ_bApplyXform
class XFORMOBJ_bApplyXform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:XFORMOBJ_iGetXform
class XFORMOBJ_iGetXform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:XLATEOBJ_cGetPalette
class XLATEOBJ_cGetPalette(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:XLATEOBJ_hGetColorTransform
class XLATEOBJ_hGetColorTransform(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:XLATEOBJ_iXlate
class XLATEOBJ_iXlate(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:XLATEOBJ_piVector
class XLATEOBJ_piVector(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None]
    __argt__ = [Unknown, ]
#EMUFUNCDONE

#EMUFUNC:bInitSystemAndFontsDirectoriesW
class bInitSystemAndFontsDirectoriesW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None]
    __argt__ = [Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:bMakePathNameW
class bMakePathNameW(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:cGetTTFFromFOT
class cGetTTFFromFOT(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None, None]
    __argt__ = [Pointer, Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


#EMUFUNC:gdiPlaySpoolStream
class gdiPlaySpoolStream(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None, None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, Unknown, Unknown, Unknown, ]
#EMUFUNCDONE

#EMUFUNC:main_entry
class main_entry(emufunc.EmuFunc):
    __callconv__ = 'stdcall'
    __argn__ = [None, None, None]
    __argt__ = [Unknown, Unknown, Unknown, ]
#EMUFUNCDONE


