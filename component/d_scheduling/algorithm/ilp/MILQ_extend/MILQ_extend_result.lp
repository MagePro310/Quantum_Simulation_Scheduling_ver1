\* Scheduling *\
Minimize
OBJ: makespan
Subject To
_C1: c_j_0 = 0
_C10: - c_j_1 + z_ikt_1_fake_belem_1 + z_ikt_1_fake_manila_1 <= 0
_C100: - c_j_1 + 31 z_ikt_1_fake_belem_31 + 31 z_ikt_1_fake_manila_31 <= 0
_C1000: - a_ij_6_6 - b_ij_3_6 - 2 d_ijk_3_6_fake_belem
 + e_ijlk_3_6_6_fake_belem >= -3
_C1001: d_ijk_3_6_fake_manila - x_ik_3_fake_manila - x_ik_6_fake_manila >= -1
_C1002: - a_ij_1_6 - b_ij_3_1 - d_ijk_3_1_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_6_1_fake_manila >= -3
_C1003: - a_ij_2_6 - b_ij_3_2 - d_ijk_3_2_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_6_2_fake_manila >= -3
_C1004: - a_ij_3_6 - b_ij_3_3 - d_ijk_3_3_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_6_3_fake_manila >= -3
_C1005: - a_ij_4_6 - b_ij_3_4 - d_ijk_3_4_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_6_4_fake_manila >= -3
_C1006: - a_ij_5_6 - b_ij_3_5 - d_ijk_3_5_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_6_5_fake_manila >= -3
_C1007: - a_ij_6_6 - b_ij_3_6 - 2 d_ijk_3_6_fake_manila
 + e_ijlk_3_6_6_fake_manila >= -3
_C1008: a_ij_4_1 + 0.001 c_j_4 - 0.001 s_j_1 >= 0
_C1009: b_ij_4_1 - 0.001 c_j_1 + 0.001 c_j_4 >= 0
_C101: z_ikt_1_fake_belem_31 + z_ikt_1_fake_manila_31 <= 1
_C1010: d_ijk_4_1_fake_belem - x_ik_1_fake_belem - x_ik_4_fake_belem >= -1
_C1011: - a_ij_1_1 - b_ij_4_1 - 2 d_ijk_4_1_fake_belem
 + e_ijlk_4_1_1_fake_belem >= -3
_C1012: - a_ij_2_1 - b_ij_4_2 - d_ijk_4_1_fake_belem - d_ijk_4_2_fake_belem
 + e_ijlk_4_1_2_fake_belem >= -3
_C1013: - a_ij_3_1 - b_ij_4_3 - d_ijk_4_1_fake_belem - d_ijk_4_3_fake_belem
 + e_ijlk_4_1_3_fake_belem >= -3
_C1014: - a_ij_4_1 - b_ij_4_4 - d_ijk_4_1_fake_belem - d_ijk_4_4_fake_belem
 + e_ijlk_4_1_4_fake_belem >= -3
_C1015: - a_ij_5_1 - b_ij_4_5 - d_ijk_4_1_fake_belem - d_ijk_4_5_fake_belem
 + e_ijlk_4_1_5_fake_belem >= -3
_C1016: - a_ij_6_1 - b_ij_4_6 - d_ijk_4_1_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_1_6_fake_belem >= -3
_C1017: d_ijk_4_1_fake_manila - x_ik_1_fake_manila - x_ik_4_fake_manila >= -1
_C1018: - a_ij_1_1 - b_ij_4_1 - 2 d_ijk_4_1_fake_manila
 + e_ijlk_4_1_1_fake_manila >= -3
_C1019: - a_ij_2_1 - b_ij_4_2 - d_ijk_4_1_fake_manila - d_ijk_4_2_fake_manila
 + e_ijlk_4_1_2_fake_manila >= -3
_C102: s_j_1 + 999969 z_ikt_1_fake_belem_31 + 999969 z_ikt_1_fake_manila_31
 <= 1000000
_C1020: - a_ij_3_1 - b_ij_4_3 - d_ijk_4_1_fake_manila - d_ijk_4_3_fake_manila
 + e_ijlk_4_1_3_fake_manila >= -3
_C1021: - a_ij_4_1 - b_ij_4_4 - d_ijk_4_1_fake_manila - d_ijk_4_4_fake_manila
 + e_ijlk_4_1_4_fake_manila >= -3
_C1022: - a_ij_5_1 - b_ij_4_5 - d_ijk_4_1_fake_manila - d_ijk_4_5_fake_manila
 + e_ijlk_4_1_5_fake_manila >= -3
_C1023: - a_ij_6_1 - b_ij_4_6 - d_ijk_4_1_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_1_6_fake_manila >= -3
_C1024: a_ij_4_2 + 0.001 c_j_4 - 0.001 s_j_2 >= 0
_C1025: b_ij_4_2 - 0.001 c_j_2 + 0.001 c_j_4 >= 0
_C1026: d_ijk_4_2_fake_belem - x_ik_2_fake_belem - x_ik_4_fake_belem >= -1
_C1027: - a_ij_1_2 - b_ij_4_1 - d_ijk_4_1_fake_belem - d_ijk_4_2_fake_belem
 + e_ijlk_4_2_1_fake_belem >= -3
_C1028: - a_ij_2_2 - b_ij_4_2 - 2 d_ijk_4_2_fake_belem
 + e_ijlk_4_2_2_fake_belem >= -3
_C1029: - a_ij_3_2 - b_ij_4_3 - d_ijk_4_2_fake_belem - d_ijk_4_3_fake_belem
 + e_ijlk_4_2_3_fake_belem >= -3
_C103: c_j_2 - makespan <= 0
_C1030: - a_ij_4_2 - b_ij_4_4 - d_ijk_4_2_fake_belem - d_ijk_4_4_fake_belem
 + e_ijlk_4_2_4_fake_belem >= -3
_C1031: - a_ij_5_2 - b_ij_4_5 - d_ijk_4_2_fake_belem - d_ijk_4_5_fake_belem
 + e_ijlk_4_2_5_fake_belem >= -3
_C1032: - a_ij_6_2 - b_ij_4_6 - d_ijk_4_2_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_2_6_fake_belem >= -3
_C1033: d_ijk_4_2_fake_manila - x_ik_2_fake_manila - x_ik_4_fake_manila >= -1
_C1034: - a_ij_1_2 - b_ij_4_1 - d_ijk_4_1_fake_manila - d_ijk_4_2_fake_manila
 + e_ijlk_4_2_1_fake_manila >= -3
_C1035: - a_ij_2_2 - b_ij_4_2 - 2 d_ijk_4_2_fake_manila
 + e_ijlk_4_2_2_fake_manila >= -3
_C1036: - a_ij_3_2 - b_ij_4_3 - d_ijk_4_2_fake_manila - d_ijk_4_3_fake_manila
 + e_ijlk_4_2_3_fake_manila >= -3
_C1037: - a_ij_4_2 - b_ij_4_4 - d_ijk_4_2_fake_manila - d_ijk_4_4_fake_manila
 + e_ijlk_4_2_4_fake_manila >= -3
_C1038: - a_ij_5_2 - b_ij_4_5 - d_ijk_4_2_fake_manila - d_ijk_4_5_fake_manila
 + e_ijlk_4_2_5_fake_manila >= -3
_C1039: - a_ij_6_2 - b_ij_4_6 - d_ijk_4_2_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_2_6_fake_manila >= -3
_C104: x_ik_2_fake_belem + x_ik_2_fake_manila = 1
_C1040: a_ij_4_3 + 0.001 c_j_4 - 0.001 s_j_3 >= 0
_C1041: b_ij_4_3 - 0.001 c_j_3 + 0.001 c_j_4 >= 0
_C1042: d_ijk_4_3_fake_belem - x_ik_3_fake_belem - x_ik_4_fake_belem >= -1
_C1043: - a_ij_1_3 - b_ij_4_1 - d_ijk_4_1_fake_belem - d_ijk_4_3_fake_belem
 + e_ijlk_4_3_1_fake_belem >= -3
_C1044: - a_ij_2_3 - b_ij_4_2 - d_ijk_4_2_fake_belem - d_ijk_4_3_fake_belem
 + e_ijlk_4_3_2_fake_belem >= -3
_C1045: - a_ij_3_3 - b_ij_4_3 - 2 d_ijk_4_3_fake_belem
 + e_ijlk_4_3_3_fake_belem >= -3
_C1046: - a_ij_4_3 - b_ij_4_4 - d_ijk_4_3_fake_belem - d_ijk_4_4_fake_belem
 + e_ijlk_4_3_4_fake_belem >= -3
_C1047: - a_ij_5_3 - b_ij_4_5 - d_ijk_4_3_fake_belem - d_ijk_4_5_fake_belem
 + e_ijlk_4_3_5_fake_belem >= -3
_C1048: - a_ij_6_3 - b_ij_4_6 - d_ijk_4_3_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_3_6_fake_belem >= -3
_C1049: d_ijk_4_3_fake_manila - x_ik_3_fake_manila - x_ik_4_fake_manila >= -1
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
_C1050: - a_ij_1_3 - b_ij_4_1 - d_ijk_4_1_fake_manila - d_ijk_4_3_fake_manila
 + e_ijlk_4_3_1_fake_manila >= -3
_C1051: - a_ij_2_3 - b_ij_4_2 - d_ijk_4_2_fake_manila - d_ijk_4_3_fake_manila
 + e_ijlk_4_3_2_fake_manila >= -3
_C1052: - a_ij_3_3 - b_ij_4_3 - 2 d_ijk_4_3_fake_manila
 + e_ijlk_4_3_3_fake_manila >= -3
_C1053: - a_ij_4_3 - b_ij_4_4 - d_ijk_4_3_fake_manila - d_ijk_4_4_fake_manila
 + e_ijlk_4_3_4_fake_manila >= -3
_C1054: - a_ij_5_3 - b_ij_4_5 - d_ijk_4_3_fake_manila - d_ijk_4_5_fake_manila
 + e_ijlk_4_3_5_fake_manila >= -3
_C1055: - a_ij_6_3 - b_ij_4_6 - d_ijk_4_3_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_3_6_fake_manila >= -3
_C1056: a_ij_4_4 = 0
_C1057: b_ij_4_4 = 0
_C1058: a_ij_4_5 + 0.001 c_j_4 - 0.001 s_j_5 >= 0
_C1059: b_ij_4_5 + 0.001 c_j_4 - 0.001 c_j_5 >= 0
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
_C1060: d_ijk_4_5_fake_belem - x_ik_4_fake_belem - x_ik_5_fake_belem >= -1
_C1061: - a_ij_1_5 - b_ij_4_1 - d_ijk_4_1_fake_belem - d_ijk_4_5_fake_belem
 + e_ijlk_4_5_1_fake_belem >= -3
_C1062: - a_ij_2_5 - b_ij_4_2 - d_ijk_4_2_fake_belem - d_ijk_4_5_fake_belem
 + e_ijlk_4_5_2_fake_belem >= -3
_C1063: - a_ij_3_5 - b_ij_4_3 - d_ijk_4_3_fake_belem - d_ijk_4_5_fake_belem
 + e_ijlk_4_5_3_fake_belem >= -3
_C1064: - a_ij_4_5 - b_ij_4_4 - d_ijk_4_4_fake_belem - d_ijk_4_5_fake_belem
 + e_ijlk_4_5_4_fake_belem >= -3
_C1065: - a_ij_5_5 - b_ij_4_5 - 2 d_ijk_4_5_fake_belem
 + e_ijlk_4_5_5_fake_belem >= -3
_C1066: - a_ij_6_5 - b_ij_4_6 - d_ijk_4_5_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_5_6_fake_belem >= -3
_C1067: d_ijk_4_5_fake_manila - x_ik_4_fake_manila - x_ik_5_fake_manila >= -1
_C1068: - a_ij_1_5 - b_ij_4_1 - d_ijk_4_1_fake_manila - d_ijk_4_5_fake_manila
 + e_ijlk_4_5_1_fake_manila >= -3
_C1069: - a_ij_2_5 - b_ij_4_2 - d_ijk_4_2_fake_manila - d_ijk_4_5_fake_manila
 + e_ijlk_4_5_2_fake_manila >= -3
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
_C1070: - a_ij_3_5 - b_ij_4_3 - d_ijk_4_3_fake_manila - d_ijk_4_5_fake_manila
 + e_ijlk_4_5_3_fake_manila >= -3
_C1071: - a_ij_4_5 - b_ij_4_4 - d_ijk_4_4_fake_manila - d_ijk_4_5_fake_manila
 + e_ijlk_4_5_4_fake_manila >= -3
_C1072: - a_ij_5_5 - b_ij_4_5 - 2 d_ijk_4_5_fake_manila
 + e_ijlk_4_5_5_fake_manila >= -3
_C1073: - a_ij_6_5 - b_ij_4_6 - d_ijk_4_5_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_5_6_fake_manila >= -3
_C1074: a_ij_4_6 + 0.001 c_j_4 - 0.001 s_j_6 >= 0
_C1075: b_ij_4_6 + 0.001 c_j_4 - 0.001 c_j_6 >= 0
_C1076: d_ijk_4_6_fake_belem - x_ik_4_fake_belem - x_ik_6_fake_belem >= -1
_C1077: - a_ij_1_6 - b_ij_4_1 - d_ijk_4_1_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_6_1_fake_belem >= -3
_C1078: - a_ij_2_6 - b_ij_4_2 - d_ijk_4_2_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_6_2_fake_belem >= -3
_C1079: - a_ij_3_6 - b_ij_4_3 - d_ijk_4_3_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_6_3_fake_belem >= -3
_C108: - c_j_2 <= 0
_C1080: - a_ij_4_6 - b_ij_4_4 - d_ijk_4_4_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_6_4_fake_belem >= -3
_C1081: - a_ij_5_6 - b_ij_4_5 - d_ijk_4_5_fake_belem - d_ijk_4_6_fake_belem
 + e_ijlk_4_6_5_fake_belem >= -3
_C1082: - a_ij_6_6 - b_ij_4_6 - 2 d_ijk_4_6_fake_belem
 + e_ijlk_4_6_6_fake_belem >= -3
_C1083: d_ijk_4_6_fake_manila - x_ik_4_fake_manila - x_ik_6_fake_manila >= -1
_C1084: - a_ij_1_6 - b_ij_4_1 - d_ijk_4_1_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_6_1_fake_manila >= -3
_C1085: - a_ij_2_6 - b_ij_4_2 - d_ijk_4_2_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_6_2_fake_manila >= -3
_C1086: - a_ij_3_6 - b_ij_4_3 - d_ijk_4_3_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_6_3_fake_manila >= -3
_C1087: - a_ij_4_6 - b_ij_4_4 - d_ijk_4_4_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_6_4_fake_manila >= -3
_C1088: - a_ij_5_6 - b_ij_4_5 - d_ijk_4_5_fake_manila - d_ijk_4_6_fake_manila
 + e_ijlk_4_6_5_fake_manila >= -3
_C1089: - a_ij_6_6 - b_ij_4_6 - 2 d_ijk_4_6_fake_manila
 + e_ijlk_4_6_6_fake_manila >= -3
_C109: z_ikt_2_fake_belem_0 + z_ikt_2_fake_manila_0 <= 1
_C1090: a_ij_5_1 + 0.001 c_j_5 - 0.001 s_j_1 >= 0
_C1091: b_ij_5_1 - 0.001 c_j_1 + 0.001 c_j_5 >= 0
_C1092: d_ijk_5_1_fake_belem - x_ik_1_fake_belem - x_ik_5_fake_belem >= -1
_C1093: - a_ij_1_1 - b_ij_5_1 - 2 d_ijk_5_1_fake_belem
 + e_ijlk_5_1_1_fake_belem >= -3
_C1094: - a_ij_2_1 - b_ij_5_2 - d_ijk_5_1_fake_belem - d_ijk_5_2_fake_belem
 + e_ijlk_5_1_2_fake_belem >= -3
_C1095: - a_ij_3_1 - b_ij_5_3 - d_ijk_5_1_fake_belem - d_ijk_5_3_fake_belem
 + e_ijlk_5_1_3_fake_belem >= -3
_C1096: - a_ij_4_1 - b_ij_5_4 - d_ijk_5_1_fake_belem - d_ijk_5_4_fake_belem
 + e_ijlk_5_1_4_fake_belem >= -3
_C1097: - a_ij_5_1 - b_ij_5_5 - d_ijk_5_1_fake_belem - d_ijk_5_5_fake_belem
 + e_ijlk_5_1_5_fake_belem >= -3
_C1098: - a_ij_6_1 - b_ij_5_6 - d_ijk_5_1_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_1_6_fake_belem >= -3
_C1099: d_ijk_5_1_fake_manila - x_ik_1_fake_manila - x_ik_5_fake_manila >= -1
_C11: z_ikt_1_fake_belem_1 + z_ikt_1_fake_manila_1 <= 1
_C110: s_j_2 + 1000000 z_ikt_2_fake_belem_0 + 1000000 z_ikt_2_fake_manila_0
 <= 1000000
_C1100: - a_ij_1_1 - b_ij_5_1 - 2 d_ijk_5_1_fake_manila
 + e_ijlk_5_1_1_fake_manila >= -3
_C1101: - a_ij_2_1 - b_ij_5_2 - d_ijk_5_1_fake_manila - d_ijk_5_2_fake_manila
 + e_ijlk_5_1_2_fake_manila >= -3
_C1102: - a_ij_3_1 - b_ij_5_3 - d_ijk_5_1_fake_manila - d_ijk_5_3_fake_manila
 + e_ijlk_5_1_3_fake_manila >= -3
_C1103: - a_ij_4_1 - b_ij_5_4 - d_ijk_5_1_fake_manila - d_ijk_5_4_fake_manila
 + e_ijlk_5_1_4_fake_manila >= -3
_C1104: - a_ij_5_1 - b_ij_5_5 - d_ijk_5_1_fake_manila - d_ijk_5_5_fake_manila
 + e_ijlk_5_1_5_fake_manila >= -3
_C1105: - a_ij_6_1 - b_ij_5_6 - d_ijk_5_1_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_1_6_fake_manila >= -3
_C1106: a_ij_5_2 + 0.001 c_j_5 - 0.001 s_j_2 >= 0
_C1107: b_ij_5_2 - 0.001 c_j_2 + 0.001 c_j_5 >= 0
_C1108: d_ijk_5_2_fake_belem - x_ik_2_fake_belem - x_ik_5_fake_belem >= -1
_C1109: - a_ij_1_2 - b_ij_5_1 - d_ijk_5_1_fake_belem - d_ijk_5_2_fake_belem
 + e_ijlk_5_2_1_fake_belem >= -3
_C111: - c_j_2 + z_ikt_2_fake_belem_1 + z_ikt_2_fake_manila_1 <= 0
_C1110: - a_ij_2_2 - b_ij_5_2 - 2 d_ijk_5_2_fake_belem
 + e_ijlk_5_2_2_fake_belem >= -3
_C1111: - a_ij_3_2 - b_ij_5_3 - d_ijk_5_2_fake_belem - d_ijk_5_3_fake_belem
 + e_ijlk_5_2_3_fake_belem >= -3
_C1112: - a_ij_4_2 - b_ij_5_4 - d_ijk_5_2_fake_belem - d_ijk_5_4_fake_belem
 + e_ijlk_5_2_4_fake_belem >= -3
_C1113: - a_ij_5_2 - b_ij_5_5 - d_ijk_5_2_fake_belem - d_ijk_5_5_fake_belem
 + e_ijlk_5_2_5_fake_belem >= -3
_C1114: - a_ij_6_2 - b_ij_5_6 - d_ijk_5_2_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_2_6_fake_belem >= -3
_C1115: d_ijk_5_2_fake_manila - x_ik_2_fake_manila - x_ik_5_fake_manila >= -1
_C1116: - a_ij_1_2 - b_ij_5_1 - d_ijk_5_1_fake_manila - d_ijk_5_2_fake_manila
 + e_ijlk_5_2_1_fake_manila >= -3
_C1117: - a_ij_2_2 - b_ij_5_2 - 2 d_ijk_5_2_fake_manila
 + e_ijlk_5_2_2_fake_manila >= -3
_C1118: - a_ij_3_2 - b_ij_5_3 - d_ijk_5_2_fake_manila - d_ijk_5_3_fake_manila
 + e_ijlk_5_2_3_fake_manila >= -3
_C1119: - a_ij_4_2 - b_ij_5_4 - d_ijk_5_2_fake_manila - d_ijk_5_4_fake_manila
 + e_ijlk_5_2_4_fake_manila >= -3
_C112: z_ikt_2_fake_belem_1 + z_ikt_2_fake_manila_1 <= 1
_C1120: - a_ij_5_2 - b_ij_5_5 - d_ijk_5_2_fake_manila - d_ijk_5_5_fake_manila
 + e_ijlk_5_2_5_fake_manila >= -3
_C1121: - a_ij_6_2 - b_ij_5_6 - d_ijk_5_2_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_2_6_fake_manila >= -3
_C1122: a_ij_5_3 + 0.001 c_j_5 - 0.001 s_j_3 >= 0
_C1123: b_ij_5_3 - 0.001 c_j_3 + 0.001 c_j_5 >= 0
_C1124: d_ijk_5_3_fake_belem - x_ik_3_fake_belem - x_ik_5_fake_belem >= -1
_C1125: - a_ij_1_3 - b_ij_5_1 - d_ijk_5_1_fake_belem - d_ijk_5_3_fake_belem
 + e_ijlk_5_3_1_fake_belem >= -3
_C1126: - a_ij_2_3 - b_ij_5_2 - d_ijk_5_2_fake_belem - d_ijk_5_3_fake_belem
 + e_ijlk_5_3_2_fake_belem >= -3
_C1127: - a_ij_3_3 - b_ij_5_3 - 2 d_ijk_5_3_fake_belem
 + e_ijlk_5_3_3_fake_belem >= -3
_C1128: - a_ij_4_3 - b_ij_5_4 - d_ijk_5_3_fake_belem - d_ijk_5_4_fake_belem
 + e_ijlk_5_3_4_fake_belem >= -3
_C1129: - a_ij_5_3 - b_ij_5_5 - d_ijk_5_3_fake_belem - d_ijk_5_5_fake_belem
 + e_ijlk_5_3_5_fake_belem >= -3
_C113: s_j_2 + 999999 z_ikt_2_fake_belem_1 + 999999 z_ikt_2_fake_manila_1
 <= 1000000
_C1130: - a_ij_6_3 - b_ij_5_6 - d_ijk_5_3_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_3_6_fake_belem >= -3
_C1131: d_ijk_5_3_fake_manila - x_ik_3_fake_manila - x_ik_5_fake_manila >= -1
_C1132: - a_ij_1_3 - b_ij_5_1 - d_ijk_5_1_fake_manila - d_ijk_5_3_fake_manila
 + e_ijlk_5_3_1_fake_manila >= -3
_C1133: - a_ij_2_3 - b_ij_5_2 - d_ijk_5_2_fake_manila - d_ijk_5_3_fake_manila
 + e_ijlk_5_3_2_fake_manila >= -3
_C1134: - a_ij_3_3 - b_ij_5_3 - 2 d_ijk_5_3_fake_manila
 + e_ijlk_5_3_3_fake_manila >= -3
_C1135: - a_ij_4_3 - b_ij_5_4 - d_ijk_5_3_fake_manila - d_ijk_5_4_fake_manila
 + e_ijlk_5_3_4_fake_manila >= -3
_C1136: - a_ij_5_3 - b_ij_5_5 - d_ijk_5_3_fake_manila - d_ijk_5_5_fake_manila
 + e_ijlk_5_3_5_fake_manila >= -3
_C1137: - a_ij_6_3 - b_ij_5_6 - d_ijk_5_3_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_3_6_fake_manila >= -3
_C1138: a_ij_5_4 + 0.001 c_j_5 - 0.001 s_j_4 >= 0
_C1139: b_ij_5_4 - 0.001 c_j_4 + 0.001 c_j_5 >= 0
_C114: - c_j_2 + 2 z_ikt_2_fake_belem_2 + 2 z_ikt_2_fake_manila_2 <= 0
_C1140: d_ijk_5_4_fake_belem - x_ik_4_fake_belem - x_ik_5_fake_belem >= -1
_C1141: - a_ij_1_4 - b_ij_5_1 - d_ijk_5_1_fake_belem - d_ijk_5_4_fake_belem
 + e_ijlk_5_4_1_fake_belem >= -3
_C1142: - a_ij_2_4 - b_ij_5_2 - d_ijk_5_2_fake_belem - d_ijk_5_4_fake_belem
 + e_ijlk_5_4_2_fake_belem >= -3
_C1143: - a_ij_3_4 - b_ij_5_3 - d_ijk_5_3_fake_belem - d_ijk_5_4_fake_belem
 + e_ijlk_5_4_3_fake_belem >= -3
_C1144: - a_ij_4_4 - b_ij_5_4 - 2 d_ijk_5_4_fake_belem
 + e_ijlk_5_4_4_fake_belem >= -3
_C1145: - a_ij_5_4 - b_ij_5_5 - d_ijk_5_4_fake_belem - d_ijk_5_5_fake_belem
 + e_ijlk_5_4_5_fake_belem >= -3
_C1146: - a_ij_6_4 - b_ij_5_6 - d_ijk_5_4_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_4_6_fake_belem >= -3
_C1147: d_ijk_5_4_fake_manila - x_ik_4_fake_manila - x_ik_5_fake_manila >= -1
_C1148: - a_ij_1_4 - b_ij_5_1 - d_ijk_5_1_fake_manila - d_ijk_5_4_fake_manila
 + e_ijlk_5_4_1_fake_manila >= -3
_C1149: - a_ij_2_4 - b_ij_5_2 - d_ijk_5_2_fake_manila - d_ijk_5_4_fake_manila
 + e_ijlk_5_4_2_fake_manila >= -3
_C115: z_ikt_2_fake_belem_2 + z_ikt_2_fake_manila_2 <= 1
_C1150: - a_ij_3_4 - b_ij_5_3 - d_ijk_5_3_fake_manila - d_ijk_5_4_fake_manila
 + e_ijlk_5_4_3_fake_manila >= -3
_C1151: - a_ij_4_4 - b_ij_5_4 - 2 d_ijk_5_4_fake_manila
 + e_ijlk_5_4_4_fake_manila >= -3
_C1152: - a_ij_5_4 - b_ij_5_5 - d_ijk_5_4_fake_manila - d_ijk_5_5_fake_manila
 + e_ijlk_5_4_5_fake_manila >= -3
_C1153: - a_ij_6_4 - b_ij_5_6 - d_ijk_5_4_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_4_6_fake_manila >= -3
_C1154: a_ij_5_5 = 0
_C1155: b_ij_5_5 = 0
_C1156: a_ij_5_6 + 0.001 c_j_5 - 0.001 s_j_6 >= 0
_C1157: b_ij_5_6 + 0.001 c_j_5 - 0.001 c_j_6 >= 0
_C1158: d_ijk_5_6_fake_belem - x_ik_5_fake_belem - x_ik_6_fake_belem >= -1
_C1159: - a_ij_1_6 - b_ij_5_1 - d_ijk_5_1_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_6_1_fake_belem >= -3
_C116: s_j_2 + 999998 z_ikt_2_fake_belem_2 + 999998 z_ikt_2_fake_manila_2
 <= 1000000
_C1160: - a_ij_2_6 - b_ij_5_2 - d_ijk_5_2_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_6_2_fake_belem >= -3
_C1161: - a_ij_3_6 - b_ij_5_3 - d_ijk_5_3_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_6_3_fake_belem >= -3
_C1162: - a_ij_4_6 - b_ij_5_4 - d_ijk_5_4_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_6_4_fake_belem >= -3
_C1163: - a_ij_5_6 - b_ij_5_5 - d_ijk_5_5_fake_belem - d_ijk_5_6_fake_belem
 + e_ijlk_5_6_5_fake_belem >= -3
_C1164: - a_ij_6_6 - b_ij_5_6 - 2 d_ijk_5_6_fake_belem
 + e_ijlk_5_6_6_fake_belem >= -3
_C1165: d_ijk_5_6_fake_manila - x_ik_5_fake_manila - x_ik_6_fake_manila >= -1
_C1166: - a_ij_1_6 - b_ij_5_1 - d_ijk_5_1_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_6_1_fake_manila >= -3
_C1167: - a_ij_2_6 - b_ij_5_2 - d_ijk_5_2_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_6_2_fake_manila >= -3
_C1168: - a_ij_3_6 - b_ij_5_3 - d_ijk_5_3_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_6_3_fake_manila >= -3
_C1169: - a_ij_4_6 - b_ij_5_4 - d_ijk_5_4_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_6_4_fake_manila >= -3
_C117: - c_j_2 + 3 z_ikt_2_fake_belem_3 + 3 z_ikt_2_fake_manila_3 <= 0
_C1170: - a_ij_5_6 - b_ij_5_5 - d_ijk_5_5_fake_manila - d_ijk_5_6_fake_manila
 + e_ijlk_5_6_5_fake_manila >= -3
_C1171: - a_ij_6_6 - b_ij_5_6 - 2 d_ijk_5_6_fake_manila
 + e_ijlk_5_6_6_fake_manila >= -3
_C1172: a_ij_6_1 + 0.001 c_j_6 - 0.001 s_j_1 >= 0
_C1173: b_ij_6_1 - 0.001 c_j_1 + 0.001 c_j_6 >= 0
_C1174: d_ijk_6_1_fake_belem - x_ik_1_fake_belem - x_ik_6_fake_belem >= -1
_C1175: - a_ij_1_1 - b_ij_6_1 - 2 d_ijk_6_1_fake_belem
 + e_ijlk_6_1_1_fake_belem >= -3
_C1176: - a_ij_2_1 - b_ij_6_2 - d_ijk_6_1_fake_belem - d_ijk_6_2_fake_belem
 + e_ijlk_6_1_2_fake_belem >= -3
_C1177: - a_ij_3_1 - b_ij_6_3 - d_ijk_6_1_fake_belem - d_ijk_6_3_fake_belem
 + e_ijlk_6_1_3_fake_belem >= -3
_C1178: - a_ij_4_1 - b_ij_6_4 - d_ijk_6_1_fake_belem - d_ijk_6_4_fake_belem
 + e_ijlk_6_1_4_fake_belem >= -3
_C1179: - a_ij_5_1 - b_ij_6_5 - d_ijk_6_1_fake_belem - d_ijk_6_5_fake_belem
 + e_ijlk_6_1_5_fake_belem >= -3
_C118: z_ikt_2_fake_belem_3 + z_ikt_2_fake_manila_3 <= 1
_C1180: - a_ij_6_1 - b_ij_6_6 - d_ijk_6_1_fake_belem - d_ijk_6_6_fake_belem
 + e_ijlk_6_1_6_fake_belem >= -3
_C1181: d_ijk_6_1_fake_manila - x_ik_1_fake_manila - x_ik_6_fake_manila >= -1
_C1182: - a_ij_1_1 - b_ij_6_1 - 2 d_ijk_6_1_fake_manila
 + e_ijlk_6_1_1_fake_manila >= -3
_C1183: - a_ij_2_1 - b_ij_6_2 - d_ijk_6_1_fake_manila - d_ijk_6_2_fake_manila
 + e_ijlk_6_1_2_fake_manila >= -3
_C1184: - a_ij_3_1 - b_ij_6_3 - d_ijk_6_1_fake_manila - d_ijk_6_3_fake_manila
 + e_ijlk_6_1_3_fake_manila >= -3
_C1185: - a_ij_4_1 - b_ij_6_4 - d_ijk_6_1_fake_manila - d_ijk_6_4_fake_manila
 + e_ijlk_6_1_4_fake_manila >= -3
_C1186: - a_ij_5_1 - b_ij_6_5 - d_ijk_6_1_fake_manila - d_ijk_6_5_fake_manila
 + e_ijlk_6_1_5_fake_manila >= -3
_C1187: - a_ij_6_1 - b_ij_6_6 - d_ijk_6_1_fake_manila - d_ijk_6_6_fake_manila
 + e_ijlk_6_1_6_fake_manila >= -3
_C1188: a_ij_6_2 + 0.001 c_j_6 - 0.001 s_j_2 >= 0
_C1189: b_ij_6_2 - 0.001 c_j_2 + 0.001 c_j_6 >= 0
_C119: s_j_2 + 999997 z_ikt_2_fake_belem_3 + 999997 z_ikt_2_fake_manila_3
 <= 1000000
