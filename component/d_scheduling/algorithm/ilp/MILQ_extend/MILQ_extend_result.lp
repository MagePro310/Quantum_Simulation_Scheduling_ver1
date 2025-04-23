\* Scheduling *\
Minimize
OBJ: makespan
Subject To
_C1: c_j_0 = 0
_C10: - c_j_1 + z_ikt_1_fake_belem_1 + z_ikt_1_fake_manila_1 <= 0
_C100: - c_j_1 + 31 z_ikt_1_fake_belem_31 + 31 z_ikt_1_fake_manila_31 <= 0
_C101: z_ikt_1_fake_belem_31 + z_ikt_1_fake_manila_31 <= 1
_C102: s_j_1 + 999969 z_ikt_1_fake_belem_31 + 999969 z_ikt_1_fake_manila_31
 <= 1000000
_C103: c_j_2 - makespan <= 0
_C104: x_ik_2_fake_belem + x_ik_2_fake_manila = 1
_C105: c_j_2 - s_j_2 - z_ikt_2_fake_belem_0 - z_ikt_2_fake_belem_1
 - z_ikt_2_fake_belem_10 - z_ikt_2_fake_belem_11 - z_ikt_2_fake_belem_12
 - z_ikt_2_fake_belem_13 - z_ikt_2_fake_belem_14 - z_ikt_2_fake_belem_15
 - z_ikt_2_fake_belem_16 - z_ikt_2_fake_belem_17 - z_ikt_2_fake_belem_18
 - z_ikt_2_fake_belem_19 - z_ikt_2_fake_belem_2 - z_ikt_2_fake_belem_20
 - z_ikt_2_fake_belem_21 - z_ikt_2_fake_belem_22 - z_ikt_2_fake_belem_23
 - z_ikt_2_fake_belem_24 - z_ikt_2_fake_belem_25 - z_ikt_2_fake_belem_26
 - z_ikt_2_fake_belem_27 - z_ikt_2_fake_belem_28 - z_ikt_2_fake_belem_29
 - z_ikt_2_fake_belem_3 - z_ikt_2_fake_belem_30 - z_ikt_2_fake_belem_31
 - z_ikt_2_fake_belem_4 - z_ikt_2_fake_belem_5 - z_ikt_2_fake_belem_6
 - z_ikt_2_fake_belem_7 - z_ikt_2_fake_belem_8 - z_ikt_2_fake_belem_9
 - z_ikt_2_fake_manila_0 - z_ikt_2_fake_manila_1 - z_ikt_2_fake_manila_10
 - z_ikt_2_fake_manila_11 - z_ikt_2_fake_manila_12 - z_ikt_2_fake_manila_13
 - z_ikt_2_fake_manila_14 - z_ikt_2_fake_manila_15 - z_ikt_2_fake_manila_16
 - z_ikt_2_fake_manila_17 - z_ikt_2_fake_manila_18 - z_ikt_2_fake_manila_19
 - z_ikt_2_fake_manila_2 - z_ikt_2_fake_manila_20 - z_ikt_2_fake_manila_21
 - z_ikt_2_fake_manila_22 - z_ikt_2_fake_manila_23 - z_ikt_2_fake_manila_24
 - z_ikt_2_fake_manila_25 - z_ikt_2_fake_manila_26 - z_ikt_2_fake_manila_27
 - z_ikt_2_fake_manila_28 - z_ikt_2_fake_manila_29 - z_ikt_2_fake_manila_3
 - z_ikt_2_fake_manila_30 - z_ikt_2_fake_manila_31 - z_ikt_2_fake_manila_4
 - z_ikt_2_fake_manila_5 - z_ikt_2_fake_manila_6 - z_ikt_2_fake_manila_7
 - z_ikt_2_fake_manila_8 - z_ikt_2_fake_manila_9 = -1
_C106: - 1000000 x_ik_2_fake_belem + z_ikt_2_fake_belem_0
 + z_ikt_2_fake_belem_1 + z_ikt_2_fake_belem_10 + z_ikt_2_fake_belem_11
 + z_ikt_2_fake_belem_12 + z_ikt_2_fake_belem_13 + z_ikt_2_fake_belem_14
 + z_ikt_2_fake_belem_15 + z_ikt_2_fake_belem_16 + z_ikt_2_fake_belem_17
 + z_ikt_2_fake_belem_18 + z_ikt_2_fake_belem_19 + z_ikt_2_fake_belem_2
 + z_ikt_2_fake_belem_20 + z_ikt_2_fake_belem_21 + z_ikt_2_fake_belem_22
 + z_ikt_2_fake_belem_23 + z_ikt_2_fake_belem_24 + z_ikt_2_fake_belem_25
 + z_ikt_2_fake_belem_26 + z_ikt_2_fake_belem_27 + z_ikt_2_fake_belem_28
 + z_ikt_2_fake_belem_29 + z_ikt_2_fake_belem_3 + z_ikt_2_fake_belem_30
 + z_ikt_2_fake_belem_31 + z_ikt_2_fake_belem_4 + z_ikt_2_fake_belem_5
 + z_ikt_2_fake_belem_6 + z_ikt_2_fake_belem_7 + z_ikt_2_fake_belem_8
 + z_ikt_2_fake_belem_9 <= 0
_C107: - 1000000 x_ik_2_fake_manila + z_ikt_2_fake_manila_0
 + z_ikt_2_fake_manila_1 + z_ikt_2_fake_manila_10 + z_ikt_2_fake_manila_11
 + z_ikt_2_fake_manila_12 + z_ikt_2_fake_manila_13 + z_ikt_2_fake_manila_14
 + z_ikt_2_fake_manila_15 + z_ikt_2_fake_manila_16 + z_ikt_2_fake_manila_17
 + z_ikt_2_fake_manila_18 + z_ikt_2_fake_manila_19 + z_ikt_2_fake_manila_2
 + z_ikt_2_fake_manila_20 + z_ikt_2_fake_manila_21 + z_ikt_2_fake_manila_22
 + z_ikt_2_fake_manila_23 + z_ikt_2_fake_manila_24 + z_ikt_2_fake_manila_25
 + z_ikt_2_fake_manila_26 + z_ikt_2_fake_manila_27 + z_ikt_2_fake_manila_28
 + z_ikt_2_fake_manila_29 + z_ikt_2_fake_manila_3 + z_ikt_2_fake_manila_30
 + z_ikt_2_fake_manila_31 + z_ikt_2_fake_manila_4 + z_ikt_2_fake_manila_5
 + z_ikt_2_fake_manila_6 + z_ikt_2_fake_manila_7 + z_ikt_2_fake_manila_8
 + z_ikt_2_fake_manila_9 <= 0
_C108: - c_j_2 <= 0
_C109: z_ikt_2_fake_belem_0 + z_ikt_2_fake_manila_0 <= 1
_C11: z_ikt_1_fake_belem_1 + z_ikt_1_fake_manila_1 <= 1
_C110: s_j_2 + 1000000 z_ikt_2_fake_belem_0 + 1000000 z_ikt_2_fake_manila_0
 <= 1000000
_C111: - c_j_2 + z_ikt_2_fake_belem_1 + z_ikt_2_fake_manila_1 <= 0
_C112: z_ikt_2_fake_belem_1 + z_ikt_2_fake_manila_1 <= 1
_C113: s_j_2 + 999999 z_ikt_2_fake_belem_1 + 999999 z_ikt_2_fake_manila_1
 <= 1000000
_C114: - c_j_2 + 2 z_ikt_2_fake_belem_2 + 2 z_ikt_2_fake_manila_2 <= 0
_C115: z_ikt_2_fake_belem_2 + z_ikt_2_fake_manila_2 <= 1
_C116: s_j_2 + 999998 z_ikt_2_fake_belem_2 + 999998 z_ikt_2_fake_manila_2
 <= 1000000
_C117: - c_j_2 + 3 z_ikt_2_fake_belem_3 + 3 z_ikt_2_fake_manila_3 <= 0
_C118: z_ikt_2_fake_belem_3 + z_ikt_2_fake_manila_3 <= 1
_C119: s_j_2 + 999997 z_ikt_2_fake_belem_3 + 999997 z_ikt_2_fake_manila_3
 <= 1000000
_C12: s_j_1 + 999999 z_ikt_1_fake_belem_1 + 999999 z_ikt_1_fake_manila_1
 <= 1000000
_C120: - c_j_2 + 4 z_ikt_2_fake_belem_4 + 4 z_ikt_2_fake_manila_4 <= 0
_C121: z_ikt_2_fake_belem_4 + z_ikt_2_fake_manila_4 <= 1
_C122: s_j_2 + 999996 z_ikt_2_fake_belem_4 + 999996 z_ikt_2_fake_manila_4
 <= 1000000
_C123: - c_j_2 + 5 z_ikt_2_fake_belem_5 + 5 z_ikt_2_fake_manila_5 <= 0
_C124: z_ikt_2_fake_belem_5 + z_ikt_2_fake_manila_5 <= 1
_C125: s_j_2 + 999995 z_ikt_2_fake_belem_5 + 999995 z_ikt_2_fake_manila_5
 <= 1000000
_C126: - c_j_2 + 6 z_ikt_2_fake_belem_6 + 6 z_ikt_2_fake_manila_6 <= 0
_C127: z_ikt_2_fake_belem_6 + z_ikt_2_fake_manila_6 <= 1
_C128: s_j_2 + 999994 z_ikt_2_fake_belem_6 + 999994 z_ikt_2_fake_manila_6
 <= 1000000
_C129: - c_j_2 + 7 z_ikt_2_fake_belem_7 + 7 z_ikt_2_fake_manila_7 <= 0
_C13: - c_j_1 + 2 z_ikt_1_fake_belem_2 + 2 z_ikt_1_fake_manila_2 <= 0
_C130: z_ikt_2_fake_belem_7 + z_ikt_2_fake_manila_7 <= 1
_C131: s_j_2 + 999993 z_ikt_2_fake_belem_7 + 999993 z_ikt_2_fake_manila_7
 <= 1000000
_C132: - c_j_2 + 8 z_ikt_2_fake_belem_8 + 8 z_ikt_2_fake_manila_8 <= 0
_C133: z_ikt_2_fake_belem_8 + z_ikt_2_fake_manila_8 <= 1
_C134: s_j_2 + 999992 z_ikt_2_fake_belem_8 + 999992 z_ikt_2_fake_manila_8
 <= 1000000
_C135: - c_j_2 + 9 z_ikt_2_fake_belem_9 + 9 z_ikt_2_fake_manila_9 <= 0
_C136: z_ikt_2_fake_belem_9 + z_ikt_2_fake_manila_9 <= 1
_C137: s_j_2 + 999991 z_ikt_2_fake_belem_9 + 999991 z_ikt_2_fake_manila_9
 <= 1000000
_C138: - c_j_2 + 10 z_ikt_2_fake_belem_10 + 10 z_ikt_2_fake_manila_10 <= 0
_C139: z_ikt_2_fake_belem_10 + z_ikt_2_fake_manila_10 <= 1
_C14: z_ikt_1_fake_belem_2 + z_ikt_1_fake_manila_2 <= 1
_C140: s_j_2 + 999990 z_ikt_2_fake_belem_10 + 999990 z_ikt_2_fake_manila_10
 <= 1000000
_C141: - c_j_2 + 11 z_ikt_2_fake_belem_11 + 11 z_ikt_2_fake_manila_11 <= 0
_C142: z_ikt_2_fake_belem_11 + z_ikt_2_fake_manila_11 <= 1
_C143: s_j_2 + 999989 z_ikt_2_fake_belem_11 + 999989 z_ikt_2_fake_manila_11
 <= 1000000
_C144: - c_j_2 + 12 z_ikt_2_fake_belem_12 + 12 z_ikt_2_fake_manila_12 <= 0
_C145: z_ikt_2_fake_belem_12 + z_ikt_2_fake_manila_12 <= 1
_C146: s_j_2 + 999988 z_ikt_2_fake_belem_12 + 999988 z_ikt_2_fake_manila_12
 <= 1000000
_C147: - c_j_2 + 13 z_ikt_2_fake_belem_13 + 13 z_ikt_2_fake_manila_13 <= 0
_C148: z_ikt_2_fake_belem_13 + z_ikt_2_fake_manila_13 <= 1
_C149: s_j_2 + 999987 z_ikt_2_fake_belem_13 + 999987 z_ikt_2_fake_manila_13
 <= 1000000
_C15: s_j_1 + 999998 z_ikt_1_fake_belem_2 + 999998 z_ikt_1_fake_manila_2
 <= 1000000
