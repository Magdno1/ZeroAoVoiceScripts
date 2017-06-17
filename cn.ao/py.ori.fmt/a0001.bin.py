﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "a0001.bin",                # FileName
        "a0002",                    # MapName
        "a0002",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 25000, 500, 20, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0001",                  # 0
        "CH00050",                # 1
        "CH00051",                # 2
        "CH00052",                # 3
        "CH00053",                # 4
        "CH00054",                # 5
        "CH00055",                # 6
        "CH00150",                # 7
        "CH00151",                # 8
        "CH00152",                # 9
        "CH00153",                # 10
        "CH00154",                # 11
        "CH00155",                # 12
        "CH00250",                # 13
        "CH00251",                # 14
        "CH00252",                # 15
        "CH00253",                # 16
        "CH00254",                # 17
        "CH00255",                # 18
        "CH00350",                # 19
        "CH00351",                # 20
        "CH00352",                # 21
        "CH00353",                # 22
        "CH00354",                # 23
        "CH00355",                # 24
        "コンシェル",             # 25
    ))

    AddCharChip((
        "chr/ch00050.itc",                   # 00
        "chr/ch00051.itc",                   # 01
        "chr/ch00052.itc",                   # 02
        "chr/ch00053.itc",                   # 03
        "chr/ch00054.itc",                   # 04
        "chr/ch40018.itc",                   # 05
        "chr/ch99999.itc",                   # 06
        "chr/ch99999.itc",                   # 07
        "chr/ch99999.itc",                   # 08
        "chr/ch99999.itc",                   # 09
        "chr/ch00150.itc",                   # 0A
        "chr/ch00151.itc",                   # 0B
        "chr/ch00152.itc",                   # 0C
        "chr/ch00153.itc",                   # 0D
        "chr/ch00154.itc",                   # 0E
        "chr/ch00155.itc",                   # 0F
        "chr/ch99999.itc",                   # 10
        "chr/ch99999.itc",                   # 11
        "chr/ch99999.itc",                   # 12
        "chr/ch99999.itc",                   # 13
        "chr/ch00250.itc",                   # 14
        "chr/ch00251.itc",                   # 15
        "chr/ch00252.itc",                   # 16
        "chr/ch00253.itc",                   # 17
        "chr/ch00254.itc",                   # 18
        "chr/ch00255.itc",                   # 19
        "chr/ch99999.itc",                   # 1A
        "chr/ch99999.itc",                   # 1B
        "chr/ch99999.itc",                   # 1C
        "chr/ch99999.itc",                   # 1D
        "chr/ch00350.itc",                   # 1E
        "chr/ch00351.itc",                   # 1F
        "chr/ch00352.itc",                   # 20
        "chr/ch00353.itc",                   # 21
        "chr/ch00354.itc",                   # 22
        "chr/ch00355.itc",                   # 23
        "chr/ch99999.itc",                   # 24
        "chr/ch99999.itc",                   # 25
        "chr/ch99999.itc",                   # 26
        "chr/ch99999.itc",                   # 27
        "chr/ch99999.itc",                   # 28
        "chr/ch99999.itc",                   # 29
        "chr/ch99999.itc",                   # 2A
        "chr/ch99999.itc",                   # 2B
        "chr/ch99999.itc",                   # 2C
        "chr/ch99999.itc",                   # 2D
        "chr/ch99999.itc",                   # 2E
        "chr/ch99999.itc",                   # 2F
        "chr/ch99999.itc",                   # 30
        "chr/ch99999.itc",                   # 31
        "chr/ch99999.itc",                   # 32
        "chr/ch99999.itc",                   # 33
        "chr/ch99999.itc",                   # 34
        "chr/ch99999.itc",                   # 35
        "chr/ch99999.itc",                   # 36
        "chr/ch99999.itc",                   # 37
        "chr/ch99999.itc",                   # 38
        "chr/ch99999.itc",                   # 39
        "chr/ch99999.itc",                   # 3A
        "chr/ch99999.itc",                   # 3B
        "monster/ch60050.itc",               # 3C
        "chr/ch40018.itc",                   # 3D
    ))

    DeclNpc(4000,    0,       4000,    180,  257,  0x0, 0,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(8000,    0,       4000,    180,  257,  0x0, 0,   1,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(12000,   0,       4000,    180,  257,  0x0, 0,   2,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(16000,   0,       4000,    180,  257,  0x0, 0,   3,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(20000,   0,       4000,    180,  257,  0x0, 0,   4,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(24000,   0,       4000,    180,  259,  0x0, 0,   5,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(4000,    0,       8000,    180,  257,  0x0, 0,   10,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(8000,    0,       8000,    180,  257,  0x0, 0,   11,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(12000,   0,       8000,    180,  257,  0x0, 0,   12,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(16000,   0,       8000,    180,  257,  0x0, 0,   13,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(20000,   0,       8000,    180,  257,  0x0, 0,   14,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(24000,   0,       8000,    180,  259,  0x0, 0,   15,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(4000,    0,       12000,   180,  257,  0x0, 0,   20,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(8000,    0,       12000,   180,  257,  0x0, 0,   21,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(12000,   0,       12000,   180,  257,  0x0, 0,   22,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(16000,   0,       12000,   180,  257,  0x0, 0,   23,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(20000,   0,       12000,   180,  257,  0x0, 0,   24,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(24000,   0,       12000,   180,  259,  0x0, 0,   25,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(4000,    0,       16000,   180,  257,  0x0, 0,   30,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(8000,    0,       16000,   180,  257,  0x0, 0,   31,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(12000,   0,       16000,   180,  257,  0x0, 0,   32,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(16000,   0,       16000,   180,  257,  0x0, 0,   33,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(20000,   0,       16000,   180,  257,  0x0, 0,   34,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(24000,   0,       16000,   180,  259,  0x0, 0,   35,  0,   255, 255, 0,   2,   255,  0)
    DeclNpc(1000,    0,       3000,    180,  257,  0x0, 0,   60,  0,   255, 255, 0,   5,   255,  0)

    ChipFrameInfo(1000, 0, [0, 1, 2, 1])                         # 0

    ScpFunction((
        "Function_0_4C4",          # 00, 0
        "Function_1_4D6",          # 01, 1
        "Function_2_4D7",          # 02, 2
        "Function_3_4EA",          # 03, 3
        "Function_4_651",          # 04, 4
        "Function_5_6F7",          # 05, 5
        "Function_6_1666",         # 06, 6
        "Function_7_167E",         # 07, 7
        "Function_8_1696",         # 08, 8
        "Function_9_16AE",         # 09, 9
        "Function_10_16C6",        # 0A, 10
        "Function_11_16DE",        # 0B, 11
        "Function_12_16FD",        # 0C, 12
        "Function_13_171C",        # 0D, 13
        "Function_14_1739",        # 0E, 14
        "Function_15_1780",        # 0F, 15
        "Function_16_17A4",        # 10, 16
        "Function_17_17B8",        # 11, 17
        "Function_18_17E5",        # 12, 18
        "Function_19_182C",        # 13, 19
        "Function_20_184C",        # 14, 20
        "Function_21_188B",        # 15, 21
        "Function_22_18C1",        # 16, 22
        "Function_23_18F7",        # 17, 23
        "Function_24_192C",        # 18, 24
    ))


    def Function_0_4C4(): pass

    label("Function_0_4C4")

    SetChrPos(0x0, 0, 0, 0, 0)
    Return()

    # Function_0_4C4 end

    def Function_1_4D6(): pass

    label("Function_1_4D6")

    Return()

    # Function_1_4D6 end

    def Function_2_4D7(): pass

    label("Function_2_4D7")

    TalkBegin(0xFF)

    #C0001
    ChrTalk(
        0xFE,
        "ふふふ\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_2_4D7 end

    def Function_3_4EA(): pass

    label("Function_3_4EA")

    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x0)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x11, 0x0)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1C, 0x0)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x16, 0x0)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x20, 0x8)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrFlags(0x4, 0x8)
    SetChrFlags(0x5, 0x8)
    SetChrFlags(0x6, 0x8)
    SetChrFlags(0x7, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0x1C, 0x8)
    SetChrFlags(0x1D, 0x8)
    SetChrFlags(0x1E, 0x8)
    SetChrFlags(0x1F, 0x8)
    OP_49()
    Return()

    # Function_3_4EA end

    def Function_4_651(): pass

    label("Function_4_651")

    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x8)
    ClearChrFlags(0x1C, 0x8)
    ClearChrFlags(0x1D, 0x8)
    ClearChrFlags(0x1E, 0x8)
    ClearChrFlags(0x1F, 0x8)
    ClearChrFlags(0x20, 0x8)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    Return()

    # Function_4_651 end

    def Function_5_6F7(): pass

    label("Function_5_6F7")

    TalkBegin(0x20)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ch00000 - ch00300\x01",      # 0
            "ch00400 - ch00700\x01",      # 1
            "ch00800 - ch01100\x01",      # 2
            "ch02000 - ch02300\x01",      # 3
            "ch02400 - ch02700\x01",      # 4
            "ch02800 - ch03100\x01",      # 5
            "ch03200 - ch03500\x01",      # 6
            "キャンセル\x01",             # 7
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B0")
    Call(0, 3)
    Jump("loc_7B1")

    label("loc_7B0")

    Return()

    label("loc_7B1")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7EB"),
        (1, "loc_A18"),
        (2, "loc_BDF"),
        (3, "loc_D6A"),
        (4, "loc_F31"),
        (5, "loc_10F8"),
        (6, "loc_12AD"),
        (7, "loc_14DA"),
        (SWITCH_DEFAULT, "loc_1647"),
    )


    label("loc_7EB")

    LoadChrToIndex("chr/ch00050.itc", 0x0)
    LoadChrToIndex("chr/ch00051.itc", 0x1)
    LoadChrToIndex("chr/ch00052.itc", 0x2)
    LoadChrToIndex("chr/ch00053.itc", 0x3)
    LoadChrToIndex("chr/ch00054.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    OP_8E(0x8, "CH00050")
    OP_8E(0x9, "CH00051")
    OP_8E(0xA, "CH00052")
    OP_8E(0xB, "CH00053")
    OP_8E(0xC, "CH00054")
    OP_8E(0xD, "CH00055")
    BeginChrThread(0x8, 0, 0, 11)
    BeginChrThread(0x9, 0, 0, 12)
    BeginChrThread(0xA, 0, 0, 6)
    BeginChrThread(0xB, 0, 0, 13)
    BeginChrThread(0xC, 0, 0, 14)
    BeginChrThread(0xD, 0, 0, 6)
    LoadChrToIndex("chr/ch00150.itc", 0xA)
    LoadChrToIndex("chr/ch00151.itc", 0xB)
    LoadChrToIndex("chr/ch00152.itc", 0xC)
    LoadChrToIndex("chr/ch00153.itc", 0xD)
    LoadChrToIndex("chr/ch00154.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    OP_8E(0xE, "CH00150")
    OP_8E(0xF, "CH00151")
    OP_8E(0x10, "CH00152")
    OP_8E(0x11, "CH00153")
    OP_8E(0x12, "CH00154")
    OP_8E(0x13, "CH00155")
    BeginChrThread(0xE, 0, 0, 11)
    BeginChrThread(0xF, 0, 0, 12)
    BeginChrThread(0x10, 0, 0, 7)
    BeginChrThread(0x11, 0, 0, 13)
    BeginChrThread(0x12, 0, 0, 14)
    BeginChrThread(0x13, 0, 0, 6)
    LoadChrToIndex("chr/ch00250.itc", 0x14)
    LoadChrToIndex("chr/ch00251.itc", 0x15)
    LoadChrToIndex("chr/ch00252.itc", 0x16)
    LoadChrToIndex("chr/ch00253.itc", 0x17)
    LoadChrToIndex("chr/ch00254.itc", 0x18)
    LoadChrToIndex("chr/ch40018.itc", 0x19)
    OP_8E(0x14, "CH00250")
    OP_8E(0x15, "CH00251")
    OP_8E(0x16, "CH00252")
    OP_8E(0x17, "CH00253")
    OP_8E(0x18, "CH00254")
    OP_8E(0x19, "CH00255")
    BeginChrThread(0x14, 0, 0, 11)
    BeginChrThread(0x15, 0, 0, 12)
    BeginChrThread(0x16, 0, 0, 8)
    BeginChrThread(0x17, 0, 0, 13)
    BeginChrThread(0x18, 0, 0, 14)
    BeginChrThread(0x19, 0, 0, 6)
    LoadChrToIndex("chr/ch00350.itc", 0x1E)
    LoadChrToIndex("chr/ch00351.itc", 0x1F)
    LoadChrToIndex("chr/ch00352.itc", 0x20)
    LoadChrToIndex("chr/ch00353.itc", 0x21)
    LoadChrToIndex("chr/ch00354.itc", 0x22)
    LoadChrToIndex("chr/ch00355.itc", 0x23)
    OP_8E(0x1A, "CH00350")
    OP_8E(0x1B, "CH00351")
    OP_8E(0x1C, "CH00352")
    OP_8E(0x1D, "CH00353")
    OP_8E(0x1E, "CH00354")
    OP_8E(0x1F, "CH00355")
    BeginChrThread(0x1A, 0, 0, 11)
    BeginChrThread(0x1B, 0, 0, 12)
    BeginChrThread(0x1C, 0, 0, 15)
    BeginChrThread(0x1D, 0, 0, 13)
    BeginChrThread(0x1E, 0, 0, 14)
    BeginChrThread(0x1F, 0, 0, 16)
    Jump("loc_1647")

    label("loc_A18")

    LoadChrToIndex("chr/ch40018.itc", 0x0)
    LoadChrToIndex("chr/ch40018.itc", 0x1)
    LoadChrToIndex("chr/ch40018.itc", 0x2)
    LoadChrToIndex("chr/ch40018.itc", 0x3)
    LoadChrToIndex("chr/ch40018.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    LoadChrToIndex("chr/ch00550.itc", 0xA)
    LoadChrToIndex("chr/ch00551.itc", 0xB)
    LoadChrToIndex("chr/ch00552.itc", 0xC)
    LoadChrToIndex("chr/ch00553.itc", 0xD)
    LoadChrToIndex("chr/ch00554.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    OP_8E(0xE, "CH00550")
    OP_8E(0xF, "CH00551")
    OP_8E(0x10, "CH00552")
    OP_8E(0x11, "CH00553")
    OP_8E(0x12, "CH00554")
    OP_8E(0x13, "CH00555")
    BeginChrThread(0xE, 0, 0, 11)
    BeginChrThread(0xF, 0, 0, 12)
    BeginChrThread(0x10, 0, 0, 8)
    BeginChrThread(0x11, 0, 0, 13)
    BeginChrThread(0x12, 0, 0, 14)
    BeginChrThread(0x13, 0, 0, 6)
    LoadChrToIndex("chr/ch00650.itc", 0x14)
    LoadChrToIndex("chr/ch00651.itc", 0x15)
    LoadChrToIndex("chr/ch00652.itc", 0x16)
    LoadChrToIndex("chr/ch00653.itc", 0x17)
    LoadChrToIndex("chr/ch00654.itc", 0x18)
    LoadChrToIndex("chr/ch00655.itc", 0x19)
    OP_8E(0x14, "CH00650")
    OP_8E(0x15, "CH00651")
    OP_8E(0x16, "CH00652")
    OP_8E(0x17, "CH00653")
    OP_8E(0x18, "CH00654")
    OP_8E(0x19, "CH00655")
    BeginChrThread(0x14, 0, 0, 11)
    BeginChrThread(0x15, 0, 0, 12)
    BeginChrThread(0x16, 0, 0, 7)
    BeginChrThread(0x17, 0, 0, 13)
    BeginChrThread(0x18, 0, 0, 14)
    BeginChrThread(0x19, 0, 0, 6)
    LoadChrToIndex("chr/ch00750.itc", 0x1E)
    LoadChrToIndex("chr/ch00751.itc", 0x1F)
    LoadChrToIndex("chr/ch00752.itc", 0x20)
    LoadChrToIndex("chr/ch00753.itc", 0x21)
    LoadChrToIndex("chr/ch00754.itc", 0x22)
    LoadChrToIndex("chr/ch00755.itc", 0x23)
    OP_8E(0x1A, "CH00750")
    OP_8E(0x1B, "CH00751")
    OP_8E(0x1C, "CH00752")
    OP_8E(0x1D, "CH00753")
    OP_8E(0x1E, "CH00754")
    OP_8E(0x1F, "CH00755")
    BeginChrThread(0x1A, 0, 0, 11)
    BeginChrThread(0x1B, 0, 0, 12)
    BeginChrThread(0x1C, 0, 0, 7)
    BeginChrThread(0x1D, 0, 0, 13)
    BeginChrThread(0x1E, 0, 0, 14)
    BeginChrThread(0x1F, 0, 0, 6)
    Jump("loc_1647")

    label("loc_BDF")

    LoadChrToIndex("chr/ch40018.itc", 0x0)
    LoadChrToIndex("chr/ch40018.itc", 0x1)
    LoadChrToIndex("chr/ch40018.itc", 0x2)
    LoadChrToIndex("chr/ch40018.itc", 0x3)
    LoadChrToIndex("chr/ch40018.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    LoadChrToIndex("chr/ch00950.itc", 0xA)
    LoadChrToIndex("chr/ch00951.itc", 0xB)
    LoadChrToIndex("chr/ch00952.itc", 0xC)
    LoadChrToIndex("chr/ch00953.itc", 0xD)
    LoadChrToIndex("chr/ch00954.itc", 0xE)
    LoadChrToIndex("chr/ch00955.itc", 0xF)
    OP_8E(0xE, "CH00950")
    OP_8E(0xF, "CH00951")
    OP_8E(0x10, "CH00952")
    OP_8E(0x11, "CH00953")
    OP_8E(0x12, "CH00954")
    OP_8E(0x13, "CH00955")
    BeginChrThread(0xE, 0, 0, 11)
    BeginChrThread(0xF, 0, 0, 12)
    BeginChrThread(0x10, 0, 0, 19)
    BeginChrThread(0x11, 0, 0, 13)
    BeginChrThread(0x12, 0, 0, 14)
    BeginChrThread(0x13, 0, 0, 20)
    LoadChrToIndex("chr/ch30800.itc", 0x14)
    LoadChrToIndex("chr/ch40018.itc", 0x15)
    LoadChrToIndex("chr/ch40018.itc", 0x16)
    LoadChrToIndex("chr/ch40018.itc", 0x17)
    LoadChrToIndex("chr/ch40018.itc", 0x18)
    LoadChrToIndex("chr/ch40018.itc", 0x19)
    OP_8E(0x14, "CH30850")
    OP_8E(0x15, "CH30851")
    OP_8E(0x16, "CH30852")
    OP_8E(0x17, "CH30853")
    OP_8E(0x18, "CH30854")
    OP_8E(0x19, "CH30855")
    BeginChrThread(0x14, 0, 0, 11)
    LoadChrToIndex("chr/ch30900.itc", 0x1E)
    LoadChrToIndex("chr/ch40018.itc", 0x1F)
    LoadChrToIndex("chr/ch40018.itc", 0x20)
    LoadChrToIndex("chr/ch40018.itc", 0x21)
    LoadChrToIndex("chr/ch40018.itc", 0x22)
    LoadChrToIndex("chr/ch40018.itc", 0x23)
    OP_8E(0x1A, "CH30950")
    OP_8E(0x1B, "CH30951")
    OP_8E(0x1C, "CH30952")
    OP_8E(0x1D, "CH30953")
    OP_8E(0x1E, "CH30954")
    OP_8E(0x1F, "CH30955")
    BeginChrThread(0x1A, 0, 0, 11)
    Jump("loc_1647")

    label("loc_D6A")

    LoadChrToIndex("chr/ch40018.itc", 0x0)
    LoadChrToIndex("chr/ch40018.itc", 0x1)
    LoadChrToIndex("chr/ch40018.itc", 0x2)
    LoadChrToIndex("chr/ch40018.itc", 0x3)
    LoadChrToIndex("chr/ch40018.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    LoadChrToIndex("chr/ch02100.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    OP_8E(0xE, "CH02150")
    OP_8E(0xF, "CH02151")
    OP_8E(0x10, "CH02152")
    OP_8E(0x11, "CH02153")
    OP_8E(0x12, "CH02154")
    OP_8E(0x13, "CH02155")
    BeginChrThread(0xE, 0, 0, 11)
    BeginChrThread(0xF, 0, 0, 11)
    BeginChrThread(0x10, 0, 0, 11)
    BeginChrThread(0x11, 0, 0, 11)
    BeginChrThread(0x12, 0, 0, 11)
    BeginChrThread(0x13, 0, 0, 6)
    LoadChrToIndex("chr/ch40018.itc", 0x14)
    LoadChrToIndex("chr/ch40018.itc", 0x15)
    LoadChrToIndex("chr/ch40018.itc", 0x16)
    LoadChrToIndex("chr/ch40018.itc", 0x17)
    LoadChrToIndex("chr/ch40018.itc", 0x18)
    LoadChrToIndex("chr/ch40018.itc", 0x19)
    OP_8E(0x14, "CH02250")
    OP_8E(0x15, "CH02251")
    OP_8E(0x16, "CH02252")
    OP_8E(0x17, "CH02253")
    OP_8E(0x18, "CH02254")
    OP_8E(0x19, "CH02255")
    BeginChrThread(0x14, 0, 0, 11)
    BeginChrThread(0x15, 0, 0, 11)
    BeginChrThread(0x16, 0, 0, 11)
    BeginChrThread(0x17, 0, 0, 11)
    BeginChrThread(0x18, 0, 0, 11)
    BeginChrThread(0x19, 0, 0, 6)
    LoadChrToIndex("chr/ch02300.itc", 0x1E)
    LoadChrToIndex("chr/ch40018.itc", 0x1F)
    LoadChrToIndex("chr/ch40018.itc", 0x20)
    LoadChrToIndex("chr/ch40018.itc", 0x21)
    LoadChrToIndex("chr/ch40018.itc", 0x22)
    LoadChrToIndex("chr/ch40018.itc", 0x23)
    OP_8E(0x1A, "CH02350")
    OP_8E(0x1B, "CH02351")
    OP_8E(0x1C, "CH02352")
    OP_8E(0x1D, "CH02353")
    OP_8E(0x1E, "CH02354")
    OP_8E(0x1F, "CH02355")
    BeginChrThread(0x1A, 0, 0, 11)
    BeginChrThread(0x1B, 0, 0, 11)
    BeginChrThread(0x1C, 0, 0, 11)
    BeginChrThread(0x1D, 0, 0, 11)
    BeginChrThread(0x1E, 0, 0, 11)
    BeginChrThread(0x1F, 0, 0, 6)
    Jump("loc_1647")

    label("loc_F31")

    LoadChrToIndex("chr/ch02450.itc", 0x0)
    LoadChrToIndex("chr/ch02451.itc", 0x1)
    LoadChrToIndex("chr/ch02452.itc", 0x2)
    LoadChrToIndex("chr/ch02453.itc", 0x3)
    LoadChrToIndex("chr/ch02454.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    OP_8E(0x8, "CH02450")
    OP_8E(0x9, "CH02451")
    OP_8E(0xA, "CH02452")
    OP_8E(0xB, "CH02453")
    OP_8E(0xC, "CH02454")
    OP_8E(0xD, "CH02450")
    BeginChrThread(0x8, 0, 0, 11)
    BeginChrThread(0x9, 0, 0, 11)
    BeginChrThread(0xA, 0, 0, 11)
    BeginChrThread(0xB, 0, 0, 13)
    BeginChrThread(0xC, 0, 0, 14)
    BeginChrThread(0xD, 0, 0, 6)
    LoadChrToIndex("chr/ch02500.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    OP_8E(0xE, "CH02500")
    OP_8E(0xF, "CH02500")
    OP_8E(0x10, "CH02500")
    OP_8E(0x11, "CH02500")
    OP_8E(0x12, "CH02500")
    OP_8E(0x13, "CH02500")
    BeginChrThread(0xE, 0, 0, 11)
    BeginChrThread(0xF, 0, 0, 11)
    BeginChrThread(0x10, 0, 0, 11)
    BeginChrThread(0x11, 0, 0, 13)
    BeginChrThread(0x12, 0, 0, 11)
    BeginChrThread(0x13, 0, 0, 6)
    LoadChrToIndex("chr/ch40018.itc", 0x14)
    LoadChrToIndex("chr/ch40018.itc", 0x15)
    LoadChrToIndex("chr/ch40018.itc", 0x16)
    LoadChrToIndex("chr/ch40018.itc", 0x17)
    LoadChrToIndex("chr/ch40018.itc", 0x18)
    LoadChrToIndex("chr/ch40018.itc", 0x19)
    LoadChrToIndex("chr/ch02750.itc", 0x1E)
    LoadChrToIndex("chr/ch02751.itc", 0x1F)
    LoadChrToIndex("chr/ch02752.itc", 0x20)
    LoadChrToIndex("chr/ch40018.itc", 0x21)
    LoadChrToIndex("chr/ch40018.itc", 0x22)
    LoadChrToIndex("chr/ch40018.itc", 0x23)
    OP_8E(0x1A, "CH02750")
    OP_8E(0x1B, "CH02750")
    OP_8E(0x1C, "CH02750")
    OP_8E(0x1D, "CH02750")
    OP_8E(0x1E, "CH02750")
    OP_8E(0x1F, "CH02750")
    BeginChrThread(0x1A, 0, 0, 11)
    BeginChrThread(0x1B, 0, 0, 11)
    BeginChrThread(0x1C, 0, 0, 11)
    BeginChrThread(0x1D, 0, 0, 11)
    BeginChrThread(0x1E, 0, 0, 11)
    BeginChrThread(0x1F, 0, 0, 6)
    Jump("loc_1647")

    label("loc_10F8")

    LoadChrToIndex("chr/ch40018.itc", 0x0)
    LoadChrToIndex("chr/ch40018.itc", 0x1)
    LoadChrToIndex("chr/ch40018.itc", 0x2)
    LoadChrToIndex("chr/ch40018.itc", 0x3)
    LoadChrToIndex("chr/ch40018.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    LoadChrToIndex("chr/ch02950.itc", 0xA)
    LoadChrToIndex("chr/ch02951.itc", 0xB)
    LoadChrToIndex("chr/ch02952.itc", 0xC)
    LoadChrToIndex("chr/ch02953.itc", 0xD)
    LoadChrToIndex("chr/ch02954.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    OP_8E(0xE, "CH02950")
    OP_8E(0xF, "CH02951")
    OP_8E(0x10, "CH02952")
    OP_8E(0x11, "CH02953")
    OP_8E(0x12, "CH02954")
    OP_8E(0x13, "CH40018")
    BeginChrThread(0xE, 0, 0, 11)
    BeginChrThread(0xF, 0, 0, 12)
    BeginChrThread(0x10, 0, 0, 17)
    LoadChrToIndex("chr/ch03050.itc", 0x14)
    LoadChrToIndex("chr/ch03051.itc", 0x15)
    LoadChrToIndex("chr/ch03052.itc", 0x16)
    LoadChrToIndex("chr/ch03053.itc", 0x17)
    LoadChrToIndex("chr/ch03054.itc", 0x18)
    LoadChrToIndex("chr/ch40018.itc", 0x19)
    OP_8E(0x14, "CH03050")
    OP_8E(0x15, "CH03051")
    OP_8E(0x16, "CH03052")
    OP_8E(0x17, "CH03053")
    OP_8E(0x18, "CH03054")
    OP_8E(0x19, "CH40018")
    BeginChrThread(0x14, 0, 0, 11)
    BeginChrThread(0x15, 0, 0, 12)
    BeginChrThread(0x16, 0, 0, 8)
    BeginChrThread(0x17, 0, 0, 13)
    BeginChrThread(0x18, 0, 0, 11)
    BeginChrThread(0x19, 0, 0, 6)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("chr/ch40018.itc", 0x1F)
    LoadChrToIndex("chr/ch40018.itc", 0x20)
    LoadChrToIndex("chr/ch40018.itc", 0x21)
    LoadChrToIndex("chr/ch40018.itc", 0x22)
    LoadChrToIndex("chr/ch40018.itc", 0x23)
    OP_8E(0x1A, "CH03100")
    OP_8E(0x1B, "CH03100")
    OP_8E(0x1C, "CH03100")
    OP_8E(0x1D, "CH03100")
    OP_8E(0x1E, "CH03100")
    OP_8E(0x1F, "CH03100")
    BeginChrThread(0x1A, 0, 0, 11)
    BeginChrThread(0x1B, 0, 0, 12)
    BeginChrThread(0x1C, 0, 0, 11)
    BeginChrThread(0x1D, 0, 0, 13)
    BeginChrThread(0x1E, 0, 0, 14)
    BeginChrThread(0x1F, 0, 0, 6)
    Jump("loc_1647")

    label("loc_12AD")

    LoadChrToIndex("chr/ch03200.itc", 0x0)
    LoadChrToIndex("chr/ch40018.itc", 0x1)
    LoadChrToIndex("chr/ch40018.itc", 0x2)
    LoadChrToIndex("chr/ch40018.itc", 0x3)
    LoadChrToIndex("chr/ch40018.itc", 0x4)
    LoadChrToIndex("chr/ch40018.itc", 0x5)
    OP_8E(0x8, "CH03250")
    OP_8E(0x9, "CH03251")
    OP_8E(0xA, "CH03252")
    OP_8E(0xB, "CH03253")
    OP_8E(0xC, "CH03254")
    OP_8E(0xD, "CH03200")
    BeginChrThread(0x8, 0, 0, 11)
    BeginChrThread(0x9, 0, 0, 12)
    BeginChrThread(0xA, 0, 0, 11)
    BeginChrThread(0xB, 0, 0, 13)
    BeginChrThread(0xC, 0, 0, 14)
    BeginChrThread(0xD, 0, 0, 6)
    LoadChrToIndex("chr/ch03300.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    OP_8E(0xE, "CH03350")
    OP_8E(0xF, "CH03351")
    OP_8E(0x10, "CH03352")
    OP_8E(0x11, "CH03353")
    OP_8E(0x12, "CH03354")
    OP_8E(0x13, "CH40018")
    BeginChrThread(0xE, 0, 0, 11)
    BeginChrThread(0xF, 0, 0, 12)
    BeginChrThread(0x10, 0, 0, 11)
    BeginChrThread(0x11, 0, 0, 13)
    BeginChrThread(0x12, 0, 0, 14)
    BeginChrThread(0x13, 0, 0, 6)
    LoadChrToIndex("chr/ch03400.itc", 0x14)
    LoadChrToIndex("chr/ch40018.itc", 0x15)
    LoadChrToIndex("chr/ch40018.itc", 0x16)
    LoadChrToIndex("chr/ch40018.itc", 0x17)
    LoadChrToIndex("chr/ch40018.itc", 0x18)
    LoadChrToIndex("chr/ch40018.itc", 0x19)
    OP_8E(0x14, "CH03450")
    OP_8E(0x15, "CH03451")
    OP_8E(0x16, "CH03452")
    OP_8E(0x17, "CH03453")
    OP_8E(0x18, "CH03454")
    OP_8E(0x19, "CH40018")
    BeginChrThread(0x14, 0, 0, 11)
    BeginChrThread(0x15, 0, 0, 12)
    BeginChrThread(0x16, 0, 0, 7)
    BeginChrThread(0x17, 0, 0, 13)
    BeginChrThread(0x18, 0, 0, 14)
    BeginChrThread(0x19, 0, 0, 6)
    LoadChrToIndex("chr/ch03500.itc", 0x1E)
    LoadChrToIndex("chr/ch40018.itc", 0x1F)
    LoadChrToIndex("chr/ch40018.itc", 0x20)
    LoadChrToIndex("chr/ch40018.itc", 0x21)
    LoadChrToIndex("chr/ch40018.itc", 0x22)
    LoadChrToIndex("chr/ch40018.itc", 0x23)
    OP_8E(0x1A, "CH03550")
    OP_8E(0x1B, "CH03551")
    OP_8E(0x1C, "CH03552")
    OP_8E(0x1D, "CH03553")
    OP_8E(0x1E, "CH03554")
    OP_8E(0x1F, "CH03550")
    BeginChrThread(0x1A, 0, 0, 11)
    BeginChrThread(0x1B, 0, 0, 12)
    BeginChrThread(0x1C, 0, 0, 11)
    BeginChrThread(0x1D, 0, 0, 13)
    BeginChrThread(0x1E, 0, 0, 14)
    BeginChrThread(0x1F, 0, 0, 6)
    Jump("loc_1647")

    label("loc_14DA")

    LoadChrToIndex("chr/ch40000.itc", 0x0)
    LoadChrToIndex("chr/ch40000.itc", 0x1)
    LoadChrToIndex("chr/ch40000.itc", 0x2)
    LoadChrToIndex("chr/ch40000.itc", 0x3)
    LoadChrToIndex("chr/ch40000.itc", 0x4)
    LoadChrToIndex("chr/ch40000.itc", 0x5)
    LoadChrToIndex("chr/ch40000.itc", 0x6)
    LoadChrToIndex("chr/ch40000.itc", 0x7)
    LoadChrToIndex("chr/ch40000.itc", 0x8)
    LoadChrToIndex("chr/ch40000.itc", 0x9)
    LoadChrToIndex("chr/ch40000.itc", 0xA)
    LoadChrToIndex("chr/ch40000.itc", 0xB)
    LoadChrToIndex("chr/ch40000.itc", 0xC)
    LoadChrToIndex("chr/ch40000.itc", 0xD)
    LoadChrToIndex("chr/ch40000.itc", 0xE)
    LoadChrToIndex("chr/ch40000.itc", 0xF)
    LoadChrToIndex("chr/ch40000.itc", 0x10)
    LoadChrToIndex("chr/ch40000.itc", 0x11)
    LoadChrToIndex("chr/ch40000.itc", 0x12)
    LoadChrToIndex("chr/ch40000.itc", 0x13)
    LoadChrToIndex("chr/ch40000.itc", 0x14)
    LoadChrToIndex("chr/ch40000.itc", 0x15)
    LoadChrToIndex("chr/ch40000.itc", 0x16)
    LoadChrToIndex("chr/ch40000.itc", 0x17)
    LoadChrToIndex("chr/ch40000.itc", 0x18)
    LoadChrToIndex("chr/ch40000.itc", 0x19)
    LoadChrToIndex("chr/ch40000.itc", 0x1A)
    LoadChrToIndex("chr/ch40000.itc", 0x1B)
    LoadChrToIndex("chr/ch40000.itc", 0x1C)
    LoadChrToIndex("chr/ch40000.itc", 0x1D)
    LoadChrToIndex("chr/ch40000.itc", 0x1E)
    LoadChrToIndex("chr/ch40000.itc", 0x1F)
    LoadChrToIndex("chr/ch40000.itc", 0x20)
    LoadChrToIndex("chr/ch40000.itc", 0x21)
    LoadChrToIndex("chr/ch40000.itc", 0x22)
    LoadChrToIndex("chr/ch40000.itc", 0x23)
    LoadChrToIndex("chr/ch40000.itc", 0x24)
    LoadChrToIndex("chr/ch40000.itc", 0x25)
    LoadChrToIndex("chr/ch40000.itc", 0x26)
    LoadChrToIndex("chr/ch40000.itc", 0x27)
    LoadChrToIndex("chr/ch40000.itc", 0x28)
    LoadChrToIndex("chr/ch40000.itc", 0x29)
    LoadChrToIndex("chr/ch40000.itc", 0x2A)
    LoadChrToIndex("chr/ch40000.itc", 0x2B)
    LoadChrToIndex("chr/ch40000.itc", 0x2C)
    LoadChrToIndex("chr/ch40000.itc", 0x2D)
    LoadChrToIndex("chr/ch40000.itc", 0x2E)
    LoadChrToIndex("chr/ch40000.itc", 0x2F)
    LoadChrToIndex("chr/ch40000.itc", 0x30)
    LoadChrToIndex("chr/ch40000.itc", 0x31)
    LoadChrToIndex("chr/ch40000.itc", 0x32)
    LoadChrToIndex("chr/ch40000.itc", 0x33)
    LoadChrToIndex("chr/ch40000.itc", 0x34)
    LoadChrToIndex("chr/ch40000.itc", 0x35)
    LoadChrToIndex("chr/ch40000.itc", 0x36)
    LoadChrToIndex("chr/ch40000.itc", 0x37)
    LoadChrToIndex("chr/ch40000.itc", 0x38)
    LoadChrToIndex("chr/ch40000.itc", 0x39)
    LoadChrToIndex("chr/ch40000.itc", 0x3A)
    LoadChrToIndex("chr/ch40000.itc", 0x3B)
    Jump("loc_1647")

    label("loc_1647")

    LoadChrToIndex("chr/ch40018.itc", 0x3D)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_165F")
    Call(0, 4)

    label("loc_165F")

    OP_60(0x0)
    TalkEnd(0x20)
    Return()

    # Function_5_6F7 end

    def Function_6_1666(): pass

    label("Function_6_1666")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_167D")
    OP_A0(0xFE, 1500, 0x0, 0x2)
    Jump("Function_6_1666")

    label("loc_167D")

    Return()

    # Function_6_1666 end

    def Function_7_167E(): pass

    label("Function_7_167E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1695")
    OP_A0(0xFE, 1500, 0x0, 0x4)
    Jump("Function_7_167E")

    label("loc_1695")

    Return()

    # Function_7_167E end

    def Function_8_1696(): pass

    label("Function_8_1696")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16AD")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("Function_8_1696")

    label("loc_16AD")

    Return()

    # Function_8_1696 end

    def Function_9_16AE(): pass

    label("Function_9_16AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16C5")
    OP_A0(0xFE, 1500, 0x0, 0x6)
    Jump("Function_9_16AE")

    label("loc_16C5")

    Return()

    # Function_9_16AE end

    def Function_10_16C6(): pass

    label("Function_10_16C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16DD")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("Function_10_16C6")

    label("loc_16DD")

    Return()

    # Function_10_16C6 end

    def Function_11_16DE(): pass

    label("Function_11_16DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16FC")
    OP_A1(0xFE, 0x4B0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_11_16DE")

    label("loc_16FC")

    Return()

    # Function_11_16DE end

    def Function_12_16FD(): pass

    label("Function_12_16FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_171B")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_12_16FD")

    label("loc_171B")

    Return()

    # Function_12_16FD end

    def Function_13_171C(): pass

    label("Function_13_171C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1738")
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Sleep(1000)
    Jump("Function_13_171C")

    label("loc_1738")

    Return()

    # Function_13_171C end

    def Function_14_1739(): pass

    label("Function_14_1739")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_177F")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x4)
    Sleep(1000)
    Jump("Function_14_1739")

    label("loc_177F")

    Return()

    # Function_14_1739 end

    def Function_15_1780(): pass

    label("Function_15_1780")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17A3")
    SetChrChipByIndex(0xFE, 0x20)
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("Function_15_1780")

    label("loc_17A3")

    Return()

    # Function_15_1780 end

    def Function_16_17A4(): pass

    label("Function_16_17A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17B7")
    Sleep(1000)
    Jump("Function_16_17A4")

    label("loc_17B7")

    Return()

    # Function_16_17A4 end

    def Function_17_17B8(): pass

    label("Function_17_17B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17E4")
    Sleep(500)
    OP_A1(0xFE, 0x6A4, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    OP_A1(0xFE, 0x6A4, 0x4, 0x4, 0x5, 0x4, 0x5)
    Sleep(500)
    Jump("Function_17_17B8")

    label("loc_17E4")

    Return()

    # Function_17_17B8 end

    def Function_18_17E5(): pass

    label("Function_18_17E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_182B")
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x5)
    OP_A1(0xFE, 0x640, 0x8, 0x0, 0x1, 0x2, 0x3, 0x3, 0x4, 0x5, 0x6)
    OP_A1(0xFE, 0x640, 0x8, 0x7, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD)
    OP_A1(0xFE, 0x640, 0x2, 0xC, 0xB)
    Sleep(1000)
    Jump("Function_18_17E5")

    label("loc_182B")

    Return()

    # Function_18_17E5 end

    def Function_19_182C(): pass

    label("Function_19_182C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_184B")
    OP_A1(0xFE, 0x708, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x0)
    Sleep(1000)
    Jump("Function_19_182C")

    label("loc_184B")

    Return()

    # Function_19_182C end

    def Function_20_184C(): pass

    label("Function_20_184C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_188A")
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xF)
    OP_A1(0xFE, 0x708, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    OP_A1(0xFE, 0x708, 0x8, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF)
    Sleep(1000)
    Jump("Function_20_184C")

    label("loc_188A")

    Return()

    # Function_20_184C end

    def Function_21_188B(): pass

    label("Function_21_188B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18C0")
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0xC)
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x2, 0x2, 0x3)
    OP_A1(0xFE, 0x960, 0x4, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_21_188B")

    label("loc_18C0")

    Return()

    # Function_21_188B end

    def Function_22_18C1(): pass

    label("Function_22_18C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18F6")
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x4)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x16)
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x2, 0x2, 0x3)
    OP_A1(0xFE, 0x960, 0x4, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_22_18C1")

    label("loc_18F6")

    Return()

    # Function_22_18C1 end

    def Function_23_18F7(): pass

    label("Function_23_18F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_192B")
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x16)
    OP_A1(0xFE, 0x960, 0x5, 0x0, 0x1, 0x2, 0x2, 0x3)
    OP_A1(0xFE, 0x960, 0x4, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_23_18F7")

    label("loc_192B")

    Return()

    # Function_23_18F7 end

    def Function_24_192C(): pass

    label("Function_24_192C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1961")
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x2, 0x2, 0x3)
    OP_A1(0xFE, 0x960, 0x4, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_24_192C")

    label("loc_1961")

    Return()

    # Function_24_192C end

    SaveToFile()

Try(main)