_C1190: d_ijk_6_2_fake_belem - x_ik_2_fake_belem - x_ik_6_fake_belem >= -1
_C1191: - a_ij_1_2 - b_ij_6_1 - d_ijk_6_1_fake_belem - d_ijk_6_2_fake_belem
 + e_ijlk_6_2_1_fake_belem >= -3
_C1192: - a_ij_2_2 - b_ij_6_2 - 2 d_ijk_6_2_fake_belem
 + e_ijlk_6_2_2_fake_belem >= -3
_C1193: - a_ij_3_2 - b_ij_6_3 - d_ijk_6_2_fake_belem - d_ijk_6_3_fake_belem
 + e_ijlk_6_2_3_fake_belem >= -3
_C1194: - a_ij_4_2 - b_ij_6_4 - d_ijk_6_2_fake_belem - d_ijk_6_4_fake_belem
 + e_ijlk_6_2_4_fake_belem >= -3
_C1195: - a_ij_5_2 - b_ij_6_5 - d_ijk_6_2_fake_belem - d_ijk_6_5_fake_belem
 + e_ijlk_6_2_5_fake_belem >= -3
_C1196: - a_ij_6_2 - b_ij_6_6 - d_ijk_6_2_fake_belem - d_ijk_6_6_fake_belem
 + e_ijlk_6_2_6_fake_belem >= -3
_C1197: d_ijk_6_2_fake_manila - x_ik_2_fake_manila - x_ik_6_fake_manila >= -1
_C1198: - a_ij_1_2 - b_ij_6_1 - d_ijk_6_1_fake_manila - d_ijk_6_2_fake_manila
 + e_ijlk_6_2_1_fake_manila >= -3
_C1199: - a_ij_2_2 - b_ij_6_2 - 2 d_ijk_6_2_fake_manila
 + e_ijlk_6_2_2_fake_manila >= -3
_C12: s_j_1 + 999999 z_ikt_1_fake_belem_1 + 999999 z_ikt_1_fake_manila_1
 <= 1000000
_C120: - c_j_2 + 4 z_ikt_2_fake_belem_4 + 4 z_ikt_2_fake_manila_4 <= 0
_C1200: - a_ij_3_2 - b_ij_6_3 - d_ijk_6_2_fake_manila - d_ijk_6_3_fake_manila
 + e_ijlk_6_2_3_fake_manila >= -3
_C1201: - a_ij_4_2 - b_ij_6_4 - d_ijk_6_2_fake_manila - d_ijk_6_4_fake_manila
 + e_ijlk_6_2_4_fake_manila >= -3
_C1202: - a_ij_5_2 - b_ij_6_5 - d_ijk_6_2_fake_manila - d_ijk_6_5_fake_manila
 + e_ijlk_6_2_5_fake_manila >= -3
_C1203: - a_ij_6_2 - b_ij_6_6 - d_ijk_6_2_fake_manila - d_ijk_6_6_fake_manila
 + e_ijlk_6_2_6_fake_manila >= -3
_C1204: a_ij_6_3 + 0.001 c_j_6 - 0.001 s_j_3 >= 0
_C1205: b_ij_6_3 - 0.001 c_j_3 + 0.001 c_j_6 >= 0
_C1206: d_ijk_6_3_fake_belem - x_ik_3_fake_belem - x_ik_6_fake_belem >= -1
_C1207: - a_ij_1_3 - b_ij_6_1 - d_ijk_6_1_fake_belem - d_ijk_6_3_fake_belem
 + e_ijlk_6_3_1_fake_belem >= -3
_C1208: - a_ij_2_3 - b_ij_6_2 - d_ijk_6_2_fake_belem - d_ijk_6_3_fake_belem
 + e_ijlk_6_3_2_fake_belem >= -3
_C1209: - a_ij_3_3 - b_ij_6_3 - 2 d_ijk_6_3_fake_belem
 + e_ijlk_6_3_3_fake_belem >= -3
_C121: z_ikt_2_fake_belem_4 + z_ikt_2_fake_manila_4 <= 1
_C1210: - a_ij_4_3 - b_ij_6_4 - d_ijk_6_3_fake_belem - d_ijk_6_4_fake_belem
 + e_ijlk_6_3_4_fake_belem >= -3
_C1211: - a_ij_5_3 - b_ij_6_5 - d_ijk_6_3_fake_belem - d_ijk_6_5_fake_belem
 + e_ijlk_6_3_5_fake_belem >= -3
_C1212: - a_ij_6_3 - b_ij_6_6 - d_ijk_6_3_fake_belem - d_ijk_6_6_fake_belem
 + e_ijlk_6_3_6_fake_belem >= -3
_C1213: d_ijk_6_3_fake_manila - x_ik_3_fake_manila - x_ik_6_fake_manila >= -1
_C1214: - a_ij_1_3 - b_ij_6_1 - d_ijk_6_1_fake_manila - d_ijk_6_3_fake_manila
 + e_ijlk_6_3_1_fake_manila >= -3
_C1215: - a_ij_2_3 - b_ij_6_2 - d_ijk_6_2_fake_manila - d_ijk_6_3_fake_manila
 + e_ijlk_6_3_2_fake_manila >= -3
_C1216: - a_ij_3_3 - b_ij_6_3 - 2 d_ijk_6_3_fake_manila
 + e_ijlk_6_3_3_fake_manila >= -3
_C1217: - a_ij_4_3 - b_ij_6_4 - d_ijk_6_3_fake_manila - d_ijk_6_4_fake_manila
 + e_ijlk_6_3_4_fake_manila >= -3
_C1218: - a_ij_5_3 - b_ij_6_5 - d_ijk_6_3_fake_manila - d_ijk_6_5_fake_manila
 + e_ijlk_6_3_5_fake_manila >= -3
_C1219: - a_ij_6_3 - b_ij_6_6 - d_ijk_6_3_fake_manila - d_ijk_6_6_fake_manila
 + e_ijlk_6_3_6_fake_manila >= -3
_C122: s_j_2 + 999996 z_ikt_2_fake_belem_4 + 999996 z_ikt_2_fake_manila_4
 <= 1000000
_C1220: a_ij_6_4 + 0.001 c_j_6 - 0.001 s_j_4 >= 0
_C1221: b_ij_6_4 - 0.001 c_j_4 + 0.001 c_j_6 >= 0
_C1222: d_ijk_6_4_fake_belem - x_ik_4_fake_belem - x_ik_6_fake_belem >= -1
_C1223: - a_ij_1_4 - b_ij_6_1 - d_ijk_6_1_fake_belem - d_ijk_6_4_fake_belem
 + e_ijlk_6_4_1_fake_belem >= -3
_C1224: - a_ij_2_4 - b_ij_6_2 - d_ijk_6_2_fake_belem - d_ijk_6_4_fake_belem
 + e_ijlk_6_4_2_fake_belem >= -3
_C1225: - a_ij_3_4 - b_ij_6_3 - d_ijk_6_3_fake_belem - d_ijk_6_4_fake_belem
 + e_ijlk_6_4_3_fake_belem >= -3
_C1226: - a_ij_4_4 - b_ij_6_4 - 2 d_ijk_6_4_fake_belem
 + e_ijlk_6_4_4_fake_belem >= -3
_C1227: - a_ij_5_4 - b_ij_6_5 - d_ijk_6_4_fake_belem - d_ijk_6_5_fake_belem
 + e_ijlk_6_4_5_fake_belem >= -3
_C1228: - a_ij_6_4 - b_ij_6_6 - d_ijk_6_4_fake_belem - d_ijk_6_6_fake_belem
 + e_ijlk_6_4_6_fake_belem >= -3
_C1229: d_ijk_6_4_fake_manila - x_ik_4_fake_manila - x_ik_6_fake_manila >= -1
_C123: - c_j_2 + 5 z_ikt_2_fake_belem_5 + 5 z_ikt_2_fake_manila_5 <= 0
_C1230: - a_ij_1_4 - b_ij_6_1 - d_ijk_6_1_fake_manila - d_ijk_6_4_fake_manila
 + e_ijlk_6_4_1_fake_manila >= -3
_C1231: - a_ij_2_4 - b_ij_6_2 - d_ijk_6_2_fake_manila - d_ijk_6_4_fake_manila
 + e_ijlk_6_4_2_fake_manila >= -3
_C1232: - a_ij_3_4 - b_ij_6_3 - d_ijk_6_3_fake_manila - d_ijk_6_4_fake_manila
 + e_ijlk_6_4_3_fake_manila >= -3
_C1233: - a_ij_4_4 - b_ij_6_4 - 2 d_ijk_6_4_fake_manila
 + e_ijlk_6_4_4_fake_manila >= -3
_C1234: - a_ij_5_4 - b_ij_6_5 - d_ijk_6_4_fake_manila - d_ijk_6_5_fake_manila
 + e_ijlk_6_4_5_fake_manila >= -3
_C1235: - a_ij_6_4 - b_ij_6_6 - d_ijk_6_4_fake_manila - d_ijk_6_6_fake_manila
 + e_ijlk_6_4_6_fake_manila >= -3
_C1236: a_ij_6_5 + 0.001 c_j_6 - 0.001 s_j_5 >= 0
_C1237: b_ij_6_5 - 0.001 c_j_5 + 0.001 c_j_6 >= 0
_C1238: d_ijk_6_5_fake_belem - x_ik_5_fake_belem - x_ik_6_fake_belem >= -1
_C1239: - a_ij_1_5 - b_ij_6_1 - d_ijk_6_1_fake_belem - d_ijk_6_5_fake_belem
 + e_ijlk_6_5_1_fake_belem >= -3
_C124: z_ikt_2_fake_belem_5 + z_ikt_2_fake_manila_5 <= 1
_C1240: - a_ij_2_5 - b_ij_6_2 - d_ijk_6_2_fake_belem - d_ijk_6_5_fake_belem
 + e_ijlk_6_5_2_fake_belem >= -3
_C1241: - a_ij_3_5 - b_ij_6_3 - d_ijk_6_3_fake_belem - d_ijk_6_5_fake_belem
 + e_ijlk_6_5_3_fake_belem >= -3
_C1242: - a_ij_4_5 - b_ij_6_4 - d_ijk_6_4_fake_belem - d_ijk_6_5_fake_belem
 + e_ijlk_6_5_4_fake_belem >= -3
_C1243: - a_ij_5_5 - b_ij_6_5 - 2 d_ijk_6_5_fake_belem
 + e_ijlk_6_5_5_fake_belem >= -3
_C1244: - a_ij_6_5 - b_ij_6_6 - d_ijk_6_5_fake_belem - d_ijk_6_6_fake_belem
 + e_ijlk_6_5_6_fake_belem >= -3
_C1245: d_ijk_6_5_fake_manila - x_ik_5_fake_manila - x_ik_6_fake_manila >= -1
_C1246: - a_ij_1_5 - b_ij_6_1 - d_ijk_6_1_fake_manila - d_ijk_6_5_fake_manila
 + e_ijlk_6_5_1_fake_manila >= -3
_C1247: - a_ij_2_5 - b_ij_6_2 - d_ijk_6_2_fake_manila - d_ijk_6_5_fake_manila
 + e_ijlk_6_5_2_fake_manila >= -3
_C1248: - a_ij_3_5 - b_ij_6_3 - d_ijk_6_3_fake_manila - d_ijk_6_5_fake_manila
 + e_ijlk_6_5_3_fake_manila >= -3
_C1249: - a_ij_4_5 - b_ij_6_4 - d_ijk_6_4_fake_manila - d_ijk_6_5_fake_manila
 + e_ijlk_6_5_4_fake_manila >= -3
_C125: s_j_2 + 999995 z_ikt_2_fake_belem_5 + 999995 z_ikt_2_fake_manila_5
 <= 1000000
_C1250: - a_ij_5_5 - b_ij_6_5 - 2 d_ijk_6_5_fake_manila
 + e_ijlk_6_5_5_fake_manila >= -3
_C1251: - a_ij_6_5 - b_ij_6_6 - d_ijk_6_5_fake_manila - d_ijk_6_6_fake_manila
 + e_ijlk_6_5_6_fake_manila >= -3
_C1252: a_ij_6_6 = 0
_C1253: b_ij_6_6 = 0
_C1254: - a_ij_1_1 - d_ijk_1_1_fake_belem - 0.001 e_ijlk_1_1_1_fake_belem
 - 0.001 e_ijlk_1_1_2_fake_belem - 0.001 e_ijlk_1_1_3_fake_belem
 - 0.001 e_ijlk_1_1_4_fake_belem - 0.001 e_ijlk_1_1_5_fake_belem
 - 0.001 e_ijlk_1_1_6_fake_belem + y_ijk_1_1_fake_belem >= -2
_C1255: - a_ij_1_1 - d_ijk_1_1_fake_manila - 0.001 e_ijlk_1_1_1_fake_manila
 - 0.001 e_ijlk_1_1_2_fake_manila - 0.001 e_ijlk_1_1_3_fake_manila
 - 0.001 e_ijlk_1_1_4_fake_manila - 0.001 e_ijlk_1_1_5_fake_manila
 - 0.001 e_ijlk_1_1_6_fake_manila + y_ijk_1_1_fake_manila >= -2
_C1256: - a_ij_1_2 - d_ijk_1_2_fake_belem - 0.001 e_ijlk_1_2_1_fake_belem
 - 0.001 e_ijlk_1_2_2_fake_belem - 0.001 e_ijlk_1_2_3_fake_belem
 - 0.001 e_ijlk_1_2_4_fake_belem - 0.001 e_ijlk_1_2_5_fake_belem
 - 0.001 e_ijlk_1_2_6_fake_belem + y_ijk_1_2_fake_belem >= -2
_C1257: - a_ij_1_2 - d_ijk_1_2_fake_manila - 0.001 e_ijlk_1_2_1_fake_manila
 - 0.001 e_ijlk_1_2_2_fake_manila - 0.001 e_ijlk_1_2_3_fake_manila
 - 0.001 e_ijlk_1_2_4_fake_manila - 0.001 e_ijlk_1_2_5_fake_manila
 - 0.001 e_ijlk_1_2_6_fake_manila + y_ijk_1_2_fake_manila >= -2
_C1258: - a_ij_1_3 - d_ijk_1_3_fake_belem - 0.001 e_ijlk_1_3_1_fake_belem
 - 0.001 e_ijlk_1_3_2_fake_belem - 0.001 e_ijlk_1_3_3_fake_belem
 - 0.001 e_ijlk_1_3_4_fake_belem - 0.001 e_ijlk_1_3_5_fake_belem
 - 0.001 e_ijlk_1_3_6_fake_belem + y_ijk_1_3_fake_belem >= -2
_C1259: - a_ij_1_3 - d_ijk_1_3_fake_manila - 0.001 e_ijlk_1_3_1_fake_manila
 - 0.001 e_ijlk_1_3_2_fake_manila - 0.001 e_ijlk_1_3_3_fake_manila
 - 0.001 e_ijlk_1_3_4_fake_manila - 0.001 e_ijlk_1_3_5_fake_manila
 - 0.001 e_ijlk_1_3_6_fake_manila + y_ijk_1_3_fake_manila >= -2
_C126: - c_j_2 + 6 z_ikt_2_fake_belem_6 + 6 z_ikt_2_fake_manila_6 <= 0
_C1260: - a_ij_1_4 - d_ijk_1_4_fake_belem - 0.001 e_ijlk_1_4_1_fake_belem
 - 0.001 e_ijlk_1_4_2_fake_belem - 0.001 e_ijlk_1_4_3_fake_belem
 - 0.001 e_ijlk_1_4_4_fake_belem - 0.001 e_ijlk_1_4_5_fake_belem
 - 0.001 e_ijlk_1_4_6_fake_belem + y_ijk_1_4_fake_belem >= -2
_C1261: - a_ij_1_4 - d_ijk_1_4_fake_manila - 0.001 e_ijlk_1_4_1_fake_manila
 - 0.001 e_ijlk_1_4_2_fake_manila - 0.001 e_ijlk_1_4_3_fake_manila
 - 0.001 e_ijlk_1_4_4_fake_manila - 0.001 e_ijlk_1_4_5_fake_manila
 - 0.001 e_ijlk_1_4_6_fake_manila + y_ijk_1_4_fake_manila >= -2
_C1262: - a_ij_1_5 - d_ijk_1_5_fake_belem - 0.001 e_ijlk_1_5_1_fake_belem
 - 0.001 e_ijlk_1_5_2_fake_belem - 0.001 e_ijlk_1_5_3_fake_belem
 - 0.001 e_ijlk_1_5_4_fake_belem - 0.001 e_ijlk_1_5_5_fake_belem
 - 0.001 e_ijlk_1_5_6_fake_belem + y_ijk_1_5_fake_belem >= -2
_C1263: - a_ij_1_5 - d_ijk_1_5_fake_manila - 0.001 e_ijlk_1_5_1_fake_manila
 - 0.001 e_ijlk_1_5_2_fake_manila - 0.001 e_ijlk_1_5_3_fake_manila
 - 0.001 e_ijlk_1_5_4_fake_manila - 0.001 e_ijlk_1_5_5_fake_manila
 - 0.001 e_ijlk_1_5_6_fake_manila + y_ijk_1_5_fake_manila >= -2
_C1264: - a_ij_1_6 - d_ijk_1_6_fake_belem - 0.001 e_ijlk_1_6_1_fake_belem
 - 0.001 e_ijlk_1_6_2_fake_belem - 0.001 e_ijlk_1_6_3_fake_belem
 - 0.001 e_ijlk_1_6_4_fake_belem - 0.001 e_ijlk_1_6_5_fake_belem
 - 0.001 e_ijlk_1_6_6_fake_belem + y_ijk_1_6_fake_belem >= -2
_C1265: - a_ij_1_6 - d_ijk_1_6_fake_manila - 0.001 e_ijlk_1_6_1_fake_manila
 - 0.001 e_ijlk_1_6_2_fake_manila - 0.001 e_ijlk_1_6_3_fake_manila
 - 0.001 e_ijlk_1_6_4_fake_manila - 0.001 e_ijlk_1_6_5_fake_manila
 - 0.001 e_ijlk_1_6_6_fake_manila + y_ijk_1_6_fake_manila >= -2
_C1266: - a_ij_2_1 - d_ijk_2_1_fake_belem - 0.001 e_ijlk_2_1_1_fake_belem
 - 0.001 e_ijlk_2_1_2_fake_belem - 0.001 e_ijlk_2_1_3_fake_belem
 - 0.001 e_ijlk_2_1_4_fake_belem - 0.001 e_ijlk_2_1_5_fake_belem
 - 0.001 e_ijlk_2_1_6_fake_belem + y_ijk_2_1_fake_belem >= -2
_C1267: - a_ij_2_1 - d_ijk_2_1_fake_manila - 0.001 e_ijlk_2_1_1_fake_manila
 - 0.001 e_ijlk_2_1_2_fake_manila - 0.001 e_ijlk_2_1_3_fake_manila
 - 0.001 e_ijlk_2_1_4_fake_manila - 0.001 e_ijlk_2_1_5_fake_manila
 - 0.001 e_ijlk_2_1_6_fake_manila + y_ijk_2_1_fake_manila >= -2
_C1268: - a_ij_2_2 - d_ijk_2_2_fake_belem - 0.001 e_ijlk_2_2_1_fake_belem
 - 0.001 e_ijlk_2_2_2_fake_belem - 0.001 e_ijlk_2_2_3_fake_belem
 - 0.001 e_ijlk_2_2_4_fake_belem - 0.001 e_ijlk_2_2_5_fake_belem
 - 0.001 e_ijlk_2_2_6_fake_belem + y_ijk_2_2_fake_belem >= -2
_C1269: - a_ij_2_2 - d_ijk_2_2_fake_manila - 0.001 e_ijlk_2_2_1_fake_manila
 - 0.001 e_ijlk_2_2_2_fake_manila - 0.001 e_ijlk_2_2_3_fake_manila
 - 0.001 e_ijlk_2_2_4_fake_manila - 0.001 e_ijlk_2_2_5_fake_manila
 - 0.001 e_ijlk_2_2_6_fake_manila + y_ijk_2_2_fake_manila >= -2
_C127: z_ikt_2_fake_belem_6 + z_ikt_2_fake_manila_6 <= 1
_C1270: - a_ij_2_3 - d_ijk_2_3_fake_belem - 0.001 e_ijlk_2_3_1_fake_belem
 - 0.001 e_ijlk_2_3_2_fake_belem - 0.001 e_ijlk_2_3_3_fake_belem
 - 0.001 e_ijlk_2_3_4_fake_belem - 0.001 e_ijlk_2_3_5_fake_belem
 - 0.001 e_ijlk_2_3_6_fake_belem + y_ijk_2_3_fake_belem >= -2
_C1271: - a_ij_2_3 - d_ijk_2_3_fake_manila - 0.001 e_ijlk_2_3_1_fake_manila
 - 0.001 e_ijlk_2_3_2_fake_manila - 0.001 e_ijlk_2_3_3_fake_manila
 - 0.001 e_ijlk_2_3_4_fake_manila - 0.001 e_ijlk_2_3_5_fake_manila
 - 0.001 e_ijlk_2_3_6_fake_manila + y_ijk_2_3_fake_manila >= -2
_C1272: - a_ij_2_4 - d_ijk_2_4_fake_belem - 0.001 e_ijlk_2_4_1_fake_belem
 - 0.001 e_ijlk_2_4_2_fake_belem - 0.001 e_ijlk_2_4_3_fake_belem
 - 0.001 e_ijlk_2_4_4_fake_belem - 0.001 e_ijlk_2_4_5_fake_belem
 - 0.001 e_ijlk_2_4_6_fake_belem + y_ijk_2_4_fake_belem >= -2
_C1273: - a_ij_2_4 - d_ijk_2_4_fake_manila - 0.001 e_ijlk_2_4_1_fake_manila
 - 0.001 e_ijlk_2_4_2_fake_manila - 0.001 e_ijlk_2_4_3_fake_manila
 - 0.001 e_ijlk_2_4_4_fake_manila - 0.001 e_ijlk_2_4_5_fake_manila
 - 0.001 e_ijlk_2_4_6_fake_manila + y_ijk_2_4_fake_manila >= -2
_C1274: - a_ij_2_5 - d_ijk_2_5_fake_belem - 0.001 e_ijlk_2_5_1_fake_belem
 - 0.001 e_ijlk_2_5_2_fake_belem - 0.001 e_ijlk_2_5_3_fake_belem
 - 0.001 e_ijlk_2_5_4_fake_belem - 0.001 e_ijlk_2_5_5_fake_belem
 - 0.001 e_ijlk_2_5_6_fake_belem + y_ijk_2_5_fake_belem >= -2
_C1275: - a_ij_2_5 - d_ijk_2_5_fake_manila - 0.001 e_ijlk_2_5_1_fake_manila
 - 0.001 e_ijlk_2_5_2_fake_manila - 0.001 e_ijlk_2_5_3_fake_manila
 - 0.001 e_ijlk_2_5_4_fake_manila - 0.001 e_ijlk_2_5_5_fake_manila
 - 0.001 e_ijlk_2_5_6_fake_manila + y_ijk_2_5_fake_manila >= -2
_C1276: - a_ij_2_6 - d_ijk_2_6_fake_belem - 0.001 e_ijlk_2_6_1_fake_belem
 - 0.001 e_ijlk_2_6_2_fake_belem - 0.001 e_ijlk_2_6_3_fake_belem
 - 0.001 e_ijlk_2_6_4_fake_belem - 0.001 e_ijlk_2_6_5_fake_belem
 - 0.001 e_ijlk_2_6_6_fake_belem + y_ijk_2_6_fake_belem >= -2
_C1277: - a_ij_2_6 - d_ijk_2_6_fake_manila - 0.001 e_ijlk_2_6_1_fake_manila
 - 0.001 e_ijlk_2_6_2_fake_manila - 0.001 e_ijlk_2_6_3_fake_manila
 - 0.001 e_ijlk_2_6_4_fake_manila - 0.001 e_ijlk_2_6_5_fake_manila
 - 0.001 e_ijlk_2_6_6_fake_manila + y_ijk_2_6_fake_manila >= -2
_C1278: - a_ij_3_1 - d_ijk_3_1_fake_belem - 0.001 e_ijlk_3_1_1_fake_belem
 - 0.001 e_ijlk_3_1_2_fake_belem - 0.001 e_ijlk_3_1_3_fake_belem
 - 0.001 e_ijlk_3_1_4_fake_belem - 0.001 e_ijlk_3_1_5_fake_belem
 - 0.001 e_ijlk_3_1_6_fake_belem + y_ijk_3_1_fake_belem >= -2
_C1279: - a_ij_3_1 - d_ijk_3_1_fake_manila - 0.001 e_ijlk_3_1_1_fake_manila
 - 0.001 e_ijlk_3_1_2_fake_manila - 0.001 e_ijlk_3_1_3_fake_manila
 - 0.001 e_ijlk_3_1_4_fake_manila - 0.001 e_ijlk_3_1_5_fake_manila
 - 0.001 e_ijlk_3_1_6_fake_manila + y_ijk_3_1_fake_manila >= -2
_C128: s_j_2 + 999994 z_ikt_2_fake_belem_6 + 999994 z_ikt_2_fake_manila_6
 <= 1000000
_C1280: - a_ij_3_2 - d_ijk_3_2_fake_belem - 0.001 e_ijlk_3_2_1_fake_belem
 - 0.001 e_ijlk_3_2_2_fake_belem - 0.001 e_ijlk_3_2_3_fake_belem
 - 0.001 e_ijlk_3_2_4_fake_belem - 0.001 e_ijlk_3_2_5_fake_belem
 - 0.001 e_ijlk_3_2_6_fake_belem + y_ijk_3_2_fake_belem >= -2
_C1281: - a_ij_3_2 - d_ijk_3_2_fake_manila - 0.001 e_ijlk_3_2_1_fake_manila
 - 0.001 e_ijlk_3_2_2_fake_manila - 0.001 e_ijlk_3_2_3_fake_manila
 - 0.001 e_ijlk_3_2_4_fake_manila - 0.001 e_ijlk_3_2_5_fake_manila
 - 0.001 e_ijlk_3_2_6_fake_manila + y_ijk_3_2_fake_manila >= -2
_C1282: - a_ij_3_3 - d_ijk_3_3_fake_belem - 0.001 e_ijlk_3_3_1_fake_belem
 - 0.001 e_ijlk_3_3_2_fake_belem - 0.001 e_ijlk_3_3_3_fake_belem
 - 0.001 e_ijlk_3_3_4_fake_belem - 0.001 e_ijlk_3_3_5_fake_belem
 - 0.001 e_ijlk_3_3_6_fake_belem + y_ijk_3_3_fake_belem >= -2
_C1283: - a_ij_3_3 - d_ijk_3_3_fake_manila - 0.001 e_ijlk_3_3_1_fake_manila
 - 0.001 e_ijlk_3_3_2_fake_manila - 0.001 e_ijlk_3_3_3_fake_manila
 - 0.001 e_ijlk_3_3_4_fake_manila - 0.001 e_ijlk_3_3_5_fake_manila
 - 0.001 e_ijlk_3_3_6_fake_manila + y_ijk_3_3_fake_manila >= -2
_C1284: - a_ij_3_4 - d_ijk_3_4_fake_belem - 0.001 e_ijlk_3_4_1_fake_belem
 - 0.001 e_ijlk_3_4_2_fake_belem - 0.001 e_ijlk_3_4_3_fake_belem
 - 0.001 e_ijlk_3_4_4_fake_belem - 0.001 e_ijlk_3_4_5_fake_belem
 - 0.001 e_ijlk_3_4_6_fake_belem + y_ijk_3_4_fake_belem >= -2
_C1285: - a_ij_3_4 - d_ijk_3_4_fake_manila - 0.001 e_ijlk_3_4_1_fake_manila
 - 0.001 e_ijlk_3_4_2_fake_manila - 0.001 e_ijlk_3_4_3_fake_manila
 - 0.001 e_ijlk_3_4_4_fake_manila - 0.001 e_ijlk_3_4_5_fake_manila
 - 0.001 e_ijlk_3_4_6_fake_manila + y_ijk_3_4_fake_manila >= -2
_C1286: - a_ij_3_5 - d_ijk_3_5_fake_belem - 0.001 e_ijlk_3_5_1_fake_belem
 - 0.001 e_ijlk_3_5_2_fake_belem - 0.001 e_ijlk_3_5_3_fake_belem
 - 0.001 e_ijlk_3_5_4_fake_belem - 0.001 e_ijlk_3_5_5_fake_belem
 - 0.001 e_ijlk_3_5_6_fake_belem + y_ijk_3_5_fake_belem >= -2
_C1287: - a_ij_3_5 - d_ijk_3_5_fake_manila - 0.001 e_ijlk_3_5_1_fake_manila
 - 0.001 e_ijlk_3_5_2_fake_manila - 0.001 e_ijlk_3_5_3_fake_manila
 - 0.001 e_ijlk_3_5_4_fake_manila - 0.001 e_ijlk_3_5_5_fake_manila
 - 0.001 e_ijlk_3_5_6_fake_manila + y_ijk_3_5_fake_manila >= -2
_C1288: - a_ij_3_6 - d_ijk_3_6_fake_belem - 0.001 e_ijlk_3_6_1_fake_belem
 - 0.001 e_ijlk_3_6_2_fake_belem - 0.001 e_ijlk_3_6_3_fake_belem
 - 0.001 e_ijlk_3_6_4_fake_belem - 0.001 e_ijlk_3_6_5_fake_belem
 - 0.001 e_ijlk_3_6_6_fake_belem + y_ijk_3_6_fake_belem >= -2
_C1289: - a_ij_3_6 - d_ijk_3_6_fake_manila - 0.001 e_ijlk_3_6_1_fake_manila
 - 0.001 e_ijlk_3_6_2_fake_manila - 0.001 e_ijlk_3_6_3_fake_manila
 - 0.001 e_ijlk_3_6_4_fake_manila - 0.001 e_ijlk_3_6_5_fake_manila
 - 0.001 e_ijlk_3_6_6_fake_manila + y_ijk_3_6_fake_manila >= -2
_C129: - c_j_2 + 7 z_ikt_2_fake_belem_7 + 7 z_ikt_2_fake_manila_7 <= 0
_C1290: - a_ij_4_1 - d_ijk_4_1_fake_belem - 0.001 e_ijlk_4_1_1_fake_belem
 - 0.001 e_ijlk_4_1_2_fake_belem - 0.001 e_ijlk_4_1_3_fake_belem
 - 0.001 e_ijlk_4_1_4_fake_belem - 0.001 e_ijlk_4_1_5_fake_belem
 - 0.001 e_ijlk_4_1_6_fake_belem + y_ijk_4_1_fake_belem >= -2
_C1291: - a_ij_4_1 - d_ijk_4_1_fake_manila - 0.001 e_ijlk_4_1_1_fake_manila
 - 0.001 e_ijlk_4_1_2_fake_manila - 0.001 e_ijlk_4_1_3_fake_manila
 - 0.001 e_ijlk_4_1_4_fake_manila - 0.001 e_ijlk_4_1_5_fake_manila
 - 0.001 e_ijlk_4_1_6_fake_manila + y_ijk_4_1_fake_manila >= -2
_C1292: - a_ij_4_2 - d_ijk_4_2_fake_belem - 0.001 e_ijlk_4_2_1_fake_belem
 - 0.001 e_ijlk_4_2_2_fake_belem - 0.001 e_ijlk_4_2_3_fake_belem
 - 0.001 e_ijlk_4_2_4_fake_belem - 0.001 e_ijlk_4_2_5_fake_belem
 - 0.001 e_ijlk_4_2_6_fake_belem + y_ijk_4_2_fake_belem >= -2
_C1293: - a_ij_4_2 - d_ijk_4_2_fake_manila - 0.001 e_ijlk_4_2_1_fake_manila
 - 0.001 e_ijlk_4_2_2_fake_manila - 0.001 e_ijlk_4_2_3_fake_manila
 - 0.001 e_ijlk_4_2_4_fake_manila - 0.001 e_ijlk_4_2_5_fake_manila
 - 0.001 e_ijlk_4_2_6_fake_manila + y_ijk_4_2_fake_manila >= -2
_C1294: - a_ij_4_3 - d_ijk_4_3_fake_belem - 0.001 e_ijlk_4_3_1_fake_belem
 - 0.001 e_ijlk_4_3_2_fake_belem - 0.001 e_ijlk_4_3_3_fake_belem
 - 0.001 e_ijlk_4_3_4_fake_belem - 0.001 e_ijlk_4_3_5_fake_belem
 - 0.001 e_ijlk_4_3_6_fake_belem + y_ijk_4_3_fake_belem >= -2