_C150: - c_j_2 + 14 z_ikt_2_fake_belem_14 + 14 z_ikt_2_fake_manila_14 <= 0
_C151: z_ikt_2_fake_belem_14 + z_ikt_2_fake_manila_14 <= 1
_C152: s_j_2 + 999986 z_ikt_2_fake_belem_14 + 999986 z_ikt_2_fake_manila_14
 <= 1000000
_C153: - c_j_2 + 15 z_ikt_2_fake_belem_15 + 15 z_ikt_2_fake_manila_15 <= 0
_C154: z_ikt_2_fake_belem_15 + z_ikt_2_fake_manila_15 <= 1
_C155: s_j_2 + 999985 z_ikt_2_fake_belem_15 + 999985 z_ikt_2_fake_manila_15
 <= 1000000
_C156: - c_j_2 + 16 z_ikt_2_fake_belem_16 + 16 z_ikt_2_fake_manila_16 <= 0
_C157: z_ikt_2_fake_belem_16 + z_ikt_2_fake_manila_16 <= 1
_C158: s_j_2 + 999984 z_ikt_2_fake_belem_16 + 999984 z_ikt_2_fake_manila_16
 <= 1000000
_C159: - c_j_2 + 17 z_ikt_2_fake_belem_17 + 17 z_ikt_2_fake_manila_17 <= 0
_C16: - c_j_1 + 3 z_ikt_1_fake_belem_3 + 3 z_ikt_1_fake_manila_3 <= 0
_C160: z_ikt_2_fake_belem_17 + z_ikt_2_fake_manila_17 <= 1
_C161: s_j_2 + 999983 z_ikt_2_fake_belem_17 + 999983 z_ikt_2_fake_manila_17
 <= 1000000
_C162: - c_j_2 + 18 z_ikt_2_fake_belem_18 + 18 z_ikt_2_fake_manila_18 <= 0
_C163: z_ikt_2_fake_belem_18 + z_ikt_2_fake_manila_18 <= 1
_C164: s_j_2 + 999982 z_ikt_2_fake_belem_18 + 999982 z_ikt_2_fake_manila_18
 <= 1000000
_C165: - c_j_2 + 19 z_ikt_2_fake_belem_19 + 19 z_ikt_2_fake_manila_19 <= 0
_C166: z_ikt_2_fake_belem_19 + z_ikt_2_fake_manila_19 <= 1
_C167: s_j_2 + 999981 z_ikt_2_fake_belem_19 + 999981 z_ikt_2_fake_manila_19
 <= 1000000
_C168: - c_j_2 + 20 z_ikt_2_fake_belem_20 + 20 z_ikt_2_fake_manila_20 <= 0
_C169: z_ikt_2_fake_belem_20 + z_ikt_2_fake_manila_20 <= 1
_C17: z_ikt_1_fake_belem_3 + z_ikt_1_fake_manila_3 <= 1
_C170: s_j_2 + 999980 z_ikt_2_fake_belem_20 + 999980 z_ikt_2_fake_manila_20
 <= 1000000
_C171: - c_j_2 + 21 z_ikt_2_fake_belem_21 + 21 z_ikt_2_fake_manila_21 <= 0
_C172: z_ikt_2_fake_belem_21 + z_ikt_2_fake_manila_21 <= 1
_C173: s_j_2 + 999979 z_ikt_2_fake_belem_21 + 999979 z_ikt_2_fake_manila_21
 <= 1000000
_C174: - c_j_2 + 22 z_ikt_2_fake_belem_22 + 22 z_ikt_2_fake_manila_22 <= 0
_C175: z_ikt_2_fake_belem_22 + z_ikt_2_fake_manila_22 <= 1
_C176: s_j_2 + 999978 z_ikt_2_fake_belem_22 + 999978 z_ikt_2_fake_manila_22
 <= 1000000
_C177: - c_j_2 + 23 z_ikt_2_fake_belem_23 + 23 z_ikt_2_fake_manila_23 <= 0
_C178: z_ikt_2_fake_belem_23 + z_ikt_2_fake_manila_23 <= 1
_C179: s_j_2 + 999977 z_ikt_2_fake_belem_23 + 999977 z_ikt_2_fake_manila_23
 <= 1000000
_C18: s_j_1 + 999997 z_ikt_1_fake_belem_3 + 999997 z_ikt_1_fake_manila_3
 <= 1000000
_C180: - c_j_2 + 24 z_ikt_2_fake_belem_24 + 24 z_ikt_2_fake_manila_24 <= 0
_C181: z_ikt_2_fake_belem_24 + z_ikt_2_fake_manila_24 <= 1
_C182: s_j_2 + 999976 z_ikt_2_fake_belem_24 + 999976 z_ikt_2_fake_manila_24
 <= 1000000
_C183: - c_j_2 + 25 z_ikt_2_fake_belem_25 + 25 z_ikt_2_fake_manila_25 <= 0
_C184: z_ikt_2_fake_belem_25 + z_ikt_2_fake_manila_25 <= 1
_C185: s_j_2 + 999975 z_ikt_2_fake_belem_25 + 999975 z_ikt_2_fake_manila_25
 <= 1000000
_C186: - c_j_2 + 26 z_ikt_2_fake_belem_26 + 26 z_ikt_2_fake_manila_26 <= 0
_C187: z_ikt_2_fake_belem_26 + z_ikt_2_fake_manila_26 <= 1
_C188: s_j_2 + 999974 z_ikt_2_fake_belem_26 + 999974 z_ikt_2_fake_manila_26
 <= 1000000
_C189: - c_j_2 + 27 z_ikt_2_fake_belem_27 + 27 z_ikt_2_fake_manila_27 <= 0
_C19: - c_j_1 + 4 z_ikt_1_fake_belem_4 + 4 z_ikt_1_fake_manila_4 <= 0
_C190: z_ikt_2_fake_belem_27 + z_ikt_2_fake_manila_27 <= 1
_C191: s_j_2 + 999973 z_ikt_2_fake_belem_27 + 999973 z_ikt_2_fake_manila_27
 <= 1000000
_C192: - c_j_2 + 28 z_ikt_2_fake_belem_28 + 28 z_ikt_2_fake_manila_28 <= 0
_C193: z_ikt_2_fake_belem_28 + z_ikt_2_fake_manila_28 <= 1
_C194: s_j_2 + 999972 z_ikt_2_fake_belem_28 + 999972 z_ikt_2_fake_manila_28
 <= 1000000
_C195: - c_j_2 + 29 z_ikt_2_fake_belem_29 + 29 z_ikt_2_fake_manila_29 <= 0
_C196: z_ikt_2_fake_belem_29 + z_ikt_2_fake_manila_29 <= 1
_C197: s_j_2 + 999971 z_ikt_2_fake_belem_29 + 999971 z_ikt_2_fake_manila_29
 <= 1000000
_C198: - c_j_2 + 30 z_ikt_2_fake_belem_30 + 30 z_ikt_2_fake_manila_30 <= 0
_C199: z_ikt_2_fake_belem_30 + z_ikt_2_fake_manila_30 <= 1
_C2: c_j_1 - makespan <= 0
_C20: z_ikt_1_fake_belem_4 + z_ikt_1_fake_manila_4 <= 1
_C200: s_j_2 + 999970 z_ikt_2_fake_belem_30 + 999970 z_ikt_2_fake_manila_30
 <= 1000000
_C201: - c_j_2 + 31 z_ikt_2_fake_belem_31 + 31 z_ikt_2_fake_manila_31 <= 0
_C202: z_ikt_2_fake_belem_31 + z_ikt_2_fake_manila_31 <= 1
_C203: s_j_2 + 999969 z_ikt_2_fake_belem_31 + 999969 z_ikt_2_fake_manila_31
 <= 1000000
_C204: c_j_3 - makespan <= 0
_C205: x_ik_3_fake_belem + x_ik_3_fake_manila = 1
_C206: c_j_3 - s_j_3 - z_ikt_3_fake_belem_0 - z_ikt_3_fake_belem_1
 - z_ikt_3_fake_belem_10 - z_ikt_3_fake_belem_11 - z_ikt_3_fake_belem_12
 - z_ikt_3_fake_belem_13 - z_ikt_3_fake_belem_14 - z_ikt_3_fake_belem_15
 - z_ikt_3_fake_belem_16 - z_ikt_3_fake_belem_17 - z_ikt_3_fake_belem_18
 - z_ikt_3_fake_belem_19 - z_ikt_3_fake_belem_2 - z_ikt_3_fake_belem_20
 - z_ikt_3_fake_belem_21 - z_ikt_3_fake_belem_22 - z_ikt_3_fake_belem_23
 - z_ikt_3_fake_belem_24 - z_ikt_3_fake_belem_25 - z_ikt_3_fake_belem_26
 - z_ikt_3_fake_belem_27 - z_ikt_3_fake_belem_28 - z_ikt_3_fake_belem_29
 - z_ikt_3_fake_belem_3 - z_ikt_3_fake_belem_30 - z_ikt_3_fake_belem_31
 - z_ikt_3_fake_belem_4 - z_ikt_3_fake_belem_5 - z_ikt_3_fake_belem_6
 - z_ikt_3_fake_belem_7 - z_ikt_3_fake_belem_8 - z_ikt_3_fake_belem_9
 - z_ikt_3_fake_manila_0 - z_ikt_3_fake_manila_1 - z_ikt_3_fake_manila_10
 - z_ikt_3_fake_manila_11 - z_ikt_3_fake_manila_12 - z_ikt_3_fake_manila_13
 - z_ikt_3_fake_manila_14 - z_ikt_3_fake_manila_15 - z_ikt_3_fake_manila_16
 - z_ikt_3_fake_manila_17 - z_ikt_3_fake_manila_18 - z_ikt_3_fake_manila_19
 - z_ikt_3_fake_manila_2 - z_ikt_3_fake_manila_20 - z_ikt_3_fake_manila_21
 - z_ikt_3_fake_manila_22 - z_ikt_3_fake_manila_23 - z_ikt_3_fake_manila_24
 - z_ikt_3_fake_manila_25 - z_ikt_3_fake_manila_26 - z_ikt_3_fake_manila_27
 - z_ikt_3_fake_manila_28 - z_ikt_3_fake_manila_29 - z_ikt_3_fake_manila_3
 - z_ikt_3_fake_manila_30 - z_ikt_3_fake_manila_31 - z_ikt_3_fake_manila_4
 - z_ikt_3_fake_manila_5 - z_ikt_3_fake_manila_6 - z_ikt_3_fake_manila_7
 - z_ikt_3_fake_manila_8 - z_ikt_3_fake_manila_9 = -1
_C207: - 1000000 x_ik_3_fake_belem + z_ikt_3_fake_belem_0
 + z_ikt_3_fake_belem_1 + z_ikt_3_fake_belem_10 + z_ikt_3_fake_belem_11
 + z_ikt_3_fake_belem_12 + z_ikt_3_fake_belem_13 + z_ikt_3_fake_belem_14
 + z_ikt_3_fake_belem_15 + z_ikt_3_fake_belem_16 + z_ikt_3_fake_belem_17
 + z_ikt_3_fake_belem_18 + z_ikt_3_fake_belem_19 + z_ikt_3_fake_belem_2
 + z_ikt_3_fake_belem_20 + z_ikt_3_fake_belem_21 + z_ikt_3_fake_belem_22
 + z_ikt_3_fake_belem_23 + z_ikt_3_fake_belem_24 + z_ikt_3_fake_belem_25
 + z_ikt_3_fake_belem_26 + z_ikt_3_fake_belem_27 + z_ikt_3_fake_belem_28
 + z_ikt_3_fake_belem_29 + z_ikt_3_fake_belem_3 + z_ikt_3_fake_belem_30
 + z_ikt_3_fake_belem_31 + z_ikt_3_fake_belem_4 + z_ikt_3_fake_belem_5
 + z_ikt_3_fake_belem_6 + z_ikt_3_fake_belem_7 + z_ikt_3_fake_belem_8
 + z_ikt_3_fake_belem_9 <= 0
_C208: - 1000000 x_ik_3_fake_manila + z_ikt_3_fake_manila_0
 + z_ikt_3_fake_manila_1 + z_ikt_3_fake_manila_10 + z_ikt_3_fake_manila_11
 + z_ikt_3_fake_manila_12 + z_ikt_3_fake_manila_13 + z_ikt_3_fake_manila_14
 + z_ikt_3_fake_manila_15 + z_ikt_3_fake_manila_16 + z_ikt_3_fake_manila_17
 + z_ikt_3_fake_manila_18 + z_ikt_3_fake_manila_19 + z_ikt_3_fake_manila_2
 + z_ikt_3_fake_manila_20 + z_ikt_3_fake_manila_21 + z_ikt_3_fake_manila_22
 + z_ikt_3_fake_manila_23 + z_ikt_3_fake_manila_24 + z_ikt_3_fake_manila_25
 + z_ikt_3_fake_manila_26 + z_ikt_3_fake_manila_27 + z_ikt_3_fake_manila_28
 + z_ikt_3_fake_manila_29 + z_ikt_3_fake_manila_3 + z_ikt_3_fake_manila_30
 + z_ikt_3_fake_manila_31 + z_ikt_3_fake_manila_4 + z_ikt_3_fake_manila_5
 + z_ikt_3_fake_manila_6 + z_ikt_3_fake_manila_7 + z_ikt_3_fake_manila_8
 + z_ikt_3_fake_manila_9 <= 0
