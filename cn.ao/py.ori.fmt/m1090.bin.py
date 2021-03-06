﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m1090.bin",                # FileName
        "m1090",                    # MapName
        "m1090",                    # Location
        0x0072,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 114, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1090",                  # 0
        "阿瑞安赫德",             # 1
        "持剑少女贞德 ",          # 2
        "长枪",                   # 3
        "阿瑞安赫德",             # 4
        "琪雅",                   # 5
        "SE控制",                 # 6
        "bm1070",                 # 7
    ))

    ATBonus("ATBonus_1CC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_28C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_26C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_270", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_274", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_278", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_27C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_280", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_284", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2AC", 0x0052, 255, 6, 45, 3, 3, 30, 0, "bm1070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms03500.dat", 0, 0, 0, 0, 0, "ms04200.dat", 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_26C", "ed7458", "ed7453", "ATBonus_1CC"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 5,   -14.5,                 5.5,                   -1.0,                  306.25,                [0.10101521760225296,  0.1414213925600052,    -0.0,                  0.0,                   -0.10101528465747833,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   2.0203046798706055,    1.2727930545806885,    0.19999998807907104,   1.0])

    ChipFrameInfo(812, 0)                                        # 0

    ScpFunction((
        "Function_0_32C",          # 00, 0
        "Function_1_356",          # 01, 1
        "Function_2_57A",          # 02, 2
        "Function_3_789",          # 03, 3
        "Function_4_7AE",          # 04, 4
        "Function_5_7D3",          # 05, 5
        "Function_6_1ADA",         # 06, 6
        "Function_7_1AF9",         # 07, 7
        "Function_8_1C33",         # 08, 8
        "Function_9_1CC5",         # 09, 9
        "Function_10_1CEA",        # 0A, 10
        "Function_11_1D23",        # 0B, 11
        "Function_12_1D3D",        # 0C, 12
        "Function_13_4A25",        # 0D, 13
        "Function_14_4A4C",        # 0E, 14
    ))


    def Function_0_32C(): pass

    label("Function_0_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_343")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 2)
    Jump("loc_355")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_355")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 12)

    label("loc_355")

    Return()

    # Function_0_32C end

    def Function_1_356(): pass

    label("Function_1_356")

    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C3")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    Jump("loc_4C7")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_END)), "loc_404")
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    Jump("loc_4C7")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C7")
    LoadEffect(0x9, "map/mpbell02.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x0, 0x1D, 0x0, 0x20)
    SetMapObjFrame(0x0, "bell_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cloud", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x1, 0x1)

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_END)), "loc_4DE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F5")

    label("loc_4DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_50A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_50A")

    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_53F")
    OP_24(0x84)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_561")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55B")
    OP_24(0x84)
    Sound(828, 1, 70, 0)
    Jump("loc_561")

    label("loc_55B")

    Sound(132, 1, 70, 0)

    label("loc_561")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_579")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_579")

    Return()

    # Function_1_356 end

    def Function_2_57A(): pass

    label("Function_2_57A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03500.itc", 0x1E)
    LoadChrToIndex("chr/ch43100.itc", 0x1F)
    LoadEffect(0x0, "battle/cr037100.eff")
    LoadEffect(0x1, "map/mpbell.eff")
    SoundLoad(828)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, -5740, 1190, 40, 90)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -6360, 1090, -1240, 45)
    SetChrFlags(0x9, 0x4)
    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    Sound(828, 2, 100, 0)
    StopEffect(0x7, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    OP_68(-3620, 3240, 10, 0)
    MoveCamera(90, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(33000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 3450, 0, 7000)
    MoveCamera(60, 15, 0, 7000)
    SetCameraDistance(21000, 7000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    SetCameraDistance(28000, 10000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x19)
    Sleep(1)
    CancelBlur(4000)
    Sound(929, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 3)
    SetMapObjFrame(0x0, "bell_add", 0x1, 0x1)
    OP_71(0x0, 0x0, 0x1D, 0x0, 0x20)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Sound(829, 0, 100, 0)
    Sleep(4000)
    StopSound(828, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r3080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_57A end

    def Function_3_789(): pass

    label("Function_3_789")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AD")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_3_789")

    label("loc_7AD")

    Return()

    # Function_3_789 end

    def Function_4_7AE(): pass

    label("Function_4_7AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D2")
    OP_82(0x64, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_4_7AE")

    label("loc_7D2")

    Return()

    # Function_4_7AE end

    def Function_5_7D3(): pass

    label("Function_5_7D3")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_841")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)

    label("loc_841")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85F")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)

    label("loc_85F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch03251.itc", 0x27)

    label("loc_87D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89B")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch02951.itc", 0x29)

    label("loc_89B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B9")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch03151.itc", 0x29)

    label("loc_8B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D7")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)

    label("loc_8D7")

    LoadChrToIndex("chr/ch03500.itc", 0x2A)
    LoadChrToIndex("chr/ch03550.itc", 0x2B)
    LoadChrToIndex("chr/ch03551.itc", 0x2C)
    LoadChrToIndex("chr/ch03552.itc", 0x2D)
    LoadChrToIndex("chr/ch03553.itc", 0x2E)
    LoadChrToIndex("chr/ch03554.itc", 0x2F)
    LoadChrToIndex("chr/ch03557.itc", 0x30)
    LoadChrToIndex("apl/ch51408.itc", 0x31)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04900.itp")
    CreatePortrait(1, 65296, 65408, 240, 128, 240, 136, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis286.itp")
    LoadEffect(0x0, "event\\ev17090.eff")
    LoadEffect(0x1, "event\\ev14015.eff")
    SoundLoad(3899)
    SoundLoad(3900)
    SoundLoad(3901)
    SoundLoad(3902)
    SoundLoad(3903)
    SoundLoad(3904)
    SoundLoad(3905)
    SoundLoad(3632)
    SoundLoad(3633)
    SoundLoad(825)
    SoundLoad(832)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13110, 0, 5580, 90)
    SetChrPos(0x102, -13470, 0, 4350, 90)
    SetChrPos(0x103, -13880, 0, 6630, 90)
    SetChrPos(0x104, -13680, 0, 2960, 90)
    SetChrPos(0xF4, -15080, 0, 6140, 90)
    SetChrPos(0xF5, -14780, 0, 3600, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5900, 1140, 0, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 16250, 0, -8350, 45)
    SetChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 17450, 0, -5600, 225)
    SetChrFlags(0xC, 0x8)
    OP_68(-5900, 5140, 0, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_68(-5900, 2140, 0, 8000)
    OP_6F(0x79)
    OP_0D()
    OP_68(-12700, 2420, 0, 5000)
    MoveCamera(90, 9, 0, 5000)
    OP_6E(550, 5000)
    SetCameraDistance(18150, 5000)

    def lambda_B17():
        OP_95(0xFE, -14680, 0, -2040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B17)
    Sleep(50)

    def lambda_B34():
        OP_95(0xFE, -15780, 0, -1400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_B34)
    Sleep(50)

    def lambda_B51():
        OP_95(0xFE, -14470, 0, -650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B51)
    Sleep(50)

    def lambda_B6E():
        OP_95(0xFE, -14110, 0, 580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6E)
    Sleep(50)

    def lambda_B8B():
        OP_95(0xFE, -16079, 0, 1140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_B8B)
    Sleep(50)

    def lambda_BA8():
        OP_95(0xFE, -14880, 0, 1630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BA8)
    WaitChrThread(0x104, 1)

    def lambda_BC6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BC6)
    WaitChrThread(0xF5, 1)

    def lambda_BD7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_BD7)
    WaitChrThread(0x102, 1)

    def lambda_BE8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BE8)
    WaitChrThread(0x101, 1)

    def lambda_BF9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF9)
    WaitChrThread(0xF4, 1)

    def lambda_C0A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_C0A)
    WaitChrThread(0x103, 1)

    def lambda_C1B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C1B)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF5, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)
    BeginChrThread(0xD, 1, 0, 11)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7584", 0)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0001
    AnonymousTalk(
        0x8,
        (
            "#3899V#3C#40W#20A你们来了啊。\x02\x03",

            "#3900V#35A看来你们拥有\x01",
            "坚定的意志与决心呢。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0002
    ChrTalk(
        0x102,
        "#00101F#6P#N『钢之圣女』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0003
    ChrTalk(
        0x103,
        "#00201F#6P#N『噬身之蛇』的使徒……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00003F#6P#N据『小丑』所说，\x01",
            "你们所谓的计划\x01",
            "已经转移到帝国了吧？\x02\x03",

            "#00001F你还有必要继续\x01",
            "留在克洛斯贝尔吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0005
    ChrTalk(
        0x8,
        (
            "#04900F#3C#30W是的，严格来说，并没有这个必要。\x02\x03",

            "虽然博士对『零之至宝』的潜在能力\x01",
            "表现出了浓厚的兴趣……\x02\x03",

            "但它对我们的计划\x01",
            "已经没有用处了。\x02\x03",

            "剩下的只是库罗伊斯家族\x01",
            "与你们之间的问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EE3")

    #C0006
    ChrTalk(
        0x109,
        "#10107F#6P#N既、既然如此，你为何还……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_F11")

    label("loc_EE3")


    #C0007
    ChrTalk(
        0x106,
        "#10701F#6P#N既然如此，你为何还要……！？\x02",
    )

    CloseMessageWindow()

    label("loc_F11")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F76")

    #C0008
    ChrTalk(
        0x105,
        (
            "#10406F#6P#N老实说，如果你与此次事件已无牵扯，\x01",
            "我很希望你能就此抽身呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD0")

    label("loc_F76")


    #C0009
    ChrTalk(
        0x104,
        (
            "#00306F#12P#N……老实说，如果你与此次事件已经没有牵扯了，\x01",
            "我们很希望你能就此离开呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD0")

    OP_57(0x0)
    OP_5A()

    #C0010
    ChrTalk(
        0x8,
        (
            "#04900F#3C我留在此地的原因很简单。\x02\x03",

            "这是身为『至宝』的圣子\x01",
            "亲自向我提出的请求。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0011
    ChrTalk(
        0x101,
        "#00005F#6P#N什、什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0012
    ChrTalk(
        0x102,
        "#00107F#6P#N小、小琪雅提出的！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x33C, 0xA)
    OP_CB(0x1, 0x1, 0x41A, 0x41A, 0x0, 0x0)
    OP_CB(0x1, 0x1, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x1)
    Sleep(800)
    OP_68(17260, 1000, -7120, 0)
    MoveCamera(68, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #C0013
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#04924F#3901V#11P#3C#20A#40W我接受你的请求。\x02\x03",

            "#04922F#3902V#56A『盟主』吩咐过我，\x01",
            "要极力满足圣子的愿望。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #C0014
    ChrTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12304F#3632V#5P#13C#20A#40W……谢谢。\x02\x03",

            "#12302F#3633V#46A请替我向你们的盟主\x01",
            "也道声谢吧。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_68(-12700, 2420, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x1, 0x1, 0x47E, 0x47E, 0x5DC, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToBright(1500, 16777215)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x33C, 0x1E)
    Sleep(500)

    #C0015
    ChrTalk(
        0x8,
        (
            "#04900F#3C#30W『战鬼』、『剑圣』……\x01",
            "此地云集着他们\x01",
            "这样的超凡之人。\x02\x03",

            "倘若继续前进，\x01",
            "你们很难保证安然无恙。\x02\x03",

            "而她不想目睹你们受到伤害……\x01",
            "圣子就是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#00206F#30W#6P#N……琪雅……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x104,
        "#00308F#30W#12P#N阿琪说了这种话……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0018
    ChrTalk(
        0x101,
        (
            "#00006F#6P#N#30W谢谢你，『钢之圣女』。\x02\x03",

            "#00000F#20W拜你所赐，\x01",
            "我心中的迷茫似乎已经完全消散了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(500)
    SetCameraDistance(17000, 500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14BF")
    Sound(540, 0, 50, 0)

    label("loc_14BF")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    OP_6F(0x79)
    OP_0D()
    Sleep(800)

    #C0019
    ChrTalk(
        0x8,
        (
            "#04900F#3C……这样啊，听了我刚才的\x01",
            "转述之后，有了如此反应吗？\x02\x03",

            "看来那些话产生了\x01",
            "决定性的推动作用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00013F#6P#N没错，我们无论如何\x01",
            "也要将你击退。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0021
    ChrTalk(
        0x102,
        (
            "#00104F#6P#N这也是为了跨越『壁障』，\x01",
            "给那孩子一个拥抱……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0022
    ChrTalk(
        0x104,
        (
            "#00307F#12P#N如果在这里退缩，\x01",
            "那就不算男人了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0023
    ChrTalk(
        0x103,
        "#00201F#6P#N……女人也是一样。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A6")

    #C0024
    ChrTalk(
        0x105,
        (
            "#10402F#6P#N呵呵，看来你们\x01",
            "已经完全燃起斗志了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16EA")

    #C0025
    ChrTalk(
        0x106,
        (
            "#10706F#6P#N各位的心情……\x01",
            "……我深有体会。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172A")

    #C0026
    ChrTalk(
        0x109,
        (
            "#10107F#6P#N我也会……\x01",
            "全力支援大家的！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_172A")

    Sleep(500)

    #C0027
    ChrTalk(
        0x8,
        "#04900F#3C#30W呵呵……好吧。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7458", 0)
    OP_68(-5900, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(15500, 3000)
    OP_6F(0x79)
    BeginChrThread(0x8, 3, 0, 7)
    WaitChrThread(0x8, 3)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 8)
    WaitChrThread(0x8, 3)
    StopSound(828, 500, 30)
    OP_68(-12700, 2420, 0, 16000)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0028
    AnonymousTalk(
        0x8,
        (
            "#3903V#3C#30W#42A蛇之使徒第七柱，\x01",
            "『钢』之阿瑞安赫德……\x02\x03",

            "#3904V#54A遵从『零』之圣子所愿，\x01",
            "于此阻拦诸位的道路。\x02\x03",

            "#3905V#30A就在此——决一胜负吧！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 10)
    Sound(2153, 255, 90, 0)    #voice#Elie
    Sound(2343, 255, 100, 1)    #voice#Randy
    Sound(2249, 255, 100, 2)    #voice#Tio
    Sound(2055, 255, 100, 3)    #voice#Lloyd
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1934")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_192B")
    OP_FC(0x4)
    Sound(2478, 255, 100, 5)    #voice#Noel
    Jump("loc_1934")

    label("loc_192B")

    OP_FC(0x3)
    Sound(2478, 255, 100, 4)    #voice#Noel

    label("loc_1934")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1967")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1961")
    Sound(2417, 255, 100, 5)    #voice#Lazy
    Jump("loc_1967")

    label("loc_1961")

    Sound(2417, 255, 100, 4)    #voice#Lazy

    label("loc_1967")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_199A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1994")
    Sound(3174, 255, 100, 5)    #voice#Rixia
    Jump("loc_199A")

    label("loc_1994")

    Sound(3174, 255, 100, 4)    #voice#Rixia

    label("loc_199A")

    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("罗伊德等人")

    #A0029
    AnonymousTalk(
        0xFF,
        "#5S#12A噢……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 0)
    Sound(829, 0, 50, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5900, 1640, 0, 1000)

    def lambda_19FB():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19FB)

    def lambda_1A10():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A10)

    def lambda_1A25():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A25)

    def lambda_1A3A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A3A)

    def lambda_1A4F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1A4F)

    def lambda_1A64():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1A64)
    Sleep(350)
    StopSound(825, 300, 100)
    StopSound(832, 300, 100)
    FadeToDark(0, -1, 0)
    FadeToDark(650, 16777215, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xF4, 0x1)
    EndChrThread(0xF5, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x8, 0x0)
    Battle("BattleInfo_2AC", 0x0, 0x0, 0x100, 0x40, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 12)
    Return()

    # Function_5_7D3 end

    def Function_6_1ADA(): pass

    label("Function_6_1ADA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AF8")
    OP_A1(0xFE, 0x4B0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_6_1ADA")

    label("loc_1AF8")

    Return()

    # Function_6_1ADA end

    def Function_7_1AF9(): pass

    label("Function_7_1AF9")

    Fade(500)
    Sound(531, 0, 80, 0)
    Sound(358, 0, 60, 0)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x31)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    OP_0D()
    SetCameraDistance(15000, 2000)
    Sound(970, 0, 100, 0)
    Sound(920, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x1, 0x0, 0xFE, 0x5, 0, 2200, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(1)
    CancelBlur(2500)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0xF)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -5900, 3300, -150, 0)

    def lambda_1BCE():
        OP_96(0xFE, 0xFFFFE8F4, 0x866, 0xFFFFFF6A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BCE)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 70, 0)
    Sound(288, 0, 70, 0)
    SetChrFlags(0xA, 0x80)
    OP_82(0x32, 0x0, 0x1388, 0x12C)
    OP_A1(0xFE, 0x4B0, 0x3, 0x5, 0x6, 0x7)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_1AF9 end

    def Function_8_1C33(): pass

    label("Function_8_1C33")

    Fade(500)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x0, 0x1F4, 0x1388, 0x1F4)
    Sound(825, 2, 100, 0)
    Sound(832, 2, 100, 0)
    Sound(881, 0, 100, 0)
    Sound(833, 0, 70, 0)
    SetCameraDistance(14500, 500)
    StopEffect(0x7, 0x0)
    PlayEffect(0x0, 0x0, 0xFE, 0x5, 0, 0, -750, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 2000)
    BeginChrThread(0x8, 0, 0, 6)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(1000)
    BeginChrThread(0xFE, 2, 0, 9)
    Return()

    # Function_8_1C33 end

    def Function_9_1CC5(): pass

    label("Function_9_1CC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CE9")
    OP_82(0x0, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_9_1CC5")

    label("loc_1CE9")

    Return()

    # Function_9_1CC5 end

    def Function_10_1CEA(): pass

    label("Function_10_1CEA")

    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sleep(500)

    label("loc_1CFE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D22")
    OP_82(0x0, 0x32, 0x1388, 0x1F4)
    Sleep(500)
    Jump("loc_1CFE")

    label("loc_1D22")

    Return()

    # Function_10_1CEA end

    def Function_11_1D23(): pass

    label("Function_11_1D23")

    OP_25(0x33C, 0x3C)
    Sleep(400)
    OP_25(0x33C, 0x32)
    Sleep(400)
    OP_25(0x33C, 0x28)
    Sleep(400)
    OP_25(0x33C, 0x1E)
    Return()

    # Function_11_1D23 end

    def Function_12_1D3D(): pass

    label("Function_12_1D3D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00056.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00156.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00256.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00356.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D97")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch0295F.itc", 0x27)

    label("loc_1D97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DB5")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch0315F.itc", 0x27)

    label("loc_1DB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DD3")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch0325A.itc", 0x27)

    label("loc_1DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DF1")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_1DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E0F")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch0315F.itc", 0x29)

    label("loc_1E0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E2D")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch0325A.itc", 0x29)

    label("loc_1E2D")

    LoadChrToIndex("chr/ch04250.itc", 0x2B)
    LoadChrToIndex("chr/ch04253.itc", 0x2E)
    LoadChrToIndex("chr/ch04254.itc", 0x2F)
    LoadChrToIndex("chr/ch00001.itc", 0x30)
    LoadChrToIndex("chr/ch00301.itc", 0x31)
    LoadChrToIndex("chr/ch02901.itc", 0x32)
    LoadChrToIndex("chr/ch03201.itc", 0x33)
    LoadEffect(0x0, "event/ev10006.eff")
    LoadEffect(0x1, "event/ev10007.eff")
    LoadEffect(0x2, "map/mpbell.eff")
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(132)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13700.itp")
    SoundLoad(3906)
    SoundLoad(3907)
    SoundLoad(3908)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -14110, 0, 580, 90)
    SetChrPos(0x102, -14470, 0, -650, 90)
    SetChrPos(0x103, -14880, 0, 1630, 90)
    SetChrPos(0x104, -14680, 0, -2040, 90)
    SetChrPos(0xF4, -16079, 0, 1140, 90)
    SetChrPos(0xF5, -15780, 0, -1400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F92")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x3)
    Jump("loc_1FCA")

    label("loc_1F92")

    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x27)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x29)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)

    label("loc_1FCA")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5900, 1140, 0, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-5900, 2140, 0, 0)
    OP_68(-12700, 2420, 0, 5000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16149, 0)
    SetCameraDistance(18150, 5000)
    BeginChrThread(0xD, 1, 0, 11)
    PlayBGM("ed7584", 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3832")
    OP_2C(0xB0, 0x5)
    OP_29(0xB0, 0x1, 0x7)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0030
    ChrTalk(
        0x8,
        "#13703F#40W………………………………\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00007F#40W#6P#N呼……呼……\x01",
            "怎……怎么样……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0032
    ChrTalk(
        0x104,
        (
            "#00307F#40W#12P#N这、这就是\x01",
            "我们的全部实力……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0033
    ChrTalk(
        0x8,
        (
            "#13704F#30W……真令人吃惊。\x02\x03",

            "#13702F竟然有人能令我\x01",
            "单膝着地……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()

    def lambda_21A3():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_21A3)
    Sleep(250)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 40, 0)
    Sound(358, 0, 60, 0)
    OP_0D()
    WaitChrThread(0x8, 2)
    Sleep(500)
    Fade(500)
    OP_68(-12700, 2420, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x101,
        "#00010F#6P#N什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2319")

    #C0035
    ChrTalk(
        0x105,
        "#10410F#6P#N#40W她还能站起来吗……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2346")

    label("loc_2319")


    #C0036
    ChrTalk(
        0x106,
        "#10707F#6P#N#40W她还能站起来……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2346")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_238D")

    #C0037
    ChrTalk(
        0x109,
        (
            "#10107F#6P#N#40W但、但是……\x01",
            "我们也……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_23BB")

    label("loc_238D")


    #C0038
    ChrTalk(
        0x106,
        (
            "#10707F#6P#N#40W但是……\x01",
            "我们也……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_23BB")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0039
    AnonymousTalk(
        0x8,
        (
            "#30W……我无意与你们\x01",
            "继续交锋。\x02\x03",

            "如此看来，\x01",
            "你们总有一天可以达到\x01",
            "『战鬼』与『剑圣』的高度。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 1500)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x2F)
    OP_A1(0x8, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(150)
    SetChrSubChip(0x8, 0x4)
    OP_0D()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 250)
    Sound(357, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)
    Fade(600)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    Sound(288, 0, 30, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-11550, 1920, 0, 0)
    MoveCamera(50, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x101,
        "#00005F#6P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0x104,
        "#00305F#6P#N你愿意离开了吗……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0042
    ChrTalk(
        0x8,
        (
            "#13704F#11P既然你们已经向我展示了自身具备\x01",
            "的可能性，我便无需继续插手了。\x02\x03",

            "#13702F至于圣子，也只能\x01",
            "接受这样的结果了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#00204F#6P#N是吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2882")

    #C0044
    ChrTalk(
        0x105,
        (
            "#10403F#6P#N『钢之圣女』……多谢你。\x02\x03",

            "#10408F但我们骑士团与你们\x01",
            "是不可能和解的……\x02\x03",

            "#10401F你应该明白这一点吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0045
    ChrTalk(
        0x8,
        (
            "#13703F#11P那当然，『苍之圣典』。\x02\x03",

            "当帝国的动乱落下帷幕之时，\x01",
            "『幻焰计划』也会随之结束……\x02\x03",

            "#13700F无论此次的事态会如何发展，\x01",
            "我们决一雌雄的时刻也已经临近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x105,
        "#10406F#6P#N嗯……也许吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2882")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29BD")

    #C0047
    ChrTalk(
        0x106,
        (
            "#10706F#6P#N『钢之圣女』……\x01",
            "请你告诉我一件事。\x02\x03",

            "#10701F你曾经……与我的父亲交过手？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0048
    ChrTalk(
        0x8,
        (
            "#13703F#11P是的，那是大约十年前的事。\x02\x03",

            "#13702F能打碎我面具的\x01",
            "强者并不多见。\x02\x03",

            "也许你已经达到了\x01",
            "他的高度……\x02\x03",

            "#13704F然而，是否要走上其它道路，\x01",
            "还是取决于你自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x106,
        "#10708F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_29BD")

    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_68(-10990, 1920, -50, 800)
    OP_9B(0x0, 0x102, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ACA")

    #C0050
    ChrTalk(
        0x102,
        (
            "#00103F#6P#N还有一个问题……\x02\x03",

            "#00108F你的那头长发，\x01",
            "以及『铁机队』这个名字……\x02\x03",

            "#00101F难道你就是\x01",
            "那场『狮子战役』中的……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2B60")

    label("loc_2ACA")


    #C0051
    ChrTalk(
        0x102,
        (
            "#00106F#6P#N『钢之圣女』……\x01",
            "请你告诉我一件事。\x02\x03",

            "#00108F你那头长发，\x01",
            "以及『铁机队』这个名字……\x02\x03",

            "#00101F难道你就是\x01",
            "那场『狮子战役』中的……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2B60")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)

    #C0052
    ChrTalk(
        0x8,
        (
            "#13704F#11P#30W呵呵……\x02\x03",

            "#13702F我只能说，\x01",
            "你的洞察力很出色。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0053
    ChrTalk(
        0x102,
        "#00105F#6P#N#4S……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0054
    ChrTalk(
        0x101,
        "#00005F#5P艾莉……？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        "#00301F#5P你在说什么……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0056
    ChrTalk(
        0x8,
        (
            "#13704F#3906V#30W#30A那么，就此告辞了。\x02\x03",

            "#3907V#30W#40A希望你们能在命运面前\x01",
            "找到自己的『答案』……\x02\x03",

            "#13702F#3908V#30W#30A我会在远方为你们祈祷的。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopBGM(0x1770)
    SetCameraDistance(12500, 2000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)
    StopSound(832, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_2D86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2D86)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    CancelBlur(1000)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-10700, 2420, 0, 0)
    OP_68(-12700, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)
    Sleep(100)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00008F#5P……艾莉，\x01",
            "你刚才到底在说什么？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EAF():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2EAF)
    Sleep(30)

    def lambda_2EBF():
        TurnDirection(0x104, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2EBF)
    Sleep(30)

    def lambda_2ECF():
        TurnDirection(0xF4, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2ECF)
    Sleep(30)

    def lambda_2EDF():
        TurnDirection(0xF5, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2EDF)
    Sleep(30)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0058
    ChrTalk(
        0x103,
        (
            "#00200F感觉好像是\x01",
            "非常有深意的对话……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-16660, 2420, -660, 1500)
    MoveCamera(90, 17, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(14000, 1500)
    Sleep(500)
    OP_93(0x102, 0x110, 0x190)
    OP_6F(0x79)

    #C0059
    ChrTalk(
        0x102,
        (
            "#00106F#11P…………是啊。\x02\x03",

            "#00108F这也许会让你们感觉很困惑，\x01",
            "因此我原本并不想说呢……\x02\x03",

            "#00101F如果我的想法没错……\x01",
            "她应该是二百五十年前的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0060
    ChrTalk(
        0x104,
        "#00307F什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30C3")

    #C0061
    ChrTalk(
        0x109,
        "#10111F这、这究竟是……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30E8")

    label("loc_30C3")


    #C0062
    ChrTalk(
        0x106,
        "#10712F这到底是怎么回事……！？\x02",
    )

    CloseMessageWindow()

    label("loc_30E8")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    SetCameraDistance(13000, 30000)
    Sleep(500)

    #C0063
    ChrTalk(
        0x102,
        (
            "#00103F#11P#30W在二百五十年前，埃雷波尼亚\x01",
            "曾经发生过一场继承者\x01",
            "之间争夺帝位的战争。\x02\x03",

            "战争波及到了整个帝国，\x01",
            "最后被冠以『狮子战役』\x01",
            "这个名称……\x02\x03",

            "#00108F就在那时，有一位持中立态度的\x01",
            "女性武者为了平息战乱，\x01",
            "毅然挺身而出。\x02\x03",

            "#00101F那位女性便是莉安娜·桑德罗特。\x02\x03",

            "她有一头美丽的金发，\x01",
            "率领着『铁骑队』\x01",
            "驰骋于战场。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00011F啊……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        "#00205F这……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        "#00310F简、简直一模一样啊！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3325")

    #C0067
    ChrTalk(
        0x109,
        (
            "#10101F我也在书上\x01",
            "看到过……！\x02\x03",

            "#10103F『女战神』莉安娜……\x01",
            "又名『枪之圣女』。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3320")

    #C0068
    ChrTalk(
        0x105,
        (
            "#10403F在帝国是家喻户晓的\x01",
            "历史名人呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3320")

    Jump("loc_3391")

    label("loc_3325")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3391")

    #C0069
    ChrTalk(
        0x105,
        (
            "#10403F在帝国是家喻户晓的\x01",
            "历史名人呢……\x02\x03",

            "#10408F而且，她还有\x01",
            "『枪之圣女』这个称号……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3391")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33D1")

    #C0070
    ChrTalk(
        0x106,
        (
            "#10701F埃雷波尼亚曾经\x01",
            "出现过那样的人物……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D1")


    #C0071
    ChrTalk(
        0x101,
        (
            "#00006F『铁骑队』和『铁机队』……\x01",
            "『枪之圣女』和『钢之圣女』……\x02\x03",

            "#00008F从外表来看也是一样，\x01",
            "相符之处实在是太多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#00106F#11P……二百五十年前，埃雷波尼亚终于\x01",
            "在她的努力之下恢复了和平。\x01",
            "但是，自那之后没过多久，她便去世了。\x02\x03",

            "#00108F有人说她是被谋杀的，有人说她是病逝的，\x01",
            "总之众说纷纭……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#00206F……按照一般的思维方式，\x01",
            "也许应该理解为\x01",
            "她在刻意模仿历史人物……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#00306F但是，从她那惊人的实力来看，\x01",
            "也只能认为她就是那位名人了。\x02\x03",

            "#00301F更何况，她还是那个\x01",
            "神秘莫测的『结社』的成员。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3614")
    Sleep(300)

    #C0075
    ChrTalk(
        0x106,
        (
            "#10708F（难道和『银』一样，\x01",
            "　是世代相传的吗……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3614")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3661")
    Sleep(300)

    #C0076
    ChrTalk(
        0x105,
        (
            "#10401F（……看来有必要\x01",
            "  将这件事报告给总长呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3661")


    #C0077
    ChrTalk(
        0x102,
        (
            "#00104F#11P呵呵……\x01",
            "果然让你们感到困惑了呢。\x02\x03",

            "#00100F不管怎么说，\x01",
            "她已经离开克洛斯贝尔了。\x02\x03",

            "我们就暂且抛开臆测，\x01",
            "集中精力来面对真正重要的问题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#00006F嗯……没错。\x02",
    )

    CloseMessageWindow()
    OP_68(-9700, 2920, 0, 2500)
    MoveCamera(90, 0, 0, 2500)
    OP_6E(550, 2500)
    SetCameraDistance(18150, 2500)

    def lambda_3744():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3744)
    Sleep(30)

    def lambda_3754():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3754)
    Sleep(30)

    def lambda_3764():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3764)
    Sleep(30)

    def lambda_3774():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3774)
    Sleep(30)

    def lambda_3784():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3784)
    Sleep(30)

    def lambda_3794():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3794)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0079
    ChrTalk(
        0x101,
        (
            "#00004F#6P#N好，让钟的共鸣停下来吧。\x02\x03",

            "#00000F如果顺利，应该就能\x01",
            "解除克洛斯贝尔市的『结界』了。\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x2C, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    Jump("loc_467A")

    label("loc_3832")

    OP_29(0xB0, 0x1, 0x6)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    def lambda_3849():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3849)
    Sound(812, 0, 100, 0)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0x101, 2)
    OP_0D()

    #C0080
    ChrTalk(
        0x101,
        "#00010F#40W#6P#N唔……还没结束……！\x02",
    )

    CloseMessageWindow()

    def lambda_38AD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_38AD)
    Sound(812, 0, 100, 0)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(805, 0, 100, 0)
    WaitChrThread(0x104, 2)
    OP_0D()

    #C0081
    ChrTalk(
        0x104,
        (
            "#00310F#40W#12P#N……怎么能在……\x01",
            "这种地方止步！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)

    def lambda_392B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_392B)
    Sleep(50)

    def lambda_3947():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3947)
    Sleep(50)

    def lambda_3963():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3963)
    Sleep(50)

    def lambda_397F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_397F)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39B5")
    Sound(540, 0, 50, 0)

    label("loc_39B5")

    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    Sleep(50)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xF5, 2)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0082
    AnonymousTalk(
        0x8,
        (
            "不可否认，你们的实力仍然不足……\x02\x03",

            "但既然能够打碎我的面具，\x01",
            "今后还是有可能达到\x01",
            "『战鬼』与『剑圣』的高度的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x2F)
    OP_A1(0x8, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x8, 0x4)
    OP_0D()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 250)
    Sound(357, 0, 100, 0)
    Sound(832, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()
    Sleep(500)
    Fade(600)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(358, 0, 50, 0)
    Sound(288, 0, 30, 0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-11550, 1920, 0, 0)
    MoveCamera(50, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0083
    ChrTalk(
        0x101,
        "#00005F#6P#N阿瑞安赫德……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0084
    ChrTalk(
        0x102,
        (
            "#00105F#6P#N难道说……\x01",
            "你愿意离开了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0085
    ChrTalk(
        0x8,
        (
            "#13704F#11P既然你们已经向我展示了自身具备\x01",
            "的可能性，我便无需继续插手了。\x02\x03",

            "#13702F至于圣子，也只能\x01",
            "接受这样的结果了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#00202F#6P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0087
    ChrTalk(
        0x104,
        "#00305F#6P#N没开玩笑吗……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F06")

    #C0088
    ChrTalk(
        0x105,
        (
            "#10403F#6P#N『钢之圣女』……多谢你。\x02\x03",

            "#10408F但我们骑士团与你们\x01",
            "是不可能和解的……\x02\x03",

            "#10401F你应该明白这一点吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0089
    ChrTalk(
        0x8,
        (
            "#13703F#11P那当然，『苍之圣典』。\x02\x03",

            "当帝国的动乱落下帷幕之时，\x01",
            "『幻焰计划』也会随之结束……\x02\x03",

            "#13700F无论此次的事态会有如何发展，\x01",
            "我们决一雌雄的时刻也已经临近了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x105,
        "#10406F#6P#N嗯……也许吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3F06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4038")

    #C0091
    ChrTalk(
        0x106,
        (
            "#10706F#6P#N『钢之圣女』……\x01",
            "请你告诉我一件事。\x02\x03",

            "#10701F你曾经……与我的父亲交过手？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0092
    ChrTalk(
        0x8,
        (
            "#13703F#11P是的，那是大约十年前的事。\x02\x03",

            "#13702F能打碎我面具的\x01",
            "强者并不多见。\x02\x03",

            "#13704F是以他的高度为目标……\x01",
            "还是走上其它的道路，\x01",
            "全都取决于你自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x106,
        "#10708F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4038")

    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_68(-5900, 2140, 0, 0)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0094
    ChrTalk(
        0x8,
        (
            "#13704F#3906V#30W#30A那么，就此告辞了。\x02\x03",

            "#3907V#30W#40A希望你们能在命运面前\x01",
            "找到自己的『答案』……\x02\x03",

            "#13702F#3908V#30W#30A我会在远方为你们祈祷的。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    StopBGM(0x1770)
    SetCameraDistance(12500, 2000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(222, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 100, 0)
    StopSound(832, 1000, 100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_41C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_41C7)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    CancelBlur(1000)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-10700, 2420, 0, 0)
    OP_68(-12700, 2420, 0, 3000)
    MoveCamera(90, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18150, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_82(0x14, 0x0, 0x7D0, 0x1F4)

    #C0095
    ChrTalk(
        0x101,
        "#00006F#40W#5P呼……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4317")

    #C0096
    ChrTalk(
        0x109,
        "#10106F#30W真、真是筋疲力尽……\x02",
    )

    CloseMessageWindow()

    label("loc_4317")


    #C0097
    ChrTalk(
        0x104,
        (
            "#00306F……真是的……\x01",
            "实在是一位不得了的圣女啊。\x02\x03",

            "#00301F虽然很漂亮，而且正是\x01",
            "我喜欢的类型，\x01",
            "但完全没机会和她搭讪呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#00211F兰迪前辈，\x01",
            "问题的重点并不在这里吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00106F话说回来……\x01",
            "真没想到我们能和她抗衡到\x01",
            "如此程度，并且打破了她的面具……\x02\x03",

            "#00102F看来我们也\x01",
            "有所成长了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00002F#5P嗯……说的没错。\x02\x03",

            "#00012F不过，我觉得更大程度上\x01",
            "是因为听到琪雅的事情之后，\x01",
            "彻底坚定了决心的缘故。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        "#00104F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#00301F嗯……\x01",
            "毕竟听到了那种话嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x103,
        (
            "#00206F……一定要把她带回来，\x01",
            "然后紧紧抱住她，不然绝不罢休。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_456B")

    #C0104
    ChrTalk(
        0x105,
        (
            "#10402F哎呀呀，\x01",
            "你们还真是疼爱孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45A5")

    #C0105
    ChrTalk(
        0x109,
        (
            "#10112F啊哈哈……\x01",
            "很符合大家的作风。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45DB")

    #C0106
    ChrTalk(
        0x106,
        (
            "#10709F呵呵……\x01",
            "我也可以理解呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45DB")

    OP_68(-9700, 2920, 0, 2500)
    MoveCamera(90, 0, 0, 2500)
    OP_6E(550, 2500)
    SetCameraDistance(18150, 2500)
    OP_6F(0x79)

    #C0107
    ChrTalk(
        0x101,
        (
            "#00004F#6P#N好，让钟的共鸣停下来吧。\x02\x03",

            "#00000F如果顺利，应该就能\x01",
            "解除克洛斯贝尔市的『结界』了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_467A")

    OP_32(0xFF, 0xFF, 0x0)
    WaitBGM()
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x104, 0x31)
    SetChrSubChip(0x104, 0x1)
    SetChrPos(0x101, 0, 1530, 2150, 180)
    SetChrPos(0x104, 0, 1530, -1900, 0)
    SetChrPos(0x102, -4480, 1300, -2860, 45)
    SetChrPos(0x103, -3630, 1320, -3800, 45)
    BeginChrThread(0x101, 3, 0, 13)
    BeginChrThread(0x104, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_474D")
    SetChrChipByIndex(0x109, 0x32)
    SetChrSubChip(0x109, 0x1)
    SetChrPos(0x109, -2200, 1530, 0, 90)
    BeginChrThread(0x109, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4737")
    SetChrPos(0xF5, -2330, 1370, -4510, 0)
    Jump("loc_4748")

    label("loc_4737")

    SetChrPos(0xF4, -2330, 1370, -4510, 0)

    label("loc_4748")

    Jump("loc_47A5")

    label("loc_474D")

    SetChrChipByIndex(0x106, 0x33)
    SetChrSubChip(0x106, 0x1)
    SetChrPos(0x106, -2200, 1530, 0, 90)
    BeginChrThread(0x106, 3, 0, 13)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4794")
    SetChrPos(0xF5, -2330, 1370, -4510, 0)
    Jump("loc_47A5")

    label("loc_4794")

    SetChrPos(0xF4, -2330, 1370, -4510, 0)

    label("loc_47A5")

    StopEffect(0x7, 0x0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 2, 0, 4)
    BeginChrThread(0xD, 1, 0, 14)
    FadeToBright(1000, 0)
    OP_68(0, 1850, 0, 0)
    OP_68(0, 2850, 0, 6000)
    MoveCamera(105, 21, 0, 0)
    MoveCamera(70, 15, 0, 6000)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(15000, 6000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 2850, 0, 0)
    MoveCamera(90, 27, 0, 0)
    MoveCamera(90, 9, 0, 5000)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    OP_6F(0x79)
    Sleep(50)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetCameraDistance(36000, 1000)
    Sound(829, 0, 100, 0)
    StopSound(828, 2000, 60)
    StopSound(825, 2000, 60)
    FadeToDark(1000, 16777215, -1)
    Sleep(1000)
    OP_6F(0x1)
    CancelBlur(100)
    OP_0D()
    EndChrThread(0x101, 0x2)
    StopEffect(0x0, 0x0)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4909")
    EndChrThread(0x109, 0x3)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_4915")

    label("loc_4909")

    EndChrThread(0x106, 0x3)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    label("loc_4915")

    OP_70(0x0, 0x1E)
    SetMapObjFrame(0x0, "bell_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "pano01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cloud", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back", 0x1, 0x1)
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    Sleep(500)
    OP_68(0, 3550, 0, 0)
    MoveCamera(50, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(20000, 5000)
    Sound(132, 2, 70, 0)
    FadeToBright(2000, 16777215)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    StopSound(132, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1D3D end

    def Function_13_4A25(): pass

    label("Function_13_4A25")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A4B")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(500)
    Jump("Function_13_4A25")

    label("loc_4A4B")

    Return()

    # Function_13_4A25 end

    def Function_14_4A4C(): pass

    label("Function_14_4A4C")

    Sound(825, 2, 10, 0)
    Sleep(200)
    OP_25(0x339, 0x14)
    OP_25(0x33C, 0x28)
    Sleep(200)
    OP_25(0x339, 0x1E)
    OP_25(0x33C, 0x32)
    Sleep(200)
    OP_25(0x339, 0x28)
    OP_25(0x33C, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x32)
    OP_25(0x33C, 0x46)
    Sleep(2000)
    OP_25(0x339, 0x3C)
    Sleep(200)
    OP_25(0x339, 0x46)
    Return()

    # Function_14_4A4C end

    SaveToFile()

Try(main)