_C1295: - a_ij_4_3 - d_ijk_4_3_fake_manila - 0.001 e_ijlk_4_3_1_fake_manila
 - 0.001 e_ijlk_4_3_2_fake_manila - 0.001 e_ijlk_4_3_3_fake_manila
 - 0.001 e_ijlk_4_3_4_fake_manila - 0.001 e_ijlk_4_3_5_fake_manila
 - 0.001 e_ijlk_4_3_6_fake_manila + y_ijk_4_3_fake_manila >= -2
_C1296: - a_ij_4_4 - d_ijk_4_4_fake_belem - 0.001 e_ijlk_4_4_1_fake_belem
 - 0.001 e_ijlk_4_4_2_fake_belem - 0.001 e_ijlk_4_4_3_fake_belem
 - 0.001 e_ijlk_4_4_4_fake_belem - 0.001 e_ijlk_4_4_5_fake_belem
 - 0.001 e_ijlk_4_4_6_fake_belem + y_ijk_4_4_fake_belem >= -2
_C1297: - a_ij_4_4 - d_ijk_4_4_fake_manila - 0.001 e_ijlk_4_4_1_fake_manila
 - 0.001 e_ijlk_4_4_2_fake_manila - 0.001 e_ijlk_4_4_3_fake_manila
 - 0.001 e_ijlk_4_4_4_fake_manila - 0.001 e_ijlk_4_4_5_fake_manila
 - 0.001 e_ijlk_4_4_6_fake_manila + y_ijk_4_4_fake_manila >= -2
_C1298: - a_ij_4_5 - d_ijk_4_5_fake_belem - 0.001 e_ijlk_4_5_1_fake_belem
 - 0.001 e_ijlk_4_5_2_fake_belem - 0.001 e_ijlk_4_5_3_fake_belem
 - 0.001 e_ijlk_4_5_4_fake_belem - 0.001 e_ijlk_4_5_5_fake_belem
 - 0.001 e_ijlk_4_5_6_fake_belem + y_ijk_4_5_fake_belem >= -2
_C1299: - a_ij_4_5 - d_ijk_4_5_fake_manila - 0.001 e_ijlk_4_5_1_fake_manila
 - 0.001 e_ijlk_4_5_2_fake_manila - 0.001 e_ijlk_4_5_3_fake_manila
 - 0.001 e_ijlk_4_5_4_fake_manila - 0.001 e_ijlk_4_5_5_fake_manila
 - 0.001 e_ijlk_4_5_6_fake_manila + y_ijk_4_5_fake_manila >= -2
_C13: - c_j_1 + 2 z_ikt_1_fake_belem_2 + 2 z_ikt_1_fake_manila_2 <= 0
_C130: z_ikt_2_fake_belem_7 + z_ikt_2_fake_manila_7 <= 1
_C1300: - a_ij_4_6 - d_ijk_4_6_fake_belem - 0.001 e_ijlk_4_6_1_fake_belem
 - 0.001 e_ijlk_4_6_2_fake_belem - 0.001 e_ijlk_4_6_3_fake_belem
 - 0.001 e_ijlk_4_6_4_fake_belem - 0.001 e_ijlk_4_6_5_fake_belem
 - 0.001 e_ijlk_4_6_6_fake_belem + y_ijk_4_6_fake_belem >= -2
_C1301: - a_ij_4_6 - d_ijk_4_6_fake_manila - 0.001 e_ijlk_4_6_1_fake_manila
 - 0.001 e_ijlk_4_6_2_fake_manila - 0.001 e_ijlk_4_6_3_fake_manila
 - 0.001 e_ijlk_4_6_4_fake_manila - 0.001 e_ijlk_4_6_5_fake_manila
 - 0.001 e_ijlk_4_6_6_fake_manila + y_ijk_4_6_fake_manila >= -2
_C1302: - a_ij_5_1 - d_ijk_5_1_fake_belem - 0.001 e_ijlk_5_1_1_fake_belem
 - 0.001 e_ijlk_5_1_2_fake_belem - 0.001 e_ijlk_5_1_3_fake_belem
 - 0.001 e_ijlk_5_1_4_fake_belem - 0.001 e_ijlk_5_1_5_fake_belem
 - 0.001 e_ijlk_5_1_6_fake_belem + y_ijk_5_1_fake_belem >= -2
_C1303: - a_ij_5_1 - d_ijk_5_1_fake_manila - 0.001 e_ijlk_5_1_1_fake_manila
 - 0.001 e_ijlk_5_1_2_fake_manila - 0.001 e_ijlk_5_1_3_fake_manila
 - 0.001 e_ijlk_5_1_4_fake_manila - 0.001 e_ijlk_5_1_5_fake_manila
 - 0.001 e_ijlk_5_1_6_fake_manila + y_ijk_5_1_fake_manila >= -2
_C1304: - a_ij_5_2 - d_ijk_5_2_fake_belem - 0.001 e_ijlk_5_2_1_fake_belem
 - 0.001 e_ijlk_5_2_2_fake_belem - 0.001 e_ijlk_5_2_3_fake_belem
 - 0.001 e_ijlk_5_2_4_fake_belem - 0.001 e_ijlk_5_2_5_fake_belem
 - 0.001 e_ijlk_5_2_6_fake_belem + y_ijk_5_2_fake_belem >= -2
_C1305: - a_ij_5_2 - d_ijk_5_2_fake_manila - 0.001 e_ijlk_5_2_1_fake_manila
 - 0.001 e_ijlk_5_2_2_fake_manila - 0.001 e_ijlk_5_2_3_fake_manila
 - 0.001 e_ijlk_5_2_4_fake_manila - 0.001 e_ijlk_5_2_5_fake_manila
 - 0.001 e_ijlk_5_2_6_fake_manila + y_ijk_5_2_fake_manila >= -2
_C1306: - a_ij_5_3 - d_ijk_5_3_fake_belem - 0.001 e_ijlk_5_3_1_fake_belem
 - 0.001 e_ijlk_5_3_2_fake_belem - 0.001 e_ijlk_5_3_3_fake_belem
 - 0.001 e_ijlk_5_3_4_fake_belem - 0.001 e_ijlk_5_3_5_fake_belem
 - 0.001 e_ijlk_5_3_6_fake_belem + y_ijk_5_3_fake_belem >= -2
_C1307: - a_ij_5_3 - d_ijk_5_3_fake_manila - 0.001 e_ijlk_5_3_1_fake_manila
 - 0.001 e_ijlk_5_3_2_fake_manila - 0.001 e_ijlk_5_3_3_fake_manila
 - 0.001 e_ijlk_5_3_4_fake_manila - 0.001 e_ijlk_5_3_5_fake_manila
 - 0.001 e_ijlk_5_3_6_fake_manila + y_ijk_5_3_fake_manila >= -2
_C1308: - a_ij_5_4 - d_ijk_5_4_fake_belem - 0.001 e_ijlk_5_4_1_fake_belem
 - 0.001 e_ijlk_5_4_2_fake_belem - 0.001 e_ijlk_5_4_3_fake_belem
 - 0.001 e_ijlk_5_4_4_fake_belem - 0.001 e_ijlk_5_4_5_fake_belem
 - 0.001 e_ijlk_5_4_6_fake_belem + y_ijk_5_4_fake_belem >= -2
_C1309: - a_ij_5_4 - d_ijk_5_4_fake_manila - 0.001 e_ijlk_5_4_1_fake_manila
 - 0.001 e_ijlk_5_4_2_fake_manila - 0.001 e_ijlk_5_4_3_fake_manila
 - 0.001 e_ijlk_5_4_4_fake_manila - 0.001 e_ijlk_5_4_5_fake_manila
 - 0.001 e_ijlk_5_4_6_fake_manila + y_ijk_5_4_fake_manila >= -2
_C131: s_j_2 + 999993 z_ikt_2_fake_belem_7 + 999993 z_ikt_2_fake_manila_7
 <= 1000000
_C1310: - a_ij_5_5 - d_ijk_5_5_fake_belem - 0.001 e_ijlk_5_5_1_fake_belem
 - 0.001 e_ijlk_5_5_2_fake_belem - 0.001 e_ijlk_5_5_3_fake_belem
 - 0.001 e_ijlk_5_5_4_fake_belem - 0.001 e_ijlk_5_5_5_fake_belem
 - 0.001 e_ijlk_5_5_6_fake_belem + y_ijk_5_5_fake_belem >= -2
_C1311: - a_ij_5_5 - d_ijk_5_5_fake_manila - 0.001 e_ijlk_5_5_1_fake_manila
 - 0.001 e_ijlk_5_5_2_fake_manila - 0.001 e_ijlk_5_5_3_fake_manila
 - 0.001 e_ijlk_5_5_4_fake_manila - 0.001 e_ijlk_5_5_5_fake_manila
 - 0.001 e_ijlk_5_5_6_fake_manila + y_ijk_5_5_fake_manila >= -2
_C1312: - a_ij_5_6 - d_ijk_5_6_fake_belem - 0.001 e_ijlk_5_6_1_fake_belem
 - 0.001 e_ijlk_5_6_2_fake_belem - 0.001 e_ijlk_5_6_3_fake_belem
 - 0.001 e_ijlk_5_6_4_fake_belem - 0.001 e_ijlk_5_6_5_fake_belem
 - 0.001 e_ijlk_5_6_6_fake_belem + y_ijk_5_6_fake_belem >= -2
_C1313: - a_ij_5_6 - d_ijk_5_6_fake_manila - 0.001 e_ijlk_5_6_1_fake_manila
 - 0.001 e_ijlk_5_6_2_fake_manila - 0.001 e_ijlk_5_6_3_fake_manila
 - 0.001 e_ijlk_5_6_4_fake_manila - 0.001 e_ijlk_5_6_5_fake_manila
 - 0.001 e_ijlk_5_6_6_fake_manila + y_ijk_5_6_fake_manila >= -2
_C1314: - a_ij_6_1 - d_ijk_6_1_fake_belem - 0.001 e_ijlk_6_1_1_fake_belem
 - 0.001 e_ijlk_6_1_2_fake_belem - 0.001 e_ijlk_6_1_3_fake_belem
 - 0.001 e_ijlk_6_1_4_fake_belem - 0.001 e_ijlk_6_1_5_fake_belem
 - 0.001 e_ijlk_6_1_6_fake_belem + y_ijk_6_1_fake_belem >= -2
_C1315: - a_ij_6_1 - d_ijk_6_1_fake_manila - 0.001 e_ijlk_6_1_1_fake_manila
 - 0.001 e_ijlk_6_1_2_fake_manila - 0.001 e_ijlk_6_1_3_fake_manila
 - 0.001 e_ijlk_6_1_4_fake_manila - 0.001 e_ijlk_6_1_5_fake_manila
 - 0.001 e_ijlk_6_1_6_fake_manila + y_ijk_6_1_fake_manila >= -2
_C1316: - a_ij_6_2 - d_ijk_6_2_fake_belem - 0.001 e_ijlk_6_2_1_fake_belem
 - 0.001 e_ijlk_6_2_2_fake_belem - 0.001 e_ijlk_6_2_3_fake_belem
 - 0.001 e_ijlk_6_2_4_fake_belem - 0.001 e_ijlk_6_2_5_fake_belem
 - 0.001 e_ijlk_6_2_6_fake_belem + y_ijk_6_2_fake_belem >= -2
_C1317: - a_ij_6_2 - d_ijk_6_2_fake_manila - 0.001 e_ijlk_6_2_1_fake_manila
 - 0.001 e_ijlk_6_2_2_fake_manila - 0.001 e_ijlk_6_2_3_fake_manila
 - 0.001 e_ijlk_6_2_4_fake_manila - 0.001 e_ijlk_6_2_5_fake_manila
 - 0.001 e_ijlk_6_2_6_fake_manila + y_ijk_6_2_fake_manila >= -2
_C1318: - a_ij_6_3 - d_ijk_6_3_fake_belem - 0.001 e_ijlk_6_3_1_fake_belem
 - 0.001 e_ijlk_6_3_2_fake_belem - 0.001 e_ijlk_6_3_3_fake_belem
 - 0.001 e_ijlk_6_3_4_fake_belem - 0.001 e_ijlk_6_3_5_fake_belem
 - 0.001 e_ijlk_6_3_6_fake_belem + y_ijk_6_3_fake_belem >= -2
_C1319: - a_ij_6_3 - d_ijk_6_3_fake_manila - 0.001 e_ijlk_6_3_1_fake_manila
 - 0.001 e_ijlk_6_3_2_fake_manila - 0.001 e_ijlk_6_3_3_fake_manila
 - 0.001 e_ijlk_6_3_4_fake_manila - 0.001 e_ijlk_6_3_5_fake_manila
 - 0.001 e_ijlk_6_3_6_fake_manila + y_ijk_6_3_fake_manila >= -2
_C132: - c_j_2 + 8 z_ikt_2_fake_belem_8 + 8 z_ikt_2_fake_manila_8 <= 0
_C1320: - a_ij_6_4 - d_ijk_6_4_fake_belem - 0.001 e_ijlk_6_4_1_fake_belem
 - 0.001 e_ijlk_6_4_2_fake_belem - 0.001 e_ijlk_6_4_3_fake_belem
 - 0.001 e_ijlk_6_4_4_fake_belem - 0.001 e_ijlk_6_4_5_fake_belem
 - 0.001 e_ijlk_6_4_6_fake_belem + y_ijk_6_4_fake_belem >= -2
_C1321: - a_ij_6_4 - d_ijk_6_4_fake_manila - 0.001 e_ijlk_6_4_1_fake_manila
 - 0.001 e_ijlk_6_4_2_fake_manila - 0.001 e_ijlk_6_4_3_fake_manila
 - 0.001 e_ijlk_6_4_4_fake_manila - 0.001 e_ijlk_6_4_5_fake_manila
 - 0.001 e_ijlk_6_4_6_fake_manila + y_ijk_6_4_fake_manila >= -2
_C1322: - a_ij_6_5 - d_ijk_6_5_fake_belem - 0.001 e_ijlk_6_5_1_fake_belem
 - 0.001 e_ijlk_6_5_2_fake_belem - 0.001 e_ijlk_6_5_3_fake_belem
 - 0.001 e_ijlk_6_5_4_fake_belem - 0.001 e_ijlk_6_5_5_fake_belem
 - 0.001 e_ijlk_6_5_6_fake_belem + y_ijk_6_5_fake_belem >= -2
_C1323: - a_ij_6_5 - d_ijk_6_5_fake_manila - 0.001 e_ijlk_6_5_1_fake_manila
 - 0.001 e_ijlk_6_5_2_fake_manila - 0.001 e_ijlk_6_5_3_fake_manila
 - 0.001 e_ijlk_6_5_4_fake_manila - 0.001 e_ijlk_6_5_5_fake_manila
 - 0.001 e_ijlk_6_5_6_fake_manila + y_ijk_6_5_fake_manila >= -2
_C1324: - a_ij_6_6 - d_ijk_6_6_fake_belem - 0.001 e_ijlk_6_6_1_fake_belem
 - 0.001 e_ijlk_6_6_2_fake_belem - 0.001 e_ijlk_6_6_3_fake_belem
 - 0.001 e_ijlk_6_6_4_fake_belem - 0.001 e_ijlk_6_6_5_fake_belem
 - 0.001 e_ijlk_6_6_6_fake_belem + y_ijk_6_6_fake_belem >= -2
_C1325: - a_ij_6_6 - d_ijk_6_6_fake_manila - 0.001 e_ijlk_6_6_1_fake_manila
 - 0.001 e_ijlk_6_6_2_fake_manila - 0.001 e_ijlk_6_6_3_fake_manila
 - 0.001 e_ijlk_6_6_4_fake_manila - 0.001 e_ijlk_6_6_5_fake_manila
 - 0.001 e_ijlk_6_6_6_fake_manila + y_ijk_6_6_fake_manila >= -2
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
_C305: c_j_4 - makespan <= 0
_C306: x_ik_4_fake_belem + x_ik_4_fake_manila = 1
_C307: c_j_4 - s_j_4 - z_ikt_4_fake_belem_0 - z_ikt_4_fake_belem_1
 - z_ikt_4_fake_belem_10 - z_ikt_4_fake_belem_11 - z_ikt_4_fake_belem_12
 - z_ikt_4_fake_belem_13 - z_ikt_4_fake_belem_14 - z_ikt_4_fake_belem_15
 - z_ikt_4_fake_belem_16 - z_ikt_4_fake_belem_17 - z_ikt_4_fake_belem_18
 - z_ikt_4_fake_belem_19 - z_ikt_4_fake_belem_2 - z_ikt_4_fake_belem_20
 - z_ikt_4_fake_belem_21 - z_ikt_4_fake_belem_22 - z_ikt_4_fake_belem_23
 - z_ikt_4_fake_belem_24 - z_ikt_4_fake_belem_25 - z_ikt_4_fake_belem_26
 - z_ikt_4_fake_belem_27 - z_ikt_4_fake_belem_28 - z_ikt_4_fake_belem_29
 - z_ikt_4_fake_belem_3 - z_ikt_4_fake_belem_30 - z_ikt_4_fake_belem_31
 - z_ikt_4_fake_belem_4 - z_ikt_4_fake_belem_5 - z_ikt_4_fake_belem_6
 - z_ikt_4_fake_belem_7 - z_ikt_4_fake_belem_8 - z_ikt_4_fake_belem_9
 - z_ikt_4_fake_manila_0 - z_ikt_4_fake_manila_1 - z_ikt_4_fake_manila_10
 - z_ikt_4_fake_manila_11 - z_ikt_4_fake_manila_12 - z_ikt_4_fake_manila_13
 - z_ikt_4_fake_manila_14 - z_ikt_4_fake_manila_15 - z_ikt_4_fake_manila_16
 - z_ikt_4_fake_manila_17 - z_ikt_4_fake_manila_18 - z_ikt_4_fake_manila_19
 - z_ikt_4_fake_manila_2 - z_ikt_4_fake_manila_20 - z_ikt_4_fake_manila_21
 - z_ikt_4_fake_manila_22 - z_ikt_4_fake_manila_23 - z_ikt_4_fake_manila_24
 - z_ikt_4_fake_manila_25 - z_ikt_4_fake_manila_26 - z_ikt_4_fake_manila_27
 - z_ikt_4_fake_manila_28 - z_ikt_4_fake_manila_29 - z_ikt_4_fake_manila_3
 - z_ikt_4_fake_manila_30 - z_ikt_4_fake_manila_31 - z_ikt_4_fake_manila_4
 - z_ikt_4_fake_manila_5 - z_ikt_4_fake_manila_6 - z_ikt_4_fake_manila_7
 - z_ikt_4_fake_manila_8 - z_ikt_4_fake_manila_9 = -1
_C308: - 1000000 x_ik_4_fake_belem + z_ikt_4_fake_belem_0
 + z_ikt_4_fake_belem_1 + z_ikt_4_fake_belem_10 + z_ikt_4_fake_belem_11
 + z_ikt_4_fake_belem_12 + z_ikt_4_fake_belem_13 + z_ikt_4_fake_belem_14
 + z_ikt_4_fake_belem_15 + z_ikt_4_fake_belem_16 + z_ikt_4_fake_belem_17
 + z_ikt_4_fake_belem_18 + z_ikt_4_fake_belem_19 + z_ikt_4_fake_belem_2
 + z_ikt_4_fake_belem_20 + z_ikt_4_fake_belem_21 + z_ikt_4_fake_belem_22
 + z_ikt_4_fake_belem_23 + z_ikt_4_fake_belem_24 + z_ikt_4_fake_belem_25
 + z_ikt_4_fake_belem_26 + z_ikt_4_fake_belem_27 + z_ikt_4_fake_belem_28
 + z_ikt_4_fake_belem_29 + z_ikt_4_fake_belem_3 + z_ikt_4_fake_belem_30
 + z_ikt_4_fake_belem_31 + z_ikt_4_fake_belem_4 + z_ikt_4_fake_belem_5
 + z_ikt_4_fake_belem_6 + z_ikt_4_fake_belem_7 + z_ikt_4_fake_belem_8
 + z_ikt_4_fake_belem_9 <= 0
_C309: - 1000000 x_ik_4_fake_manila + z_ikt_4_fake_manila_0
 + z_ikt_4_fake_manila_1 + z_ikt_4_fake_manila_10 + z_ikt_4_fake_manila_11
 + z_ikt_4_fake_manila_12 + z_ikt_4_fake_manila_13 + z_ikt_4_fake_manila_14
 + z_ikt_4_fake_manila_15 + z_ikt_4_fake_manila_16 + z_ikt_4_fake_manila_17
 + z_ikt_4_fake_manila_18 + z_ikt_4_fake_manila_19 + z_ikt_4_fake_manila_2
 + z_ikt_4_fake_manila_20 + z_ikt_4_fake_manila_21 + z_ikt_4_fake_manila_22
 + z_ikt_4_fake_manila_23 + z_ikt_4_fake_manila_24 + z_ikt_4_fake_manila_25
 + z_ikt_4_fake_manila_26 + z_ikt_4_fake_manila_27 + z_ikt_4_fake_manila_28
 + z_ikt_4_fake_manila_29 + z_ikt_4_fake_manila_3 + z_ikt_4_fake_manila_30
 + z_ikt_4_fake_manila_31 + z_ikt_4_fake_manila_4 + z_ikt_4_fake_manila_5
 + z_ikt_4_fake_manila_6 + z_ikt_4_fake_manila_7 + z_ikt_4_fake_manila_8
 + z_ikt_4_fake_manila_9 <= 0
_C31: - c_j_1 + 8 z_ikt_1_fake_belem_8 + 8 z_ikt_1_fake_manila_8 <= 0
_C310: - c_j_4 <= 0
_C311: z_ikt_4_fake_belem_0 + z_ikt_4_fake_manila_0 <= 1
_C312: s_j_4 + 1000000 z_ikt_4_fake_belem_0 + 1000000 z_ikt_4_fake_manila_0
 <= 1000000
_C313: - c_j_4 + z_ikt_4_fake_belem_1 + z_ikt_4_fake_manila_1 <= 0
_C314: z_ikt_4_fake_belem_1 + z_ikt_4_fake_manila_1 <= 1
_C315: s_j_4 + 999999 z_ikt_4_fake_belem_1 + 999999 z_ikt_4_fake_manila_1
 <= 1000000
_C316: - c_j_4 + 2 z_ikt_4_fake_belem_2 + 2 z_ikt_4_fake_manila_2 <= 0
_C317: z_ikt_4_fake_belem_2 + z_ikt_4_fake_manila_2 <= 1
_C318: s_j_4 + 999998 z_ikt_4_fake_belem_2 + 999998 z_ikt_4_fake_manila_2
 <= 1000000
_C319: - c_j_4 + 3 z_ikt_4_fake_belem_3 + 3 z_ikt_4_fake_manila_3 <= 0
_C32: z_ikt_1_fake_belem_8 + z_ikt_1_fake_manila_8 <= 1
_C320: z_ikt_4_fake_belem_3 + z_ikt_4_fake_manila_3 <= 1
_C321: s_j_4 + 999997 z_ikt_4_fake_belem_3 + 999997 z_ikt_4_fake_manila_3
 <= 1000000
_C322: - c_j_4 + 4 z_ikt_4_fake_belem_4 + 4 z_ikt_4_fake_manila_4 <= 0
_C323: z_ikt_4_fake_belem_4 + z_ikt_4_fake_manila_4 <= 1
_C324: s_j_4 + 999996 z_ikt_4_fake_belem_4 + 999996 z_ikt_4_fake_manila_4
 <= 1000000
_C325: - c_j_4 + 5 z_ikt_4_fake_belem_5 + 5 z_ikt_4_fake_manila_5 <= 0
_C326: z_ikt_4_fake_belem_5 + z_ikt_4_fake_manila_5 <= 1
_C327: s_j_4 + 999995 z_ikt_4_fake_belem_5 + 999995 z_ikt_4_fake_manila_5
 <= 1000000
_C328: - c_j_4 + 6 z_ikt_4_fake_belem_6 + 6 z_ikt_4_fake_manila_6 <= 0
_C329: z_ikt_4_fake_belem_6 + z_ikt_4_fake_manila_6 <= 1
_C33: s_j_1 + 999992 z_ikt_1_fake_belem_8 + 999992 z_ikt_1_fake_manila_8
 <= 1000000
_C330: s_j_4 + 999994 z_ikt_4_fake_belem_6 + 999994 z_ikt_4_fake_manila_6
 <= 1000000
_C331: - c_j_4 + 7 z_ikt_4_fake_belem_7 + 7 z_ikt_4_fake_manila_7 <= 0
_C332: z_ikt_4_fake_belem_7 + z_ikt_4_fake_manila_7 <= 1
_C333: s_j_4 + 999993 z_ikt_4_fake_belem_7 + 999993 z_ikt_4_fake_manila_7
 <= 1000000
_C334: - c_j_4 + 8 z_ikt_4_fake_belem_8 + 8 z_ikt_4_fake_manila_8 <= 0
_C335: z_ikt_4_fake_belem_8 + z_ikt_4_fake_manila_8 <= 1
_C336: s_j_4 + 999992 z_ikt_4_fake_belem_8 + 999992 z_ikt_4_fake_manila_8
 <= 1000000
_C337: - c_j_4 + 9 z_ikt_4_fake_belem_9 + 9 z_ikt_4_fake_manila_9 <= 0
_C338: z_ikt_4_fake_belem_9 + z_ikt_4_fake_manila_9 <= 1
_C339: s_j_4 + 999991 z_ikt_4_fake_belem_9 + 999991 z_ikt_4_fake_manila_9
 <= 1000000
_C34: - c_j_1 + 9 z_ikt_1_fake_belem_9 + 9 z_ikt_1_fake_manila_9 <= 0
_C340: - c_j_4 + 10 z_ikt_4_fake_belem_10 + 10 z_ikt_4_fake_manila_10 <= 0
_C341: z_ikt_4_fake_belem_10 + z_ikt_4_fake_manila_10 <= 1
_C342: s_j_4 + 999990 z_ikt_4_fake_belem_10 + 999990 z_ikt_4_fake_manila_10
 <= 1000000
_C343: - c_j_4 + 11 z_ikt_4_fake_belem_11 + 11 z_ikt_4_fake_manila_11 <= 0
_C344: z_ikt_4_fake_belem_11 + z_ikt_4_fake_manila_11 <= 1
_C345: s_j_4 + 999989 z_ikt_4_fake_belem_11 + 999989 z_ikt_4_fake_manila_11
 <= 1000000
_C346: - c_j_4 + 12 z_ikt_4_fake_belem_12 + 12 z_ikt_4_fake_manila_12 <= 0
_C347: z_ikt_4_fake_belem_12 + z_ikt_4_fake_manila_12 <= 1
_C348: s_j_4 + 999988 z_ikt_4_fake_belem_12 + 999988 z_ikt_4_fake_manila_12
 <= 1000000
_C349: - c_j_4 + 13 z_ikt_4_fake_belem_13 + 13 z_ikt_4_fake_manila_13 <= 0
_C35: z_ikt_1_fake_belem_9 + z_ikt_1_fake_manila_9 <= 1
_C350: z_ikt_4_fake_belem_13 + z_ikt_4_fake_manila_13 <= 1
_C351: s_j_4 + 999987 z_ikt_4_fake_belem_13 + 999987 z_ikt_4_fake_manila_13
 <= 1000000
_C352: - c_j_4 + 14 z_ikt_4_fake_belem_14 + 14 z_ikt_4_fake_manila_14 <= 0
_C353: z_ikt_4_fake_belem_14 + z_ikt_4_fake_manila_14 <= 1
_C354: s_j_4 + 999986 z_ikt_4_fake_belem_14 + 999986 z_ikt_4_fake_manila_14
 <= 1000000
_C355: - c_j_4 + 15 z_ikt_4_fake_belem_15 + 15 z_ikt_4_fake_manila_15 <= 0
_C356: z_ikt_4_fake_belem_15 + z_ikt_4_fake_manila_15 <= 1
_C357: s_j_4 + 999985 z_ikt_4_fake_belem_15 + 999985 z_ikt_4_fake_manila_15
 <= 1000000
_C358: - c_j_4 + 16 z_ikt_4_fake_belem_16 + 16 z_ikt_4_fake_manila_16 <= 0
_C359: z_ikt_4_fake_belem_16 + z_ikt_4_fake_manila_16 <= 1
_C36: s_j_1 + 999991 z_ikt_1_fake_belem_9 + 999991 z_ikt_1_fake_manila_9
 <= 1000000
_C360: s_j_4 + 999984 z_ikt_4_fake_belem_16 + 999984 z_ikt_4_fake_manila_16
 <= 1000000
_C361: - c_j_4 + 17 z_ikt_4_fake_belem_17 + 17 z_ikt_4_fake_manila_17 <= 0
_C362: z_ikt_4_fake_belem_17 + z_ikt_4_fake_manila_17 <= 1
_C363: s_j_4 + 999983 z_ikt_4_fake_belem_17 + 999983 z_ikt_4_fake_manila_17
 <= 1000000
_C364: - c_j_4 + 18 z_ikt_4_fake_belem_18 + 18 z_ikt_4_fake_manila_18 <= 0
_C365: z_ikt_4_fake_belem_18 + z_ikt_4_fake_manila_18 <= 1
_C366: s_j_4 + 999982 z_ikt_4_fake_belem_18 + 999982 z_ikt_4_fake_manila_18
 <= 1000000
_C367: - c_j_4 + 19 z_ikt_4_fake_belem_19 + 19 z_ikt_4_fake_manila_19 <= 0
_C368: z_ikt_4_fake_belem_19 + z_ikt_4_fake_manila_19 <= 1
_C369: s_j_4 + 999981 z_ikt_4_fake_belem_19 + 999981 z_ikt_4_fake_manila_19
 <= 1000000
_C37: - c_j_1 + 10 z_ikt_1_fake_belem_10 + 10 z_ikt_1_fake_manila_10 <= 0
_C370: - c_j_4 + 20 z_ikt_4_fake_belem_20 + 20 z_ikt_4_fake_manila_20 <= 0
_C371: z_ikt_4_fake_belem_20 + z_ikt_4_fake_manila_20 <= 1
_C372: s_j_4 + 999980 z_ikt_4_fake_belem_20 + 999980 z_ikt_4_fake_manila_20
 <= 1000000
_C373: - c_j_4 + 21 z_ikt_4_fake_belem_21 + 21 z_ikt_4_fake_manila_21 <= 0
_C374: z_ikt_4_fake_belem_21 + z_ikt_4_fake_manila_21 <= 1
_C375: s_j_4 + 999979 z_ikt_4_fake_belem_21 + 999979 z_ikt_4_fake_manila_21
 <= 1000000
_C376: - c_j_4 + 22 z_ikt_4_fake_belem_22 + 22 z_ikt_4_fake_manila_22 <= 0
_C377: z_ikt_4_fake_belem_22 + z_ikt_4_fake_manila_22 <= 1
_C378: s_j_4 + 999978 z_ikt_4_fake_belem_22 + 999978 z_ikt_4_fake_manila_22
 <= 1000000
_C379: - c_j_4 + 23 z_ikt_4_fake_belem_23 + 23 z_ikt_4_fake_manila_23 <= 0
_C38: z_ikt_1_fake_belem_10 + z_ikt_1_fake_manila_10 <= 1
_C380: z_ikt_4_fake_belem_23 + z_ikt_4_fake_manila_23 <= 1
_C381: s_j_4 + 999977 z_ikt_4_fake_belem_23 + 999977 z_ikt_4_fake_manila_23
 <= 1000000
_C382: - c_j_4 + 24 z_ikt_4_fake_belem_24 + 24 z_ikt_4_fake_manila_24 <= 0
_C383: z_ikt_4_fake_belem_24 + z_ikt_4_fake_manila_24 <= 1
_C384: s_j_4 + 999976 z_ikt_4_fake_belem_24 + 999976 z_ikt_4_fake_manila_24
 <= 1000000
_C385: - c_j_4 + 25 z_ikt_4_fake_belem_25 + 25 z_ikt_4_fake_manila_25 <= 0
_C386: z_ikt_4_fake_belem_25 + z_ikt_4_fake_manila_25 <= 1
_C387: s_j_4 + 999975 z_ikt_4_fake_belem_25 + 999975 z_ikt_4_fake_manila_25
 <= 1000000
_C388: - c_j_4 + 26 z_ikt_4_fake_belem_26 + 26 z_ikt_4_fake_manila_26 <= 0
_C389: z_ikt_4_fake_belem_26 + z_ikt_4_fake_manila_26 <= 1
_C39: s_j_1 + 999990 z_ikt_1_fake_belem_10 + 999990 z_ikt_1_fake_manila_10
 <= 1000000