_C209: - c_j_3 <= 0
_C21: s_j_1 + 999996 z_ikt_1_fake_belem_4 + 999996 z_ikt_1_fake_manila_4
 <= 1000000
_C210: z_ikt_3_fake_belem_0 + z_ikt_3_fake_manila_0 <= 1
_C211: s_j_3 + 1000000 z_ikt_3_fake_belem_0 + 1000000 z_ikt_3_fake_manila_0
 <= 1000000
_C212: - c_j_3 + z_ikt_3_fake_belem_1 + z_ikt_3_fake_manila_1 <= 0
_C213: z_ikt_3_fake_belem_1 + z_ikt_3_fake_manila_1 <= 1
_C214: s_j_3 + 999999 z_ikt_3_fake_belem_1 + 999999 z_ikt_3_fake_manila_1
 <= 1000000
_C215: - c_j_3 + 2 z_ikt_3_fake_belem_2 + 2 z_ikt_3_fake_manila_2 <= 0
_C216: z_ikt_3_fake_belem_2 + z_ikt_3_fake_manila_2 <= 1
_C217: s_j_3 + 999998 z_ikt_3_fake_belem_2 + 999998 z_ikt_3_fake_manila_2
 <= 1000000
_C218: - c_j_3 + 3 z_ikt_3_fake_belem_3 + 3 z_ikt_3_fake_manila_3 <= 0
_C219: z_ikt_3_fake_belem_3 + z_ikt_3_fake_manila_3 <= 1
_C22: - c_j_1 + 5 z_ikt_1_fake_belem_5 + 5 z_ikt_1_fake_manila_5 <= 0
_C220: s_j_3 + 999997 z_ikt_3_fake_belem_3 + 999997 z_ikt_3_fake_manila_3
 <= 1000000
_C221: - c_j_3 + 4 z_ikt_3_fake_belem_4 + 4 z_ikt_3_fake_manila_4 <= 0
_C222: z_ikt_3_fake_belem_4 + z_ikt_3_fake_manila_4 <= 1
_C223: s_j_3 + 999996 z_ikt_3_fake_belem_4 + 999996 z_ikt_3_fake_manila_4
 <= 1000000
_C224: - c_j_3 + 5 z_ikt_3_fake_belem_5 + 5 z_ikt_3_fake_manila_5 <= 0
_C225: z_ikt_3_fake_belem_5 + z_ikt_3_fake_manila_5 <= 1
_C226: s_j_3 + 999995 z_ikt_3_fake_belem_5 + 999995 z_ikt_3_fake_manila_5
 <= 1000000
_C227: - c_j_3 + 6 z_ikt_3_fake_belem_6 + 6 z_ikt_3_fake_manila_6 <= 0
_C228: z_ikt_3_fake_belem_6 + z_ikt_3_fake_manila_6 <= 1
_C229: s_j_3 + 999994 z_ikt_3_fake_belem_6 + 999994 z_ikt_3_fake_manila_6
 <= 1000000
_C23: z_ikt_1_fake_belem_5 + z_ikt_1_fake_manila_5 <= 1
_C230: - c_j_3 + 7 z_ikt_3_fake_belem_7 + 7 z_ikt_3_fake_manila_7 <= 0
_C231: z_ikt_3_fake_belem_7 + z_ikt_3_fake_manila_7 <= 1
_C232: s_j_3 + 999993 z_ikt_3_fake_belem_7 + 999993 z_ikt_3_fake_manila_7
 <= 1000000
_C233: - c_j_3 + 8 z_ikt_3_fake_belem_8 + 8 z_ikt_3_fake_manila_8 <= 0
_C234: z_ikt_3_fake_belem_8 + z_ikt_3_fake_manila_8 <= 1
_C235: s_j_3 + 999992 z_ikt_3_fake_belem_8 + 999992 z_ikt_3_fake_manila_8
 <= 1000000
_C236: - c_j_3 + 9 z_ikt_3_fake_belem_9 + 9 z_ikt_3_fake_manila_9 <= 0
_C237: z_ikt_3_fake_belem_9 + z_ikt_3_fake_manila_9 <= 1
_C238: s_j_3 + 999991 z_ikt_3_fake_belem_9 + 999991 z_ikt_3_fake_manila_9
 <= 1000000
_C239: - c_j_3 + 10 z_ikt_3_fake_belem_10 + 10 z_ikt_3_fake_manila_10 <= 0
_C24: s_j_1 + 999995 z_ikt_1_fake_belem_5 + 999995 z_ikt_1_fake_manila_5
 <= 1000000
_C240: z_ikt_3_fake_belem_10 + z_ikt_3_fake_manila_10 <= 1
_C241: s_j_3 + 999990 z_ikt_3_fake_belem_10 + 999990 z_ikt_3_fake_manila_10
 <= 1000000
_C242: - c_j_3 + 11 z_ikt_3_fake_belem_11 + 11 z_ikt_3_fake_manila_11 <= 0
_C243: z_ikt_3_fake_belem_11 + z_ikt_3_fake_manila_11 <= 1
_C244: s_j_3 + 999989 z_ikt_3_fake_belem_11 + 999989 z_ikt_3_fake_manila_11
 <= 1000000
_C245: - c_j_3 + 12 z_ikt_3_fake_belem_12 + 12 z_ikt_3_fake_manila_12 <= 0
_C246: z_ikt_3_fake_belem_12 + z_ikt_3_fake_manila_12 <= 1
_C247: s_j_3 + 999988 z_ikt_3_fake_belem_12 + 999988 z_ikt_3_fake_manila_12
 <= 1000000
_C248: - c_j_3 + 13 z_ikt_3_fake_belem_13 + 13 z_ikt_3_fake_manila_13 <= 0
_C249: z_ikt_3_fake_belem_13 + z_ikt_3_fake_manila_13 <= 1
_C25: - c_j_1 + 6 z_ikt_1_fake_belem_6 + 6 z_ikt_1_fake_manila_6 <= 0
_C250: s_j_3 + 999987 z_ikt_3_fake_belem_13 + 999987 z_ikt_3_fake_manila_13
 <= 1000000
_C251: - c_j_3 + 14 z_ikt_3_fake_belem_14 + 14 z_ikt_3_fake_manila_14 <= 0
_C252: z_ikt_3_fake_belem_14 + z_ikt_3_fake_manila_14 <= 1
_C253: s_j_3 + 999986 z_ikt_3_fake_belem_14 + 999986 z_ikt_3_fake_manila_14
 <= 1000000
_C254: - c_j_3 + 15 z_ikt_3_fake_belem_15 + 15 z_ikt_3_fake_manila_15 <= 0
_C255: z_ikt_3_fake_belem_15 + z_ikt_3_fake_manila_15 <= 1
_C256: s_j_3 + 999985 z_ikt_3_fake_belem_15 + 999985 z_ikt_3_fake_manila_15
 <= 1000000
_C257: - c_j_3 + 16 z_ikt_3_fake_belem_16 + 16 z_ikt_3_fake_manila_16 <= 0
_C258: z_ikt_3_fake_belem_16 + z_ikt_3_fake_manila_16 <= 1
_C259: s_j_3 + 999984 z_ikt_3_fake_belem_16 + 999984 z_ikt_3_fake_manila_16
 <= 1000000
_C26: z_ikt_1_fake_belem_6 + z_ikt_1_fake_manila_6 <= 1
_C260: - c_j_3 + 17 z_ikt_3_fake_belem_17 + 17 z_ikt_3_fake_manila_17 <= 0
_C261: z_ikt_3_fake_belem_17 + z_ikt_3_fake_manila_17 <= 1
_C262: s_j_3 + 999983 z_ikt_3_fake_belem_17 + 999983 z_ikt_3_fake_manila_17
 <= 1000000
_C263: - c_j_3 + 18 z_ikt_3_fake_belem_18 + 18 z_ikt_3_fake_manila_18 <= 0
_C264: z_ikt_3_fake_belem_18 + z_ikt_3_fake_manila_18 <= 1
_C265: s_j_3 + 999982 z_ikt_3_fake_belem_18 + 999982 z_ikt_3_fake_manila_18
 <= 1000000
_C266: - c_j_3 + 19 z_ikt_3_fake_belem_19 + 19 z_ikt_3_fake_manila_19 <= 0
_C267: z_ikt_3_fake_belem_19 + z_ikt_3_fake_manila_19 <= 1
_C268: s_j_3 + 999981 z_ikt_3_fake_belem_19 + 999981 z_ikt_3_fake_manila_19
 <= 1000000
_C269: - c_j_3 + 20 z_ikt_3_fake_belem_20 + 20 z_ikt_3_fake_manila_20 <= 0
_C27: s_j_1 + 999994 z_ikt_1_fake_belem_6 + 999994 z_ikt_1_fake_manila_6
 <= 1000000
_C270: z_ikt_3_fake_belem_20 + z_ikt_3_fake_manila_20 <= 1
_C271: s_j_3 + 999980 z_ikt_3_fake_belem_20 + 999980 z_ikt_3_fake_manila_20
 <= 1000000
_C272: - c_j_3 + 21 z_ikt_3_fake_belem_21 + 21 z_ikt_3_fake_manila_21 <= 0
_C273: z_ikt_3_fake_belem_21 + z_ikt_3_fake_manila_21 <= 1
_C274: s_j_3 + 999979 z_ikt_3_fake_belem_21 + 999979 z_ikt_3_fake_manila_21
 <= 1000000
_C275: - c_j_3 + 22 z_ikt_3_fake_belem_22 + 22 z_ikt_3_fake_manila_22 <= 0
_C276: z_ikt_3_fake_belem_22 + z_ikt_3_fake_manila_22 <= 1
_C277: s_j_3 + 999978 z_ikt_3_fake_belem_22 + 999978 z_ikt_3_fake_manila_22
 <= 1000000
_C278: - c_j_3 + 23 z_ikt_3_fake_belem_23 + 23 z_ikt_3_fake_manila_23 <= 0
_C279: z_ikt_3_fake_belem_23 + z_ikt_3_fake_manila_23 <= 1
_C28: - c_j_1 + 7 z_ikt_1_fake_belem_7 + 7 z_ikt_1_fake_manila_7 <= 0
_C280: s_j_3 + 999977 z_ikt_3_fake_belem_23 + 999977 z_ikt_3_fake_manila_23
 <= 1000000
_C281: - c_j_3 + 24 z_ikt_3_fake_belem_24 + 24 z_ikt_3_fake_manila_24 <= 0
_C282: z_ikt_3_fake_belem_24 + z_ikt_3_fake_manila_24 <= 1
_C283: s_j_3 + 999976 z_ikt_3_fake_belem_24 + 999976 z_ikt_3_fake_manila_24
 <= 1000000
_C284: - c_j_3 + 25 z_ikt_3_fake_belem_25 + 25 z_ikt_3_fake_manila_25 <= 0
_C285: z_ikt_3_fake_belem_25 + z_ikt_3_fake_manila_25 <= 1
_C286: s_j_3 + 999975 z_ikt_3_fake_belem_25 + 999975 z_ikt_3_fake_manila_25
 <= 1000000
_C287: - c_j_3 + 26 z_ikt_3_fake_belem_26 + 26 z_ikt_3_fake_manila_26 <= 0
_C288: z_ikt_3_fake_belem_26 + z_ikt_3_fake_manila_26 <= 1
_C289: s_j_3 + 999974 z_ikt_3_fake_belem_26 + 999974 z_ikt_3_fake_manila_26
 <= 1000000
_C29: z_ikt_1_fake_belem_7 + z_ikt_1_fake_manila_7 <= 1
_C290: - c_j_3 + 27 z_ikt_3_fake_belem_27 + 27 z_ikt_3_fake_manila_27 <= 0
_C291: z_ikt_3_fake_belem_27 + z_ikt_3_fake_manila_27 <= 1
_C292: s_j_3 + 999973 z_ikt_3_fake_belem_27 + 999973 z_ikt_3_fake_manila_27
 <= 1000000
