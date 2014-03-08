# -*- coding: utf-8 -*-

"""Mappings between the ordering of PyFR nodes, and those of external formats

"""
import numpy as np


class GmshNodeMaps(object):
    """Mappings between the node ordering of PyFR and that of Gmsh

    Node mappings are contained within two dictionaries; one maps from
    Gmsh node ordering to PyFR, and the other provides the inverse.
    Dictionary items are keyed by a tuple of element type (string) and
    number of solution points per element (integer).

    Each dictionary value is a list of integers that provide mappings
    via their list index. When lists in the "gmsh_to_pyfr" dictionary
    are indexed using the Gmsh node number, they return the equivalent
    PyFR node number.  The reverse is true for the "pyfr_to_gmsh"
    dictionary.

    :Example: Convert Gmsh node number 4, in a 64 point hexahedra, to
              the equivalent node number in PyFR:

    >>> from pyfr.readers.nodemaps import GmshNodeMaps
    >>> GmshNodeMaps.gmsh_to_pyfr['hex', 64][4]
    >>> 48
    """
    to_pyfr = {
        ('tet', 4): np.array([0, 1, 2, 3]),
        ('tet', 10): np.array([0, 2, 5, 9, 1, 4, 3, 6, 8, 7]),
        ('tet', 20): np.array([0, 3, 9, 19, 1, 2, 6, 8, 7, 4, 16, 10, 18, 15,
                               17, 12, 5, 11, 13, 14]),
        ('tet', 35): np.array([0, 4, 14, 34, 1, 2, 3, 8, 11, 13, 12, 9, 5, 31,
                               25, 15, 33, 30, 24, 32, 27, 18, 6, 10, 7, 16,
                               17, 26, 19, 28, 22, 29, 21, 23, 20]),
        ('tet', 56): np.array([0, 5, 20, 55, 1, 2, 3, 4, 10, 14, 17, 19, 18,
                               15, 11, 6, 52, 46, 36, 21, 54, 51, 45, 35, 53,
                               48, 39, 25, 7, 16, 9, 12, 13, 8, 22, 24, 47,
                               23, 38, 37, 26, 49, 33, 40, 43, 30, 50, 29, 34,
                               42, 32, 44, 27, 28, 31, 41]),
        ('tet', 84): np.array([0, 6, 27, 83, 1, 2, 3, 4, 5, 12, 17, 21, 24,
                               26, 25, 22, 18, 13, 7, 80, 74, 64, 49, 28, 82,
                               79, 73, 63, 48, 81, 76, 67, 53, 33, 8, 23, 11,
                               14, 19, 20, 16, 10, 9, 15, 29, 32, 75, 30, 31,
                               52, 66, 65, 50, 51, 34, 77, 46, 54, 68, 71, 61,
                               43, 39, 58, 78, 38, 47, 70, 57, 42, 45, 62, 72,
                               60, 35, 37, 44, 69, 36, 41, 40, 55, 59, 56]),
        ('pri', 6): np.array([0, 1, 2, 3, 4, 5]),
        ('pri', 18): np.array([0, 2, 5, 12, 14, 17, 1, 3, 6, 4, 8, 11, 13, 15,
                               16, 7, 9, 10]),
        ('pri', 40): np.array([0, 3, 9, 30, 33, 39, 1, 2, 4, 7, 10, 20, 6, 8,
                               13, 23, 19, 29, 31, 32, 34, 37, 36, 38, 5, 35,
                               11, 12, 22, 21, 14, 24, 27, 17, 16, 18, 28, 26,
                               15, 25]),
        ('pri', 75): np.array([0, 4, 14, 60, 64, 74, 1, 2, 3, 5, 9, 12, 15,
                               30, 45, 8, 11, 13, 19, 34, 49, 29, 44, 59, 61,
                               62, 63, 65, 69, 72, 68, 71, 73, 6, 10, 7, 66,
                               67, 70, 16, 18, 48, 46, 17, 33, 47, 31, 32, 20,
                               50, 57, 27, 35, 54, 42, 24, 39, 23, 28, 58, 53,
                               26, 43, 56, 38, 41, 21, 51, 36, 22, 52, 37, 25,
                               55, 40]),
        ('pri', 126): np.array([0, 5, 20, 105, 110, 125, 1, 2, 3, 4, 6, 11,
                                15, 18, 21, 42, 63, 84, 10, 14, 17, 19, 26,
                                47, 68, 89, 41, 62, 83, 104, 106, 107, 108,
                                109, 111, 116, 120, 123, 115, 119, 122, 124,
                                7, 16, 9, 12, 13, 8, 112, 114, 121, 113, 118,
                                117, 22, 25, 88, 85, 23, 24, 46, 67, 87, 86,
                                64, 43, 44, 45, 66, 65, 27, 90, 102, 39, 48,
                                69, 95, 99, 81, 60, 36, 32, 53, 74, 78, 57,
                                31, 40, 103, 94, 35, 38, 61, 82, 101, 98, 73,
                                52, 56, 59, 80, 77, 28, 91, 49, 70, 30, 93,
                                51, 72, 37, 100, 58, 79, 29, 92, 50, 71, 34,
                                97, 55, 76, 33, 96, 54, 75]),
        ('pri', 196): np.array([0, 6, 27, 168, 174, 195, 1, 2, 3, 4, 5, 7, 13,
                                18, 22, 25, 28, 56, 84, 112, 140, 12, 17, 21,
                                24, 26, 34, 62, 90, 118, 146, 55, 83, 111,
                                139, 167, 169, 170, 171, 172, 173, 175, 181,
                                186, 190, 193, 180, 185, 189, 192, 194, 8, 23,
                                11, 14, 19, 20, 16, 10, 9, 15, 176, 179, 191,
                                177, 178, 184, 188, 187, 182, 183, 29, 33,
                                145, 141, 30, 31, 32, 61, 89, 117, 144, 143,
                                142, 113, 85, 57, 58, 60, 116, 114, 59, 88,
                                115, 86, 87, 35, 147, 165, 53, 63, 91, 119,
                                153, 158, 162, 137, 109, 81, 50, 46, 41, 69,
                                125, 134, 78, 97, 130, 106, 74, 102, 40, 54,
                                166, 152, 45, 49, 52, 82, 110, 138, 164, 161,
                                157, 124, 96, 68, 73, 80, 136, 129, 77, 108,
                                133, 101, 105, 36, 148, 64, 92, 120, 39, 151,
                                67, 95, 123, 51, 163, 79, 107, 135, 37, 149,
                                65, 93, 121, 38, 150, 66, 94, 122, 44, 156,
                                72, 100, 128, 48, 160, 76, 104, 132, 47, 159,
                                75, 103, 131, 42, 154, 70, 98, 126, 43, 155,
                                71, 99, 127]),
        ('hex', 8): np.array([0, 1, 3, 2, 4, 5, 7, 6]),
        ('hex', 27): np.array([0, 2, 8, 6, 18, 20, 26, 24, 1, 3, 9, 5, 11, 7,
                               17, 15, 19, 21, 23, 25, 4, 10, 12, 14, 16, 22,
                               13]),
        ('hex', 64): np.array([0, 3, 15, 12, 48, 51, 63, 60, 1, 2, 4, 8, 16,
                               32, 7, 11, 19, 35, 14, 13, 31, 47, 28, 44, 49,
                               50, 52, 56, 55, 59, 62, 61, 5, 9, 10, 6, 17, 18,
                               34, 33, 20, 36, 40, 24, 23, 27, 43, 39, 30, 29,
                               45, 46, 53, 54, 58, 57, 21, 22, 26, 25, 37, 38,
                               42, 41]),
        ('hex', 125): np.array([0, 4, 24, 20, 100, 104, 124, 120, 1, 2, 3, 5,
                                10, 15, 25, 50, 75, 9, 14, 19, 29, 54, 79, 23,
                                22, 21, 49, 74, 99, 45, 70, 95, 101, 102, 103,
                                105, 110, 115, 109, 114, 119, 123, 122, 121, 6,
                                16, 18, 8, 11, 17, 13, 7, 12, 26, 28, 78, 76,
                                27, 53, 77, 51, 52, 30, 80, 90, 40, 55, 85, 65,
                                35, 60, 34, 44, 94, 84, 39, 69, 89, 59, 64, 48,
                                46, 96, 98, 47, 71, 97, 73, 72, 106, 108, 118,
                                116, 107, 113, 117, 111, 112, 31, 33, 43, 41,
                                81, 83, 93, 91, 32, 36, 56, 38, 58, 42, 68, 66,
                                82, 86, 88, 92, 37, 57, 61, 63, 67, 87, 62]),
        ('hex', 216): np.array([0, 5, 35, 30, 180, 185, 215, 210, 1, 2, 3, 4,
                                6, 12, 18, 24, 36, 72, 108, 144, 11, 17, 23,
                                29, 41, 77, 113, 149, 34, 33, 32, 31, 71, 107,
                                143, 179, 66, 102, 138, 174, 181, 182, 183,
                                184, 186, 192, 198, 204, 191, 197, 203, 209,
                                214, 213, 212, 211, 7, 25, 28, 10, 13, 19, 26,
                                27, 22, 16, 9, 8, 14, 20, 21, 15, 37, 40, 148,
                                145, 38, 39, 76, 112, 147, 146, 109, 73, 74,
                                75, 111, 110, 42, 150, 168, 60, 78, 114, 156,
                                162, 132, 96, 54, 48, 84, 120, 126, 90, 47, 65,
                                173, 155, 53, 59, 101, 137, 167, 161, 119, 83,
                                89, 95, 131, 125, 70, 67, 175, 178, 69, 68,
                                103, 139, 176, 177, 142, 106, 105, 104, 140,
                                141, 187, 190, 208, 205, 188, 189, 196, 202,
                                207, 206, 199, 193, 194, 195, 201, 200, 43, 46,
                                64, 61, 151, 154, 172, 169, 44, 45, 49, 55, 79,
                                115, 52, 58, 82, 118, 63, 62, 100, 136, 97,
                                133, 152, 153, 157, 163, 160, 166, 171, 170,
                                50, 56, 57, 51, 80, 81, 117, 116, 85, 121, 127,
                                91, 88, 94, 130, 124, 99, 98, 134, 135, 158,
                                159, 165, 164, 86, 87, 93, 92, 122, 123, 129,
                                128]),
        ('tri', 3): np.array([0, 1, 2]),
        ('tri', 6): np.array([0, 2, 5, 1, 4, 3]),
        ('tri', 10): np.array([0, 3, 9, 1, 2, 6, 8, 7, 4, 5]),
        ('tri', 15): np.array([0, 4, 14, 1, 2, 3, 8, 11, 13, 12, 9, 5, 6, 7,
                               10]),
        ('tri', 21): np.array([0, 5, 20, 1, 2, 3, 4, 10, 14, 17, 19, 18, 15,
                               11, 6, 7, 8, 9, 13, 16, 12]),
        ('quad', 4): np.array([0, 1, 3, 2]),
        ('quad', 9): np.array([0, 2, 8, 6, 1, 5, 7, 3, 4]),
        ('quad', 16): np.array([0, 3, 15, 12, 1, 2, 7, 11, 14, 13, 8, 4, 5, 6,
                                10, 9]),
        ('quad', 25): np.array([0, 4, 24, 20, 1, 2, 3, 9, 14, 19, 23, 22, 21,
                                15, 10, 5, 6, 8, 18, 16, 7, 13, 17, 11, 12]),
        ('quad', 36): np.array([0, 5, 35, 30, 1, 2, 3, 4, 11, 17, 23, 29, 34,
                                33, 32, 31, 24, 18, 12, 6, 7, 10, 28, 25, 8, 9,
                                16, 22, 27, 26, 19, 13, 14, 15, 21, 20])
    }

    from_pyfr = {k: np.argsort(v) for k, v in to_pyfr.iteritems()}