_C390: s_j_4 + 999974 z_ikt_4_fake_belem_26 + 999974 z_ikt_4_fake_manila_26
 <= 1000000
_C391: - c_j_4 + 27 z_ikt_4_fake_belem_27 + 27 z_ikt_4_fake_manila_27 <= 0
_C392: z_ikt_4_fake_belem_27 + z_ikt_4_fake_manila_27 <= 1
_C393: s_j_4 + 999973 z_ikt_4_fake_belem_27 + 999973 z_ikt_4_fake_manila_27
 <= 1000000
_C394: - c_j_4 + 28 z_ikt_4_fake_belem_28 + 28 z_ikt_4_fake_manila_28 <= 0
_C395: z_ikt_4_fake_belem_28 + z_ikt_4_fake_manila_28 <= 1
_C396: s_j_4 + 999972 z_ikt_4_fake_belem_28 + 999972 z_ikt_4_fake_manila_28
 <= 1000000
_C397: - c_j_4 + 29 z_ikt_4_fake_belem_29 + 29 z_ikt_4_fake_manila_29 <= 0
_C398: z_ikt_4_fake_belem_29 + z_ikt_4_fake_manila_29 <= 1
_C399: s_j_4 + 999971 z_ikt_4_fake_belem_29 + 999971 z_ikt_4_fake_manila_29
 <= 1000000
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
_C400: - c_j_4 + 30 z_ikt_4_fake_belem_30 + 30 z_ikt_4_fake_manila_30 <= 0
_C401: z_ikt_4_fake_belem_30 + z_ikt_4_fake_manila_30 <= 1
_C402: s_j_4 + 999970 z_ikt_4_fake_belem_30 + 999970 z_ikt_4_fake_manila_30
 <= 1000000
_C403: - c_j_4 + 31 z_ikt_4_fake_belem_31 + 31 z_ikt_4_fake_manila_31 <= 0
_C404: z_ikt_4_fake_belem_31 + z_ikt_4_fake_manila_31 <= 1
_C405: s_j_4 + 999969 z_ikt_4_fake_belem_31 + 999969 z_ikt_4_fake_manila_31
 <= 1000000
_C406: c_j_5 - makespan <= 0
_C407: x_ik_5_fake_belem + x_ik_5_fake_manila = 1
_C408: c_j_5 - s_j_5 - z_ikt_5_fake_belem_0 - z_ikt_5_fake_belem_1
 - z_ikt_5_fake_belem_10 - z_ikt_5_fake_belem_11 - z_ikt_5_fake_belem_12
 - z_ikt_5_fake_belem_13 - z_ikt_5_fake_belem_14 - z_ikt_5_fake_belem_15
 - z_ikt_5_fake_belem_16 - z_ikt_5_fake_belem_17 - z_ikt_5_fake_belem_18
 - z_ikt_5_fake_belem_19 - z_ikt_5_fake_belem_2 - z_ikt_5_fake_belem_20
 - z_ikt_5_fake_belem_21 - z_ikt_5_fake_belem_22 - z_ikt_5_fake_belem_23
 - z_ikt_5_fake_belem_24 - z_ikt_5_fake_belem_25 - z_ikt_5_fake_belem_26
 - z_ikt_5_fake_belem_27 - z_ikt_5_fake_belem_28 - z_ikt_5_fake_belem_29
 - z_ikt_5_fake_belem_3 - z_ikt_5_fake_belem_30 - z_ikt_5_fake_belem_31
 - z_ikt_5_fake_belem_4 - z_ikt_5_fake_belem_5 - z_ikt_5_fake_belem_6
 - z_ikt_5_fake_belem_7 - z_ikt_5_fake_belem_8 - z_ikt_5_fake_belem_9
 - z_ikt_5_fake_manila_0 - z_ikt_5_fake_manila_1 - z_ikt_5_fake_manila_10
 - z_ikt_5_fake_manila_11 - z_ikt_5_fake_manila_12 - z_ikt_5_fake_manila_13
 - z_ikt_5_fake_manila_14 - z_ikt_5_fake_manila_15 - z_ikt_5_fake_manila_16
 - z_ikt_5_fake_manila_17 - z_ikt_5_fake_manila_18 - z_ikt_5_fake_manila_19
 - z_ikt_5_fake_manila_2 - z_ikt_5_fake_manila_20 - z_ikt_5_fake_manila_21
 - z_ikt_5_fake_manila_22 - z_ikt_5_fake_manila_23 - z_ikt_5_fake_manila_24
 - z_ikt_5_fake_manila_25 - z_ikt_5_fake_manila_26 - z_ikt_5_fake_manila_27
 - z_ikt_5_fake_manila_28 - z_ikt_5_fake_manila_29 - z_ikt_5_fake_manila_3
 - z_ikt_5_fake_manila_30 - z_ikt_5_fake_manila_31 - z_ikt_5_fake_manila_4
 - z_ikt_5_fake_manila_5 - z_ikt_5_fake_manila_6 - z_ikt_5_fake_manila_7
 - z_ikt_5_fake_manila_8 - z_ikt_5_fake_manila_9 = -1
_C409: - 1000000 x_ik_5_fake_belem + z_ikt_5_fake_belem_0
 + z_ikt_5_fake_belem_1 + z_ikt_5_fake_belem_10 + z_ikt_5_fake_belem_11
 + z_ikt_5_fake_belem_12 + z_ikt_5_fake_belem_13 + z_ikt_5_fake_belem_14
 + z_ikt_5_fake_belem_15 + z_ikt_5_fake_belem_16 + z_ikt_5_fake_belem_17
 + z_ikt_5_fake_belem_18 + z_ikt_5_fake_belem_19 + z_ikt_5_fake_belem_2
 + z_ikt_5_fake_belem_20 + z_ikt_5_fake_belem_21 + z_ikt_5_fake_belem_22
 + z_ikt_5_fake_belem_23 + z_ikt_5_fake_belem_24 + z_ikt_5_fake_belem_25
 + z_ikt_5_fake_belem_26 + z_ikt_5_fake_belem_27 + z_ikt_5_fake_belem_28
 + z_ikt_5_fake_belem_29 + z_ikt_5_fake_belem_3 + z_ikt_5_fake_belem_30
 + z_ikt_5_fake_belem_31 + z_ikt_5_fake_belem_4 + z_ikt_5_fake_belem_5
 + z_ikt_5_fake_belem_6 + z_ikt_5_fake_belem_7 + z_ikt_5_fake_belem_8
 + z_ikt_5_fake_belem_9 <= 0
_C41: z_ikt_1_fake_belem_11 + z_ikt_1_fake_manila_11 <= 1
_C410: - 1000000 x_ik_5_fake_manila + z_ikt_5_fake_manila_0
 + z_ikt_5_fake_manila_1 + z_ikt_5_fake_manila_10 + z_ikt_5_fake_manila_11
 + z_ikt_5_fake_manila_12 + z_ikt_5_fake_manila_13 + z_ikt_5_fake_manila_14
 + z_ikt_5_fake_manila_15 + z_ikt_5_fake_manila_16 + z_ikt_5_fake_manila_17
 + z_ikt_5_fake_manila_18 + z_ikt_5_fake_manila_19 + z_ikt_5_fake_manila_2
 + z_ikt_5_fake_manila_20 + z_ikt_5_fake_manila_21 + z_ikt_5_fake_manila_22
 + z_ikt_5_fake_manila_23 + z_ikt_5_fake_manila_24 + z_ikt_5_fake_manila_25
 + z_ikt_5_fake_manila_26 + z_ikt_5_fake_manila_27 + z_ikt_5_fake_manila_28
 + z_ikt_5_fake_manila_29 + z_ikt_5_fake_manila_3 + z_ikt_5_fake_manila_30
 + z_ikt_5_fake_manila_31 + z_ikt_5_fake_manila_4 + z_ikt_5_fake_manila_5
 + z_ikt_5_fake_manila_6 + z_ikt_5_fake_manila_7 + z_ikt_5_fake_manila_8
 + z_ikt_5_fake_manila_9 <= 0
_C411: - c_j_5 <= 0
_C412: z_ikt_5_fake_belem_0 + z_ikt_5_fake_manila_0 <= 1
_C413: s_j_5 + 1000000 z_ikt_5_fake_belem_0 + 1000000 z_ikt_5_fake_manila_0
 <= 1000000
_C414: - c_j_5 + z_ikt_5_fake_belem_1 + z_ikt_5_fake_manila_1 <= 0
_C415: z_ikt_5_fake_belem_1 + z_ikt_5_fake_manila_1 <= 1
_C416: s_j_5 + 999999 z_ikt_5_fake_belem_1 + 999999 z_ikt_5_fake_manila_1
 <= 1000000
_C417: - c_j_5 + 2 z_ikt_5_fake_belem_2 + 2 z_ikt_5_fake_manila_2 <= 0
_C418: z_ikt_5_fake_belem_2 + z_ikt_5_fake_manila_2 <= 1
_C419: s_j_5 + 999998 z_ikt_5_fake_belem_2 + 999998 z_ikt_5_fake_manila_2
 <= 1000000
_C42: s_j_1 + 999989 z_ikt_1_fake_belem_11 + 999989 z_ikt_1_fake_manila_11
 <= 1000000
_C420: - c_j_5 + 3 z_ikt_5_fake_belem_3 + 3 z_ikt_5_fake_manila_3 <= 0
_C421: z_ikt_5_fake_belem_3 + z_ikt_5_fake_manila_3 <= 1
_C422: s_j_5 + 999997 z_ikt_5_fake_belem_3 + 999997 z_ikt_5_fake_manila_3
 <= 1000000
_C423: - c_j_5 + 4 z_ikt_5_fake_belem_4 + 4 z_ikt_5_fake_manila_4 <= 0
_C424: z_ikt_5_fake_belem_4 + z_ikt_5_fake_manila_4 <= 1
_C425: s_j_5 + 999996 z_ikt_5_fake_belem_4 + 999996 z_ikt_5_fake_manila_4
 <= 1000000
_C426: - c_j_5 + 5 z_ikt_5_fake_belem_5 + 5 z_ikt_5_fake_manila_5 <= 0
_C427: z_ikt_5_fake_belem_5 + z_ikt_5_fake_manila_5 <= 1
_C428: s_j_5 + 999995 z_ikt_5_fake_belem_5 + 999995 z_ikt_5_fake_manila_5
 <= 1000000
_C429: - c_j_5 + 6 z_ikt_5_fake_belem_6 + 6 z_ikt_5_fake_manila_6 <= 0
_C43: - c_j_1 + 12 z_ikt_1_fake_belem_12 + 12 z_ikt_1_fake_manila_12 <= 0
_C430: z_ikt_5_fake_belem_6 + z_ikt_5_fake_manila_6 <= 1
_C431: s_j_5 + 999994 z_ikt_5_fake_belem_6 + 999994 z_ikt_5_fake_manila_6
 <= 1000000
_C432: - c_j_5 + 7 z_ikt_5_fake_belem_7 + 7 z_ikt_5_fake_manila_7 <= 0
_C433: z_ikt_5_fake_belem_7 + z_ikt_5_fake_manila_7 <= 1
_C434: s_j_5 + 999993 z_ikt_5_fake_belem_7 + 999993 z_ikt_5_fake_manila_7
 <= 1000000
_C435: - c_j_5 + 8 z_ikt_5_fake_belem_8 + 8 z_ikt_5_fake_manila_8 <= 0
_C436: z_ikt_5_fake_belem_8 + z_ikt_5_fake_manila_8 <= 1
_C437: s_j_5 + 999992 z_ikt_5_fake_belem_8 + 999992 z_ikt_5_fake_manila_8
 <= 1000000
_C438: - c_j_5 + 9 z_ikt_5_fake_belem_9 + 9 z_ikt_5_fake_manila_9 <= 0
_C439: z_ikt_5_fake_belem_9 + z_ikt_5_fake_manila_9 <= 1
_C44: z_ikt_1_fake_belem_12 + z_ikt_1_fake_manila_12 <= 1
_C440: s_j_5 + 999991 z_ikt_5_fake_belem_9 + 999991 z_ikt_5_fake_manila_9
 <= 1000000
_C441: - c_j_5 + 10 z_ikt_5_fake_belem_10 + 10 z_ikt_5_fake_manila_10 <= 0
_C442: z_ikt_5_fake_belem_10 + z_ikt_5_fake_manila_10 <= 1
_C443: s_j_5 + 999990 z_ikt_5_fake_belem_10 + 999990 z_ikt_5_fake_manila_10
 <= 1000000
_C444: - c_j_5 + 11 z_ikt_5_fake_belem_11 + 11 z_ikt_5_fake_manila_11 <= 0
_C445: z_ikt_5_fake_belem_11 + z_ikt_5_fake_manila_11 <= 1
_C446: s_j_5 + 999989 z_ikt_5_fake_belem_11 + 999989 z_ikt_5_fake_manila_11
 <= 1000000
_C447: - c_j_5 + 12 z_ikt_5_fake_belem_12 + 12 z_ikt_5_fake_manila_12 <= 0
_C448: z_ikt_5_fake_belem_12 + z_ikt_5_fake_manila_12 <= 1
_C449: s_j_5 + 999988 z_ikt_5_fake_belem_12 + 999988 z_ikt_5_fake_manila_12
 <= 1000000
_C45: s_j_1 + 999988 z_ikt_1_fake_belem_12 + 999988 z_ikt_1_fake_manila_12
 <= 1000000
_C450: - c_j_5 + 13 z_ikt_5_fake_belem_13 + 13 z_ikt_5_fake_manila_13 <= 0
_C451: z_ikt_5_fake_belem_13 + z_ikt_5_fake_manila_13 <= 1
_C452: s_j_5 + 999987 z_ikt_5_fake_belem_13 + 999987 z_ikt_5_fake_manila_13
 <= 1000000
_C453: - c_j_5 + 14 z_ikt_5_fake_belem_14 + 14 z_ikt_5_fake_manila_14 <= 0
_C454: z_ikt_5_fake_belem_14 + z_ikt_5_fake_manila_14 <= 1
_C455: s_j_5 + 999986 z_ikt_5_fake_belem_14 + 999986 z_ikt_5_fake_manila_14
 <= 1000000
_C456: - c_j_5 + 15 z_ikt_5_fake_belem_15 + 15 z_ikt_5_fake_manila_15 <= 0
_C457: z_ikt_5_fake_belem_15 + z_ikt_5_fake_manila_15 <= 1
_C458: s_j_5 + 999985 z_ikt_5_fake_belem_15 + 999985 z_ikt_5_fake_manila_15
 <= 1000000
_C459: - c_j_5 + 16 z_ikt_5_fake_belem_16 + 16 z_ikt_5_fake_manila_16 <= 0
_C46: - c_j_1 + 13 z_ikt_1_fake_belem_13 + 13 z_ikt_1_fake_manila_13 <= 0
_C460: z_ikt_5_fake_belem_16 + z_ikt_5_fake_manila_16 <= 1
_C461: s_j_5 + 999984 z_ikt_5_fake_belem_16 + 999984 z_ikt_5_fake_manila_16
 <= 1000000
_C462: - c_j_5 + 17 z_ikt_5_fake_belem_17 + 17 z_ikt_5_fake_manila_17 <= 0
_C463: z_ikt_5_fake_belem_17 + z_ikt_5_fake_manila_17 <= 1
_C464: s_j_5 + 999983 z_ikt_5_fake_belem_17 + 999983 z_ikt_5_fake_manila_17
 <= 1000000
_C465: - c_j_5 + 18 z_ikt_5_fake_belem_18 + 18 z_ikt_5_fake_manila_18 <= 0
_C466: z_ikt_5_fake_belem_18 + z_ikt_5_fake_manila_18 <= 1
_C467: s_j_5 + 999982 z_ikt_5_fake_belem_18 + 999982 z_ikt_5_fake_manila_18
 <= 1000000
_C468: - c_j_5 + 19 z_ikt_5_fake_belem_19 + 19 z_ikt_5_fake_manila_19 <= 0
_C469: z_ikt_5_fake_belem_19 + z_ikt_5_fake_manila_19 <= 1
_C47: z_ikt_1_fake_belem_13 + z_ikt_1_fake_manila_13 <= 1
_C470: s_j_5 + 999981 z_ikt_5_fake_belem_19 + 999981 z_ikt_5_fake_manila_19
 <= 1000000
_C471: - c_j_5 + 20 z_ikt_5_fake_belem_20 + 20 z_ikt_5_fake_manila_20 <= 0
_C472: z_ikt_5_fake_belem_20 + z_ikt_5_fake_manila_20 <= 1
_C473: s_j_5 + 999980 z_ikt_5_fake_belem_20 + 999980 z_ikt_5_fake_manila_20
 <= 1000000
_C474: - c_j_5 + 21 z_ikt_5_fake_belem_21 + 21 z_ikt_5_fake_manila_21 <= 0
_C475: z_ikt_5_fake_belem_21 + z_ikt_5_fake_manila_21 <= 1
_C476: s_j_5 + 999979 z_ikt_5_fake_belem_21 + 999979 z_ikt_5_fake_manila_21
 <= 1000000
_C477: - c_j_5 + 22 z_ikt_5_fake_belem_22 + 22 z_ikt_5_fake_manila_22 <= 0
_C478: z_ikt_5_fake_belem_22 + z_ikt_5_fake_manila_22 <= 1
_C479: s_j_5 + 999978 z_ikt_5_fake_belem_22 + 999978 z_ikt_5_fake_manila_22
 <= 1000000
_C48: s_j_1 + 999987 z_ikt_1_fake_belem_13 + 999987 z_ikt_1_fake_manila_13
 <= 1000000
_C480: - c_j_5 + 23 z_ikt_5_fake_belem_23 + 23 z_ikt_5_fake_manila_23 <= 0
_C481: z_ikt_5_fake_belem_23 + z_ikt_5_fake_manila_23 <= 1
_C482: s_j_5 + 999977 z_ikt_5_fake_belem_23 + 999977 z_ikt_5_fake_manila_23
 <= 1000000
_C483: - c_j_5 + 24 z_ikt_5_fake_belem_24 + 24 z_ikt_5_fake_manila_24 <= 0
_C484: z_ikt_5_fake_belem_24 + z_ikt_5_fake_manila_24 <= 1
_C485: s_j_5 + 999976 z_ikt_5_fake_belem_24 + 999976 z_ikt_5_fake_manila_24
 <= 1000000
_C486: - c_j_5 + 25 z_ikt_5_fake_belem_25 + 25 z_ikt_5_fake_manila_25 <= 0
_C487: z_ikt_5_fake_belem_25 + z_ikt_5_fake_manila_25 <= 1
_C488: s_j_5 + 999975 z_ikt_5_fake_belem_25 + 999975 z_ikt_5_fake_manila_25
 <= 1000000
_C489: - c_j_5 + 26 z_ikt_5_fake_belem_26 + 26 z_ikt_5_fake_manila_26 <= 0
_C49: - c_j_1 + 14 z_ikt_1_fake_belem_14 + 14 z_ikt_1_fake_manila_14 <= 0
_C490: z_ikt_5_fake_belem_26 + z_ikt_5_fake_manila_26 <= 1
_C491: s_j_5 + 999974 z_ikt_5_fake_belem_26 + 999974 z_ikt_5_fake_manila_26
 <= 1000000
_C492: - c_j_5 + 27 z_ikt_5_fake_belem_27 + 27 z_ikt_5_fake_manila_27 <= 0
_C493: z_ikt_5_fake_belem_27 + z_ikt_5_fake_manila_27 <= 1
_C494: s_j_5 + 999973 z_ikt_5_fake_belem_27 + 999973 z_ikt_5_fake_manila_27
 <= 1000000
_C495: - c_j_5 + 28 z_ikt_5_fake_belem_28 + 28 z_ikt_5_fake_manila_28 <= 0
_C496: z_ikt_5_fake_belem_28 + z_ikt_5_fake_manila_28 <= 1
_C497: s_j_5 + 999972 z_ikt_5_fake_belem_28 + 999972 z_ikt_5_fake_manila_28
 <= 1000000
_C498: - c_j_5 + 29 z_ikt_5_fake_belem_29 + 29 z_ikt_5_fake_manila_29 <= 0
_C499: z_ikt_5_fake_belem_29 + z_ikt_5_fake_manila_29 <= 1
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
_C500: s_j_5 + 999971 z_ikt_5_fake_belem_29 + 999971 z_ikt_5_fake_manila_29
 <= 1000000
_C501: - c_j_5 + 30 z_ikt_5_fake_belem_30 + 30 z_ikt_5_fake_manila_30 <= 0
_C502: z_ikt_5_fake_belem_30 + z_ikt_5_fake_manila_30 <= 1
_C503: s_j_5 + 999970 z_ikt_5_fake_belem_30 + 999970 z_ikt_5_fake_manila_30
 <= 1000000
_C504: - c_j_5 + 31 z_ikt_5_fake_belem_31 + 31 z_ikt_5_fake_manila_31 <= 0
_C505: z_ikt_5_fake_belem_31 + z_ikt_5_fake_manila_31 <= 1
_C506: s_j_5 + 999969 z_ikt_5_fake_belem_31 + 999969 z_ikt_5_fake_manila_31
 <= 1000000
_C507: c_j_6 - makespan <= 0
_C508: x_ik_6_fake_belem + x_ik_6_fake_manila = 1
_C509: c_j_6 - s_j_6 - z_ikt_6_fake_belem_0 - z_ikt_6_fake_belem_1
 - z_ikt_6_fake_belem_10 - z_ikt_6_fake_belem_11 - z_ikt_6_fake_belem_12
 - z_ikt_6_fake_belem_13 - z_ikt_6_fake_belem_14 - z_ikt_6_fake_belem_15
 - z_ikt_6_fake_belem_16 - z_ikt_6_fake_belem_17 - z_ikt_6_fake_belem_18
 - z_ikt_6_fake_belem_19 - z_ikt_6_fake_belem_2 - z_ikt_6_fake_belem_20
 - z_ikt_6_fake_belem_21 - z_ikt_6_fake_belem_22 - z_ikt_6_fake_belem_23
 - z_ikt_6_fake_belem_24 - z_ikt_6_fake_belem_25 - z_ikt_6_fake_belem_26
 - z_ikt_6_fake_belem_27 - z_ikt_6_fake_belem_28 - z_ikt_6_fake_belem_29
 - z_ikt_6_fake_belem_3 - z_ikt_6_fake_belem_30 - z_ikt_6_fake_belem_31
 - z_ikt_6_fake_belem_4 - z_ikt_6_fake_belem_5 - z_ikt_6_fake_belem_6
 - z_ikt_6_fake_belem_7 - z_ikt_6_fake_belem_8 - z_ikt_6_fake_belem_9
 - z_ikt_6_fake_manila_0 - z_ikt_6_fake_manila_1 - z_ikt_6_fake_manila_10
 - z_ikt_6_fake_manila_11 - z_ikt_6_fake_manila_12 - z_ikt_6_fake_manila_13
 - z_ikt_6_fake_manila_14 - z_ikt_6_fake_manila_15 - z_ikt_6_fake_manila_16
 - z_ikt_6_fake_manila_17 - z_ikt_6_fake_manila_18 - z_ikt_6_fake_manila_19
 - z_ikt_6_fake_manila_2 - z_ikt_6_fake_manila_20 - z_ikt_6_fake_manila_21
 - z_ikt_6_fake_manila_22 - z_ikt_6_fake_manila_23 - z_ikt_6_fake_manila_24
 - z_ikt_6_fake_manila_25 - z_ikt_6_fake_manila_26 - z_ikt_6_fake_manila_27
 - z_ikt_6_fake_manila_28 - z_ikt_6_fake_manila_29 - z_ikt_6_fake_manila_3
 - z_ikt_6_fake_manila_30 - z_ikt_6_fake_manila_31 - z_ikt_6_fake_manila_4
 - z_ikt_6_fake_manila_5 - z_ikt_6_fake_manila_6 - z_ikt_6_fake_manila_7
 - z_ikt_6_fake_manila_8 - z_ikt_6_fake_manila_9 = -1
_C51: s_j_1 + 999986 z_ikt_1_fake_belem_14 + 999986 z_ikt_1_fake_manila_14
 <= 1000000
_C510: - 1000000 x_ik_6_fake_belem + z_ikt_6_fake_belem_0
 + z_ikt_6_fake_belem_1 + z_ikt_6_fake_belem_10 + z_ikt_6_fake_belem_11
 + z_ikt_6_fake_belem_12 + z_ikt_6_fake_belem_13 + z_ikt_6_fake_belem_14
 + z_ikt_6_fake_belem_15 + z_ikt_6_fake_belem_16 + z_ikt_6_fake_belem_17
 + z_ikt_6_fake_belem_18 + z_ikt_6_fake_belem_19 + z_ikt_6_fake_belem_2
 + z_ikt_6_fake_belem_20 + z_ikt_6_fake_belem_21 + z_ikt_6_fake_belem_22
 + z_ikt_6_fake_belem_23 + z_ikt_6_fake_belem_24 + z_ikt_6_fake_belem_25
 + z_ikt_6_fake_belem_26 + z_ikt_6_fake_belem_27 + z_ikt_6_fake_belem_28
 + z_ikt_6_fake_belem_29 + z_ikt_6_fake_belem_3 + z_ikt_6_fake_belem_30
 + z_ikt_6_fake_belem_31 + z_ikt_6_fake_belem_4 + z_ikt_6_fake_belem_5
 + z_ikt_6_fake_belem_6 + z_ikt_6_fake_belem_7 + z_ikt_6_fake_belem_8
 + z_ikt_6_fake_belem_9 <= 0
_C511: - 1000000 x_ik_6_fake_manila + z_ikt_6_fake_manila_0
 + z_ikt_6_fake_manila_1 + z_ikt_6_fake_manila_10 + z_ikt_6_fake_manila_11
 + z_ikt_6_fake_manila_12 + z_ikt_6_fake_manila_13 + z_ikt_6_fake_manila_14
 + z_ikt_6_fake_manila_15 + z_ikt_6_fake_manila_16 + z_ikt_6_fake_manila_17
 + z_ikt_6_fake_manila_18 + z_ikt_6_fake_manila_19 + z_ikt_6_fake_manila_2
 + z_ikt_6_fake_manila_20 + z_ikt_6_fake_manila_21 + z_ikt_6_fake_manila_22
 + z_ikt_6_fake_manila_23 + z_ikt_6_fake_manila_24 + z_ikt_6_fake_manila_25
 + z_ikt_6_fake_manila_26 + z_ikt_6_fake_manila_27 + z_ikt_6_fake_manila_28
 + z_ikt_6_fake_manila_29 + z_ikt_6_fake_manila_3 + z_ikt_6_fake_manila_30
 + z_ikt_6_fake_manila_31 + z_ikt_6_fake_manila_4 + z_ikt_6_fake_manila_5
 + z_ikt_6_fake_manila_6 + z_ikt_6_fake_manila_7 + z_ikt_6_fake_manila_8
 + z_ikt_6_fake_manila_9 <= 0
_C512: - c_j_6 <= 0
_C513: z_ikt_6_fake_belem_0 + z_ikt_6_fake_manila_0 <= 1
_C514: s_j_6 + 1000000 z_ikt_6_fake_belem_0 + 1000000 z_ikt_6_fake_manila_0
 <= 1000000
_C515: - c_j_6 + z_ikt_6_fake_belem_1 + z_ikt_6_fake_manila_1 <= 0
_C516: z_ikt_6_fake_belem_1 + z_ikt_6_fake_manila_1 <= 1
_C517: s_j_6 + 999999 z_ikt_6_fake_belem_1 + 999999 z_ikt_6_fake_manila_1
 <= 1000000
_C518: - c_j_6 + 2 z_ikt_6_fake_belem_2 + 2 z_ikt_6_fake_manila_2 <= 0
_C519: z_ikt_6_fake_belem_2 + z_ikt_6_fake_manila_2 <= 1
_C52: - c_j_1 + 15 z_ikt_1_fake_belem_15 + 15 z_ikt_1_fake_manila_15 <= 0
_C520: s_j_6 + 999998 z_ikt_6_fake_belem_2 + 999998 z_ikt_6_fake_manila_2
 <= 1000000
_C521: - c_j_6 + 3 z_ikt_6_fake_belem_3 + 3 z_ikt_6_fake_manila_3 <= 0
_C522: z_ikt_6_fake_belem_3 + z_ikt_6_fake_manila_3 <= 1
_C523: s_j_6 + 999997 z_ikt_6_fake_belem_3 + 999997 z_ikt_6_fake_manila_3
 <= 1000000
_C524: - c_j_6 + 4 z_ikt_6_fake_belem_4 + 4 z_ikt_6_fake_manila_4 <= 0
_C525: z_ikt_6_fake_belem_4 + z_ikt_6_fake_manila_4 <= 1
_C526: s_j_6 + 999996 z_ikt_6_fake_belem_4 + 999996 z_ikt_6_fake_manila_4
 <= 1000000
_C527: - c_j_6 + 5 z_ikt_6_fake_belem_5 + 5 z_ikt_6_fake_manila_5 <= 0
_C528: z_ikt_6_fake_belem_5 + z_ikt_6_fake_manila_5 <= 1
_C529: s_j_6 + 999995 z_ikt_6_fake_belem_5 + 999995 z_ikt_6_fake_manila_5
 <= 1000000
_C53: z_ikt_1_fake_belem_15 + z_ikt_1_fake_manila_15 <= 1
_C530: - c_j_6 + 6 z_ikt_6_fake_belem_6 + 6 z_ikt_6_fake_manila_6 <= 0
_C531: z_ikt_6_fake_belem_6 + z_ikt_6_fake_manila_6 <= 1
_C532: s_j_6 + 999994 z_ikt_6_fake_belem_6 + 999994 z_ikt_6_fake_manila_6
 <= 1000000
_C533: - c_j_6 + 7 z_ikt_6_fake_belem_7 + 7 z_ikt_6_fake_manila_7 <= 0
_C534: z_ikt_6_fake_belem_7 + z_ikt_6_fake_manila_7 <= 1
_C535: s_j_6 + 999993 z_ikt_6_fake_belem_7 + 999993 z_ikt_6_fake_manila_7
 <= 1000000
_C536: - c_j_6 + 8 z_ikt_6_fake_belem_8 + 8 z_ikt_6_fake_manila_8 <= 0
_C537: z_ikt_6_fake_belem_8 + z_ikt_6_fake_manila_8 <= 1
_C538: s_j_6 + 999992 z_ikt_6_fake_belem_8 + 999992 z_ikt_6_fake_manila_8
 <= 1000000
_C539: - c_j_6 + 9 z_ikt_6_fake_belem_9 + 9 z_ikt_6_fake_manila_9 <= 0
_C54: s_j_1 + 999985 z_ikt_1_fake_belem_15 + 999985 z_ikt_1_fake_manila_15
 <= 1000000
_C540: z_ikt_6_fake_belem_9 + z_ikt_6_fake_manila_9 <= 1
_C541: s_j_6 + 999991 z_ikt_6_fake_belem_9 + 999991 z_ikt_6_fake_manila_9
 <= 1000000
_C542: - c_j_6 + 10 z_ikt_6_fake_belem_10 + 10 z_ikt_6_fake_manila_10 <= 0
_C543: z_ikt_6_fake_belem_10 + z_ikt_6_fake_manila_10 <= 1
_C544: s_j_6 + 999990 z_ikt_6_fake_belem_10 + 999990 z_ikt_6_fake_manila_10
 <= 1000000
_C545: - c_j_6 + 11 z_ikt_6_fake_belem_11 + 11 z_ikt_6_fake_manila_11 <= 0
_C546: z_ikt_6_fake_belem_11 + z_ikt_6_fake_manila_11 <= 1
_C547: s_j_6 + 999989 z_ikt_6_fake_belem_11 + 999989 z_ikt_6_fake_manila_11
 <= 1000000
_C548: - c_j_6 + 12 z_ikt_6_fake_belem_12 + 12 z_ikt_6_fake_manila_12 <= 0
_C549: z_ikt_6_fake_belem_12 + z_ikt_6_fake_manila_12 <= 1
_C55: - c_j_1 + 16 z_ikt_1_fake_belem_16 + 16 z_ikt_1_fake_manila_16 <= 0
_C550: s_j_6 + 999988 z_ikt_6_fake_belem_12 + 999988 z_ikt_6_fake_manila_12
 <= 1000000
_C551: - c_j_6 + 13 z_ikt_6_fake_belem_13 + 13 z_ikt_6_fake_manila_13 <= 0
_C552: z_ikt_6_fake_belem_13 + z_ikt_6_fake_manila_13 <= 1
_C553: s_j_6 + 999987 z_ikt_6_fake_belem_13 + 999987 z_ikt_6_fake_manila_13
 <= 1000000