_C293: - c_j_3 + 28 z_ikt_3_fake_belem_28 + 28 z_ikt_3_fake_manila_28 <= 0
_C294: z_ikt_3_fake_belem_28 + z_ikt_3_fake_manila_28 <= 1
_C295: s_j_3 + 999972 z_ikt_3_fake_belem_28 + 999972 z_ikt_3_fake_manila_28
 <= 1000000
_C296: - c_j_3 + 29 z_ikt_3_fake_belem_29 + 29 z_ikt_3_fake_manila_29 <= 0
_C297: z_ikt_3_fake_belem_29 + z_ikt_3_fake_manila_29 <= 1
_C298: s_j_3 + 999971 z_ikt_3_fake_belem_29 + 999971 z_ikt_3_fake_manila_29
 <= 1000000
_C299: - c_j_3 + 30 z_ikt_3_fake_belem_30 + 30 z_ikt_3_fake_manila_30 <= 0
_C3: x_ik_1_fake_belem + x_ik_1_fake_manila = 1
_C30: s_j_1 + 999993 z_ikt_1_fake_belem_7 + 999993 z_ikt_1_fake_manila_7
 <= 1000000
_C300: z_ikt_3_fake_belem_30 + z_ikt_3_fake_manila_30 <= 1
_C301: s_j_3 + 999970 z_ikt_3_fake_belem_30 + 999970 z_ikt_3_fake_manila_30
 <= 1000000
_C302: - c_j_3 + 31 z_ikt_3_fake_belem_31 + 31 z_ikt_3_fake_manila_31 <= 0
_C303: z_ikt_3_fake_belem_31 + z_ikt_3_fake_manila_31 <= 1
_C304: s_j_3 + 999969 z_ikt_3_fake_belem_31 + 999969 z_ikt_3_fake_manila_31
 <= 1000000
_C305: 2 z_ikt_1_fake_belem_0 + 2 z_ikt_2_fake_belem_0
 + 2 z_ikt_3_fake_belem_0 <= 5
_C306: 2 z_ikt_1_fake_manila_0 + 2 z_ikt_2_fake_manila_0
 + 2 z_ikt_3_fake_manila_0 <= 5
_C307: 2 z_ikt_1_fake_belem_1 + 2 z_ikt_2_fake_belem_1
 + 2 z_ikt_3_fake_belem_1 <= 5
_C308: 2 z_ikt_1_fake_manila_1 + 2 z_ikt_2_fake_manila_1
 + 2 z_ikt_3_fake_manila_1 <= 5
_C309: 2 z_ikt_1_fake_belem_2 + 2 z_ikt_2_fake_belem_2
 + 2 z_ikt_3_fake_belem_2 <= 5
_C31: - c_j_1 + 8 z_ikt_1_fake_belem_8 + 8 z_ikt_1_fake_manila_8 <= 0
_C310: 2 z_ikt_1_fake_manila_2 + 2 z_ikt_2_fake_manila_2
 + 2 z_ikt_3_fake_manila_2 <= 5
_C311: 2 z_ikt_1_fake_belem_3 + 2 z_ikt_2_fake_belem_3
 + 2 z_ikt_3_fake_belem_3 <= 5
_C312: 2 z_ikt_1_fake_manila_3 + 2 z_ikt_2_fake_manila_3
 + 2 z_ikt_3_fake_manila_3 <= 5
_C313: 2 z_ikt_1_fake_belem_4 + 2 z_ikt_2_fake_belem_4
 + 2 z_ikt_3_fake_belem_4 <= 5
_C314: 2 z_ikt_1_fake_manila_4 + 2 z_ikt_2_fake_manila_4
 + 2 z_ikt_3_fake_manila_4 <= 5
_C315: 2 z_ikt_1_fake_belem_5 + 2 z_ikt_2_fake_belem_5
 + 2 z_ikt_3_fake_belem_5 <= 5
_C316: 2 z_ikt_1_fake_manila_5 + 2 z_ikt_2_fake_manila_5
 + 2 z_ikt_3_fake_manila_5 <= 5
_C317: 2 z_ikt_1_fake_belem_6 + 2 z_ikt_2_fake_belem_6
 + 2 z_ikt_3_fake_belem_6 <= 5
_C318: 2 z_ikt_1_fake_manila_6 + 2 z_ikt_2_fake_manila_6
 + 2 z_ikt_3_fake_manila_6 <= 5
_C319: 2 z_ikt_1_fake_belem_7 + 2 z_ikt_2_fake_belem_7
 + 2 z_ikt_3_fake_belem_7 <= 5
_C32: z_ikt_1_fake_belem_8 + z_ikt_1_fake_manila_8 <= 1
_C320: 2 z_ikt_1_fake_manila_7 + 2 z_ikt_2_fake_manila_7
 + 2 z_ikt_3_fake_manila_7 <= 5
_C321: 2 z_ikt_1_fake_belem_8 + 2 z_ikt_2_fake_belem_8
 + 2 z_ikt_3_fake_belem_8 <= 5
_C322: 2 z_ikt_1_fake_manila_8 + 2 z_ikt_2_fake_manila_8
 + 2 z_ikt_3_fake_manila_8 <= 5
_C323: 2 z_ikt_1_fake_belem_9 + 2 z_ikt_2_fake_belem_9
 + 2 z_ikt_3_fake_belem_9 <= 5
_C324: 2 z_ikt_1_fake_manila_9 + 2 z_ikt_2_fake_manila_9
 + 2 z_ikt_3_fake_manila_9 <= 5
_C325: 2 z_ikt_1_fake_belem_10 + 2 z_ikt_2_fake_belem_10
 + 2 z_ikt_3_fake_belem_10 <= 5
_C326: 2 z_ikt_1_fake_manila_10 + 2 z_ikt_2_fake_manila_10
 + 2 z_ikt_3_fake_manila_10 <= 5
_C327: 2 z_ikt_1_fake_belem_11 + 2 z_ikt_2_fake_belem_11
 + 2 z_ikt_3_fake_belem_11 <= 5
_C328: 2 z_ikt_1_fake_manila_11 + 2 z_ikt_2_fake_manila_11
 + 2 z_ikt_3_fake_manila_11 <= 5
_C329: 2 z_ikt_1_fake_belem_12 + 2 z_ikt_2_fake_belem_12
 + 2 z_ikt_3_fake_belem_12 <= 5
_C33: s_j_1 + 999992 z_ikt_1_fake_belem_8 + 999992 z_ikt_1_fake_manila_8
 <= 1000000
_C330: 2 z_ikt_1_fake_manila_12 + 2 z_ikt_2_fake_manila_12
 + 2 z_ikt_3_fake_manila_12 <= 5
_C331: 2 z_ikt_1_fake_belem_13 + 2 z_ikt_2_fake_belem_13
 + 2 z_ikt_3_fake_belem_13 <= 5
_C332: 2 z_ikt_1_fake_manila_13 + 2 z_ikt_2_fake_manila_13
 + 2 z_ikt_3_fake_manila_13 <= 5
_C333: 2 z_ikt_1_fake_belem_14 + 2 z_ikt_2_fake_belem_14
 + 2 z_ikt_3_fake_belem_14 <= 5
_C334: 2 z_ikt_1_fake_manila_14 + 2 z_ikt_2_fake_manila_14
 + 2 z_ikt_3_fake_manila_14 <= 5
_C335: 2 z_ikt_1_fake_belem_15 + 2 z_ikt_2_fake_belem_15
 + 2 z_ikt_3_fake_belem_15 <= 5
_C336: 2 z_ikt_1_fake_manila_15 + 2 z_ikt_2_fake_manila_15
 + 2 z_ikt_3_fake_manila_15 <= 5
_C337: 2 z_ikt_1_fake_belem_16 + 2 z_ikt_2_fake_belem_16
 + 2 z_ikt_3_fake_belem_16 <= 5
_C338: 2 z_ikt_1_fake_manila_16 + 2 z_ikt_2_fake_manila_16
 + 2 z_ikt_3_fake_manila_16 <= 5
_C339: 2 z_ikt_1_fake_belem_17 + 2 z_ikt_2_fake_belem_17
 + 2 z_ikt_3_fake_belem_17 <= 5
_C34: - c_j_1 + 9 z_ikt_1_fake_belem_9 + 9 z_ikt_1_fake_manila_9 <= 0
_C340: 2 z_ikt_1_fake_manila_17 + 2 z_ikt_2_fake_manila_17
 + 2 z_ikt_3_fake_manila_17 <= 5
_C341: 2 z_ikt_1_fake_belem_18 + 2 z_ikt_2_fake_belem_18
 + 2 z_ikt_3_fake_belem_18 <= 5
_C342: 2 z_ikt_1_fake_manila_18 + 2 z_ikt_2_fake_manila_18
 + 2 z_ikt_3_fake_manila_18 <= 5
_C343: 2 z_ikt_1_fake_belem_19 + 2 z_ikt_2_fake_belem_19
 + 2 z_ikt_3_fake_belem_19 <= 5
_C344: 2 z_ikt_1_fake_manila_19 + 2 z_ikt_2_fake_manila_19
 + 2 z_ikt_3_fake_manila_19 <= 5
_C345: 2 z_ikt_1_fake_belem_20 + 2 z_ikt_2_fake_belem_20
 + 2 z_ikt_3_fake_belem_20 <= 5
_C346: 2 z_ikt_1_fake_manila_20 + 2 z_ikt_2_fake_manila_20
 + 2 z_ikt_3_fake_manila_20 <= 5
_C347: 2 z_ikt_1_fake_belem_21 + 2 z_ikt_2_fake_belem_21
 + 2 z_ikt_3_fake_belem_21 <= 5
_C348: 2 z_ikt_1_fake_manila_21 + 2 z_ikt_2_fake_manila_21
 + 2 z_ikt_3_fake_manila_21 <= 5
_C349: 2 z_ikt_1_fake_belem_22 + 2 z_ikt_2_fake_belem_22
 + 2 z_ikt_3_fake_belem_22 <= 5
_C35: z_ikt_1_fake_belem_9 + z_ikt_1_fake_manila_9 <= 1
_C350: 2 z_ikt_1_fake_manila_22 + 2 z_ikt_2_fake_manila_22
 + 2 z_ikt_3_fake_manila_22 <= 5
_C351: 2 z_ikt_1_fake_belem_23 + 2 z_ikt_2_fake_belem_23
 + 2 z_ikt_3_fake_belem_23 <= 5
_C352: 2 z_ikt_1_fake_manila_23 + 2 z_ikt_2_fake_manila_23
 + 2 z_ikt_3_fake_manila_23 <= 5
_C353: 2 z_ikt_1_fake_belem_24 + 2 z_ikt_2_fake_belem_24
 + 2 z_ikt_3_fake_belem_24 <= 5
_C354: 2 z_ikt_1_fake_manila_24 + 2 z_ikt_2_fake_manila_24
 + 2 z_ikt_3_fake_manila_24 <= 5
_C355: 2 z_ikt_1_fake_belem_25 + 2 z_ikt_2_fake_belem_25
 + 2 z_ikt_3_fake_belem_25 <= 5
_C356: 2 z_ikt_1_fake_manila_25 + 2 z_ikt_2_fake_manila_25
 + 2 z_ikt_3_fake_manila_25 <= 5
_C357: 2 z_ikt_1_fake_belem_26 + 2 z_ikt_2_fake_belem_26
 + 2 z_ikt_3_fake_belem_26 <= 5
_C358: 2 z_ikt_1_fake_manila_26 + 2 z_ikt_2_fake_manila_26
 + 2 z_ikt_3_fake_manila_26 <= 5
_C359: 2 z_ikt_1_fake_belem_27 + 2 z_ikt_2_fake_belem_27
 + 2 z_ikt_3_fake_belem_27 <= 5
_C36: s_j_1 + 999991 z_ikt_1_fake_belem_9 + 999991 z_ikt_1_fake_manila_9
 <= 1000000
_C360: 2 z_ikt_1_fake_manila_27 + 2 z_ikt_2_fake_manila_27
 + 2 z_ikt_3_fake_manila_27 <= 5
_C361: 2 z_ikt_1_fake_belem_28 + 2 z_ikt_2_fake_belem_28
 + 2 z_ikt_3_fake_belem_28 <= 5
_C362: 2 z_ikt_1_fake_manila_28 + 2 z_ikt_2_fake_manila_28
 + 2 z_ikt_3_fake_manila_28 <= 5
_C363: 2 z_ikt_1_fake_belem_29 + 2 z_ikt_2_fake_belem_29
 + 2 z_ikt_3_fake_belem_29 <= 5
_C364: 2 z_ikt_1_fake_manila_29 + 2 z_ikt_2_fake_manila_29
 + 2 z_ikt_3_fake_manila_29 <= 5
_C365: 2 z_ikt_1_fake_belem_30 + 2 z_ikt_2_fake_belem_30
 + 2 z_ikt_3_fake_belem_30 <= 5
