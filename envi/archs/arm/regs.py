from envi.archs.arm.const import *
import envi.registers as e_reg


reg_table = [(None,0,None, None) for x in xrange(17*16)]
arm_regnames = ("r0","r1","r2","r3","r4","r5","r6","r7","r8","r9","sl","fp","ip","sp","lr","pc","cpsr")
reg_base = ("r0_","r1_","r2_","r3_","r4_","r5_","r6_","r7_","r8_","r9_","r10_","r11_","r12_","r13_","r14_","error-r15_","SPSR_")
"""
modes = ("usr","fiq","irq","svc","abt","und")  #more mode-related stuff in const.py
mode_defs = {   # ( Arm_regs, 
    "usr":  ( 15, PM_usr, ),  # user mode
    "fiq":  ( 8,  PM_fiq, ),
    "irq":  ( 13, PM_irq, ),
    "svc":  ( 13, PM_svc, ),
    "abt":  ( 13, PM_abt, ),
    "und":  ( 13, PM_und, ),
    "sys":  ( 15, PM_sys, ),
}
"""
for modenum in proc_modes.keys():
    mode_name, short_name, desc, mode_reg_base, creg_count, psr_offset = proc_modes[modenum]
    #mode_reg_base = (modenum&0xf) * 17
    #print mode_reg_base
    for x in range(creg_count):
        # (reg_name, bitsize, regidx_for_emulation, init_val)
        reg_table[mode_reg_base + x] = (arm_regnames[x], 32, x, 0)
    
    for x in range(creg_count, 15):
        reg_table[mode_reg_base + x] = (reg_base[x] + short_name, 32, mode_reg_base+x, 0)
    
    reg_table[mode_reg_base + 15] = (arm_regnames[15], 32, 15, 0)                   # program counter
    reg_table[mode_reg_base + 16] = (reg_base[16] + short_name, 32, mode_reg_base+16, modenum) # SPSR
#FIXME: What to do with CPSR...  hack... "hey yall check this out!"
reg_table[REG_OFFSET_CPSR] = ("cpsr", 32, REG_OFFSET_CPSR, PM_usr)     # CPSR will maintain it's own value, to be stored into SPSR's as modes change.
reg_table[REG_SPSR_sys] = ("cpsr", 32, REG_OFFSET_CPSR, PM_usr)        # SPSR_sys is same reg as SPSR_usr.
#reg_table[REG_SPSR_sys] = ("SPSR_sys", 32, 16, 0)               # SPSR_sys is same reg as SPSR_usr.

PSR_N = 31  # negative
PSR_Z = 30  # zero
PSR_C = 29  # carry
PSR_V = 28  # oVerflow
PSR_Q = 27
PSR_J = 24
PSR_GE = 16
PSR_E = 9
PSR_A = 8
PSR_I = 7
PSR_F = 6
PSR_T = 5
PSR_M = 0

PSR_C_bit  = 1 << PSR_C
PSR_C_mask = 0xffffffff ^ PSR_C_bit

psr_fields = [None for x in xrange(32)]
psr_fields[PSR_M] = "M"
psr_fields[PSR_T] = "T"
psr_fields[PSR_F] = "F"
psr_fields[PSR_I] = "I"
psr_fields[PSR_A] = "A"
psr_fields[PSR_E] = "E"
psr_fields[PSR_GE] = "GE"
psr_fields[PSR_GE+1] = "GE+1"
psr_fields[PSR_GE+2] = "GE+2"
psr_fields[PSR_GE+3] = "GE+3"
psr_fields[PSR_J] = "J"
psr_fields[PSR_Q] = "Q"
psr_fields[PSR_V] = "V"
psr_fields[PSR_C] = "C"
psr_fields[PSR_Z] = "Z"
psr_fields[PSR_N] = "N"

ArmRegs = [reg_table[x][:2] for x in xrange((17*16))]
ArmMeta =tuple([("N", REG_FLAGS, PSR_N, 1),
                ("Z", REG_FLAGS, PSR_Z, 1),
                ("C", REG_FLAGS, PSR_C, 1),
                ("V", REG_FLAGS, PSR_V, 1),
                ("Q", REG_FLAGS, PSR_Q, 1),
                ("J", REG_FLAGS, PSR_J, 1),
                ("GE",REG_FLAGS, PSR_GE, 4),
                ("E", REG_FLAGS, PSR_E, 1),
                ("A", REG_FLAGS, PSR_A, 1),
                ("I", REG_FLAGS, PSR_I, 1),
                ("F", REG_FLAGS, PSR_F, 1),
                ("T", REG_FLAGS, PSR_T, 1),
                ("M", REG_FLAGS, PSR_M, 5),
                ])


class ArmRegisterContext(e_reg.RegisterContext):
    def __init__(self):
        e_reg.RegisterContext.__init__(self)
        self.loadRegDef(ArmRegs)
        self.loadRegMetas(ArmMeta)
        self.setRegisterIndexes(REG_PC, REG_SP)
        for n,s,idx,val in reg_table:
            if val != None:
                self._rctx_vals[idx] = val