_C554: - c_j_6 + 14 z_ikt_6_fake_belem_14 + 14 z_ikt_6_fake_manila_14 <= 0
_C555: z_ikt_6_fake_belem_14 + z_ikt_6_fake_manila_14 <= 1
_C556: s_j_6 + 999986 z_ikt_6_fake_belem_14 + 999986 z_ikt_6_fake_manila_14
 <= 1000000
_C557: - c_j_6 + 15 z_ikt_6_fake_belem_15 + 15 z_ikt_6_fake_manila_15 <= 0
_C558: z_ikt_6_fake_belem_15 + z_ikt_6_fake_manila_15 <= 1
_C559: s_j_6 + 999985 z_ikt_6_fake_belem_15 + 999985 z_ikt_6_fake_manila_15
 <= 1000000
_C56: z_ikt_1_fake_belem_16 + z_ikt_1_fake_manila_16 <= 1
_C560: - c_j_6 + 16 z_ikt_6_fake_belem_16 + 16 z_ikt_6_fake_manila_16 <= 0
_C561: z_ikt_6_fake_belem_16 + z_ikt_6_fake_manila_16 <= 1
_C562: s_j_6 + 999984 z_ikt_6_fake_belem_16 + 999984 z_ikt_6_fake_manila_16
 <= 1000000
_C563: - c_j_6 + 17 z_ikt_6_fake_belem_17 + 17 z_ikt_6_fake_manila_17 <= 0
_C564: z_ikt_6_fake_belem_17 + z_ikt_6_fake_manila_17 <= 1
_C565: s_j_6 + 999983 z_ikt_6_fake_belem_17 + 999983 z_ikt_6_fake_manila_17
 <= 1000000
_C566: - c_j_6 + 18 z_ikt_6_fake_belem_18 + 18 z_ikt_6_fake_manila_18 <= 0
_C567: z_ikt_6_fake_belem_18 + z_ikt_6_fake_manila_18 <= 1
_C568: s_j_6 + 999982 z_ikt_6_fake_belem_18 + 999982 z_ikt_6_fake_manila_18
 <= 1000000
_C569: - c_j_6 + 19 z_ikt_6_fake_belem_19 + 19 z_ikt_6_fake_manila_19 <= 0
_C57: s_j_1 + 999984 z_ikt_1_fake_belem_16 + 999984 z_ikt_1_fake_manila_16
 <= 1000000
_C570: z_ikt_6_fake_belem_19 + z_ikt_6_fake_manila_19 <= 1
_C571: s_j_6 + 999981 z_ikt_6_fake_belem_19 + 999981 z_ikt_6_fake_manila_19
 <= 1000000
_C572: - c_j_6 + 20 z_ikt_6_fake_belem_20 + 20 z_ikt_6_fake_manila_20 <= 0
_C573: z_ikt_6_fake_belem_20 + z_ikt_6_fake_manila_20 <= 1
_C574: s_j_6 + 999980 z_ikt_6_fake_belem_20 + 999980 z_ikt_6_fake_manila_20
 <= 1000000
_C575: - c_j_6 + 21 z_ikt_6_fake_belem_21 + 21 z_ikt_6_fake_manila_21 <= 0
_C576: z_ikt_6_fake_belem_21 + z_ikt_6_fake_manila_21 <= 1
_C577: s_j_6 + 999979 z_ikt_6_fake_belem_21 + 999979 z_ikt_6_fake_manila_21
 <= 1000000
_C578: - c_j_6 + 22 z_ikt_6_fake_belem_22 + 22 z_ikt_6_fake_manila_22 <= 0
_C579: z_ikt_6_fake_belem_22 + z_ikt_6_fake_manila_22 <= 1
_C58: - c_j_1 + 17 z_ikt_1_fake_belem_17 + 17 z_ikt_1_fake_manila_17 <= 0
_C580: s_j_6 + 999978 z_ikt_6_fake_belem_22 + 999978 z_ikt_6_fake_manila_22
 <= 1000000
_C581: - c_j_6 + 23 z_ikt_6_fake_belem_23 + 23 z_ikt_6_fake_manila_23 <= 0
_C582: z_ikt_6_fake_belem_23 + z_ikt_6_fake_manila_23 <= 1
_C583: s_j_6 + 999977 z_ikt_6_fake_belem_23 + 999977 z_ikt_6_fake_manila_23
 <= 1000000
_C584: - c_j_6 + 24 z_ikt_6_fake_belem_24 + 24 z_ikt_6_fake_manila_24 <= 0
_C585: z_ikt_6_fake_belem_24 + z_ikt_6_fake_manila_24 <= 1
_C586: s_j_6 + 999976 z_ikt_6_fake_belem_24 + 999976 z_ikt_6_fake_manila_24
 <= 1000000
_C587: - c_j_6 + 25 z_ikt_6_fake_belem_25 + 25 z_ikt_6_fake_manila_25 <= 0
_C588: z_ikt_6_fake_belem_25 + z_ikt_6_fake_manila_25 <= 1
_C589: s_j_6 + 999975 z_ikt_6_fake_belem_25 + 999975 z_ikt_6_fake_manila_25
 <= 1000000
_C59: z_ikt_1_fake_belem_17 + z_ikt_1_fake_manila_17 <= 1
_C590: - c_j_6 + 26 z_ikt_6_fake_belem_26 + 26 z_ikt_6_fake_manila_26 <= 0
_C591: z_ikt_6_fake_belem_26 + z_ikt_6_fake_manila_26 <= 1
_C592: s_j_6 + 999974 z_ikt_6_fake_belem_26 + 999974 z_ikt_6_fake_manila_26
 <= 1000000
_C593: - c_j_6 + 27 z_ikt_6_fake_belem_27 + 27 z_ikt_6_fake_manila_27 <= 0
_C594: z_ikt_6_fake_belem_27 + z_ikt_6_fake_manila_27 <= 1
_C595: s_j_6 + 999973 z_ikt_6_fake_belem_27 + 999973 z_ikt_6_fake_manila_27
 <= 1000000
_C596: - c_j_6 + 28 z_ikt_6_fake_belem_28 + 28 z_ikt_6_fake_manila_28 <= 0
_C597: z_ikt_6_fake_belem_28 + z_ikt_6_fake_manila_28 <= 1
_C598: s_j_6 + 999972 z_ikt_6_fake_belem_28 + 999972 z_ikt_6_fake_manila_28
 <= 1000000
_C599: - c_j_6 + 29 z_ikt_6_fake_belem_29 + 29 z_ikt_6_fake_manila_29 <= 0
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
_C600: z_ikt_6_fake_belem_29 + z_ikt_6_fake_manila_29 <= 1
_C601: s_j_6 + 999971 z_ikt_6_fake_belem_29 + 999971 z_ikt_6_fake_manila_29
 <= 1000000
_C602: - c_j_6 + 30 z_ikt_6_fake_belem_30 + 30 z_ikt_6_fake_manila_30 <= 0
_C603: z_ikt_6_fake_belem_30 + z_ikt_6_fake_manila_30 <= 1
_C604: s_j_6 + 999970 z_ikt_6_fake_belem_30 + 999970 z_ikt_6_fake_manila_30
 <= 1000000
_C605: - c_j_6 + 31 z_ikt_6_fake_belem_31 + 31 z_ikt_6_fake_manila_31 <= 0
_C606: z_ikt_6_fake_belem_31 + z_ikt_6_fake_manila_31 <= 1
_C607: s_j_6 + 999969 z_ikt_6_fake_belem_31 + 999969 z_ikt_6_fake_manila_31
 <= 1000000
_C608: 5 z_ikt_1_fake_belem_0 + z_ikt_2_fake_belem_0 + 5 z_ikt_3_fake_belem_0
 + z_ikt_4_fake_belem_0 + 5 z_ikt_5_fake_belem_0 + z_ikt_6_fake_belem_0 <= 5
_C609: 5 z_ikt_1_fake_manila_0 + z_ikt_2_fake_manila_0
 + 5 z_ikt_3_fake_manila_0 + z_ikt_4_fake_manila_0 + 5 z_ikt_5_fake_manila_0
 + z_ikt_6_fake_manila_0 <= 5
_C61: - c_j_1 + 18 z_ikt_1_fake_belem_18 + 18 z_ikt_1_fake_manila_18 <= 0
_C610: 5 z_ikt_1_fake_belem_1 + z_ikt_2_fake_belem_1 + 5 z_ikt_3_fake_belem_1
 + z_ikt_4_fake_belem_1 + 5 z_ikt_5_fake_belem_1 + z_ikt_6_fake_belem_1 <= 5
_C611: 5 z_ikt_1_fake_manila_1 + z_ikt_2_fake_manila_1
 + 5 z_ikt_3_fake_manila_1 + z_ikt_4_fake_manila_1 + 5 z_ikt_5_fake_manila_1
 + z_ikt_6_fake_manila_1 <= 5
_C612: 5 z_ikt_1_fake_belem_2 + z_ikt_2_fake_belem_2 + 5 z_ikt_3_fake_belem_2
 + z_ikt_4_fake_belem_2 + 5 z_ikt_5_fake_belem_2 + z_ikt_6_fake_belem_2 <= 5
_C613: 5 z_ikt_1_fake_manila_2 + z_ikt_2_fake_manila_2
 + 5 z_ikt_3_fake_manila_2 + z_ikt_4_fake_manila_2 + 5 z_ikt_5_fake_manila_2
 + z_ikt_6_fake_manila_2 <= 5
_C614: 5 z_ikt_1_fake_belem_3 + z_ikt_2_fake_belem_3 + 5 z_ikt_3_fake_belem_3
 + z_ikt_4_fake_belem_3 + 5 z_ikt_5_fake_belem_3 + z_ikt_6_fake_belem_3 <= 5
_C615: 5 z_ikt_1_fake_manila_3 + z_ikt_2_fake_manila_3
 + 5 z_ikt_3_fake_manila_3 + z_ikt_4_fake_manila_3 + 5 z_ikt_5_fake_manila_3
 + z_ikt_6_fake_manila_3 <= 5
_C616: 5 z_ikt_1_fake_belem_4 + z_ikt_2_fake_belem_4 + 5 z_ikt_3_fake_belem_4
 + z_ikt_4_fake_belem_4 + 5 z_ikt_5_fake_belem_4 + z_ikt_6_fake_belem_4 <= 5
_C617: 5 z_ikt_1_fake_manila_4 + z_ikt_2_fake_manila_4
 + 5 z_ikt_3_fake_manila_4 + z_ikt_4_fake_manila_4 + 5 z_ikt_5_fake_manila_4
 + z_ikt_6_fake_manila_4 <= 5
_C618: 5 z_ikt_1_fake_belem_5 + z_ikt_2_fake_belem_5 + 5 z_ikt_3_fake_belem_5
 + z_ikt_4_fake_belem_5 + 5 z_ikt_5_fake_belem_5 + z_ikt_6_fake_belem_5 <= 5
_C619: 5 z_ikt_1_fake_manila_5 + z_ikt_2_fake_manila_5
 + 5 z_ikt_3_fake_manila_5 + z_ikt_4_fake_manila_5 + 5 z_ikt_5_fake_manila_5
 + z_ikt_6_fake_manila_5 <= 5
_C62: z_ikt_1_fake_belem_18 + z_ikt_1_fake_manila_18 <= 1
_C620: 5 z_ikt_1_fake_belem_6 + z_ikt_2_fake_belem_6 + 5 z_ikt_3_fake_belem_6
 + z_ikt_4_fake_belem_6 + 5 z_ikt_5_fake_belem_6 + z_ikt_6_fake_belem_6 <= 5
_C621: 5 z_ikt_1_fake_manila_6 + z_ikt_2_fake_manila_6
 + 5 z_ikt_3_fake_manila_6 + z_ikt_4_fake_manila_6 + 5 z_ikt_5_fake_manila_6
 + z_ikt_6_fake_manila_6 <= 5
_C622: 5 z_ikt_1_fake_belem_7 + z_ikt_2_fake_belem_7 + 5 z_ikt_3_fake_belem_7
 + z_ikt_4_fake_belem_7 + 5 z_ikt_5_fake_belem_7 + z_ikt_6_fake_belem_7 <= 5
_C623: 5 z_ikt_1_fake_manila_7 + z_ikt_2_fake_manila_7
 + 5 z_ikt_3_fake_manila_7 + z_ikt_4_fake_manila_7 + 5 z_ikt_5_fake_manila_7
 + z_ikt_6_fake_manila_7 <= 5
_C624: 5 z_ikt_1_fake_belem_8 + z_ikt_2_fake_belem_8 + 5 z_ikt_3_fake_belem_8
 + z_ikt_4_fake_belem_8 + 5 z_ikt_5_fake_belem_8 + z_ikt_6_fake_belem_8 <= 5
_C625: 5 z_ikt_1_fake_manila_8 + z_ikt_2_fake_manila_8
 + 5 z_ikt_3_fake_manila_8 + z_ikt_4_fake_manila_8 + 5 z_ikt_5_fake_manila_8
 + z_ikt_6_fake_manila_8 <= 5
_C626: 5 z_ikt_1_fake_belem_9 + z_ikt_2_fake_belem_9 + 5 z_ikt_3_fake_belem_9
 + z_ikt_4_fake_belem_9 + 5 z_ikt_5_fake_belem_9 + z_ikt_6_fake_belem_9 <= 5
_C627: 5 z_ikt_1_fake_manila_9 + z_ikt_2_fake_manila_9
 + 5 z_ikt_3_fake_manila_9 + z_ikt_4_fake_manila_9 + 5 z_ikt_5_fake_manila_9
 + z_ikt_6_fake_manila_9 <= 5
_C628: 5 z_ikt_1_fake_belem_10 + z_ikt_2_fake_belem_10
 + 5 z_ikt_3_fake_belem_10 + z_ikt_4_fake_belem_10 + 5 z_ikt_5_fake_belem_10
 + z_ikt_6_fake_belem_10 <= 5
_C629: 5 z_ikt_1_fake_manila_10 + z_ikt_2_fake_manila_10
 + 5 z_ikt_3_fake_manila_10 + z_ikt_4_fake_manila_10
 + 5 z_ikt_5_fake_manila_10 + z_ikt_6_fake_manila_10 <= 5
_C63: s_j_1 + 999982 z_ikt_1_fake_belem_18 + 999982 z_ikt_1_fake_manila_18
 <= 1000000
_C630: 5 z_ikt_1_fake_belem_11 + z_ikt_2_fake_belem_11
 + 5 z_ikt_3_fake_belem_11 + z_ikt_4_fake_belem_11 + 5 z_ikt_5_fake_belem_11
 + z_ikt_6_fake_belem_11 <= 5
_C631: 5 z_ikt_1_fake_manila_11 + z_ikt_2_fake_manila_11
 + 5 z_ikt_3_fake_manila_11 + z_ikt_4_fake_manila_11
 + 5 z_ikt_5_fake_manila_11 + z_ikt_6_fake_manila_11 <= 5
_C632: 5 z_ikt_1_fake_belem_12 + z_ikt_2_fake_belem_12
 + 5 z_ikt_3_fake_belem_12 + z_ikt_4_fake_belem_12 + 5 z_ikt_5_fake_belem_12
 + z_ikt_6_fake_belem_12 <= 5
_C633: 5 z_ikt_1_fake_manila_12 + z_ikt_2_fake_manila_12
 + 5 z_ikt_3_fake_manila_12 + z_ikt_4_fake_manila_12
 + 5 z_ikt_5_fake_manila_12 + z_ikt_6_fake_manila_12 <= 5
_C634: 5 z_ikt_1_fake_belem_13 + z_ikt_2_fake_belem_13
 + 5 z_ikt_3_fake_belem_13 + z_ikt_4_fake_belem_13 + 5 z_ikt_5_fake_belem_13
 + z_ikt_6_fake_belem_13 <= 5
_C635: 5 z_ikt_1_fake_manila_13 + z_ikt_2_fake_manila_13
 + 5 z_ikt_3_fake_manila_13 + z_ikt_4_fake_manila_13
 + 5 z_ikt_5_fake_manila_13 + z_ikt_6_fake_manila_13 <= 5
_C636: 5 z_ikt_1_fake_belem_14 + z_ikt_2_fake_belem_14
 + 5 z_ikt_3_fake_belem_14 + z_ikt_4_fake_belem_14 + 5 z_ikt_5_fake_belem_14
 + z_ikt_6_fake_belem_14 <= 5
_C637: 5 z_ikt_1_fake_manila_14 + z_ikt_2_fake_manila_14
 + 5 z_ikt_3_fake_manila_14 + z_ikt_4_fake_manila_14
 + 5 z_ikt_5_fake_manila_14 + z_ikt_6_fake_manila_14 <= 5
_C638: 5 z_ikt_1_fake_belem_15 + z_ikt_2_fake_belem_15
 + 5 z_ikt_3_fake_belem_15 + z_ikt_4_fake_belem_15 + 5 z_ikt_5_fake_belem_15
 + z_ikt_6_fake_belem_15 <= 5
_C639: 5 z_ikt_1_fake_manila_15 + z_ikt_2_fake_manila_15
 + 5 z_ikt_3_fake_manila_15 + z_ikt_4_fake_manila_15
 + 5 z_ikt_5_fake_manila_15 + z_ikt_6_fake_manila_15 <= 5
_C64: - c_j_1 + 19 z_ikt_1_fake_belem_19 + 19 z_ikt_1_fake_manila_19 <= 0
_C640: 5 z_ikt_1_fake_belem_16 + z_ikt_2_fake_belem_16
 + 5 z_ikt_3_fake_belem_16 + z_ikt_4_fake_belem_16 + 5 z_ikt_5_fake_belem_16
 + z_ikt_6_fake_belem_16 <= 5
_C641: 5 z_ikt_1_fake_manila_16 + z_ikt_2_fake_manila_16
 + 5 z_ikt_3_fake_manila_16 + z_ikt_4_fake_manila_16
 + 5 z_ikt_5_fake_manila_16 + z_ikt_6_fake_manila_16 <= 5
_C642: 5 z_ikt_1_fake_belem_17 + z_ikt_2_fake_belem_17
 + 5 z_ikt_3_fake_belem_17 + z_ikt_4_fake_belem_17 + 5 z_ikt_5_fake_belem_17
 + z_ikt_6_fake_belem_17 <= 5
_C643: 5 z_ikt_1_fake_manila_17 + z_ikt_2_fake_manila_17
 + 5 z_ikt_3_fake_manila_17 + z_ikt_4_fake_manila_17
 + 5 z_ikt_5_fake_manila_17 + z_ikt_6_fake_manila_17 <= 5
_C644: 5 z_ikt_1_fake_belem_18 + z_ikt_2_fake_belem_18
 + 5 z_ikt_3_fake_belem_18 + z_ikt_4_fake_belem_18 + 5 z_ikt_5_fake_belem_18
 + z_ikt_6_fake_belem_18 <= 5
_C645: 5 z_ikt_1_fake_manila_18 + z_ikt_2_fake_manila_18
 + 5 z_ikt_3_fake_manila_18 + z_ikt_4_fake_manila_18
 + 5 z_ikt_5_fake_manila_18 + z_ikt_6_fake_manila_18 <= 5
_C646: 5 z_ikt_1_fake_belem_19 + z_ikt_2_fake_belem_19
 + 5 z_ikt_3_fake_belem_19 + z_ikt_4_fake_belem_19 + 5 z_ikt_5_fake_belem_19
 + z_ikt_6_fake_belem_19 <= 5
_C647: 5 z_ikt_1_fake_manila_19 + z_ikt_2_fake_manila_19
 + 5 z_ikt_3_fake_manila_19 + z_ikt_4_fake_manila_19
 + 5 z_ikt_5_fake_manila_19 + z_ikt_6_fake_manila_19 <= 5
_C648: 5 z_ikt_1_fake_belem_20 + z_ikt_2_fake_belem_20
 + 5 z_ikt_3_fake_belem_20 + z_ikt_4_fake_belem_20 + 5 z_ikt_5_fake_belem_20
 + z_ikt_6_fake_belem_20 <= 5
_C649: 5 z_ikt_1_fake_manila_20 + z_ikt_2_fake_manila_20
 + 5 z_ikt_3_fake_manila_20 + z_ikt_4_fake_manila_20
 + 5 z_ikt_5_fake_manila_20 + z_ikt_6_fake_manila_20 <= 5
_C65: z_ikt_1_fake_belem_19 + z_ikt_1_fake_manila_19 <= 1
_C650: 5 z_ikt_1_fake_belem_21 + z_ikt_2_fake_belem_21
 + 5 z_ikt_3_fake_belem_21 + z_ikt_4_fake_belem_21 + 5 z_ikt_5_fake_belem_21
 + z_ikt_6_fake_belem_21 <= 5
_C651: 5 z_ikt_1_fake_manila_21 + z_ikt_2_fake_manila_21
 + 5 z_ikt_3_fake_manila_21 + z_ikt_4_fake_manila_21
 + 5 z_ikt_5_fake_manila_21 + z_ikt_6_fake_manila_21 <= 5
_C652: 5 z_ikt_1_fake_belem_22 + z_ikt_2_fake_belem_22
 + 5 z_ikt_3_fake_belem_22 + z_ikt_4_fake_belem_22 + 5 z_ikt_5_fake_belem_22
 + z_ikt_6_fake_belem_22 <= 5
_C653: 5 z_ikt_1_fake_manila_22 + z_ikt_2_fake_manila_22
 + 5 z_ikt_3_fake_manila_22 + z_ikt_4_fake_manila_22
 + 5 z_ikt_5_fake_manila_22 + z_ikt_6_fake_manila_22 <= 5
_C654: 5 z_ikt_1_fake_belem_23 + z_ikt_2_fake_belem_23
 + 5 z_ikt_3_fake_belem_23 + z_ikt_4_fake_belem_23 + 5 z_ikt_5_fake_belem_23
 + z_ikt_6_fake_belem_23 <= 5
_C655: 5 z_ikt_1_fake_manila_23 + z_ikt_2_fake_manila_23
 + 5 z_ikt_3_fake_manila_23 + z_ikt_4_fake_manila_23
 + 5 z_ikt_5_fake_manila_23 + z_ikt_6_fake_manila_23 <= 5
_C656: 5 z_ikt_1_fake_belem_24 + z_ikt_2_fake_belem_24
 + 5 z_ikt_3_fake_belem_24 + z_ikt_4_fake_belem_24 + 5 z_ikt_5_fake_belem_24
 + z_ikt_6_fake_belem_24 <= 5
_C657: 5 z_ikt_1_fake_manila_24 + z_ikt_2_fake_manila_24
 + 5 z_ikt_3_fake_manila_24 + z_ikt_4_fake_manila_24
 + 5 z_ikt_5_fake_manila_24 + z_ikt_6_fake_manila_24 <= 5
_C658: 5 z_ikt_1_fake_belem_25 + z_ikt_2_fake_belem_25
 + 5 z_ikt_3_fake_belem_25 + z_ikt_4_fake_belem_25 + 5 z_ikt_5_fake_belem_25
 + z_ikt_6_fake_belem_25 <= 5
_C659: 5 z_ikt_1_fake_manila_25 + z_ikt_2_fake_manila_25
 + 5 z_ikt_3_fake_manila_25 + z_ikt_4_fake_manila_25
 + 5 z_ikt_5_fake_manila_25 + z_ikt_6_fake_manila_25 <= 5
_C66: s_j_1 + 999981 z_ikt_1_fake_belem_19 + 999981 z_ikt_1_fake_manila_19
 <= 1000000
_C660: 5 z_ikt_1_fake_belem_26 + z_ikt_2_fake_belem_26
 + 5 z_ikt_3_fake_belem_26 + z_ikt_4_fake_belem_26 + 5 z_ikt_5_fake_belem_26
 + z_ikt_6_fake_belem_26 <= 5
_C661: 5 z_ikt_1_fake_manila_26 + z_ikt_2_fake_manila_26
 + 5 z_ikt_3_fake_manila_26 + z_ikt_4_fake_manila_26
 + 5 z_ikt_5_fake_manila_26 + z_ikt_6_fake_manila_26 <= 5
_C662: 5 z_ikt_1_fake_belem_27 + z_ikt_2_fake_belem_27
 + 5 z_ikt_3_fake_belem_27 + z_ikt_4_fake_belem_27 + 5 z_ikt_5_fake_belem_27
 + z_ikt_6_fake_belem_27 <= 5
_C663: 5 z_ikt_1_fake_manila_27 + z_ikt_2_fake_manila_27
 + 5 z_ikt_3_fake_manila_27 + z_ikt_4_fake_manila_27
 + 5 z_ikt_5_fake_manila_27 + z_ikt_6_fake_manila_27 <= 5
_C664: 5 z_ikt_1_fake_belem_28 + z_ikt_2_fake_belem_28
 + 5 z_ikt_3_fake_belem_28 + z_ikt_4_fake_belem_28 + 5 z_ikt_5_fake_belem_28
 + z_ikt_6_fake_belem_28 <= 5
_C665: 5 z_ikt_1_fake_manila_28 + z_ikt_2_fake_manila_28
 + 5 z_ikt_3_fake_manila_28 + z_ikt_4_fake_manila_28
 + 5 z_ikt_5_fake_manila_28 + z_ikt_6_fake_manila_28 <= 5
_C666: 5 z_ikt_1_fake_belem_29 + z_ikt_2_fake_belem_29
 + 5 z_ikt_3_fake_belem_29 + z_ikt_4_fake_belem_29 + 5 z_ikt_5_fake_belem_29
 + z_ikt_6_fake_belem_29 <= 5
_C667: 5 z_ikt_1_fake_manila_29 + z_ikt_2_fake_manila_29
 + 5 z_ikt_3_fake_manila_29 + z_ikt_4_fake_manila_29
 + 5 z_ikt_5_fake_manila_29 + z_ikt_6_fake_manila_29 <= 5
_C668: 5 z_ikt_1_fake_belem_30 + z_ikt_2_fake_belem_30
 + 5 z_ikt_3_fake_belem_30 + z_ikt_4_fake_belem_30 + 5 z_ikt_5_fake_belem_30
 + z_ikt_6_fake_belem_30 <= 5
_C669: 5 z_ikt_1_fake_manila_30 + z_ikt_2_fake_manila_30
 + 5 z_ikt_3_fake_manila_30 + z_ikt_4_fake_manila_30
 + 5 z_ikt_5_fake_manila_30 + z_ikt_6_fake_manila_30 <= 5
_C67: - c_j_1 + 20 z_ikt_1_fake_belem_20 + 20 z_ikt_1_fake_manila_20 <= 0
_C670: 5 z_ikt_1_fake_belem_31 + z_ikt_2_fake_belem_31
 + 5 z_ikt_3_fake_belem_31 + z_ikt_4_fake_belem_31 + 5 z_ikt_5_fake_belem_31
 + z_ikt_6_fake_belem_31 <= 5
_C671: 5 z_ikt_1_fake_manila_31 + z_ikt_2_fake_manila_31
 + 5 z_ikt_3_fake_manila_31 + z_ikt_4_fake_manila_31
 + 5 z_ikt_5_fake_manila_31 + z_ikt_6_fake_manila_31 <= 5
_C672: y_ijk_0_1_fake_belem + y_ijk_0_1_fake_manila + y_ijk_1_1_fake_belem
 + y_ijk_1_1_fake_manila + y_ijk_2_1_fake_belem + y_ijk_2_1_fake_manila
 + y_ijk_3_1_fake_belem + y_ijk_3_1_fake_manila + y_ijk_4_1_fake_belem
 + y_ijk_4_1_fake_manila + y_ijk_5_1_fake_belem + y_ijk_5_1_fake_manila
 + y_ijk_6_1_fake_belem + y_ijk_6_1_fake_manila >= 1
_C673: c_j_1 - s_j_1 - 12 x_ik_1_fake_belem - 9 x_ik_1_fake_manila
 - 50 y_ijk_1_1_fake_belem - 50 y_ijk_1_1_fake_manila - 6 y_ijk_2_1_fake_belem
 - 8 y_ijk_2_1_fake_manila - 8 y_ijk_3_1_fake_belem - 12 y_ijk_3_1_fake_manila
 - 6 y_ijk_4_1_fake_belem - 10 y_ijk_4_1_fake_manila - 8 y_ijk_5_1_fake_belem
 - 11 y_ijk_5_1_fake_manila - 8 y_ijk_6_1_fake_belem - 8 y_ijk_6_1_fake_manila
 >= 0
_C674: x_ik_1_fake_belem - 0.001 y_ijk_0_1_fake_belem
 - 0.001 y_ijk_1_1_fake_belem - 0.001 y_ijk_2_1_fake_belem
 - 0.001 y_ijk_3_1_fake_belem - 0.001 y_ijk_4_1_fake_belem
 - 0.001 y_ijk_5_1_fake_belem - 0.001 y_ijk_6_1_fake_belem >= 0
_C675: x_ik_1_fake_belem - 0.001 y_ijk_1_0_fake_belem
 - 0.001 y_ijk_1_1_fake_belem - 0.001 y_ijk_1_2_fake_belem
 - 0.001 y_ijk_1_3_fake_belem - 0.001 y_ijk_1_4_fake_belem
 - 0.001 y_ijk_1_5_fake_belem - 0.001 y_ijk_1_6_fake_belem >= 0
_C676: - y_ijk_0_1_fake_belem + z_ikt_1_fake_belem_0 = 0
_C677: x_ik_1_fake_manila - 0.001 y_ijk_0_1_fake_manila
 - 0.001 y_ijk_1_1_fake_manila - 0.001 y_ijk_2_1_fake_manila
 - 0.001 y_ijk_3_1_fake_manila - 0.001 y_ijk_4_1_fake_manila
 - 0.001 y_ijk_5_1_fake_manila - 0.001 y_ijk_6_1_fake_manila >= 0
_C678: x_ik_1_fake_manila - 0.001 y_ijk_1_0_fake_manila
 - 0.001 y_ijk_1_1_fake_manila - 0.001 y_ijk_1_2_fake_manila
 - 0.001 y_ijk_1_3_fake_manila - 0.001 y_ijk_1_4_fake_manila
 - 0.001 y_ijk_1_5_fake_manila - 0.001 y_ijk_1_6_fake_manila >= 0
_C679: - y_ijk_0_1_fake_manila + z_ikt_1_fake_manila_0 = 0
_C68: z_ikt_1_fake_belem_20 + z_ikt_1_fake_manila_20 <= 1
_C680: c_j_0 - s_j_1 + 1000 y_ijk_0_1_fake_belem + 1000 y_ijk_0_1_fake_manila
 <= 1000
_C681: c_j_1 - s_j_1 + 1000 y_ijk_1_1_fake_belem + 1000 y_ijk_1_1_fake_manila
 <= 1000
_C682: c_j_2 - s_j_1 + 1000 y_ijk_2_1_fake_belem + 1000 y_ijk_2_1_fake_manila
 <= 1000
_C683: c_j_3 - s_j_1 + 1000 y_ijk_3_1_fake_belem + 1000 y_ijk_3_1_fake_manila
 <= 1000
_C684: c_j_4 - s_j_1 + 1000 y_ijk_4_1_fake_belem + 1000 y_ijk_4_1_fake_manila
 <= 1000
_C685: c_j_5 - s_j_1 + 1000 y_ijk_5_1_fake_belem + 1000 y_ijk_5_1_fake_manila
 <= 1000
_C686: c_j_6 - s_j_1 + 1000 y_ijk_6_1_fake_belem + 1000 y_ijk_6_1_fake_manila
 <= 1000
_C687: y_ijk_0_2_fake_belem + y_ijk_0_2_fake_manila + y_ijk_1_2_fake_belem
 + y_ijk_1_2_fake_manila + y_ijk_2_2_fake_belem + y_ijk_2_2_fake_manila
 + y_ijk_3_2_fake_belem + y_ijk_3_2_fake_manila + y_ijk_4_2_fake_belem
 + y_ijk_4_2_fake_manila + y_ijk_5_2_fake_belem + y_ijk_5_2_fake_manila
 + y_ijk_6_2_fake_belem + y_ijk_6_2_fake_manila >= 1
_C688: c_j_2 - s_j_2 - 8 x_ik_2_fake_belem - 5 x_ik_2_fake_manila
 - 6 y_ijk_1_2_fake_belem - 6 y_ijk_1_2_fake_manila - 50 y_ijk_2_2_fake_belem
 - 50 y_ijk_2_2_fake_manila - 8 y_ijk_3_2_fake_belem - 9 y_ijk_3_2_fake_manila
 - 5 y_ijk_4_2_fake_belem - 6 y_ijk_4_2_fake_manila - 10 y_ijk_5_2_fake_belem
 - 9 y_ijk_5_2_fake_manila - 7 y_ijk_6_2_fake_belem - 5 y_ijk_6_2_fake_manila
 >= 0