_C366: 2 z_ikt_1_fake_manila_30 + 2 z_ikt_2_fake_manila_30
 + 2 z_ikt_3_fake_manila_30 <= 5
_C367: 2 z_ikt_1_fake_belem_31 + 2 z_ikt_2_fake_belem_31
 + 2 z_ikt_3_fake_belem_31 <= 5
_C368: 2 z_ikt_1_fake_manila_31 + 2 z_ikt_2_fake_manila_31
 + 2 z_ikt_3_fake_manila_31 <= 5
_C369: y_ijk_0_1_fake_belem + y_ijk_0_1_fake_manila + y_ijk_1_1_fake_belem
 + y_ijk_1_1_fake_manila + y_ijk_2_1_fake_belem + y_ijk_2_1_fake_manila
 + y_ijk_3_1_fake_belem + y_ijk_3_1_fake_manila >= 1
_C37: - c_j_1 + 10 z_ikt_1_fake_belem_10 + 10 z_ikt_1_fake_manila_10 <= 0
_C370: c_j_1 - s_j_1 - 7 x_ik_1_fake_belem - 5 x_ik_1_fake_manila
 - 50 y_ijk_1_1_fake_belem - 50 y_ijk_1_1_fake_manila - 6 y_ijk_2_1_fake_belem
 - 8 y_ijk_2_1_fake_manila - 8 y_ijk_3_1_fake_belem - 8 y_ijk_3_1_fake_manila
 >= 0
_C371: x_ik_1_fake_belem - 0.001 y_ijk_0_1_fake_belem
 - 0.001 y_ijk_1_1_fake_belem - 0.001 y_ijk_2_1_fake_belem
 - 0.001 y_ijk_3_1_fake_belem >= 0
_C372: x_ik_1_fake_belem - 0.001 y_ijk_1_0_fake_belem
 - 0.001 y_ijk_1_1_fake_belem - 0.001 y_ijk_1_2_fake_belem
 - 0.001 y_ijk_1_3_fake_belem >= 0
_C373: - y_ijk_0_1_fake_belem + z_ikt_1_fake_belem_0 = 0
_C374: x_ik_1_fake_manila - 0.001 y_ijk_0_1_fake_manila
 - 0.001 y_ijk_1_1_fake_manila - 0.001 y_ijk_2_1_fake_manila
 - 0.001 y_ijk_3_1_fake_manila >= 0
_C375: x_ik_1_fake_manila - 0.001 y_ijk_1_0_fake_manila
 - 0.001 y_ijk_1_1_fake_manila - 0.001 y_ijk_1_2_fake_manila
 - 0.001 y_ijk_1_3_fake_manila >= 0
_C376: - y_ijk_0_1_fake_manila + z_ikt_1_fake_manila_0 = 0
_C377: c_j_0 - s_j_1 + 1000 y_ijk_0_1_fake_belem + 1000 y_ijk_0_1_fake_manila
 <= 1000
_C378: c_j_1 - s_j_1 + 1000 y_ijk_1_1_fake_belem + 1000 y_ijk_1_1_fake_manila
 <= 1000
_C379: c_j_2 - s_j_1 + 1000 y_ijk_2_1_fake_belem + 1000 y_ijk_2_1_fake_manila
 <= 1000
_C38: z_ikt_1_fake_belem_10 + z_ikt_1_fake_manila_10 <= 1
_C380: c_j_3 - s_j_1 + 1000 y_ijk_3_1_fake_belem + 1000 y_ijk_3_1_fake_manila
 <= 1000
_C381: y_ijk_0_2_fake_belem + y_ijk_0_2_fake_manila + y_ijk_1_2_fake_belem
 + y_ijk_1_2_fake_manila + y_ijk_2_2_fake_belem + y_ijk_2_2_fake_manila
 + y_ijk_3_2_fake_belem + y_ijk_3_2_fake_manila >= 1
_C382: c_j_2 - s_j_2 - 8 x_ik_2_fake_belem - 6 x_ik_2_fake_manila
 - 6 y_ijk_1_2_fake_belem - 8 y_ijk_1_2_fake_manila - 50 y_ijk_2_2_fake_belem
 - 50 y_ijk_2_2_fake_manila - 5 y_ijk_3_2_fake_belem - 9 y_ijk_3_2_fake_manila
 >= 0
_C383: x_ik_2_fake_belem - 0.001 y_ijk_0_2_fake_belem
 - 0.001 y_ijk_1_2_fake_belem - 0.001 y_ijk_2_2_fake_belem
 - 0.001 y_ijk_3_2_fake_belem >= 0
_C384: x_ik_2_fake_belem - 0.001 y_ijk_2_0_fake_belem
 - 0.001 y_ijk_2_1_fake_belem - 0.001 y_ijk_2_2_fake_belem
 - 0.001 y_ijk_2_3_fake_belem >= 0
_C385: - y_ijk_0_2_fake_belem + z_ikt_2_fake_belem_0 = 0
_C386: x_ik_2_fake_manila - 0.001 y_ijk_0_2_fake_manila
 - 0.001 y_ijk_1_2_fake_manila - 0.001 y_ijk_2_2_fake_manila
 - 0.001 y_ijk_3_2_fake_manila >= 0
_C387: x_ik_2_fake_manila - 0.001 y_ijk_2_0_fake_manila
 - 0.001 y_ijk_2_1_fake_manila - 0.001 y_ijk_2_2_fake_manila
 - 0.001 y_ijk_2_3_fake_manila >= 0
_C388: - y_ijk_0_2_fake_manila + z_ikt_2_fake_manila_0 = 0
_C389: c_j_0 - s_j_2 + 1000 y_ijk_0_2_fake_belem + 1000 y_ijk_0_2_fake_manila
 <= 1000
_C39: s_j_1 + 999990 z_ikt_1_fake_belem_10 + 999990 z_ikt_1_fake_manila_10
 <= 1000000
_C390: c_j_1 - s_j_2 + 1000 y_ijk_1_2_fake_belem + 1000 y_ijk_1_2_fake_manila
 <= 1000
_C391: c_j_2 - s_j_2 + 1000 y_ijk_2_2_fake_belem + 1000 y_ijk_2_2_fake_manila
 <= 1000
_C392: c_j_3 - s_j_2 + 1000 y_ijk_3_2_fake_belem + 1000 y_ijk_3_2_fake_manila
 <= 1000
_C393: y_ijk_0_3_fake_belem + y_ijk_0_3_fake_manila + y_ijk_1_3_fake_belem
 + y_ijk_1_3_fake_manila + y_ijk_2_3_fake_belem + y_ijk_2_3_fake_manila
 + y_ijk_3_3_fake_belem + y_ijk_3_3_fake_manila >= 1
_C394: c_j_3 - s_j_3 - 8 x_ik_3_fake_belem - 6 x_ik_3_fake_manila
 - 9 y_ijk_1_3_fake_belem - 6 y_ijk_1_3_fake_manila - 6 y_ijk_2_3_fake_belem
 - 6 y_ijk_2_3_fake_manila - 50 y_ijk_3_3_fake_belem
 - 50 y_ijk_3_3_fake_manila >= 0
_C395: x_ik_3_fake_belem - 0.001 y_ijk_0_3_fake_belem
 - 0.001 y_ijk_1_3_fake_belem - 0.001 y_ijk_2_3_fake_belem
 - 0.001 y_ijk_3_3_fake_belem >= 0
_C396: x_ik_3_fake_belem - 0.001 y_ijk_3_0_fake_belem
 - 0.001 y_ijk_3_1_fake_belem - 0.001 y_ijk_3_2_fake_belem
 - 0.001 y_ijk_3_3_fake_belem >= 0
_C397: - y_ijk_0_3_fake_belem + z_ikt_3_fake_belem_0 = 0
_C398: x_ik_3_fake_manila - 0.001 y_ijk_0_3_fake_manila
 - 0.001 y_ijk_1_3_fake_manila - 0.001 y_ijk_2_3_fake_manila
 - 0.001 y_ijk_3_3_fake_manila >= 0
_C399: x_ik_3_fake_manila - 0.001 y_ijk_3_0_fake_manila
 - 0.001 y_ijk_3_1_fake_manila - 0.001 y_ijk_3_2_fake_manila
 - 0.001 y_ijk_3_3_fake_manila >= 0
_C4: c_j_1 - s_j_1 - z_ikt_1_fake_belem_0 - z_ikt_1_fake_belem_1
 - z_ikt_1_fake_belem_10 - z_ikt_1_fake_belem_11 - z_ikt_1_fake_belem_12
 - z_ikt_1_fake_belem_13 - z_ikt_1_fake_belem_14 - z_ikt_1_fake_belem_15
 - z_ikt_1_fake_belem_16 - z_ikt_1_fake_belem_17 - z_ikt_1_fake_belem_18
 - z_ikt_1_fake_belem_19 - z_ikt_1_fake_belem_2 - z_ikt_1_fake_belem_20
 - z_ikt_1_fake_belem_21 - z_ikt_1_fake_belem_22 - z_ikt_1_fake_belem_23
 - z_ikt_1_fake_belem_24 - z_ikt_1_fake_belem_25 - z_ikt_1_fake_belem_26
 - z_ikt_1_fake_belem_27 - z_ikt_1_fake_belem_28 - z_ikt_1_fake_belem_29
 - z_ikt_1_fake_belem_3 - z_ikt_1_fake_belem_30 - z_ikt_1_fake_belem_31
 - z_ikt_1_fake_belem_4 - z_ikt_1_fake_belem_5 - z_ikt_1_fake_belem_6
 - z_ikt_1_fake_belem_7 - z_ikt_1_fake_belem_8 - z_ikt_1_fake_belem_9
 - z_ikt_1_fake_manila_0 - z_ikt_1_fake_manila_1 - z_ikt_1_fake_manila_10
 - z_ikt_1_fake_manila_11 - z_ikt_1_fake_manila_12 - z_ikt_1_fake_manila_13
 - z_ikt_1_fake_manila_14 - z_ikt_1_fake_manila_15 - z_ikt_1_fake_manila_16
 - z_ikt_1_fake_manila_17 - z_ikt_1_fake_manila_18 - z_ikt_1_fake_manila_19
 - z_ikt_1_fake_manila_2 - z_ikt_1_fake_manila_20 - z_ikt_1_fake_manila_21
 - z_ikt_1_fake_manila_22 - z_ikt_1_fake_manila_23 - z_ikt_1_fake_manila_24
 - z_ikt_1_fake_manila_25 - z_ikt_1_fake_manila_26 - z_ikt_1_fake_manila_27
 - z_ikt_1_fake_manila_28 - z_ikt_1_fake_manila_29 - z_ikt_1_fake_manila_3
 - z_ikt_1_fake_manila_30 - z_ikt_1_fake_manila_31 - z_ikt_1_fake_manila_4
 - z_ikt_1_fake_manila_5 - z_ikt_1_fake_manila_6 - z_ikt_1_fake_manila_7
 - z_ikt_1_fake_manila_8 - z_ikt_1_fake_manila_9 = -1
_C40: - c_j_1 + 11 z_ikt_1_fake_belem_11 + 11 z_ikt_1_fake_manila_11 <= 0
_C400: - y_ijk_0_3_fake_manila + z_ikt_3_fake_manila_0 = 0
_C401: c_j_0 - s_j_3 + 1000 y_ijk_0_3_fake_belem + 1000 y_ijk_0_3_fake_manila
 <= 1000
_C402: c_j_1 - s_j_3 + 1000 y_ijk_1_3_fake_belem + 1000 y_ijk_1_3_fake_manila
 <= 1000
_C403: c_j_2 - s_j_3 + 1000 y_ijk_2_3_fake_belem + 1000 y_ijk_2_3_fake_manila
 <= 1000
_C404: c_j_3 - s_j_3 + 1000 y_ijk_3_3_fake_belem + 1000 y_ijk_3_3_fake_manila
 <= 1000
_C405: a_ij_1_1 = 0
_C406: b_ij_1_1 = 0
_C407: a_ij_1_2 + 0.001 c_j_1 - 0.001 s_j_2 >= 0
_C408: b_ij_1_2 + 0.001 c_j_1 - 0.001 c_j_2 >= 0
_C409: d_ijk_1_2_fake_belem - x_ik_1_fake_belem - x_ik_2_fake_belem >= -1
_C41: z_ikt_1_fake_belem_11 + z_ikt_1_fake_manila_11 <= 1
_C410: - a_ij_1_2 - b_ij_1_1 - d_ijk_1_1_fake_belem - d_ijk_1_2_fake_belem
 + e_ijlk_1_2_1_fake_belem >= -3