_C689: x_ik_2_fake_belem - 0.001 y_ijk_0_2_fake_belem
 - 0.001 y_ijk_1_2_fake_belem - 0.001 y_ijk_2_2_fake_belem
 - 0.001 y_ijk_3_2_fake_belem - 0.001 y_ijk_4_2_fake_belem
 - 0.001 y_ijk_5_2_fake_belem - 0.001 y_ijk_6_2_fake_belem >= 0
_C69: s_j_1 + 999980 z_ikt_1_fake_belem_20 + 999980 z_ikt_1_fake_manila_20
 <= 1000000
_C690: x_ik_2_fake_belem - 0.001 y_ijk_2_0_fake_belem
 - 0.001 y_ijk_2_1_fake_belem - 0.001 y_ijk_2_2_fake_belem
 - 0.001 y_ijk_2_3_fake_belem - 0.001 y_ijk_2_4_fake_belem
 - 0.001 y_ijk_2_5_fake_belem - 0.001 y_ijk_2_6_fake_belem >= 0
_C691: - y_ijk_0_2_fake_belem + z_ikt_2_fake_belem_0 = 0
_C692: x_ik_2_fake_manila - 0.001 y_ijk_0_2_fake_manila
 - 0.001 y_ijk_1_2_fake_manila - 0.001 y_ijk_2_2_fake_manila
 - 0.001 y_ijk_3_2_fake_manila - 0.001 y_ijk_4_2_fake_manila
 - 0.001 y_ijk_5_2_fake_manila - 0.001 y_ijk_6_2_fake_manila >= 0
_C693: x_ik_2_fake_manila - 0.001 y_ijk_2_0_fake_manila
 - 0.001 y_ijk_2_1_fake_manila - 0.001 y_ijk_2_2_fake_manila
 - 0.001 y_ijk_2_3_fake_manila - 0.001 y_ijk_2_4_fake_manila
 - 0.001 y_ijk_2_5_fake_manila - 0.001 y_ijk_2_6_fake_manila >= 0
_C694: - y_ijk_0_2_fake_manila + z_ikt_2_fake_manila_0 = 0
_C695: c_j_0 - s_j_2 + 1000 y_ijk_0_2_fake_belem + 1000 y_ijk_0_2_fake_manila
 <= 1000
_C696: c_j_1 - s_j_2 + 1000 y_ijk_1_2_fake_belem + 1000 y_ijk_1_2_fake_manila
 <= 1000
_C697: c_j_2 - s_j_2 + 1000 y_ijk_2_2_fake_belem + 1000 y_ijk_2_2_fake_manila
 <= 1000
_C698: c_j_3 - s_j_2 + 1000 y_ijk_3_2_fake_belem + 1000 y_ijk_3_2_fake_manila
 <= 1000
_C699: c_j_4 - s_j_2 + 1000 y_ijk_4_2_fake_belem + 1000 y_ijk_4_2_fake_manila
 <= 1000
_C7: - c_j_1 <= 0
_C70: - c_j_1 + 21 z_ikt_1_fake_belem_21 + 21 z_ikt_1_fake_manila_21 <= 0
_C700: c_j_5 - s_j_2 + 1000 y_ijk_5_2_fake_belem + 1000 y_ijk_5_2_fake_manila
 <= 1000
_C701: c_j_6 - s_j_2 + 1000 y_ijk_6_2_fake_belem + 1000 y_ijk_6_2_fake_manila
 <= 1000
_C702: y_ijk_0_3_fake_belem + y_ijk_0_3_fake_manila + y_ijk_1_3_fake_belem
 + y_ijk_1_3_fake_manila + y_ijk_2_3_fake_belem + y_ijk_2_3_fake_manila
 + y_ijk_3_3_fake_belem + y_ijk_3_3_fake_manila + y_ijk_4_3_fake_belem
 + y_ijk_4_3_fake_manila + y_ijk_5_3_fake_belem + y_ijk_5_3_fake_manila
 + y_ijk_6_3_fake_belem + y_ijk_6_3_fake_manila >= 1
_C703: c_j_3 - s_j_3 - 8 x_ik_3_fake_belem - 11 x_ik_3_fake_manila
 - 8 y_ijk_1_3_fake_belem - 8 y_ijk_1_3_fake_manila - 10 y_ijk_2_3_fake_belem
 - 7 y_ijk_2_3_fake_manila - 50 y_ijk_3_3_fake_belem
 - 50 y_ijk_3_3_fake_manila - 6 y_ijk_4_3_fake_belem - 7 y_ijk_4_3_fake_manila
 - 12 y_ijk_5_3_fake_belem - 12 y_ijk_5_3_fake_manila - 7 y_ijk_6_3_fake_belem
 - 10 y_ijk_6_3_fake_manila >= 0
_C704: x_ik_3_fake_belem - 0.001 y_ijk_0_3_fake_belem
 - 0.001 y_ijk_1_3_fake_belem - 0.001 y_ijk_2_3_fake_belem
 - 0.001 y_ijk_3_3_fake_belem - 0.001 y_ijk_4_3_fake_belem
 - 0.001 y_ijk_5_3_fake_belem - 0.001 y_ijk_6_3_fake_belem >= 0
_C705: x_ik_3_fake_belem - 0.001 y_ijk_3_0_fake_belem
 - 0.001 y_ijk_3_1_fake_belem - 0.001 y_ijk_3_2_fake_belem
 - 0.001 y_ijk_3_3_fake_belem - 0.001 y_ijk_3_4_fake_belem
 - 0.001 y_ijk_3_5_fake_belem - 0.001 y_ijk_3_6_fake_belem >= 0
_C706: - y_ijk_0_3_fake_belem + z_ikt_3_fake_belem_0 = 0
_C707: x_ik_3_fake_manila - 0.001 y_ijk_0_3_fake_manila
 - 0.001 y_ijk_1_3_fake_manila - 0.001 y_ijk_2_3_fake_manila
 - 0.001 y_ijk_3_3_fake_manila - 0.001 y_ijk_4_3_fake_manila
 - 0.001 y_ijk_5_3_fake_manila - 0.001 y_ijk_6_3_fake_manila >= 0
_C708: x_ik_3_fake_manila - 0.001 y_ijk_3_0_fake_manila
 - 0.001 y_ijk_3_1_fake_manila - 0.001 y_ijk_3_2_fake_manila
 - 0.001 y_ijk_3_3_fake_manila - 0.001 y_ijk_3_4_fake_manila
 - 0.001 y_ijk_3_5_fake_manila - 0.001 y_ijk_3_6_fake_manila >= 0
_C709: - y_ijk_0_3_fake_manila + z_ikt_3_fake_manila_0 = 0
_C71: z_ikt_1_fake_belem_21 + z_ikt_1_fake_manila_21 <= 1
_C710: c_j_0 - s_j_3 + 1000 y_ijk_0_3_fake_belem + 1000 y_ijk_0_3_fake_manila
 <= 1000
_C711: c_j_1 - s_j_3 + 1000 y_ijk_1_3_fake_belem + 1000 y_ijk_1_3_fake_manila
 <= 1000
_C712: c_j_2 - s_j_3 + 1000 y_ijk_2_3_fake_belem + 1000 y_ijk_2_3_fake_manila
 <= 1000
_C713: c_j_3 - s_j_3 + 1000 y_ijk_3_3_fake_belem + 1000 y_ijk_3_3_fake_manila
 <= 1000
_C714: c_j_4 - s_j_3 + 1000 y_ijk_4_3_fake_belem + 1000 y_ijk_4_3_fake_manila
 <= 1000
_C715: c_j_5 - s_j_3 + 1000 y_ijk_5_3_fake_belem + 1000 y_ijk_5_3_fake_manila
 <= 1000
_C716: c_j_6 - s_j_3 + 1000 y_ijk_6_3_fake_belem + 1000 y_ijk_6_3_fake_manila
 <= 1000
_C717: y_ijk_0_4_fake_belem + y_ijk_0_4_fake_manila + y_ijk_1_4_fake_belem
 + y_ijk_1_4_fake_manila + y_ijk_2_4_fake_belem + y_ijk_2_4_fake_manila
 + y_ijk_3_4_fake_belem + y_ijk_3_4_fake_manila + y_ijk_4_4_fake_belem
 + y_ijk_4_4_fake_manila + y_ijk_5_4_fake_belem + y_ijk_5_4_fake_manila
 + y_ijk_6_4_fake_belem + y_ijk_6_4_fake_manila >= 1
_C718: c_j_4 - s_j_4 - 7 x_ik_4_fake_belem - 7 x_ik_4_fake_manila
 - 9 y_ijk_1_4_fake_belem - 8 y_ijk_1_4_fake_manila - 5 y_ijk_2_4_fake_belem
 - 4 y_ijk_2_4_fake_manila - 8 y_ijk_3_4_fake_belem - 8 y_ijk_3_4_fake_manila
 - 50 y_ijk_4_4_fake_belem - 50 y_ijk_4_4_fake_manila - 8 y_ijk_5_4_fake_belem
 - 10 y_ijk_5_4_fake_manila - 4 y_ijk_6_4_fake_belem - 8 y_ijk_6_4_fake_manila
 >= 0
_C719: x_ik_4_fake_belem - 0.001 y_ijk_0_4_fake_belem
 - 0.001 y_ijk_1_4_fake_belem - 0.001 y_ijk_2_4_fake_belem
 - 0.001 y_ijk_3_4_fake_belem - 0.001 y_ijk_4_4_fake_belem
 - 0.001 y_ijk_5_4_fake_belem - 0.001 y_ijk_6_4_fake_belem >= 0
_C72: s_j_1 + 999979 z_ikt_1_fake_belem_21 + 999979 z_ikt_1_fake_manila_21
 <= 1000000
_C720: x_ik_4_fake_belem - 0.001 y_ijk_4_0_fake_belem
 - 0.001 y_ijk_4_1_fake_belem - 0.001 y_ijk_4_2_fake_belem
 - 0.001 y_ijk_4_3_fake_belem - 0.001 y_ijk_4_4_fake_belem
 - 0.001 y_ijk_4_5_fake_belem - 0.001 y_ijk_4_6_fake_belem >= 0
_C721: - y_ijk_0_4_fake_belem + z_ikt_4_fake_belem_0 = 0
_C722: x_ik_4_fake_manila - 0.001 y_ijk_0_4_fake_manila
 - 0.001 y_ijk_1_4_fake_manila - 0.001 y_ijk_2_4_fake_manila
 - 0.001 y_ijk_3_4_fake_manila - 0.001 y_ijk_4_4_fake_manila
 - 0.001 y_ijk_5_4_fake_manila - 0.001 y_ijk_6_4_fake_manila >= 0
_C723: x_ik_4_fake_manila - 0.001 y_ijk_4_0_fake_manila
 - 0.001 y_ijk_4_1_fake_manila - 0.001 y_ijk_4_2_fake_manila
 - 0.001 y_ijk_4_3_fake_manila - 0.001 y_ijk_4_4_fake_manila
 - 0.001 y_ijk_4_5_fake_manila - 0.001 y_ijk_4_6_fake_manila >= 0
_C724: - y_ijk_0_4_fake_manila + z_ikt_4_fake_manila_0 = 0
_C725: c_j_0 - s_j_4 + 1000 y_ijk_0_4_fake_belem + 1000 y_ijk_0_4_fake_manila
 <= 1000
_C726: c_j_1 - s_j_4 + 1000 y_ijk_1_4_fake_belem + 1000 y_ijk_1_4_fake_manila
 <= 1000
_C727: c_j_2 - s_j_4 + 1000 y_ijk_2_4_fake_belem + 1000 y_ijk_2_4_fake_manila
 <= 1000
_C728: c_j_3 - s_j_4 + 1000 y_ijk_3_4_fake_belem + 1000 y_ijk_3_4_fake_manila
 <= 1000
_C729: c_j_4 - s_j_4 + 1000 y_ijk_4_4_fake_belem + 1000 y_ijk_4_4_fake_manila
 <= 1000
_C73: - c_j_1 + 22 z_ikt_1_fake_belem_22 + 22 z_ikt_1_fake_manila_22 <= 0
_C730: c_j_5 - s_j_4 + 1000 y_ijk_5_4_fake_belem + 1000 y_ijk_5_4_fake_manila
 <= 1000
_C731: c_j_6 - s_j_4 + 1000 y_ijk_6_4_fake_belem + 1000 y_ijk_6_4_fake_manila
 <= 1000
_C732: y_ijk_0_5_fake_belem + y_ijk_0_5_fake_manila + y_ijk_1_5_fake_belem
 + y_ijk_1_5_fake_manila + y_ijk_2_5_fake_belem + y_ijk_2_5_fake_manila
 + y_ijk_3_5_fake_belem + y_ijk_3_5_fake_manila + y_ijk_4_5_fake_belem
 + y_ijk_4_5_fake_manila + y_ijk_5_5_fake_belem + y_ijk_5_5_fake_manila
 + y_ijk_6_5_fake_belem + y_ijk_6_5_fake_manila >= 1
_C733: c_j_5 - s_j_5 - 12 x_ik_5_fake_belem - 8 x_ik_5_fake_manila
 - 10 y_ijk_1_5_fake_belem - 8 y_ijk_1_5_fake_manila - 9 y_ijk_2_5_fake_belem
 - 6 y_ijk_2_5_fake_manila - 8 y_ijk_3_5_fake_belem - 10 y_ijk_3_5_fake_manila
 - 7 y_ijk_4_5_fake_belem - 9 y_ijk_4_5_fake_manila - 50 y_ijk_5_5_fake_belem
 - 50 y_ijk_5_5_fake_manila - 9 y_ijk_6_5_fake_belem - 9 y_ijk_6_5_fake_manila
 >= 0
_C734: x_ik_5_fake_belem - 0.001 y_ijk_0_5_fake_belem
 - 0.001 y_ijk_1_5_fake_belem - 0.001 y_ijk_2_5_fake_belem
 - 0.001 y_ijk_3_5_fake_belem - 0.001 y_ijk_4_5_fake_belem
 - 0.001 y_ijk_5_5_fake_belem - 0.001 y_ijk_6_5_fake_belem >= 0
_C735: x_ik_5_fake_belem - 0.001 y_ijk_5_0_fake_belem
 - 0.001 y_ijk_5_1_fake_belem - 0.001 y_ijk_5_2_fake_belem
 - 0.001 y_ijk_5_3_fake_belem - 0.001 y_ijk_5_4_fake_belem
 - 0.001 y_ijk_5_5_fake_belem - 0.001 y_ijk_5_6_fake_belem >= 0
_C736: - y_ijk_0_5_fake_belem + z_ikt_5_fake_belem_0 = 0
_C737: x_ik_5_fake_manila - 0.001 y_ijk_0_5_fake_manila
 - 0.001 y_ijk_1_5_fake_manila - 0.001 y_ijk_2_5_fake_manila
 - 0.001 y_ijk_3_5_fake_manila - 0.001 y_ijk_4_5_fake_manila
 - 0.001 y_ijk_5_5_fake_manila - 0.001 y_ijk_6_5_fake_manila >= 0
_C738: x_ik_5_fake_manila - 0.001 y_ijk_5_0_fake_manila
 - 0.001 y_ijk_5_1_fake_manila - 0.001 y_ijk_5_2_fake_manila
 - 0.001 y_ijk_5_3_fake_manila - 0.001 y_ijk_5_4_fake_manila
 - 0.001 y_ijk_5_5_fake_manila - 0.001 y_ijk_5_6_fake_manila >= 0
_C739: - y_ijk_0_5_fake_manila + z_ikt_5_fake_manila_0 = 0
_C74: z_ikt_1_fake_belem_22 + z_ikt_1_fake_manila_22 <= 1
_C740: c_j_0 - s_j_5 + 1000 y_ijk_0_5_fake_belem + 1000 y_ijk_0_5_fake_manila
 <= 1000
_C741: c_j_1 - s_j_5 + 1000 y_ijk_1_5_fake_belem + 1000 y_ijk_1_5_fake_manila
 <= 1000
_C742: c_j_2 - s_j_5 + 1000 y_ijk_2_5_fake_belem + 1000 y_ijk_2_5_fake_manila
 <= 1000
_C743: c_j_3 - s_j_5 + 1000 y_ijk_3_5_fake_belem + 1000 y_ijk_3_5_fake_manila
 <= 1000
_C744: c_j_4 - s_j_5 + 1000 y_ijk_4_5_fake_belem + 1000 y_ijk_4_5_fake_manila
 <= 1000
_C745: c_j_5 - s_j_5 + 1000 y_ijk_5_5_fake_belem + 1000 y_ijk_5_5_fake_manila
 <= 1000
_C746: c_j_6 - s_j_5 + 1000 y_ijk_6_5_fake_belem + 1000 y_ijk_6_5_fake_manila
 <= 1000
_C747: y_ijk_0_6_fake_belem + y_ijk_0_6_fake_manila + y_ijk_1_6_fake_belem
 + y_ijk_1_6_fake_manila + y_ijk_2_6_fake_belem + y_ijk_2_6_fake_manila
 + y_ijk_3_6_fake_belem + y_ijk_3_6_fake_manila + y_ijk_4_6_fake_belem
 + y_ijk_4_6_fake_manila + y_ijk_5_6_fake_belem + y_ijk_5_6_fake_manila
 + y_ijk_6_6_fake_belem + y_ijk_6_6_fake_manila >= 1
_C748: c_j_6 - s_j_6 - 8 x_ik_6_fake_belem - 8 x_ik_6_fake_manila
 - 8 y_ijk_1_6_fake_belem - 8 y_ijk_1_6_fake_manila - 7 y_ijk_2_6_fake_belem
 - 5 y_ijk_2_6_fake_manila - 10 y_ijk_3_6_fake_belem - 8 y_ijk_3_6_fake_manila
 - 8 y_ijk_4_6_fake_belem - 6 y_ijk_4_6_fake_manila - 9 y_ijk_5_6_fake_belem
 - 10 y_ijk_5_6_fake_manila - 50 y_ijk_6_6_fake_belem
 - 50 y_ijk_6_6_fake_manila >= 0
_C749: x_ik_6_fake_belem - 0.001 y_ijk_0_6_fake_belem
 - 0.001 y_ijk_1_6_fake_belem - 0.001 y_ijk_2_6_fake_belem
 - 0.001 y_ijk_3_6_fake_belem - 0.001 y_ijk_4_6_fake_belem
 - 0.001 y_ijk_5_6_fake_belem - 0.001 y_ijk_6_6_fake_belem >= 0
_C75: s_j_1 + 999978 z_ikt_1_fake_belem_22 + 999978 z_ikt_1_fake_manila_22
 <= 1000000
_C750: x_ik_6_fake_belem - 0.001 y_ijk_6_0_fake_belem
 - 0.001 y_ijk_6_1_fake_belem - 0.001 y_ijk_6_2_fake_belem
 - 0.001 y_ijk_6_3_fake_belem - 0.001 y_ijk_6_4_fake_belem
 - 0.001 y_ijk_6_5_fake_belem - 0.001 y_ijk_6_6_fake_belem >= 0
_C751: - y_ijk_0_6_fake_belem + z_ikt_6_fake_belem_0 = 0
_C752: x_ik_6_fake_manila - 0.001 y_ijk_0_6_fake_manila
 - 0.001 y_ijk_1_6_fake_manila - 0.001 y_ijk_2_6_fake_manila
 - 0.001 y_ijk_3_6_fake_manila - 0.001 y_ijk_4_6_fake_manila
 - 0.001 y_ijk_5_6_fake_manila - 0.001 y_ijk_6_6_fake_manila >= 0
_C753: x_ik_6_fake_manila - 0.001 y_ijk_6_0_fake_manila
 - 0.001 y_ijk_6_1_fake_manila - 0.001 y_ijk_6_2_fake_manila
 - 0.001 y_ijk_6_3_fake_manila - 0.001 y_ijk_6_4_fake_manila
 - 0.001 y_ijk_6_5_fake_manila - 0.001 y_ijk_6_6_fake_manila >= 0
_C754: - y_ijk_0_6_fake_manila + z_ikt_6_fake_manila_0 = 0
_C755: c_j_0 - s_j_6 + 1000 y_ijk_0_6_fake_belem + 1000 y_ijk_0_6_fake_manila
 <= 1000
_C756: c_j_1 - s_j_6 + 1000 y_ijk_1_6_fake_belem + 1000 y_ijk_1_6_fake_manila
 <= 1000
_C757: c_j_2 - s_j_6 + 1000 y_ijk_2_6_fake_belem + 1000 y_ijk_2_6_fake_manila
 <= 1000
_C758: c_j_3 - s_j_6 + 1000 y_ijk_3_6_fake_belem + 1000 y_ijk_3_6_fake_manila
 <= 1000
_C759: c_j_4 - s_j_6 + 1000 y_ijk_4_6_fake_belem + 1000 y_ijk_4_6_fake_manila
 <= 1000
_C76: - c_j_1 + 23 z_ikt_1_fake_belem_23 + 23 z_ikt_1_fake_manila_23 <= 0
_C760: c_j_5 - s_j_6 + 1000 y_ijk_5_6_fake_belem + 1000 y_ijk_5_6_fake_manila
 <= 1000
_C761: c_j_6 - s_j_6 + 1000 y_ijk_6_6_fake_belem + 1000 y_ijk_6_6_fake_manila
 <= 1000
_C762: a_ij_1_1 = 0
_C763: b_ij_1_1 = 0
_C764: a_ij_1_2 + 0.001 c_j_1 - 0.001 s_j_2 >= 0
_C765: b_ij_1_2 + 0.001 c_j_1 - 0.001 c_j_2 >= 0
_C766: d_ijk_1_2_fake_belem - x_ik_1_fake_belem - x_ik_2_fake_belem >= -1
_C767: - a_ij_1_2 - b_ij_1_1 - d_ijk_1_1_fake_belem - d_ijk_1_2_fake_belem
 + e_ijlk_1_2_1_fake_belem >= -3
_C768: - a_ij_2_2 - b_ij_1_2 - 2 d_ijk_1_2_fake_belem
 + e_ijlk_1_2_2_fake_belem >= -3
_C769: - a_ij_3_2 - b_ij_1_3 - d_ijk_1_2_fake_belem - d_ijk_1_3_fake_belem
 + e_ijlk_1_2_3_fake_belem >= -3
_C77: z_ikt_1_fake_belem_23 + z_ikt_1_fake_manila_23 <= 1
_C770: - a_ij_4_2 - b_ij_1_4 - d_ijk_1_2_fake_belem - d_ijk_1_4_fake_belem
 + e_ijlk_1_2_4_fake_belem >= -3
_C771: - a_ij_5_2 - b_ij_1_5 - d_ijk_1_2_fake_belem - d_ijk_1_5_fake_belem
 + e_ijlk_1_2_5_fake_belem >= -3
_C772: - a_ij_6_2 - b_ij_1_6 - d_ijk_1_2_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_2_6_fake_belem >= -3
_C773: d_ijk_1_2_fake_manila - x_ik_1_fake_manila - x_ik_2_fake_manila >= -1
_C774: - a_ij_1_2 - b_ij_1_1 - d_ijk_1_1_fake_manila - d_ijk_1_2_fake_manila
 + e_ijlk_1_2_1_fake_manila >= -3
_C775: - a_ij_2_2 - b_ij_1_2 - 2 d_ijk_1_2_fake_manila
 + e_ijlk_1_2_2_fake_manila >= -3
_C776: - a_ij_3_2 - b_ij_1_3 - d_ijk_1_2_fake_manila - d_ijk_1_3_fake_manila
 + e_ijlk_1_2_3_fake_manila >= -3
_C777: - a_ij_4_2 - b_ij_1_4 - d_ijk_1_2_fake_manila - d_ijk_1_4_fake_manila
 + e_ijlk_1_2_4_fake_manila >= -3
_C778: - a_ij_5_2 - b_ij_1_5 - d_ijk_1_2_fake_manila - d_ijk_1_5_fake_manila
 + e_ijlk_1_2_5_fake_manila >= -3
_C779: - a_ij_6_2 - b_ij_1_6 - d_ijk_1_2_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_2_6_fake_manila >= -3
_C78: s_j_1 + 999977 z_ikt_1_fake_belem_23 + 999977 z_ikt_1_fake_manila_23
 <= 1000000
_C780: a_ij_1_3 + 0.001 c_j_1 - 0.001 s_j_3 >= 0
_C781: b_ij_1_3 + 0.001 c_j_1 - 0.001 c_j_3 >= 0
_C782: d_ijk_1_3_fake_belem - x_ik_1_fake_belem - x_ik_3_fake_belem >= -1
_C783: - a_ij_1_3 - b_ij_1_1 - d_ijk_1_1_fake_belem - d_ijk_1_3_fake_belem
 + e_ijlk_1_3_1_fake_belem >= -3
_C784: - a_ij_2_3 - b_ij_1_2 - d_ijk_1_2_fake_belem - d_ijk_1_3_fake_belem
 + e_ijlk_1_3_2_fake_belem >= -3
_C785: - a_ij_3_3 - b_ij_1_3 - 2 d_ijk_1_3_fake_belem
 + e_ijlk_1_3_3_fake_belem >= -3
_C786: - a_ij_4_3 - b_ij_1_4 - d_ijk_1_3_fake_belem - d_ijk_1_4_fake_belem
 + e_ijlk_1_3_4_fake_belem >= -3
_C787: - a_ij_5_3 - b_ij_1_5 - d_ijk_1_3_fake_belem - d_ijk_1_5_fake_belem
 + e_ijlk_1_3_5_fake_belem >= -3
_C788: - a_ij_6_3 - b_ij_1_6 - d_ijk_1_3_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_3_6_fake_belem >= -3
_C789: d_ijk_1_3_fake_manila - x_ik_1_fake_manila - x_ik_3_fake_manila >= -1
_C79: - c_j_1 + 24 z_ikt_1_fake_belem_24 + 24 z_ikt_1_fake_manila_24 <= 0
_C790: - a_ij_1_3 - b_ij_1_1 - d_ijk_1_1_fake_manila - d_ijk_1_3_fake_manila
 + e_ijlk_1_3_1_fake_manila >= -3
_C791: - a_ij_2_3 - b_ij_1_2 - d_ijk_1_2_fake_manila - d_ijk_1_3_fake_manila
 + e_ijlk_1_3_2_fake_manila >= -3
_C792: - a_ij_3_3 - b_ij_1_3 - 2 d_ijk_1_3_fake_manila
 + e_ijlk_1_3_3_fake_manila >= -3
_C793: - a_ij_4_3 - b_ij_1_4 - d_ijk_1_3_fake_manila - d_ijk_1_4_fake_manila
 + e_ijlk_1_3_4_fake_manila >= -3
_C794: - a_ij_5_3 - b_ij_1_5 - d_ijk_1_3_fake_manila - d_ijk_1_5_fake_manila
 + e_ijlk_1_3_5_fake_manila >= -3
_C795: - a_ij_6_3 - b_ij_1_6 - d_ijk_1_3_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_3_6_fake_manila >= -3
_C796: a_ij_1_4 + 0.001 c_j_1 - 0.001 s_j_4 >= 0
_C797: b_ij_1_4 + 0.001 c_j_1 - 0.001 c_j_4 >= 0
_C798: d_ijk_1_4_fake_belem - x_ik_1_fake_belem - x_ik_4_fake_belem >= -1
_C799: - a_ij_1_4 - b_ij_1_1 - d_ijk_1_1_fake_belem - d_ijk_1_4_fake_belem
 + e_ijlk_1_4_1_fake_belem >= -3
_C8: z_ikt_1_fake_belem_0 + z_ikt_1_fake_manila_0 <= 1
_C80: z_ikt_1_fake_belem_24 + z_ikt_1_fake_manila_24 <= 1
_C800: - a_ij_2_4 - b_ij_1_2 - d_ijk_1_2_fake_belem - d_ijk_1_4_fake_belem
 + e_ijlk_1_4_2_fake_belem >= -3
_C801: - a_ij_3_4 - b_ij_1_3 - d_ijk_1_3_fake_belem - d_ijk_1_4_fake_belem
 + e_ijlk_1_4_3_fake_belem >= -3
_C802: - a_ij_4_4 - b_ij_1_4 - 2 d_ijk_1_4_fake_belem
 + e_ijlk_1_4_4_fake_belem >= -3
_C803: - a_ij_5_4 - b_ij_1_5 - d_ijk_1_4_fake_belem - d_ijk_1_5_fake_belem
 + e_ijlk_1_4_5_fake_belem >= -3
_C804: - a_ij_6_4 - b_ij_1_6 - d_ijk_1_4_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_4_6_fake_belem >= -3
_C805: d_ijk_1_4_fake_manila - x_ik_1_fake_manila - x_ik_4_fake_manila >= -1
_C806: - a_ij_1_4 - b_ij_1_1 - d_ijk_1_1_fake_manila - d_ijk_1_4_fake_manila
 + e_ijlk_1_4_1_fake_manila >= -3
_C807: - a_ij_2_4 - b_ij_1_2 - d_ijk_1_2_fake_manila - d_ijk_1_4_fake_manila
 + e_ijlk_1_4_2_fake_manila >= -3
_C808: - a_ij_3_4 - b_ij_1_3 - d_ijk_1_3_fake_manila - d_ijk_1_4_fake_manila
 + e_ijlk_1_4_3_fake_manila >= -3
_C809: - a_ij_4_4 - b_ij_1_4 - 2 d_ijk_1_4_fake_manila
 + e_ijlk_1_4_4_fake_manila >= -3
_C81: s_j_1 + 999976 z_ikt_1_fake_belem_24 + 999976 z_ikt_1_fake_manila_24
 <= 1000000
_C810: - a_ij_5_4 - b_ij_1_5 - d_ijk_1_4_fake_manila - d_ijk_1_5_fake_manila
 + e_ijlk_1_4_5_fake_manila >= -3
_C811: - a_ij_6_4 - b_ij_1_6 - d_ijk_1_4_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_4_6_fake_manila >= -3
_C812: a_ij_1_5 + 0.001 c_j_1 - 0.001 s_j_5 >= 0
_C813: b_ij_1_5 + 0.001 c_j_1 - 0.001 c_j_5 >= 0
_C814: d_ijk_1_5_fake_belem - x_ik_1_fake_belem - x_ik_5_fake_belem >= -1
_C815: - a_ij_1_5 - b_ij_1_1 - d_ijk_1_1_fake_belem - d_ijk_1_5_fake_belem
 + e_ijlk_1_5_1_fake_belem >= -3
_C816: - a_ij_2_5 - b_ij_1_2 - d_ijk_1_2_fake_belem - d_ijk_1_5_fake_belem
 + e_ijlk_1_5_2_fake_belem >= -3
_C817: - a_ij_3_5 - b_ij_1_3 - d_ijk_1_3_fake_belem - d_ijk_1_5_fake_belem
 + e_ijlk_1_5_3_fake_belem >= -3
_C818: - a_ij_4_5 - b_ij_1_4 - d_ijk_1_4_fake_belem - d_ijk_1_5_fake_belem
 + e_ijlk_1_5_4_fake_belem >= -3
_C819: - a_ij_5_5 - b_ij_1_5 - 2 d_ijk_1_5_fake_belem
 + e_ijlk_1_5_5_fake_belem >= -3
_C82: - c_j_1 + 25 z_ikt_1_fake_belem_25 + 25 z_ikt_1_fake_manila_25 <= 0
_C820: - a_ij_6_5 - b_ij_1_6 - d_ijk_1_5_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_5_6_fake_belem >= -3
_C821: d_ijk_1_5_fake_manila - x_ik_1_fake_manila - x_ik_5_fake_manila >= -1
_C822: - a_ij_1_5 - b_ij_1_1 - d_ijk_1_1_fake_manila - d_ijk_1_5_fake_manila
 + e_ijlk_1_5_1_fake_manila >= -3
_C823: - a_ij_2_5 - b_ij_1_2 - d_ijk_1_2_fake_manila - d_ijk_1_5_fake_manila
 + e_ijlk_1_5_2_fake_manila >= -3
_C824: - a_ij_3_5 - b_ij_1_3 - d_ijk_1_3_fake_manila - d_ijk_1_5_fake_manila
 + e_ijlk_1_5_3_fake_manila >= -3
_C825: - a_ij_4_5 - b_ij_1_4 - d_ijk_1_4_fake_manila - d_ijk_1_5_fake_manila
 + e_ijlk_1_5_4_fake_manila >= -3
_C826: - a_ij_5_5 - b_ij_1_5 - 2 d_ijk_1_5_fake_manila
 + e_ijlk_1_5_5_fake_manila >= -3
_C827: - a_ij_6_5 - b_ij_1_6 - d_ijk_1_5_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_5_6_fake_manila >= -3
_C828: a_ij_1_6 + 0.001 c_j_1 - 0.001 s_j_6 >= 0
_C829: b_ij_1_6 + 0.001 c_j_1 - 0.001 c_j_6 >= 0
_C83: z_ikt_1_fake_belem_25 + z_ikt_1_fake_manila_25 <= 1
_C830: d_ijk_1_6_fake_belem - x_ik_1_fake_belem - x_ik_6_fake_belem >= -1
_C831: - a_ij_1_6 - b_ij_1_1 - d_ijk_1_1_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_6_1_fake_belem >= -3
_C832: - a_ij_2_6 - b_ij_1_2 - d_ijk_1_2_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_6_2_fake_belem >= -3
_C833: - a_ij_3_6 - b_ij_1_3 - d_ijk_1_3_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_6_3_fake_belem >= -3
_C834: - a_ij_4_6 - b_ij_1_4 - d_ijk_1_4_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_6_4_fake_belem >= -3
_C835: - a_ij_5_6 - b_ij_1_5 - d_ijk_1_5_fake_belem - d_ijk_1_6_fake_belem
 + e_ijlk_1_6_5_fake_belem >= -3
_C836: - a_ij_6_6 - b_ij_1_6 - 2 d_ijk_1_6_fake_belem
 + e_ijlk_1_6_6_fake_belem >= -3
_C837: d_ijk_1_6_fake_manila - x_ik_1_fake_manila - x_ik_6_fake_manila >= -1
_C838: - a_ij_1_6 - b_ij_1_1 - d_ijk_1_1_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_6_1_fake_manila >= -3
_C839: - a_ij_2_6 - b_ij_1_2 - d_ijk_1_2_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_6_2_fake_manila >= -3
_C84: s_j_1 + 999975 z_ikt_1_fake_belem_25 + 999975 z_ikt_1_fake_manila_25
 <= 1000000
_C840: - a_ij_3_6 - b_ij_1_3 - d_ijk_1_3_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_6_3_fake_manila >= -3
_C841: - a_ij_4_6 - b_ij_1_4 - d_ijk_1_4_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_6_4_fake_manila >= -3
_C842: - a_ij_5_6 - b_ij_1_5 - d_ijk_1_5_fake_manila - d_ijk_1_6_fake_manila
 + e_ijlk_1_6_5_fake_manila >= -3
_C843: - a_ij_6_6 - b_ij_1_6 - 2 d_ijk_1_6_fake_manila
 + e_ijlk_1_6_6_fake_manila >= -3
_C844: a_ij_2_1 + 0.001 c_j_2 - 0.001 s_j_1 >= 0
_C845: b_ij_2_1 - 0.001 c_j_1 + 0.001 c_j_2 >= 0
_C846: d_ijk_2_1_fake_belem - x_ik_1_fake_belem - x_ik_2_fake_belem >= -1
_C847: - a_ij_1_1 - b_ij_2_1 - 2 d_ijk_2_1_fake_belem
 + e_ijlk_2_1_1_fake_belem >= -3
_C848: - a_ij_2_1 - b_ij_2_2 - d_ijk_2_1_fake_belem - d_ijk_2_2_fake_belem
 + e_ijlk_2_1_2_fake_belem >= -3
_C849: - a_ij_3_1 - b_ij_2_3 - d_ijk_2_1_fake_belem - d_ijk_2_3_fake_belem
 + e_ijlk_2_1_3_fake_belem >= -3
_C85: - c_j_1 + 26 z_ikt_1_fake_belem_26 + 26 z_ikt_1_fake_manila_26 <= 0
_C850: - a_ij_4_1 - b_ij_2_4 - d_ijk_2_1_fake_belem - d_ijk_2_4_fake_belem
 + e_ijlk_2_1_4_fake_belem >= -3
_C851: - a_ij_5_1 - b_ij_2_5 - d_ijk_2_1_fake_belem - d_ijk_2_5_fake_belem
 + e_ijlk_2_1_5_fake_belem >= -3
_C852: - a_ij_6_1 - b_ij_2_6 - d_ijk_2_1_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_1_6_fake_belem >= -3
_C853: d_ijk_2_1_fake_manila - x_ik_1_fake_manila - x_ik_2_fake_manila >= -1
_C854: - a_ij_1_1 - b_ij_2_1 - 2 d_ijk_2_1_fake_manila
 + e_ijlk_2_1_1_fake_manila >= -3
_C855: - a_ij_2_1 - b_ij_2_2 - d_ijk_2_1_fake_manila - d_ijk_2_2_fake_manila
 + e_ijlk_2_1_2_fake_manila >= -3
_C856: - a_ij_3_1 - b_ij_2_3 - d_ijk_2_1_fake_manila - d_ijk_2_3_fake_manila
 + e_ijlk_2_1_3_fake_manila >= -3
_C857: - a_ij_4_1 - b_ij_2_4 - d_ijk_2_1_fake_manila - d_ijk_2_4_fake_manila
 + e_ijlk_2_1_4_fake_manila >= -3
_C858: - a_ij_5_1 - b_ij_2_5 - d_ijk_2_1_fake_manila - d_ijk_2_5_fake_manila
 + e_ijlk_2_1_5_fake_manila >= -3
_C859: - a_ij_6_1 - b_ij_2_6 - d_ijk_2_1_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_1_6_fake_manila >= -3
_C86: z_ikt_1_fake_belem_26 + z_ikt_1_fake_manila_26 <= 1
_C860: a_ij_2_2 = 0
_C861: b_ij_2_2 = 0
_C862: a_ij_2_3 + 0.001 c_j_2 - 0.001 s_j_3 >= 0
_C863: b_ij_2_3 + 0.001 c_j_2 - 0.001 c_j_3 >= 0
_C864: d_ijk_2_3_fake_belem - x_ik_2_fake_belem - x_ik_3_fake_belem >= -1
_C865: - a_ij_1_3 - b_ij_2_1 - d_ijk_2_1_fake_belem - d_ijk_2_3_fake_belem
 + e_ijlk_2_3_1_fake_belem >= -3
_C866: - a_ij_2_3 - b_ij_2_2 - d_ijk_2_2_fake_belem - d_ijk_2_3_fake_belem
 + e_ijlk_2_3_2_fake_belem >= -3
_C867: - a_ij_3_3 - b_ij_2_3 - 2 d_ijk_2_3_fake_belem
 + e_ijlk_2_3_3_fake_belem >= -3
_C868: - a_ij_4_3 - b_ij_2_4 - d_ijk_2_3_fake_belem - d_ijk_2_4_fake_belem
 + e_ijlk_2_3_4_fake_belem >= -3
_C869: - a_ij_5_3 - b_ij_2_5 - d_ijk_2_3_fake_belem - d_ijk_2_5_fake_belem
 + e_ijlk_2_3_5_fake_belem >= -3
_C87: s_j_1 + 999974 z_ikt_1_fake_belem_26 + 999974 z_ikt_1_fake_manila_26
 <= 1000000
_C870: - a_ij_6_3 - b_ij_2_6 - d_ijk_2_3_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_3_6_fake_belem >= -3
_C871: d_ijk_2_3_fake_manila - x_ik_2_fake_manila - x_ik_3_fake_manila >= -1
_C872: - a_ij_1_3 - b_ij_2_1 - d_ijk_2_1_fake_manila - d_ijk_2_3_fake_manila
 + e_ijlk_2_3_1_fake_manila >= -3
_C873: - a_ij_2_3 - b_ij_2_2 - d_ijk_2_2_fake_manila - d_ijk_2_3_fake_manila
 + e_ijlk_2_3_2_fake_manila >= -3
_C874: - a_ij_3_3 - b_ij_2_3 - 2 d_ijk_2_3_fake_manila
 + e_ijlk_2_3_3_fake_manila >= -3
_C875: - a_ij_4_3 - b_ij_2_4 - d_ijk_2_3_fake_manila - d_ijk_2_4_fake_manila
 + e_ijlk_2_3_4_fake_manila >= -3
_C876: - a_ij_5_3 - b_ij_2_5 - d_ijk_2_3_fake_manila - d_ijk_2_5_fake_manila
 + e_ijlk_2_3_5_fake_manila >= -3
_C877: - a_ij_6_3 - b_ij_2_6 - d_ijk_2_3_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_3_6_fake_manila >= -3
_C878: a_ij_2_4 + 0.001 c_j_2 - 0.001 s_j_4 >= 0
_C879: b_ij_2_4 + 0.001 c_j_2 - 0.001 c_j_4 >= 0
_C88: - c_j_1 + 27 z_ikt_1_fake_belem_27 + 27 z_ikt_1_fake_manila_27 <= 0
_C880: d_ijk_2_4_fake_belem - x_ik_2_fake_belem - x_ik_4_fake_belem >= -1
_C881: - a_ij_1_4 - b_ij_2_1 - d_ijk_2_1_fake_belem - d_ijk_2_4_fake_belem
 + e_ijlk_2_4_1_fake_belem >= -3
_C882: - a_ij_2_4 - b_ij_2_2 - d_ijk_2_2_fake_belem - d_ijk_2_4_fake_belem
 + e_ijlk_2_4_2_fake_belem >= -3
_C883: - a_ij_3_4 - b_ij_2_3 - d_ijk_2_3_fake_belem - d_ijk_2_4_fake_belem
 + e_ijlk_2_4_3_fake_belem >= -3
_C884: - a_ij_4_4 - b_ij_2_4 - 2 d_ijk_2_4_fake_belem
 + e_ijlk_2_4_4_fake_belem >= -3
_C885: - a_ij_5_4 - b_ij_2_5 - d_ijk_2_4_fake_belem - d_ijk_2_5_fake_belem
 + e_ijlk_2_4_5_fake_belem >= -3
_C886: - a_ij_6_4 - b_ij_2_6 - d_ijk_2_4_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_4_6_fake_belem >= -3
_C887: d_ijk_2_4_fake_manila - x_ik_2_fake_manila - x_ik_4_fake_manila >= -1
_C888: - a_ij_1_4 - b_ij_2_1 - d_ijk_2_1_fake_manila - d_ijk_2_4_fake_manila
 + e_ijlk_2_4_1_fake_manila >= -3
_C889: - a_ij_2_4 - b_ij_2_2 - d_ijk_2_2_fake_manila - d_ijk_2_4_fake_manila
 + e_ijlk_2_4_2_fake_manila >= -3
_C89: z_ikt_1_fake_belem_27 + z_ikt_1_fake_manila_27 <= 1
_C890: - a_ij_3_4 - b_ij_2_3 - d_ijk_2_3_fake_manila - d_ijk_2_4_fake_manila
 + e_ijlk_2_4_3_fake_manila >= -3
_C891: - a_ij_4_4 - b_ij_2_4 - 2 d_ijk_2_4_fake_manila
 + e_ijlk_2_4_4_fake_manila >= -3
_C892: - a_ij_5_4 - b_ij_2_5 - d_ijk_2_4_fake_manila - d_ijk_2_5_fake_manila
 + e_ijlk_2_4_5_fake_manila >= -3
_C893: - a_ij_6_4 - b_ij_2_6 - d_ijk_2_4_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_4_6_fake_manila >= -3
_C894: a_ij_2_5 + 0.001 c_j_2 - 0.001 s_j_5 >= 0
_C895: b_ij_2_5 + 0.001 c_j_2 - 0.001 c_j_5 >= 0
_C896: d_ijk_2_5_fake_belem - x_ik_2_fake_belem - x_ik_5_fake_belem >= -1
_C897: - a_ij_1_5 - b_ij_2_1 - d_ijk_2_1_fake_belem - d_ijk_2_5_fake_belem
 + e_ijlk_2_5_1_fake_belem >= -3
_C898: - a_ij_2_5 - b_ij_2_2 - d_ijk_2_2_fake_belem - d_ijk_2_5_fake_belem
 + e_ijlk_2_5_2_fake_belem >= -3
_C899: - a_ij_3_5 - b_ij_2_3 - d_ijk_2_3_fake_belem - d_ijk_2_5_fake_belem
 + e_ijlk_2_5_3_fake_belem >= -3
_C9: s_j_1 + 1000000 z_ikt_1_fake_belem_0 + 1000000 z_ikt_1_fake_manila_0
 <= 1000000
_C90: s_j_1 + 999973 z_ikt_1_fake_belem_27 + 999973 z_ikt_1_fake_manila_27
 <= 1000000
_C900: - a_ij_4_5 - b_ij_2_4 - d_ijk_2_4_fake_belem - d_ijk_2_5_fake_belem
 + e_ijlk_2_5_4_fake_belem >= -3
_C901: - a_ij_5_5 - b_ij_2_5 - 2 d_ijk_2_5_fake_belem
 + e_ijlk_2_5_5_fake_belem >= -3
_C902: - a_ij_6_5 - b_ij_2_6 - d_ijk_2_5_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_5_6_fake_belem >= -3
_C903: d_ijk_2_5_fake_manila - x_ik_2_fake_manila - x_ik_5_fake_manila >= -1
_C904: - a_ij_1_5 - b_ij_2_1 - d_ijk_2_1_fake_manila - d_ijk_2_5_fake_manila
 + e_ijlk_2_5_1_fake_manila >= -3
_C905: - a_ij_2_5 - b_ij_2_2 - d_ijk_2_2_fake_manila - d_ijk_2_5_fake_manila
 + e_ijlk_2_5_2_fake_manila >= -3
_C906: - a_ij_3_5 - b_ij_2_3 - d_ijk_2_3_fake_manila - d_ijk_2_5_fake_manila
 + e_ijlk_2_5_3_fake_manila >= -3
_C907: - a_ij_4_5 - b_ij_2_4 - d_ijk_2_4_fake_manila - d_ijk_2_5_fake_manila
 + e_ijlk_2_5_4_fake_manila >= -3
_C908: - a_ij_5_5 - b_ij_2_5 - 2 d_ijk_2_5_fake_manila
 + e_ijlk_2_5_5_fake_manila >= -3
_C909: - a_ij_6_5 - b_ij_2_6 - d_ijk_2_5_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_5_6_fake_manila >= -3
_C91: - c_j_1 + 28 z_ikt_1_fake_belem_28 + 28 z_ikt_1_fake_manila_28 <= 0
_C910: a_ij_2_6 + 0.001 c_j_2 - 0.001 s_j_6 >= 0
_C911: b_ij_2_6 + 0.001 c_j_2 - 0.001 c_j_6 >= 0
_C912: d_ijk_2_6_fake_belem - x_ik_2_fake_belem - x_ik_6_fake_belem >= -1
_C913: - a_ij_1_6 - b_ij_2_1 - d_ijk_2_1_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_6_1_fake_belem >= -3
_C914: - a_ij_2_6 - b_ij_2_2 - d_ijk_2_2_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_6_2_fake_belem >= -3
_C915: - a_ij_3_6 - b_ij_2_3 - d_ijk_2_3_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_6_3_fake_belem >= -3
_C916: - a_ij_4_6 - b_ij_2_4 - d_ijk_2_4_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_6_4_fake_belem >= -3
_C917: - a_ij_5_6 - b_ij_2_5 - d_ijk_2_5_fake_belem - d_ijk_2_6_fake_belem
 + e_ijlk_2_6_5_fake_belem >= -3
_C918: - a_ij_6_6 - b_ij_2_6 - 2 d_ijk_2_6_fake_belem
 + e_ijlk_2_6_6_fake_belem >= -3
_C919: d_ijk_2_6_fake_manila - x_ik_2_fake_manila - x_ik_6_fake_manila >= -1
_C92: z_ikt_1_fake_belem_28 + z_ikt_1_fake_manila_28 <= 1
_C920: - a_ij_1_6 - b_ij_2_1 - d_ijk_2_1_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_6_1_fake_manila >= -3
_C921: - a_ij_2_6 - b_ij_2_2 - d_ijk_2_2_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_6_2_fake_manila >= -3
_C922: - a_ij_3_6 - b_ij_2_3 - d_ijk_2_3_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_6_3_fake_manila >= -3
_C923: - a_ij_4_6 - b_ij_2_4 - d_ijk_2_4_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_6_4_fake_manila >= -3
_C924: - a_ij_5_6 - b_ij_2_5 - d_ijk_2_5_fake_manila - d_ijk_2_6_fake_manila
 + e_ijlk_2_6_5_fake_manila >= -3
_C925: - a_ij_6_6 - b_ij_2_6 - 2 d_ijk_2_6_fake_manila
 + e_ijlk_2_6_6_fake_manila >= -3
_C926: a_ij_3_1 + 0.001 c_j_3 - 0.001 s_j_1 >= 0
_C927: b_ij_3_1 - 0.001 c_j_1 + 0.001 c_j_3 >= 0
_C928: d_ijk_3_1_fake_belem - x_ik_1_fake_belem - x_ik_3_fake_belem >= -1
_C929: - a_ij_1_1 - b_ij_3_1 - 2 d_ijk_3_1_fake_belem
 + e_ijlk_3_1_1_fake_belem >= -3
_C93: s_j_1 + 999972 z_ikt_1_fake_belem_28 + 999972 z_ikt_1_fake_manila_28
 <= 1000000
_C930: - a_ij_2_1 - b_ij_3_2 - d_ijk_3_1_fake_belem - d_ijk_3_2_fake_belem
 + e_ijlk_3_1_2_fake_belem >= -3
_C931: - a_ij_3_1 - b_ij_3_3 - d_ijk_3_1_fake_belem - d_ijk_3_3_fake_belem
 + e_ijlk_3_1_3_fake_belem >= -3
_C932: - a_ij_4_1 - b_ij_3_4 - d_ijk_3_1_fake_belem - d_ijk_3_4_fake_belem
 + e_ijlk_3_1_4_fake_belem >= -3
_C933: - a_ij_5_1 - b_ij_3_5 - d_ijk_3_1_fake_belem - d_ijk_3_5_fake_belem
 + e_ijlk_3_1_5_fake_belem >= -3
_C934: - a_ij_6_1 - b_ij_3_6 - d_ijk_3_1_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_1_6_fake_belem >= -3
_C935: d_ijk_3_1_fake_manila - x_ik_1_fake_manila - x_ik_3_fake_manila >= -1
_C936: - a_ij_1_1 - b_ij_3_1 - 2 d_ijk_3_1_fake_manila
 + e_ijlk_3_1_1_fake_manila >= -3
_C937: - a_ij_2_1 - b_ij_3_2 - d_ijk_3_1_fake_manila - d_ijk_3_2_fake_manila
 + e_ijlk_3_1_2_fake_manila >= -3
_C938: - a_ij_3_1 - b_ij_3_3 - d_ijk_3_1_fake_manila - d_ijk_3_3_fake_manila
 + e_ijlk_3_1_3_fake_manila >= -3
_C939: - a_ij_4_1 - b_ij_3_4 - d_ijk_3_1_fake_manila - d_ijk_3_4_fake_manila
 + e_ijlk_3_1_4_fake_manila >= -3
_C94: - c_j_1 + 29 z_ikt_1_fake_belem_29 + 29 z_ikt_1_fake_manila_29 <= 0
_C940: - a_ij_5_1 - b_ij_3_5 - d_ijk_3_1_fake_manila - d_ijk_3_5_fake_manila
 + e_ijlk_3_1_5_fake_manila >= -3
_C941: - a_ij_6_1 - b_ij_3_6 - d_ijk_3_1_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_1_6_fake_manila >= -3
_C942: a_ij_3_2 + 0.001 c_j_3 - 0.001 s_j_2 >= 0
_C943: b_ij_3_2 - 0.001 c_j_2 + 0.001 c_j_3 >= 0
_C944: d_ijk_3_2_fake_belem - x_ik_2_fake_belem - x_ik_3_fake_belem >= -1
_C945: - a_ij_1_2 - b_ij_3_1 - d_ijk_3_1_fake_belem - d_ijk_3_2_fake_belem
 + e_ijlk_3_2_1_fake_belem >= -3
_C946: - a_ij_2_2 - b_ij_3_2 - 2 d_ijk_3_2_fake_belem
 + e_ijlk_3_2_2_fake_belem >= -3
_C947: - a_ij_3_2 - b_ij_3_3 - d_ijk_3_2_fake_belem - d_ijk_3_3_fake_belem
 + e_ijlk_3_2_3_fake_belem >= -3
_C948: - a_ij_4_2 - b_ij_3_4 - d_ijk_3_2_fake_belem - d_ijk_3_4_fake_belem
 + e_ijlk_3_2_4_fake_belem >= -3
_C949: - a_ij_5_2 - b_ij_3_5 - d_ijk_3_2_fake_belem - d_ijk_3_5_fake_belem
 + e_ijlk_3_2_5_fake_belem >= -3
_C95: z_ikt_1_fake_belem_29 + z_ikt_1_fake_manila_29 <= 1
_C950: - a_ij_6_2 - b_ij_3_6 - d_ijk_3_2_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_2_6_fake_belem >= -3
_C951: d_ijk_3_2_fake_manila - x_ik_2_fake_manila - x_ik_3_fake_manila >= -1
_C952: - a_ij_1_2 - b_ij_3_1 - d_ijk_3_1_fake_manila - d_ijk_3_2_fake_manila
 + e_ijlk_3_2_1_fake_manila >= -3
_C953: - a_ij_2_2 - b_ij_3_2 - 2 d_ijk_3_2_fake_manila
 + e_ijlk_3_2_2_fake_manila >= -3
_C954: - a_ij_3_2 - b_ij_3_3 - d_ijk_3_2_fake_manila - d_ijk_3_3_fake_manila
 + e_ijlk_3_2_3_fake_manila >= -3
_C955: - a_ij_4_2 - b_ij_3_4 - d_ijk_3_2_fake_manila - d_ijk_3_4_fake_manila
 + e_ijlk_3_2_4_fake_manila >= -3
_C956: - a_ij_5_2 - b_ij_3_5 - d_ijk_3_2_fake_manila - d_ijk_3_5_fake_manila
 + e_ijlk_3_2_5_fake_manila >= -3
_C957: - a_ij_6_2 - b_ij_3_6 - d_ijk_3_2_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_2_6_fake_manila >= -3
_C958: a_ij_3_3 = 0
_C959: b_ij_3_3 = 0
_C96: s_j_1 + 999971 z_ikt_1_fake_belem_29 + 999971 z_ikt_1_fake_manila_29
 <= 1000000
_C960: a_ij_3_4 + 0.001 c_j_3 - 0.001 s_j_4 >= 0
_C961: b_ij_3_4 + 0.001 c_j_3 - 0.001 c_j_4 >= 0
_C962: d_ijk_3_4_fake_belem - x_ik_3_fake_belem - x_ik_4_fake_belem >= -1
_C963: - a_ij_1_4 - b_ij_3_1 - d_ijk_3_1_fake_belem - d_ijk_3_4_fake_belem
 + e_ijlk_3_4_1_fake_belem >= -3
_C964: - a_ij_2_4 - b_ij_3_2 - d_ijk_3_2_fake_belem - d_ijk_3_4_fake_belem
 + e_ijlk_3_4_2_fake_belem >= -3
_C965: - a_ij_3_4 - b_ij_3_3 - d_ijk_3_3_fake_belem - d_ijk_3_4_fake_belem
 + e_ijlk_3_4_3_fake_belem >= -3
_C966: - a_ij_4_4 - b_ij_3_4 - 2 d_ijk_3_4_fake_belem
 + e_ijlk_3_4_4_fake_belem >= -3
_C967: - a_ij_5_4 - b_ij_3_5 - d_ijk_3_4_fake_belem - d_ijk_3_5_fake_belem
 + e_ijlk_3_4_5_fake_belem >= -3
_C968: - a_ij_6_4 - b_ij_3_6 - d_ijk_3_4_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_4_6_fake_belem >= -3
_C969: d_ijk_3_4_fake_manila - x_ik_3_fake_manila - x_ik_4_fake_manila >= -1
_C97: - c_j_1 + 30 z_ikt_1_fake_belem_30 + 30 z_ikt_1_fake_manila_30 <= 0
_C970: - a_ij_1_4 - b_ij_3_1 - d_ijk_3_1_fake_manila - d_ijk_3_4_fake_manila
 + e_ijlk_3_4_1_fake_manila >= -3
_C971: - a_ij_2_4 - b_ij_3_2 - d_ijk_3_2_fake_manila - d_ijk_3_4_fake_manila
 + e_ijlk_3_4_2_fake_manila >= -3
_C972: - a_ij_3_4 - b_ij_3_3 - d_ijk_3_3_fake_manila - d_ijk_3_4_fake_manila
 + e_ijlk_3_4_3_fake_manila >= -3
_C973: - a_ij_4_4 - b_ij_3_4 - 2 d_ijk_3_4_fake_manila
 + e_ijlk_3_4_4_fake_manila >= -3
_C974: - a_ij_5_4 - b_ij_3_5 - d_ijk_3_4_fake_manila - d_ijk_3_5_fake_manila
 + e_ijlk_3_4_5_fake_manila >= -3
_C975: - a_ij_6_4 - b_ij_3_6 - d_ijk_3_4_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_4_6_fake_manila >= -3
_C976: a_ij_3_5 + 0.001 c_j_3 - 0.001 s_j_5 >= 0
_C977: b_ij_3_5 + 0.001 c_j_3 - 0.001 c_j_5 >= 0
_C978: d_ijk_3_5_fake_belem - x_ik_3_fake_belem - x_ik_5_fake_belem >= -1
_C979: - a_ij_1_5 - b_ij_3_1 - d_ijk_3_1_fake_belem - d_ijk_3_5_fake_belem
 + e_ijlk_3_5_1_fake_belem >= -3
_C98: z_ikt_1_fake_belem_30 + z_ikt_1_fake_manila_30 <= 1
_C980: - a_ij_2_5 - b_ij_3_2 - d_ijk_3_2_fake_belem - d_ijk_3_5_fake_belem
 + e_ijlk_3_5_2_fake_belem >= -3
_C981: - a_ij_3_5 - b_ij_3_3 - d_ijk_3_3_fake_belem - d_ijk_3_5_fake_belem
 + e_ijlk_3_5_3_fake_belem >= -3
_C982: - a_ij_4_5 - b_ij_3_4 - d_ijk_3_4_fake_belem - d_ijk_3_5_fake_belem
 + e_ijlk_3_5_4_fake_belem >= -3
_C983: - a_ij_5_5 - b_ij_3_5 - 2 d_ijk_3_5_fake_belem
 + e_ijlk_3_5_5_fake_belem >= -3
_C984: - a_ij_6_5 - b_ij_3_6 - d_ijk_3_5_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_5_6_fake_belem >= -3
_C985: d_ijk_3_5_fake_manila - x_ik_3_fake_manila - x_ik_5_fake_manila >= -1
_C986: - a_ij_1_5 - b_ij_3_1 - d_ijk_3_1_fake_manila - d_ijk_3_5_fake_manila
 + e_ijlk_3_5_1_fake_manila >= -3
_C987: - a_ij_2_5 - b_ij_3_2 - d_ijk_3_2_fake_manila - d_ijk_3_5_fake_manila
 + e_ijlk_3_5_2_fake_manila >= -3
_C988: - a_ij_3_5 - b_ij_3_3 - d_ijk_3_3_fake_manila - d_ijk_3_5_fake_manila
 + e_ijlk_3_5_3_fake_manila >= -3
_C989: - a_ij_4_5 - b_ij_3_4 - d_ijk_3_4_fake_manila - d_ijk_3_5_fake_manila
 + e_ijlk_3_5_4_fake_manila >= -3
_C99: s_j_1 + 999970 z_ikt_1_fake_belem_30 + 999970 z_ikt_1_fake_manila_30
 <= 1000000
_C990: - a_ij_5_5 - b_ij_3_5 - 2 d_ijk_3_5_fake_manila
 + e_ijlk_3_5_5_fake_manila >= -3
_C991: - a_ij_6_5 - b_ij_3_6 - d_ijk_3_5_fake_manila - d_ijk_3_6_fake_manila
 + e_ijlk_3_5_6_fake_manila >= -3
_C992: a_ij_3_6 + 0.001 c_j_3 - 0.001 s_j_6 >= 0
_C993: b_ij_3_6 + 0.001 c_j_3 - 0.001 c_j_6 >= 0
_C994: d_ijk_3_6_fake_belem - x_ik_3_fake_belem - x_ik_6_fake_belem >= -1
_C995: - a_ij_1_6 - b_ij_3_1 - d_ijk_3_1_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_6_1_fake_belem >= -3
_C996: - a_ij_2_6 - b_ij_3_2 - d_ijk_3_2_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_6_2_fake_belem >= -3
_C997: - a_ij_3_6 - b_ij_3_3 - d_ijk_3_3_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_6_3_fake_belem >= -3
_C998: - a_ij_4_6 - b_ij_3_4 - d_ijk_3_4_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_6_4_fake_belem >= -3
_C999: - a_ij_5_6 - b_ij_3_5 - d_ijk_3_5_fake_belem - d_ijk_3_6_fake_belem
 + e_ijlk_3_6_5_fake_belem >= -3