_C411: - a_ij_2_2 - b_ij_1_2 - 2 d_ijk_1_2_fake_belem
 + e_ijlk_1_2_2_fake_belem >= -3
_C412: - a_ij_3_2 - b_ij_1_3 - d_ijk_1_2_fake_belem - d_ijk_1_3_fake_belem
 + e_ijlk_1_2_3_fake_belem >= -3
_C413: d_ijk_1_2_fake_manila - x_ik_1_fake_manila - x_ik_2_fake_manila >= -1
_C414: - a_ij_1_2 - b_ij_1_1 - d_ijk_1_1_fake_manila - d_ijk_1_2_fake_manila
 + e_ijlk_1_2_1_fake_manila >= -3
_C415: - a_ij_2_2 - b_ij_1_2 - 2 d_ijk_1_2_fake_manila
 + e_ijlk_1_2_2_fake_manila >= -3
_C416: - a_ij_3_2 - b_ij_1_3 - d_ijk_1_2_fake_manila - d_ijk_1_3_fake_manila
 + e_ijlk_1_2_3_fake_manila >= -3
_C417: a_ij_1_3 + 0.001 c_j_1 - 0.001 s_j_3 >= 0
_C418: b_ij_1_3 + 0.001 c_j_1 - 0.001 c_j_3 >= 0
_C419: d_ijk_1_3_fake_belem - x_ik_1_fake_belem - x_ik_3_fake_belem >= -1
_C42: s_j_1 + 999989 z_ikt_1_fake_belem_11 + 999989 z_ikt_1_fake_manila_11
 <= 1000000
_C420: - a_ij_1_3 - b_ij_1_1 - d_ijk_1_1_fake_belem - d_ijk_1_3_fake_belem
 + e_ijlk_1_3_1_fake_belem >= -3
_C421: - a_ij_2_3 - b_ij_1_2 - d_ijk_1_2_fake_belem - d_ijk_1_3_fake_belem
 + e_ijlk_1_3_2_fake_belem >= -3
_C422: - a_ij_3_3 - b_ij_1_3 - 2 d_ijk_1_3_fake_belem
 + e_ijlk_1_3_3_fake_belem >= -3
_C423: d_ijk_1_3_fake_manila - x_ik_1_fake_manila - x_ik_3_fake_manila >= -1
_C424: - a_ij_1_3 - b_ij_1_1 - d_ijk_1_1_fake_manila - d_ijk_1_3_fake_manila
 + e_ijlk_1_3_1_fake_manila >= -3
_C425: - a_ij_2_3 - b_ij_1_2 - d_ijk_1_2_fake_manila - d_ijk_1_3_fake_manila
 + e_ijlk_1_3_2_fake_manila >= -3
_C426: - a_ij_3_3 - b_ij_1_3 - 2 d_ijk_1_3_fake_manila
 + e_ijlk_1_3_3_fake_manila >= -3
_C427: a_ij_2_1 + 0.001 c_j_2 - 0.001 s_j_1 >= 0
_C428: b_ij_2_1 - 0.001 c_j_1 + 0.001 c_j_2 >= 0
_C429: d_ijk_2_1_fake_belem - x_ik_1_fake_belem - x_ik_2_fake_belem >= -1
_C43: - c_j_1 + 12 z_ikt_1_fake_belem_12 + 12 z_ikt_1_fake_manila_12 <= 0
_C430: - a_ij_1_1 - b_ij_2_1 - 2 d_ijk_2_1_fake_belem
 + e_ijlk_2_1_1_fake_belem >= -3
_C431: - a_ij_2_1 - b_ij_2_2 - d_ijk_2_1_fake_belem - d_ijk_2_2_fake_belem
 + e_ijlk_2_1_2_fake_belem >= -3
_C432: - a_ij_3_1 - b_ij_2_3 - d_ijk_2_1_fake_belem - d_ijk_2_3_fake_belem
 + e_ijlk_2_1_3_fake_belem >= -3
_C433: d_ijk_2_1_fake_manila - x_ik_1_fake_manila - x_ik_2_fake_manila >= -1
_C434: - a_ij_1_1 - b_ij_2_1 - 2 d_ijk_2_1_fake_manila
 + e_ijlk_2_1_1_fake_manila >= -3
_C435: - a_ij_2_1 - b_ij_2_2 - d_ijk_2_1_fake_manila - d_ijk_2_2_fake_manila
 + e_ijlk_2_1_2_fake_manila >= -3
_C436: - a_ij_3_1 - b_ij_2_3 - d_ijk_2_1_fake_manila - d_ijk_2_3_fake_manila
 + e_ijlk_2_1_3_fake_manila >= -3
_C437: a_ij_2_2 = 0
_C438: b_ij_2_2 = 0
_C439: a_ij_2_3 + 0.001 c_j_2 - 0.001 s_j_3 >= 0
_C44: z_ikt_1_fake_belem_12 + z_ikt_1_fake_manila_12 <= 1
_C440: b_ij_2_3 + 0.001 c_j_2 - 0.001 c_j_3 >= 0
_C441: d_ijk_2_3_fake_belem - x_ik_2_fake_belem - x_ik_3_fake_belem >= -1
_C442: - a_ij_1_3 - b_ij_2_1 - d_ijk_2_1_fake_belem - d_ijk_2_3_fake_belem
 + e_ijlk_2_3_1_fake_belem >= -3
_C443: - a_ij_2_3 - b_ij_2_2 - d_ijk_2_2_fake_belem - d_ijk_2_3_fake_belem
 + e_ijlk_2_3_2_fake_belem >= -3
_C444: - a_ij_3_3 - b_ij_2_3 - 2 d_ijk_2_3_fake_belem
 + e_ijlk_2_3_3_fake_belem >= -3
_C445: d_ijk_2_3_fake_manila - x_ik_2_fake_manila - x_ik_3_fake_manila >= -1
_C446: - a_ij_1_3 - b_ij_2_1 - d_ijk_2_1_fake_manila - d_ijk_2_3_fake_manila
 + e_ijlk_2_3_1_fake_manila >= -3
_C447: - a_ij_2_3 - b_ij_2_2 - d_ijk_2_2_fake_manila - d_ijk_2_3_fake_manila
 + e_ijlk_2_3_2_fake_manila >= -3
_C448: - a_ij_3_3 - b_ij_2_3 - 2 d_ijk_2_3_fake_manila
 + e_ijlk_2_3_3_fake_manila >= -3
_C449: a_ij_3_1 + 0.001 c_j_3 - 0.001 s_j_1 >= 0
_C45: s_j_1 + 999988 z_ikt_1_fake_belem_12 + 999988 z_ikt_1_fake_manila_12
 <= 1000000
_C450: b_ij_3_1 - 0.001 c_j_1 + 0.001 c_j_3 >= 0
_C451: d_ijk_3_1_fake_belem - x_ik_1_fake_belem - x_ik_3_fake_belem >= -1
_C452: - a_ij_1_1 - b_ij_3_1 - 2 d_ijk_3_1_fake_belem
 + e_ijlk_3_1_1_fake_belem >= -3
_C453: - a_ij_2_1 - b_ij_3_2 - d_ijk_3_1_fake_belem - d_ijk_3_2_fake_belem
 + e_ijlk_3_1_2_fake_belem >= -3
_C454: - a_ij_3_1 - b_ij_3_3 - d_ijk_3_1_fake_belem - d_ijk_3_3_fake_belem
 + e_ijlk_3_1_3_fake_belem >= -3
_C455: d_ijk_3_1_fake_manila - x_ik_1_fake_manila - x_ik_3_fake_manila >= -1
_C456: - a_ij_1_1 - b_ij_3_1 - 2 d_ijk_3_1_fake_manila
 + e_ijlk_3_1_1_fake_manila >= -3
_C457: - a_ij_2_1 - b_ij_3_2 - d_ijk_3_1_fake_manila - d_ijk_3_2_fake_manila
 + e_ijlk_3_1_2_fake_manila >= -3
_C458: - a_ij_3_1 - b_ij_3_3 - d_ijk_3_1_fake_manila - d_ijk_3_3_fake_manila
 + e_ijlk_3_1_3_fake_manila >= -3
_C459: a_ij_3_2 + 0.001 c_j_3 - 0.001 s_j_2 >= 0
_C46: - c_j_1 + 13 z_ikt_1_fake_belem_13 + 13 z_ikt_1_fake_manila_13 <= 0
_C460: b_ij_3_2 - 0.001 c_j_2 + 0.001 c_j_3 >= 0
_C461: d_ijk_3_2_fake_belem - x_ik_2_fake_belem - x_ik_3_fake_belem >= -1
_C462: - a_ij_1_2 - b_ij_3_1 - d_ijk_3_1_fake_belem - d_ijk_3_2_fake_belem
 + e_ijlk_3_2_1_fake_belem >= -3
_C463: - a_ij_2_2 - b_ij_3_2 - 2 d_ijk_3_2_fake_belem
 + e_ijlk_3_2_2_fake_belem >= -3
_C464: - a_ij_3_2 - b_ij_3_3 - d_ijk_3_2_fake_belem - d_ijk_3_3_fake_belem
 + e_ijlk_3_2_3_fake_belem >= -3
_C465: d_ijk_3_2_fake_manila - x_ik_2_fake_manila - x_ik_3_fake_manila >= -1
_C466: - a_ij_1_2 - b_ij_3_1 - d_ijk_3_1_fake_manila - d_ijk_3_2_fake_manila
 + e_ijlk_3_2_1_fake_manila >= -3
_C467: - a_ij_2_2 - b_ij_3_2 - 2 d_ijk_3_2_fake_manila
 + e_ijlk_3_2_2_fake_manila >= -3
_C468: - a_ij_3_2 - b_ij_3_3 - d_ijk_3_2_fake_manila - d_ijk_3_3_fake_manila
 + e_ijlk_3_2_3_fake_manila >= -3
_C469: a_ij_3_3 = 0
_C47: z_ikt_1_fake_belem_13 + z_ikt_1_fake_manila_13 <= 1
_C470: b_ij_3_3 = 0
_C471: - a_ij_1_1 - d_ijk_1_1_fake_belem - 0.001 e_ijlk_1_1_1_fake_belem
 - 0.001 e_ijlk_1_1_2_fake_belem - 0.001 e_ijlk_1_1_3_fake_belem
 + y_ijk_1_1_fake_belem >= -2
_C472: - a_ij_1_1 - d_ijk_1_1_fake_manila - 0.001 e_ijlk_1_1_1_fake_manila
 - 0.001 e_ijlk_1_1_2_fake_manila - 0.001 e_ijlk_1_1_3_fake_manila
 + y_ijk_1_1_fake_manila >= -2
_C473: - a_ij_1_2 - d_ijk_1_2_fake_belem - 0.001 e_ijlk_1_2_1_fake_belem
 - 0.001 e_ijlk_1_2_2_fake_belem - 0.001 e_ijlk_1_2_3_fake_belem
 + y_ijk_1_2_fake_belem >= -2
_C474: - a_ij_1_2 - d_ijk_1_2_fake_manila - 0.001 e_ijlk_1_2_1_fake_manila
 - 0.001 e_ijlk_1_2_2_fake_manila - 0.001 e_ijlk_1_2_3_fake_manila
 + y_ijk_1_2_fake_manila >= -2
_C475: - a_ij_1_3 - d_ijk_1_3_fake_belem - 0.001 e_ijlk_1_3_1_fake_belem
 - 0.001 e_ijlk_1_3_2_fake_belem - 0.001 e_ijlk_1_3_3_fake_belem
 + y_ijk_1_3_fake_belem >= -2
_C476: - a_ij_1_3 - d_ijk_1_3_fake_manila - 0.001 e_ijlk_1_3_1_fake_manila
 - 0.001 e_ijlk_1_3_2_fake_manila - 0.001 e_ijlk_1_3_3_fake_manila
 + y_ijk_1_3_fake_manila >= -2
_C477: - a_ij_2_1 - d_ijk_2_1_fake_belem - 0.001 e_ijlk_2_1_1_fake_belem
 - 0.001 e_ijlk_2_1_2_fake_belem - 0.001 e_ijlk_2_1_3_fake_belem
 + y_ijk_2_1_fake_belem >= -2
_C478: - a_ij_2_1 - d_ijk_2_1_fake_manila - 0.001 e_ijlk_2_1_1_fake_manila
 - 0.001 e_ijlk_2_1_2_fake_manila - 0.001 e_ijlk_2_1_3_fake_manila
 + y_ijk_2_1_fake_manila >= -2
_C479: - a_ij_2_2 - d_ijk_2_2_fake_belem - 0.001 e_ijlk_2_2_1_fake_belem
 - 0.001 e_ijlk_2_2_2_fake_belem - 0.001 e_ijlk_2_2_3_fake_belem
 + y_ijk_2_2_fake_belem >= -2
_C48: s_j_1 + 999987 z_ikt_1_fake_belem_13 + 999987 z_ikt_1_fake_manila_13
 <= 1000000
_C480: - a_ij_2_2 - d_ijk_2_2_fake_manila - 0.001 e_ijlk_2_2_1_fake_manila
 - 0.001 e_ijlk_2_2_2_fake_manila - 0.001 e_ijlk_2_2_3_fake_manila
 + y_ijk_2_2_fake_manila >= -2
_C481: - a_ij_2_3 - d_ijk_2_3_fake_belem - 0.001 e_ijlk_2_3_1_fake_belem
 - 0.001 e_ijlk_2_3_2_fake_belem - 0.001 e_ijlk_2_3_3_fake_belem
 + y_ijk_2_3_fake_belem >= -2
_C482: - a_ij_2_3 - d_ijk_2_3_fake_manila - 0.001 e_ijlk_2_3_1_fake_manila
 - 0.001 e_ijlk_2_3_2_fake_manila - 0.001 e_ijlk_2_3_3_fake_manila
 + y_ijk_2_3_fake_manila >= -2
_C483: - a_ij_3_1 - d_ijk_3_1_fake_belem - 0.001 e_ijlk_3_1_1_fake_belem
 - 0.001 e_ijlk_3_1_2_fake_belem - 0.001 e_ijlk_3_1_3_fake_belem
 + y_ijk_3_1_fake_belem >= -2
_C484: - a_ij_3_1 - d_ijk_3_1_fake_manila - 0.001 e_ijlk_3_1_1_fake_manila
 - 0.001 e_ijlk_3_1_2_fake_manila - 0.001 e_ijlk_3_1_3_fake_manila
 + y_ijk_3_1_fake_manila >= -2
_C485: - a_ij_3_2 - d_ijk_3_2_fake_belem - 0.001 e_ijlk_3_2_1_fake_belem
 - 0.001 e_ijlk_3_2_2_fake_belem - 0.001 e_ijlk_3_2_3_fake_belem
 + y_ijk_3_2_fake_belem >= -2
_C486: - a_ij_3_2 - d_ijk_3_2_fake_manila - 0.001 e_ijlk_3_2_1_fake_manila
 - 0.001 e_ijlk_3_2_2_fake_manila - 0.001 e_ijlk_3_2_3_fake_manila
 + y_ijk_3_2_fake_manila >= -2
_C487: - a_ij_3_3 - d_ijk_3_3_fake_belem - 0.001 e_ijlk_3_3_1_fake_belem
 - 0.001 e_ijlk_3_3_2_fake_belem - 0.001 e_ijlk_3_3_3_fake_belem
 + y_ijk_3_3_fake_belem >= -2
_C488: - a_ij_3_3 - d_ijk_3_3_fake_manila - 0.001 e_ijlk_3_3_1_fake_manila
 - 0.001 e_ijlk_3_3_2_fake_manila - 0.001 e_ijlk_3_3_3_fake_manila
 + y_ijk_3_3_fake_manila >= -2
_C49: - c_j_1 + 14 z_ikt_1_fake_belem_14 + 14 z_ikt_1_fake_manila_14 <= 0
_C5: - 1000000 x_ik_1_fake_belem + z_ikt_1_fake_belem_0 + z_ikt_1_fake_belem_1
 + z_ikt_1_fake_belem_10 + z_ikt_1_fake_belem_11 + z_ikt_1_fake_belem_12
 + z_ikt_1_fake_belem_13 + z_ikt_1_fake_belem_14 + z_ikt_1_fake_belem_15
 + z_ikt_1_fake_belem_16 + z_ikt_1_fake_belem_17 + z_ikt_1_fake_belem_18
 + z_ikt_1_fake_belem_19 + z_ikt_1_fake_belem_2 + z_ikt_1_fake_belem_20
 + z_ikt_1_fake_belem_21 + z_ikt_1_fake_belem_22 + z_ikt_1_fake_belem_23
 + z_ikt_1_fake_belem_24 + z_ikt_1_fake_belem_25 + z_ikt_1_fake_belem_26
 + z_ikt_1_fake_belem_27 + z_ikt_1_fake_belem_28 + z_ikt_1_fake_belem_29
 + z_ikt_1_fake_belem_3 + z_ikt_1_fake_belem_30 + z_ikt_1_fake_belem_31
 + z_ikt_1_fake_belem_4 + z_ikt_1_fake_belem_5 + z_ikt_1_fake_belem_6
 + z_ikt_1_fake_belem_7 + z_ikt_1_fake_belem_8 + z_ikt_1_fake_belem_9 <= 0
_C50: z_ikt_1_fake_belem_14 + z_ikt_1_fake_manila_14 <= 1
_C51: s_j_1 + 999986 z_ikt_1_fake_belem_14 + 999986 z_ikt_1_fake_manila_14
 <= 1000000
_C52: - c_j_1 + 15 z_ikt_1_fake_belem_15 + 15 z_ikt_1_fake_manila_15 <= 0
_C53: z_ikt_1_fake_belem_15 + z_ikt_1_fake_manila_15 <= 1
_C54: s_j_1 + 999985 z_ikt_1_fake_belem_15 + 999985 z_ikt_1_fake_manila_15
 <= 1000000
_C55: - c_j_1 + 16 z_ikt_1_fake_belem_16 + 16 z_ikt_1_fake_manila_16 <= 0
_C56: z_ikt_1_fake_belem_16 + z_ikt_1_fake_manila_16 <= 1
_C57: s_j_1 + 999984 z_ikt_1_fake_belem_16 + 999984 z_ikt_1_fake_manila_16
 <= 1000000
_C58: - c_j_1 + 17 z_ikt_1_fake_belem_17 + 17 z_ikt_1_fake_manila_17 <= 0
_C59: z_ikt_1_fake_belem_17 + z_ikt_1_fake_manila_17 <= 1
_C6: - 1000000 x_ik_1_fake_manila + z_ikt_1_fake_manila_0
 + z_ikt_1_fake_manila_1 + z_ikt_1_fake_manila_10 + z_ikt_1_fake_manila_11
 + z_ikt_1_fake_manila_12 + z_ikt_1_fake_manila_13 + z_ikt_1_fake_manila_14
 + z_ikt_1_fake_manila_15 + z_ikt_1_fake_manila_16 + z_ikt_1_fake_manila_17
 + z_ikt_1_fake_manila_18 + z_ikt_1_fake_manila_19 + z_ikt_1_fake_manila_2
 + z_ikt_1_fake_manila_20 + z_ikt_1_fake_manila_21 + z_ikt_1_fake_manila_22
 + z_ikt_1_fake_manila_23 + z_ikt_1_fake_manila_24 + z_ikt_1_fake_manila_25
 + z_ikt_1_fake_manila_26 + z_ikt_1_fake_manila_27 + z_ikt_1_fake_manila_28
 + z_ikt_1_fake_manila_29 + z_ikt_1_fake_manila_3 + z_ikt_1_fake_manila_30
 + z_ikt_1_fake_manila_31 + z_ikt_1_fake_manila_4 + z_ikt_1_fake_manila_5
 + z_ikt_1_fake_manila_6 + z_ikt_1_fake_manila_7 + z_ikt_1_fake_manila_8
 + z_ikt_1_fake_manila_9 <= 0
_C60: s_j_1 + 999983 z_ikt_1_fake_belem_17 + 999983 z_ikt_1_fake_manila_17
 <= 1000000
_C61: - c_j_1 + 18 z_ikt_1_fake_belem_18 + 18 z_ikt_1_fake_manila_18 <= 0
_C62: z_ikt_1_fake_belem_18 + z_ikt_1_fake_manila_18 <= 1
_C63: s_j_1 + 999982 z_ikt_1_fake_belem_18 + 999982 z_ikt_1_fake_manila_18
 <= 1000000
_C64: - c_j_1 + 19 z_ikt_1_fake_belem_19 + 19 z_ikt_1_fake_manila_19 <= 0
_C65: z_ikt_1_fake_belem_19 + z_ikt_1_fake_manila_19 <= 1
_C66: s_j_1 + 999981 z_ikt_1_fake_belem_19 + 999981 z_ikt_1_fake_manila_19
 <= 1000000
_C67: - c_j_1 + 20 z_ikt_1_fake_belem_20 + 20 z_ikt_1_fake_manila_20 <= 0
_C68: z_ikt_1_fake_belem_20 + z_ikt_1_fake_manila_20 <= 1
_C69: s_j_1 + 999980 z_ikt_1_fake_belem_20 + 999980 z_ikt_1_fake_manila_20
 <= 1000000
_C7: - c_j_1 <= 0
_C70: - c_j_1 + 21 z_ikt_1_fake_belem_21 + 21 z_ikt_1_fake_manila_21 <= 0
_C71: z_ikt_1_fake_belem_21 + z_ikt_1_fake_manila_21 <= 1
_C72: s_j_1 + 999979 z_ikt_1_fake_belem_21 + 999979 z_ikt_1_fake_manila_21
 <= 1000000
_C73: - c_j_1 + 22 z_ikt_1_fake_belem_22 + 22 z_ikt_1_fake_manila_22 <= 0
_C74: z_ikt_1_fake_belem_22 + z_ikt_1_fake_manila_22 <= 1
_C75: s_j_1 + 999978 z_ikt_1_fake_belem_22 + 999978 z_ikt_1_fake_manila_22
 <= 1000000
_C76: - c_j_1 + 23 z_ikt_1_fake_belem_23 + 23 z_ikt_1_fake_manila_23 <= 0
_C77: z_ikt_1_fake_belem_23 + z_ikt_1_fake_manila_23 <= 1
_C78: s_j_1 + 999977 z_ikt_1_fake_belem_23 + 999977 z_ikt_1_fake_manila_23
 <= 1000000
_C79: - c_j_1 + 24 z_ikt_1_fake_belem_24 + 24 z_ikt_1_fake_manila_24 <= 0
_C8: z_ikt_1_fake_belem_0 + z_ikt_1_fake_manila_0 <= 1
_C80: z_ikt_1_fake_belem_24 + z_ikt_1_fake_manila_24 <= 1
_C81: s_j_1 + 999976 z_ikt_1_fake_belem_24 + 999976 z_ikt_1_fake_manila_24
 <= 1000000
_C82: - c_j_1 + 25 z_ikt_1_fake_belem_25 + 25 z_ikt_1_fake_manila_25 <= 0
_C83: z_ikt_1_fake_belem_25 + z_ikt_1_fake_manila_25 <= 1
_C84: s_j_1 + 999975 z_ikt_1_fake_belem_25 + 999975 z_ikt_1_fake_manila_25
 <= 1000000
_C85: - c_j_1 + 26 z_ikt_1_fake_belem_26 + 26 z_ikt_1_fake_manila_26 <= 0
_C86: z_ikt_1_fake_belem_26 + z_ikt_1_fake_manila_26 <= 1
_C87: s_j_1 + 999974 z_ikt_1_fake_belem_26 + 999974 z_ikt_1_fake_manila_26
 <= 1000000
_C88: - c_j_1 + 27 z_ikt_1_fake_belem_27 + 27 z_ikt_1_fake_manila_27 <= 0
_C89: z_ikt_1_fake_belem_27 + z_ikt_1_fake_manila_27 <= 1
_C9: s_j_1 + 1000000 z_ikt_1_fake_belem_0 + 1000000 z_ikt_1_fake_manila_0
 <= 1000000
_C90: s_j_1 + 999973 z_ikt_1_fake_belem_27 + 999973 z_ikt_1_fake_manila_27
 <= 1000000
_C91: - c_j_1 + 28 z_ikt_1_fake_belem_28 + 28 z_ikt_1_fake_manila_28 <= 0
_C92: z_ikt_1_fake_belem_28 + z_ikt_1_fake_manila_28 <= 1
_C93: s_j_1 + 999972 z_ikt_1_fake_belem_28 + 999972 z_ikt_1_fake_manila_28
 <= 1000000
_C94: - c_j_1 + 29 z_ikt_1_fake_belem_29 + 29 z_ikt_1_fake_manila_29 <= 0
_C95: z_ikt_1_fake_belem_29 + z_ikt_1_fake_manila_29 <= 1
_C96: s_j_1 + 999971 z_ikt_1_fake_belem_29 + 999971 z_ikt_1_fake_manila_29
 <= 1000000
_C97: - c_j_1 + 30 z_ikt_1_fake_belem_30 + 30 z_ikt_1_fake_manila_30 <= 0
_C98: z_ikt_1_fake_belem_30 + z_ikt_1_fake_manila_30 <= 1
_C99: s_j_1 + 999970 z_ikt_1_fake_belem_30 + 999970 z_ikt_1_fake_manila_30
 <= 1000000