Binaries
a_ij_1_1
a_ij_1_2
a_ij_1_3
a_ij_1_4
a_ij_1_5
a_ij_1_6
a_ij_2_1
a_ij_2_2
a_ij_2_3
a_ij_2_4
a_ij_2_5
a_ij_2_6
a_ij_3_1
a_ij_3_2
a_ij_3_3
a_ij_3_4
a_ij_3_5
a_ij_3_6
a_ij_4_1
a_ij_4_2
a_ij_4_3
a_ij_4_4
a_ij_4_5
a_ij_4_6
a_ij_5_1
a_ij_5_2
a_ij_5_3
a_ij_5_4
a_ij_5_5
a_ij_5_6
a_ij_6_1
a_ij_6_2
a_ij_6_3
a_ij_6_4
a_ij_6_5
a_ij_6_6
b_ij_1_1
b_ij_1_2
b_ij_1_3
b_ij_1_4
b_ij_1_5
b_ij_1_6
b_ij_2_1
b_ij_2_2
b_ij_2_3
b_ij_2_4
b_ij_2_5
b_ij_2_6
b_ij_3_1
b_ij_3_2
b_ij_3_3
b_ij_3_4
b_ij_3_5
b_ij_3_6
b_ij_4_1
b_ij_4_2
b_ij_4_3
b_ij_4_4
b_ij_4_5
b_ij_4_6
b_ij_5_1
b_ij_5_2
b_ij_5_3
b_ij_5_4
b_ij_5_5
b_ij_5_6
b_ij_6_1
b_ij_6_2
b_ij_6_3
b_ij_6_4
b_ij_6_5
b_ij_6_6
d_ijk_1_1_fake_belem
d_ijk_1_1_fake_manila
d_ijk_1_2_fake_belem
d_ijk_1_2_fake_manila
d_ijk_1_3_fake_belem
d_ijk_1_3_fake_manila
d_ijk_1_4_fake_belem
d_ijk_1_4_fake_manila
d_ijk_1_5_fake_belem
d_ijk_1_5_fake_manila
d_ijk_1_6_fake_belem
d_ijk_1_6_fake_manila
d_ijk_2_1_fake_belem
d_ijk_2_1_fake_manila
d_ijk_2_2_fake_belem
d_ijk_2_2_fake_manila
d_ijk_2_3_fake_belem
d_ijk_2_3_fake_manila
d_ijk_2_4_fake_belem
d_ijk_2_4_fake_manila
d_ijk_2_5_fake_belem
d_ijk_2_5_fake_manila
d_ijk_2_6_fake_belem
d_ijk_2_6_fake_manila
d_ijk_3_1_fake_belem
d_ijk_3_1_fake_manila
d_ijk_3_2_fake_belem
d_ijk_3_2_fake_manila
d_ijk_3_3_fake_belem
d_ijk_3_3_fake_manila
d_ijk_3_4_fake_belem
d_ijk_3_4_fake_manila
d_ijk_3_5_fake_belem
d_ijk_3_5_fake_manila
d_ijk_3_6_fake_belem
d_ijk_3_6_fake_manila
d_ijk_4_1_fake_belem
d_ijk_4_1_fake_manila
d_ijk_4_2_fake_belem
d_ijk_4_2_fake_manila
d_ijk_4_3_fake_belem
d_ijk_4_3_fake_manila
d_ijk_4_4_fake_belem
d_ijk_4_4_fake_manila
d_ijk_4_5_fake_belem
d_ijk_4_5_fake_manila
d_ijk_4_6_fake_belem
d_ijk_4_6_fake_manila
d_ijk_5_1_fake_belem
d_ijk_5_1_fake_manila
d_ijk_5_2_fake_belem
d_ijk_5_2_fake_manila
d_ijk_5_3_fake_belem
d_ijk_5_3_fake_manila
d_ijk_5_4_fake_belem
d_ijk_5_4_fake_manila
d_ijk_5_5_fake_belem
d_ijk_5_5_fake_manila
d_ijk_5_6_fake_belem
d_ijk_5_6_fake_manila
d_ijk_6_1_fake_belem
d_ijk_6_1_fake_manila
d_ijk_6_2_fake_belem
d_ijk_6_2_fake_manila
d_ijk_6_3_fake_belem
d_ijk_6_3_fake_manila
d_ijk_6_4_fake_belem
d_ijk_6_4_fake_manila
d_ijk_6_5_fake_belem
d_ijk_6_5_fake_manila
d_ijk_6_6_fake_belem
d_ijk_6_6_fake_manila
e_ijlk_1_1_1_fake_belem
e_ijlk_1_1_1_fake_manila
e_ijlk_1_1_2_fake_belem
e_ijlk_1_1_2_fake_manila
e_ijlk_1_1_3_fake_belem
e_ijlk_1_1_3_fake_manila
e_ijlk_1_1_4_fake_belem
e_ijlk_1_1_4_fake_manila
e_ijlk_1_1_5_fake_belem
e_ijlk_1_1_5_fake_manila
e_ijlk_1_1_6_fake_belem
e_ijlk_1_1_6_fake_manila
e_ijlk_1_2_1_fake_belem
e_ijlk_1_2_1_fake_manila
e_ijlk_1_2_2_fake_belem
e_ijlk_1_2_2_fake_manila
e_ijlk_1_2_3_fake_belem
e_ijlk_1_2_3_fake_manila
e_ijlk_1_2_4_fake_belem
e_ijlk_1_2_4_fake_manila
e_ijlk_1_2_5_fake_belem
e_ijlk_1_2_5_fake_manila
e_ijlk_1_2_6_fake_belem
e_ijlk_1_2_6_fake_manila
e_ijlk_1_3_1_fake_belem
e_ijlk_1_3_1_fake_manila
e_ijlk_1_3_2_fake_belem
e_ijlk_1_3_2_fake_manila
e_ijlk_1_3_3_fake_belem
e_ijlk_1_3_3_fake_manila
e_ijlk_1_3_4_fake_belem
e_ijlk_1_3_4_fake_manila
e_ijlk_1_3_5_fake_belem
e_ijlk_1_3_5_fake_manila
e_ijlk_1_3_6_fake_belem
e_ijlk_1_3_6_fake_manila
e_ijlk_1_4_1_fake_belem
e_ijlk_1_4_1_fake_manila
e_ijlk_1_4_2_fake_belem
e_ijlk_1_4_2_fake_manila
e_ijlk_1_4_3_fake_belem
e_ijlk_1_4_3_fake_manila
e_ijlk_1_4_4_fake_belem
e_ijlk_1_4_4_fake_manila
e_ijlk_1_4_5_fake_belem
e_ijlk_1_4_5_fake_manila
e_ijlk_1_4_6_fake_belem
e_ijlk_1_4_6_fake_manila
e_ijlk_1_5_1_fake_belem
e_ijlk_1_5_1_fake_manila
e_ijlk_1_5_2_fake_belem
e_ijlk_1_5_2_fake_manila
e_ijlk_1_5_3_fake_belem
e_ijlk_1_5_3_fake_manila
e_ijlk_1_5_4_fake_belem
e_ijlk_1_5_4_fake_manila
e_ijlk_1_5_5_fake_belem
e_ijlk_1_5_5_fake_manila
e_ijlk_1_5_6_fake_belem
e_ijlk_1_5_6_fake_manila
e_ijlk_1_6_1_fake_belem
e_ijlk_1_6_1_fake_manila
e_ijlk_1_6_2_fake_belem
e_ijlk_1_6_2_fake_manila
e_ijlk_1_6_3_fake_belem
e_ijlk_1_6_3_fake_manila
e_ijlk_1_6_4_fake_belem
e_ijlk_1_6_4_fake_manila
e_ijlk_1_6_5_fake_belem
e_ijlk_1_6_5_fake_manila
e_ijlk_1_6_6_fake_belem
e_ijlk_1_6_6_fake_manila
e_ijlk_2_1_1_fake_belem
e_ijlk_2_1_1_fake_manila
e_ijlk_2_1_2_fake_belem
e_ijlk_2_1_2_fake_manila
e_ijlk_2_1_3_fake_belem
e_ijlk_2_1_3_fake_manila
e_ijlk_2_1_4_fake_belem
e_ijlk_2_1_4_fake_manila
e_ijlk_2_1_5_fake_belem
e_ijlk_2_1_5_fake_manila
e_ijlk_2_1_6_fake_belem
e_ijlk_2_1_6_fake_manila
e_ijlk_2_2_1_fake_belem
e_ijlk_2_2_1_fake_manila
e_ijlk_2_2_2_fake_belem
e_ijlk_2_2_2_fake_manila
e_ijlk_2_2_3_fake_belem
e_ijlk_2_2_3_fake_manila
e_ijlk_2_2_4_fake_belem
e_ijlk_2_2_4_fake_manila
e_ijlk_2_2_5_fake_belem
e_ijlk_2_2_5_fake_manila
e_ijlk_2_2_6_fake_belem
e_ijlk_2_2_6_fake_manila
e_ijlk_2_3_1_fake_belem
e_ijlk_2_3_1_fake_manila
e_ijlk_2_3_2_fake_belem
e_ijlk_2_3_2_fake_manila
e_ijlk_2_3_3_fake_belem
e_ijlk_2_3_3_fake_manila
e_ijlk_2_3_4_fake_belem
e_ijlk_2_3_4_fake_manila
e_ijlk_2_3_5_fake_belem
e_ijlk_2_3_5_fake_manila
e_ijlk_2_3_6_fake_belem
e_ijlk_2_3_6_fake_manila
e_ijlk_2_4_1_fake_belem
e_ijlk_2_4_1_fake_manila
e_ijlk_2_4_2_fake_belem
e_ijlk_2_4_2_fake_manila
e_ijlk_2_4_3_fake_belem
e_ijlk_2_4_3_fake_manila
e_ijlk_2_4_4_fake_belem
e_ijlk_2_4_4_fake_manila
e_ijlk_2_4_5_fake_belem
e_ijlk_2_4_5_fake_manila
e_ijlk_2_4_6_fake_belem
e_ijlk_2_4_6_fake_manila
e_ijlk_2_5_1_fake_belem
e_ijlk_2_5_1_fake_manila
e_ijlk_2_5_2_fake_belem
e_ijlk_2_5_2_fake_manila
e_ijlk_2_5_3_fake_belem
e_ijlk_2_5_3_fake_manila
e_ijlk_2_5_4_fake_belem
e_ijlk_2_5_4_fake_manila
e_ijlk_2_5_5_fake_belem
e_ijlk_2_5_5_fake_manila
e_ijlk_2_5_6_fake_belem
e_ijlk_2_5_6_fake_manila
e_ijlk_2_6_1_fake_belem
e_ijlk_2_6_1_fake_manila
e_ijlk_2_6_2_fake_belem
e_ijlk_2_6_2_fake_manila
e_ijlk_2_6_3_fake_belem
e_ijlk_2_6_3_fake_manila
e_ijlk_2_6_4_fake_belem
e_ijlk_2_6_4_fake_manila
e_ijlk_2_6_5_fake_belem
e_ijlk_2_6_5_fake_manila
e_ijlk_2_6_6_fake_belem
e_ijlk_2_6_6_fake_manila
e_ijlk_3_1_1_fake_belem
e_ijlk_3_1_1_fake_manila
e_ijlk_3_1_2_fake_belem
e_ijlk_3_1_2_fake_manila
e_ijlk_3_1_3_fake_belem
e_ijlk_3_1_3_fake_manila
e_ijlk_3_1_4_fake_belem
e_ijlk_3_1_4_fake_manila
e_ijlk_3_1_5_fake_belem
e_ijlk_3_1_5_fake_manila
e_ijlk_3_1_6_fake_belem
e_ijlk_3_1_6_fake_manila
e_ijlk_3_2_1_fake_belem
e_ijlk_3_2_1_fake_manila
e_ijlk_3_2_2_fake_belem
e_ijlk_3_2_2_fake_manila
e_ijlk_3_2_3_fake_belem
e_ijlk_3_2_3_fake_manila
e_ijlk_3_2_4_fake_belem
e_ijlk_3_2_4_fake_manila
e_ijlk_3_2_5_fake_belem
e_ijlk_3_2_5_fake_manila
e_ijlk_3_2_6_fake_belem
e_ijlk_3_2_6_fake_manila
e_ijlk_3_3_1_fake_belem
e_ijlk_3_3_1_fake_manila
e_ijlk_3_3_2_fake_belem
e_ijlk_3_3_2_fake_manila
e_ijlk_3_3_3_fake_belem
e_ijlk_3_3_3_fake_manila
e_ijlk_3_3_4_fake_belem
e_ijlk_3_3_4_fake_manila
e_ijlk_3_3_5_fake_belem
e_ijlk_3_3_5_fake_manila
e_ijlk_3_3_6_fake_belem
e_ijlk_3_3_6_fake_manila
e_ijlk_3_4_1_fake_belem
e_ijlk_3_4_1_fake_manila
e_ijlk_3_4_2_fake_belem
e_ijlk_3_4_2_fake_manila
e_ijlk_3_4_3_fake_belem
e_ijlk_3_4_3_fake_manila
e_ijlk_3_4_4_fake_belem
e_ijlk_3_4_4_fake_manila
e_ijlk_3_4_5_fake_belem
e_ijlk_3_4_5_fake_manila
e_ijlk_3_4_6_fake_belem
e_ijlk_3_4_6_fake_manila
e_ijlk_3_5_1_fake_belem
e_ijlk_3_5_1_fake_manila
e_ijlk_3_5_2_fake_belem
e_ijlk_3_5_2_fake_manila
e_ijlk_3_5_3_fake_belem
e_ijlk_3_5_3_fake_manila
e_ijlk_3_5_4_fake_belem
e_ijlk_3_5_4_fake_manila
e_ijlk_3_5_5_fake_belem
e_ijlk_3_5_5_fake_manila
e_ijlk_3_5_6_fake_belem
e_ijlk_3_5_6_fake_manila
e_ijlk_3_6_1_fake_belem
e_ijlk_3_6_1_fake_manila
e_ijlk_3_6_2_fake_belem
e_ijlk_3_6_2_fake_manila
e_ijlk_3_6_3_fake_belem
e_ijlk_3_6_3_fake_manila
e_ijlk_3_6_4_fake_belem
e_ijlk_3_6_4_fake_manila
e_ijlk_3_6_5_fake_belem
e_ijlk_3_6_5_fake_manila
e_ijlk_3_6_6_fake_belem
e_ijlk_3_6_6_fake_manila
e_ijlk_4_1_1_fake_belem
e_ijlk_4_1_1_fake_manila
e_ijlk_4_1_2_fake_belem
e_ijlk_4_1_2_fake_manila
e_ijlk_4_1_3_fake_belem
e_ijlk_4_1_3_fake_manila
e_ijlk_4_1_4_fake_belem
e_ijlk_4_1_4_fake_manila
e_ijlk_4_1_5_fake_belem
e_ijlk_4_1_5_fake_manila
e_ijlk_4_1_6_fake_belem
e_ijlk_4_1_6_fake_manila
e_ijlk_4_2_1_fake_belem
e_ijlk_4_2_1_fake_manila
e_ijlk_4_2_2_fake_belem
e_ijlk_4_2_2_fake_manila
e_ijlk_4_2_3_fake_belem
e_ijlk_4_2_3_fake_manila
e_ijlk_4_2_4_fake_belem
e_ijlk_4_2_4_fake_manila
e_ijlk_4_2_5_fake_belem
e_ijlk_4_2_5_fake_manila
e_ijlk_4_2_6_fake_belem
e_ijlk_4_2_6_fake_manila
e_ijlk_4_3_1_fake_belem
e_ijlk_4_3_1_fake_manila
e_ijlk_4_3_2_fake_belem
e_ijlk_4_3_2_fake_manila
e_ijlk_4_3_3_fake_belem
e_ijlk_4_3_3_fake_manila
e_ijlk_4_3_4_fake_belem
e_ijlk_4_3_4_fake_manila
e_ijlk_4_3_5_fake_belem
e_ijlk_4_3_5_fake_manila
e_ijlk_4_3_6_fake_belem
e_ijlk_4_3_6_fake_manila
e_ijlk_4_4_1_fake_belem
e_ijlk_4_4_1_fake_manila
e_ijlk_4_4_2_fake_belem
e_ijlk_4_4_2_fake_manila
e_ijlk_4_4_3_fake_belem
e_ijlk_4_4_3_fake_manila
e_ijlk_4_4_4_fake_belem
e_ijlk_4_4_4_fake_manila
e_ijlk_4_4_5_fake_belem
e_ijlk_4_4_5_fake_manila
e_ijlk_4_4_6_fake_belem
e_ijlk_4_4_6_fake_manila
e_ijlk_4_5_1_fake_belem
e_ijlk_4_5_1_fake_manila
e_ijlk_4_5_2_fake_belem
e_ijlk_4_5_2_fake_manila
e_ijlk_4_5_3_fake_belem
e_ijlk_4_5_3_fake_manila
e_ijlk_4_5_4_fake_belem
e_ijlk_4_5_4_fake_manila
e_ijlk_4_5_5_fake_belem
e_ijlk_4_5_5_fake_manila
e_ijlk_4_5_6_fake_belem
e_ijlk_4_5_6_fake_manila
e_ijlk_4_6_1_fake_belem
e_ijlk_4_6_1_fake_manila
e_ijlk_4_6_2_fake_belem
e_ijlk_4_6_2_fake_manila
e_ijlk_4_6_3_fake_belem
e_ijlk_4_6_3_fake_manila
e_ijlk_4_6_4_fake_belem
e_ijlk_4_6_4_fake_manila
e_ijlk_4_6_5_fake_belem
e_ijlk_4_6_5_fake_manila
e_ijlk_4_6_6_fake_belem
e_ijlk_4_6_6_fake_manila
e_ijlk_5_1_1_fake_belem
e_ijlk_5_1_1_fake_manila
e_ijlk_5_1_2_fake_belem
e_ijlk_5_1_2_fake_manila
e_ijlk_5_1_3_fake_belem
e_ijlk_5_1_3_fake_manila
e_ijlk_5_1_4_fake_belem
e_ijlk_5_1_4_fake_manila
e_ijlk_5_1_5_fake_belem
e_ijlk_5_1_5_fake_manila
e_ijlk_5_1_6_fake_belem
e_ijlk_5_1_6_fake_manila
e_ijlk_5_2_1_fake_belem
e_ijlk_5_2_1_fake_manila
e_ijlk_5_2_2_fake_belem
e_ijlk_5_2_2_fake_manila
e_ijlk_5_2_3_fake_belem
e_ijlk_5_2_3_fake_manila
e_ijlk_5_2_4_fake_belem
e_ijlk_5_2_4_fake_manila
e_ijlk_5_2_5_fake_belem
e_ijlk_5_2_5_fake_manila
e_ijlk_5_2_6_fake_belem
e_ijlk_5_2_6_fake_manila
e_ijlk_5_3_1_fake_belem
e_ijlk_5_3_1_fake_manila
e_ijlk_5_3_2_fake_belem
e_ijlk_5_3_2_fake_manila
e_ijlk_5_3_3_fake_belem
e_ijlk_5_3_3_fake_manila
e_ijlk_5_3_4_fake_belem
e_ijlk_5_3_4_fake_manila
e_ijlk_5_3_5_fake_belem
e_ijlk_5_3_5_fake_manila
e_ijlk_5_3_6_fake_belem
e_ijlk_5_3_6_fake_manila
e_ijlk_5_4_1_fake_belem
e_ijlk_5_4_1_fake_manila
e_ijlk_5_4_2_fake_belem
e_ijlk_5_4_2_fake_manila
e_ijlk_5_4_3_fake_belem
e_ijlk_5_4_3_fake_manila
e_ijlk_5_4_4_fake_belem
e_ijlk_5_4_4_fake_manila
e_ijlk_5_4_5_fake_belem
e_ijlk_5_4_5_fake_manila
e_ijlk_5_4_6_fake_belem
e_ijlk_5_4_6_fake_manila
e_ijlk_5_5_1_fake_belem
e_ijlk_5_5_1_fake_manila
e_ijlk_5_5_2_fake_belem
e_ijlk_5_5_2_fake_manila
e_ijlk_5_5_3_fake_belem
e_ijlk_5_5_3_fake_manila
e_ijlk_5_5_4_fake_belem
e_ijlk_5_5_4_fake_manila
e_ijlk_5_5_5_fake_belem
e_ijlk_5_5_5_fake_manila
e_ijlk_5_5_6_fake_belem
e_ijlk_5_5_6_fake_manila
e_ijlk_5_6_1_fake_belem
e_ijlk_5_6_1_fake_manila
e_ijlk_5_6_2_fake_belem
e_ijlk_5_6_2_fake_manila
e_ijlk_5_6_3_fake_belem
e_ijlk_5_6_3_fake_manila
e_ijlk_5_6_4_fake_belem
e_ijlk_5_6_4_fake_manila
e_ijlk_5_6_5_fake_belem
e_ijlk_5_6_5_fake_manila
e_ijlk_5_6_6_fake_belem
e_ijlk_5_6_6_fake_manila
e_ijlk_6_1_1_fake_belem
e_ijlk_6_1_1_fake_manila
e_ijlk_6_1_2_fake_belem
e_ijlk_6_1_2_fake_manila
e_ijlk_6_1_3_fake_belem
e_ijlk_6_1_3_fake_manila
e_ijlk_6_1_4_fake_belem
e_ijlk_6_1_4_fake_manila
e_ijlk_6_1_5_fake_belem
e_ijlk_6_1_5_fake_manila
e_ijlk_6_1_6_fake_belem
e_ijlk_6_1_6_fake_manila
e_ijlk_6_2_1_fake_belem
e_ijlk_6_2_1_fake_manila
e_ijlk_6_2_2_fake_belem
e_ijlk_6_2_2_fake_manila
e_ijlk_6_2_3_fake_belem
e_ijlk_6_2_3_fake_manila
e_ijlk_6_2_4_fake_belem
e_ijlk_6_2_4_fake_manila
e_ijlk_6_2_5_fake_belem
e_ijlk_6_2_5_fake_manila
e_ijlk_6_2_6_fake_belem
e_ijlk_6_2_6_fake_manila
e_ijlk_6_3_1_fake_belem
e_ijlk_6_3_1_fake_manila
e_ijlk_6_3_2_fake_belem
e_ijlk_6_3_2_fake_manila
e_ijlk_6_3_3_fake_belem
e_ijlk_6_3_3_fake_manila
e_ijlk_6_3_4_fake_belem
e_ijlk_6_3_4_fake_manila
e_ijlk_6_3_5_fake_belem
e_ijlk_6_3_5_fake_manila
e_ijlk_6_3_6_fake_belem
e_ijlk_6_3_6_fake_manila
e_ijlk_6_4_1_fake_belem
e_ijlk_6_4_1_fake_manila
e_ijlk_6_4_2_fake_belem
e_ijlk_6_4_2_fake_manila
e_ijlk_6_4_3_fake_belem
e_ijlk_6_4_3_fake_manila
e_ijlk_6_4_4_fake_belem
e_ijlk_6_4_4_fake_manila
e_ijlk_6_4_5_fake_belem
e_ijlk_6_4_5_fake_manila
e_ijlk_6_4_6_fake_belem
e_ijlk_6_4_6_fake_manila
e_ijlk_6_5_1_fake_belem
e_ijlk_6_5_1_fake_manila
e_ijlk_6_5_2_fake_belem
e_ijlk_6_5_2_fake_manila
e_ijlk_6_5_3_fake_belem
e_ijlk_6_5_3_fake_manila
e_ijlk_6_5_4_fake_belem
e_ijlk_6_5_4_fake_manila
e_ijlk_6_5_5_fake_belem
e_ijlk_6_5_5_fake_manila
e_ijlk_6_5_6_fake_belem
e_ijlk_6_5_6_fake_manila
e_ijlk_6_6_1_fake_belem
e_ijlk_6_6_1_fake_manila
e_ijlk_6_6_2_fake_belem
e_ijlk_6_6_2_fake_manila
e_ijlk_6_6_3_fake_belem
e_ijlk_6_6_3_fake_manila
e_ijlk_6_6_4_fake_belem
e_ijlk_6_6_4_fake_manila
e_ijlk_6_6_5_fake_belem
e_ijlk_6_6_5_fake_manila
e_ijlk_6_6_6_fake_belem
e_ijlk_6_6_6_fake_manila
x_ik_1_fake_belem
x_ik_1_fake_manila
x_ik_2_fake_belem
x_ik_2_fake_manila
x_ik_3_fake_belem
x_ik_3_fake_manila
x_ik_4_fake_belem
x_ik_4_fake_manila
x_ik_5_fake_belem
x_ik_5_fake_manila
x_ik_6_fake_belem
x_ik_6_fake_manila
y_ijk_0_1_fake_belem
y_ijk_0_1_fake_manila
y_ijk_0_2_fake_belem
y_ijk_0_2_fake_manila
y_ijk_0_3_fake_belem
y_ijk_0_3_fake_manila
y_ijk_0_4_fake_belem
y_ijk_0_4_fake_manila
y_ijk_0_5_fake_belem
y_ijk_0_5_fake_manila
y_ijk_0_6_fake_belem
y_ijk_0_6_fake_manila
y_ijk_1_0_fake_belem
y_ijk_1_0_fake_manila
y_ijk_1_1_fake_belem
y_ijk_1_1_fake_manila
y_ijk_1_2_fake_belem
y_ijk_1_2_fake_manila
y_ijk_1_3_fake_belem
y_ijk_1_3_fake_manila
y_ijk_1_4_fake_belem
y_ijk_1_4_fake_manila
y_ijk_1_5_fake_belem
y_ijk_1_5_fake_manila
y_ijk_1_6_fake_belem
y_ijk_1_6_fake_manila
y_ijk_2_0_fake_belem
y_ijk_2_0_fake_manila
y_ijk_2_1_fake_belem
y_ijk_2_1_fake_manila
y_ijk_2_2_fake_belem
y_ijk_2_2_fake_manila
y_ijk_2_3_fake_belem
y_ijk_2_3_fake_manila
y_ijk_2_4_fake_belem
y_ijk_2_4_fake_manila
y_ijk_2_5_fake_belem
y_ijk_2_5_fake_manila
y_ijk_2_6_fake_belem
y_ijk_2_6_fake_manila
y_ijk_3_0_fake_belem
y_ijk_3_0_fake_manila
y_ijk_3_1_fake_belem
y_ijk_3_1_fake_manila
y_ijk_3_2_fake_belem
y_ijk_3_2_fake_manila
y_ijk_3_3_fake_belem
y_ijk_3_3_fake_manila
y_ijk_3_4_fake_belem
y_ijk_3_4_fake_manila
y_ijk_3_5_fake_belem
y_ijk_3_5_fake_manila
y_ijk_3_6_fake_belem
y_ijk_3_6_fake_manila
y_ijk_4_0_fake_belem
y_ijk_4_0_fake_manila
y_ijk_4_1_fake_belem
y_ijk_4_1_fake_manila
y_ijk_4_2_fake_belem
y_ijk_4_2_fake_manila
y_ijk_4_3_fake_belem
y_ijk_4_3_fake_manila
y_ijk_4_4_fake_belem
y_ijk_4_4_fake_manila
y_ijk_4_5_fake_belem
y_ijk_4_5_fake_manila
y_ijk_4_6_fake_belem
y_ijk_4_6_fake_manila
y_ijk_5_0_fake_belem
y_ijk_5_0_fake_manila
y_ijk_5_1_fake_belem
y_ijk_5_1_fake_manila
y_ijk_5_2_fake_belem
y_ijk_5_2_fake_manila
y_ijk_5_3_fake_belem
y_ijk_5_3_fake_manila
y_ijk_5_4_fake_belem
y_ijk_5_4_fake_manila
y_ijk_5_5_fake_belem
y_ijk_5_5_fake_manila
y_ijk_5_6_fake_belem
y_ijk_5_6_fake_manila
y_ijk_6_0_fake_belem
y_ijk_6_0_fake_manila
y_ijk_6_1_fake_belem
y_ijk_6_1_fake_manila
y_ijk_6_2_fake_belem
y_ijk_6_2_fake_manila
y_ijk_6_3_fake_belem
y_ijk_6_3_fake_manila
y_ijk_6_4_fake_belem
y_ijk_6_4_fake_manila
y_ijk_6_5_fake_belem
y_ijk_6_5_fake_manila
y_ijk_6_6_fake_belem
y_ijk_6_6_fake_manila
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
z_ikt_4_fake_belem_0
z_ikt_4_fake_belem_1
z_ikt_4_fake_belem_10
z_ikt_4_fake_belem_11
z_ikt_4_fake_belem_12
z_ikt_4_fake_belem_13
z_ikt_4_fake_belem_14
z_ikt_4_fake_belem_15
z_ikt_4_fake_belem_16
z_ikt_4_fake_belem_17
z_ikt_4_fake_belem_18
z_ikt_4_fake_belem_19
z_ikt_4_fake_belem_2
z_ikt_4_fake_belem_20
z_ikt_4_fake_belem_21
z_ikt_4_fake_belem_22
z_ikt_4_fake_belem_23
z_ikt_4_fake_belem_24
z_ikt_4_fake_belem_25
z_ikt_4_fake_belem_26
z_ikt_4_fake_belem_27
z_ikt_4_fake_belem_28
z_ikt_4_fake_belem_29
z_ikt_4_fake_belem_3
z_ikt_4_fake_belem_30
z_ikt_4_fake_belem_31
z_ikt_4_fake_belem_4
z_ikt_4_fake_belem_5
z_ikt_4_fake_belem_6
z_ikt_4_fake_belem_7
z_ikt_4_fake_belem_8
z_ikt_4_fake_belem_9
z_ikt_4_fake_manila_0
z_ikt_4_fake_manila_1
z_ikt_4_fake_manila_10
z_ikt_4_fake_manila_11
z_ikt_4_fake_manila_12
z_ikt_4_fake_manila_13
z_ikt_4_fake_manila_14
z_ikt_4_fake_manila_15
z_ikt_4_fake_manila_16
z_ikt_4_fake_manila_17
z_ikt_4_fake_manila_18
z_ikt_4_fake_manila_19
z_ikt_4_fake_manila_2
z_ikt_4_fake_manila_20
z_ikt_4_fake_manila_21
z_ikt_4_fake_manila_22
z_ikt_4_fake_manila_23
z_ikt_4_fake_manila_24
z_ikt_4_fake_manila_25
z_ikt_4_fake_manila_26
z_ikt_4_fake_manila_27
z_ikt_4_fake_manila_28
z_ikt_4_fake_manila_29
z_ikt_4_fake_manila_3
z_ikt_4_fake_manila_30
z_ikt_4_fake_manila_31
z_ikt_4_fake_manila_4
z_ikt_4_fake_manila_5
z_ikt_4_fake_manila_6
z_ikt_4_fake_manila_7
z_ikt_4_fake_manila_8
z_ikt_4_fake_manila_9
z_ikt_5_fake_belem_0
z_ikt_5_fake_belem_1
z_ikt_5_fake_belem_10
z_ikt_5_fake_belem_11
z_ikt_5_fake_belem_12
z_ikt_5_fake_belem_13
z_ikt_5_fake_belem_14
z_ikt_5_fake_belem_15
z_ikt_5_fake_belem_16
z_ikt_5_fake_belem_17
z_ikt_5_fake_belem_18
z_ikt_5_fake_belem_19
z_ikt_5_fake_belem_2
z_ikt_5_fake_belem_20
z_ikt_5_fake_belem_21
z_ikt_5_fake_belem_22
z_ikt_5_fake_belem_23
z_ikt_5_fake_belem_24
z_ikt_5_fake_belem_25
z_ikt_5_fake_belem_26
z_ikt_5_fake_belem_27
z_ikt_5_fake_belem_28
z_ikt_5_fake_belem_29
z_ikt_5_fake_belem_3
z_ikt_5_fake_belem_30
z_ikt_5_fake_belem_31
z_ikt_5_fake_belem_4
z_ikt_5_fake_belem_5
z_ikt_5_fake_belem_6
z_ikt_5_fake_belem_7
z_ikt_5_fake_belem_8
z_ikt_5_fake_belem_9
z_ikt_5_fake_manila_0
z_ikt_5_fake_manila_1
z_ikt_5_fake_manila_10
z_ikt_5_fake_manila_11
z_ikt_5_fake_manila_12
z_ikt_5_fake_manila_13
z_ikt_5_fake_manila_14
z_ikt_5_fake_manila_15
z_ikt_5_fake_manila_16
z_ikt_5_fake_manila_17
z_ikt_5_fake_manila_18
z_ikt_5_fake_manila_19
z_ikt_5_fake_manila_2
z_ikt_5_fake_manila_20
z_ikt_5_fake_manila_21
z_ikt_5_fake_manila_22
z_ikt_5_fake_manila_23
z_ikt_5_fake_manila_24
z_ikt_5_fake_manila_25
z_ikt_5_fake_manila_26
z_ikt_5_fake_manila_27
z_ikt_5_fake_manila_28
z_ikt_5_fake_manila_29
z_ikt_5_fake_manila_3
z_ikt_5_fake_manila_30
z_ikt_5_fake_manila_31
z_ikt_5_fake_manila_4
z_ikt_5_fake_manila_5
z_ikt_5_fake_manila_6
z_ikt_5_fake_manila_7
z_ikt_5_fake_manila_8
z_ikt_5_fake_manila_9
z_ikt_6_fake_belem_0
z_ikt_6_fake_belem_1
z_ikt_6_fake_belem_10
z_ikt_6_fake_belem_11
z_ikt_6_fake_belem_12
z_ikt_6_fake_belem_13
z_ikt_6_fake_belem_14
z_ikt_6_fake_belem_15
z_ikt_6_fake_belem_16
z_ikt_6_fake_belem_17
z_ikt_6_fake_belem_18
z_ikt_6_fake_belem_19
z_ikt_6_fake_belem_2
z_ikt_6_fake_belem_20
z_ikt_6_fake_belem_21
z_ikt_6_fake_belem_22
z_ikt_6_fake_belem_23
z_ikt_6_fake_belem_24
z_ikt_6_fake_belem_25
z_ikt_6_fake_belem_26
z_ikt_6_fake_belem_27
z_ikt_6_fake_belem_28
z_ikt_6_fake_belem_29
z_ikt_6_fake_belem_3
z_ikt_6_fake_belem_30
z_ikt_6_fake_belem_31
z_ikt_6_fake_belem_4
z_ikt_6_fake_belem_5
z_ikt_6_fake_belem_6
z_ikt_6_fake_belem_7
z_ikt_6_fake_belem_8
z_ikt_6_fake_belem_9
z_ikt_6_fake_manila_0
z_ikt_6_fake_manila_1
z_ikt_6_fake_manila_10
z_ikt_6_fake_manila_11
z_ikt_6_fake_manila_12
z_ikt_6_fake_manila_13
z_ikt_6_fake_manila_14
z_ikt_6_fake_manila_15
z_ikt_6_fake_manila_16
z_ikt_6_fake_manila_17
z_ikt_6_fake_manila_18
z_ikt_6_fake_manila_19
z_ikt_6_fake_manila_2
z_ikt_6_fake_manila_20
z_ikt_6_fake_manila_21
z_ikt_6_fake_manila_22
z_ikt_6_fake_manila_23
z_ikt_6_fake_manila_24
z_ikt_6_fake_manila_25
z_ikt_6_fake_manila_26
z_ikt_6_fake_manila_27
z_ikt_6_fake_manila_28
z_ikt_6_fake_manila_29
z_ikt_6_fake_manila_3
z_ikt_6_fake_manila_30
z_ikt_6_fake_manila_31
z_ikt_6_fake_manila_4
z_ikt_6_fake_manila_5
z_ikt_6_fake_manila_6
z_ikt_6_fake_manila_7
z_ikt_6_fake_manila_8
z_ikt_6_fake_manila_9
End