Binaries
a_ij_1_1
a_ij_1_2
a_ij_1_3
a_ij_2_1
a_ij_2_2
a_ij_2_3
a_ij_3_1
a_ij_3_2
a_ij_3_3
b_ij_1_1
b_ij_1_2
b_ij_1_3
b_ij_2_1
b_ij_2_2
b_ij_2_3
b_ij_3_1
b_ij_3_2
b_ij_3_3
d_ijk_1_1_fake_belem
d_ijk_1_1_fake_manila
d_ijk_1_2_fake_belem
d_ijk_1_2_fake_manila
d_ijk_1_3_fake_belem
d_ijk_1_3_fake_manila
d_ijk_2_1_fake_belem
d_ijk_2_1_fake_manila
d_ijk_2_2_fake_belem
d_ijk_2_2_fake_manila
d_ijk_2_3_fake_belem
d_ijk_2_3_fake_manila
d_ijk_3_1_fake_belem
d_ijk_3_1_fake_manila
d_ijk_3_2_fake_belem
d_ijk_3_2_fake_manila
d_ijk_3_3_fake_belem
d_ijk_3_3_fake_manila
e_ijlk_1_1_1_fake_belem
e_ijlk_1_1_1_fake_manila
e_ijlk_1_1_2_fake_belem
e_ijlk_1_1_2_fake_manila
e_ijlk_1_1_3_fake_belem
e_ijlk_1_1_3_fake_manila
e_ijlk_1_2_1_fake_belem
e_ijlk_1_2_1_fake_manila
e_ijlk_1_2_2_fake_belem
e_ijlk_1_2_2_fake_manila
e_ijlk_1_2_3_fake_belem
e_ijlk_1_2_3_fake_manila
e_ijlk_1_3_1_fake_belem
e_ijlk_1_3_1_fake_manila
e_ijlk_1_3_2_fake_belem
e_ijlk_1_3_2_fake_manila
e_ijlk_1_3_3_fake_belem
e_ijlk_1_3_3_fake_manila
e_ijlk_2_1_1_fake_belem
e_ijlk_2_1_1_fake_manila
e_ijlk_2_1_2_fake_belem
e_ijlk_2_1_2_fake_manila
e_ijlk_2_1_3_fake_belem
e_ijlk_2_1_3_fake_manila
e_ijlk_2_2_1_fake_belem
e_ijlk_2_2_1_fake_manila
e_ijlk_2_2_2_fake_belem
e_ijlk_2_2_2_fake_manila
e_ijlk_2_2_3_fake_belem
e_ijlk_2_2_3_fake_manila
e_ijlk_2_3_1_fake_belem
e_ijlk_2_3_1_fake_manila
e_ijlk_2_3_2_fake_belem
e_ijlk_2_3_2_fake_manila
e_ijlk_2_3_3_fake_belem
e_ijlk_2_3_3_fake_manila
e_ijlk_3_1_1_fake_belem
e_ijlk_3_1_1_fake_manila
e_ijlk_3_1_2_fake_belem
e_ijlk_3_1_2_fake_manila
e_ijlk_3_1_3_fake_belem
e_ijlk_3_1_3_fake_manila
e_ijlk_3_2_1_fake_belem
e_ijlk_3_2_1_fake_manila
e_ijlk_3_2_2_fake_belem
e_ijlk_3_2_2_fake_manila
e_ijlk_3_2_3_fake_belem
e_ijlk_3_2_3_fake_manila
e_ijlk_3_3_1_fake_belem
e_ijlk_3_3_1_fake_manila
e_ijlk_3_3_2_fake_belem
e_ijlk_3_3_2_fake_manila
e_ijlk_3_3_3_fake_belem
e_ijlk_3_3_3_fake_manila
x_ik_1_fake_belem
x_ik_1_fake_manila
x_ik_2_fake_belem
x_ik_2_fake_manila
x_ik_3_fake_belem
x_ik_3_fake_manila
y_ijk_0_1_fake_belem
y_ijk_0_1_fake_manila
y_ijk_0_2_fake_belem
y_ijk_0_2_fake_manila
y_ijk_0_3_fake_belem
y_ijk_0_3_fake_manila
y_ijk_1_0_fake_belem
y_ijk_1_0_fake_manila
y_ijk_1_1_fake_belem
y_ijk_1_1_fake_manila
y_ijk_1_2_fake_belem
y_ijk_1_2_fake_manila
y_ijk_1_3_fake_belem
y_ijk_1_3_fake_manila
y_ijk_2_0_fake_belem
y_ijk_2_0_fake_manila
y_ijk_2_1_fake_belem
y_ijk_2_1_fake_manila
y_ijk_2_2_fake_belem
y_ijk_2_2_fake_manila
y_ijk_2_3_fake_belem
y_ijk_2_3_fake_manila
y_ijk_3_0_fake_belem
y_ijk_3_0_fake_manila
y_ijk_3_1_fake_belem
y_ijk_3_1_fake_manila
y_ijk_3_2_fake_belem
y_ijk_3_2_fake_manila
y_ijk_3_3_fake_belem
y_ijk_3_3_fake_manila
z_ikt_1_fake_belem_0
z_ikt_1_fake_belem_1
z_ikt_1_fake_belem_10
z_ikt_1_fake_belem_11
z_ikt_1_fake_belem_12
z_ikt_1_fake_belem_13
z_ikt_1_fake_belem_14
z_ikt_1_fake_belem_15
z_ikt_1_fake_belem_16
z_ikt_1_fake_belem_17
z_ikt_1_fake_belem_18
z_ikt_1_fake_belem_19
z_ikt_1_fake_belem_2
z_ikt_1_fake_belem_20
z_ikt_1_fake_belem_21
z_ikt_1_fake_belem_22
z_ikt_1_fake_belem_23
z_ikt_1_fake_belem_24
z_ikt_1_fake_belem_25
z_ikt_1_fake_belem_26
z_ikt_1_fake_belem_27
z_ikt_1_fake_belem_28
z_ikt_1_fake_belem_29
z_ikt_1_fake_belem_3
z_ikt_1_fake_belem_30
z_ikt_1_fake_belem_31
z_ikt_1_fake_belem_4
z_ikt_1_fake_belem_5
z_ikt_1_fake_belem_6
z_ikt_1_fake_belem_7
z_ikt_1_fake_belem_8
z_ikt_1_fake_belem_9
z_ikt_1_fake_manila_0
z_ikt_1_fake_manila_1
z_ikt_1_fake_manila_10
z_ikt_1_fake_manila_11
z_ikt_1_fake_manila_12
z_ikt_1_fake_manila_13
z_ikt_1_fake_manila_14
z_ikt_1_fake_manila_15
z_ikt_1_fake_manila_16
z_ikt_1_fake_manila_17
z_ikt_1_fake_manila_18
z_ikt_1_fake_manila_19
z_ikt_1_fake_manila_2
z_ikt_1_fake_manila_20
z_ikt_1_fake_manila_21
z_ikt_1_fake_manila_22
z_ikt_1_fake_manila_23
z_ikt_1_fake_manila_24
z_ikt_1_fake_manila_25
z_ikt_1_fake_manila_26
z_ikt_1_fake_manila_27
z_ikt_1_fake_manila_28
z_ikt_1_fake_manila_29
z_ikt_1_fake_manila_3
z_ikt_1_fake_manila_30
z_ikt_1_fake_manila_31
z_ikt_1_fake_manila_4
z_ikt_1_fake_manila_5
z_ikt_1_fake_manila_6
z_ikt_1_fake_manila_7
z_ikt_1_fake_manila_8
z_ikt_1_fake_manila_9
z_ikt_2_fake_belem_0
z_ikt_2_fake_belem_1
z_ikt_2_fake_belem_10
z_ikt_2_fake_belem_11
z_ikt_2_fake_belem_12
z_ikt_2_fake_belem_13
z_ikt_2_fake_belem_14
z_ikt_2_fake_belem_15
z_ikt_2_fake_belem_16
z_ikt_2_fake_belem_17
z_ikt_2_fake_belem_18
z_ikt_2_fake_belem_19
z_ikt_2_fake_belem_2
z_ikt_2_fake_belem_20
z_ikt_2_fake_belem_21
z_ikt_2_fake_belem_22
z_ikt_2_fake_belem_23
z_ikt_2_fake_belem_24
z_ikt_2_fake_belem_25
z_ikt_2_fake_belem_26
z_ikt_2_fake_belem_27
z_ikt_2_fake_belem_28
z_ikt_2_fake_belem_29
z_ikt_2_fake_belem_3
z_ikt_2_fake_belem_30
z_ikt_2_fake_belem_31
z_ikt_2_fake_belem_4
z_ikt_2_fake_belem_5
z_ikt_2_fake_belem_6
z_ikt_2_fake_belem_7
z_ikt_2_fake_belem_8
z_ikt_2_fake_belem_9
z_ikt_2_fake_manila_0
z_ikt_2_fake_manila_1
z_ikt_2_fake_manila_10
z_ikt_2_fake_manila_11
z_ikt_2_fake_manila_12
z_ikt_2_fake_manila_13
z_ikt_2_fake_manila_14
z_ikt_2_fake_manila_15
z_ikt_2_fake_manila_16
z_ikt_2_fake_manila_17
z_ikt_2_fake_manila_18
z_ikt_2_fake_manila_19
z_ikt_2_fake_manila_2
z_ikt_2_fake_manila_20
z_ikt_2_fake_manila_21
z_ikt_2_fake_manila_22
z_ikt_2_fake_manila_23
z_ikt_2_fake_manila_24
z_ikt_2_fake_manila_25
z_ikt_2_fake_manila_26
z_ikt_2_fake_manila_27
z_ikt_2_fake_manila_28
z_ikt_2_fake_manila_29
z_ikt_2_fake_manila_3
z_ikt_2_fake_manila_30
z_ikt_2_fake_manila_31
z_ikt_2_fake_manila_4
z_ikt_2_fake_manila_5
z_ikt_2_fake_manila_6
z_ikt_2_fake_manila_7
z_ikt_2_fake_manila_8
z_ikt_2_fake_manila_9
z_ikt_3_fake_belem_0
z_ikt_3_fake_belem_1
z_ikt_3_fake_belem_10
z_ikt_3_fake_belem_11
z_ikt_3_fake_belem_12
z_ikt_3_fake_belem_13
z_ikt_3_fake_belem_14
z_ikt_3_fake_belem_15
z_ikt_3_fake_belem_16
z_ikt_3_fake_belem_17
z_ikt_3_fake_belem_18
z_ikt_3_fake_belem_19
z_ikt_3_fake_belem_2
z_ikt_3_fake_belem_20
z_ikt_3_fake_belem_21
z_ikt_3_fake_belem_22
z_ikt_3_fake_belem_23
z_ikt_3_fake_belem_24
z_ikt_3_fake_belem_25
z_ikt_3_fake_belem_26
z_ikt_3_fake_belem_27
z_ikt_3_fake_belem_28
z_ikt_3_fake_belem_29
z_ikt_3_fake_belem_3
z_ikt_3_fake_belem_30
z_ikt_3_fake_belem_31
z_ikt_3_fake_belem_4
z_ikt_3_fake_belem_5
z_ikt_3_fake_belem_6
z_ikt_3_fake_belem_7
z_ikt_3_fake_belem_8
z_ikt_3_fake_belem_9
z_ikt_3_fake_manila_0
z_ikt_3_fake_manila_1
z_ikt_3_fake_manila_10
z_ikt_3_fake_manila_11
z_ikt_3_fake_manila_12
z_ikt_3_fake_manila_13
z_ikt_3_fake_manila_14
z_ikt_3_fake_manila_15
z_ikt_3_fake_manila_16
z_ikt_3_fake_manila_17
z_ikt_3_fake_manila_18
z_ikt_3_fake_manila_19
z_ikt_3_fake_manila_2
z_ikt_3_fake_manila_20
z_ikt_3_fake_manila_21
z_ikt_3_fake_manila_22
z_ikt_3_fake_manila_23
z_ikt_3_fake_manila_24
z_ikt_3_fake_manila_25
z_ikt_3_fake_manila_26
z_ikt_3_fake_manila_27
z_ikt_3_fake_manila_28
z_ikt_3_fake_manila_29
z_ikt_3_fake_manila_3
z_ikt_3_fake_manila_30
z_ikt_3_fake_manila_31
z_ikt_3_fake_manila_4
z_ikt_3_fake_manila_5
z_ikt_3_fake_manila_6
z_ikt_3_fake_manila_7
z_ikt_3_fake_manila_8
z_ikt_3_fake_manila_9
End
