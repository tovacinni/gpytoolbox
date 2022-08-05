from .context import gpytoolbox
from .context import numpy as np
from .context import unittest
import scipy

class TestLinearElasticityStiffness(unittest.TestCase):
    def test_no_external_forces(self):
        # Build very small mesh
        V, F = gpytoolbox.regular_square_mesh(3)
        V = (V + 1.)/2.
        K, C, strain, A, M = gpytoolbox.linear_elasticity_stiffness(V,F)
        # print(V)
        # print(F)
        # gpytoolbox.write_mesh("~/test.obj",np.hstack((V,np.zeros((V.shape[0],1)))),F)
        I = np.array([
        1,
        2,
        4,
        11,
        13,
        14,
        1,
        2,
        3,
        5,
        10,
        11,
        12,
        14,
        15,
        2,
        3,
        6,
        11,
        12,
        15,
        1,
        4,
        5,
        7,
        10,
        13,
        14,
        16,
        17,
        2,
        4,
        5,
        6,
        8,
        10,
        11,
        13,
        14,
        15,
        17,
        18,
        3,
        5,
        6,
        9,
        11,
        12,
        14,
        15,
        18,
        4,
        7,
        8,
        13,
        16,
        17,
        5,
        7,
        8,
        9,
        13,
        14,
        16,
        17,
        18,
        6,
        8,
        9,
        14,
        15,
        17,
        2,
        4,
        5,
        10,
        11,
        13,
        1,
        2,
        3,
        5,
        6,
        10,
        11,
        12,
        14,
        2,
        3,
        6,
        11,
        12,
        15,
        1,
        4,
        5,
        7,
        8,
        10,
        13,
        14,
        16,
        1,
        2,
        4,
        5,
        6,
        8,
        9,
        11,
        13,
        14,
        15,
        17,
        2,
        3,
        5,
        6,
        9,
        12,
        14,
        15,
        18,
        4,
        7,
        8,
        13,
        16,
        17,
        4,
        5,
        7,
        8,
        9,
        14,
        16,
        17,
        18,
        5,
        6,
        8,
        15,
        17,
        18])
        J = np.array([
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        3,
        3,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        4,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        7,
        7,
        7,
        7,
        7,
        7,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        8,
        9,
        9,
        9,
        9,
        9,
        9,
        10,
        10,
        10,
        10,
        10,
        10,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        12,
        12,
        12,
        12,
        12,
        12,
        13,
        13,
        13,
        13,
        13,
        13,
        13,
        13,
        13,
        14,
        14,
        14,
        14,
        14,
        14,
        14,
        14,
        14,
        14,
        14,
        14,
        15,
        15,
        15,
        15,
        15,
        15,
        15,
        15,
        15,
        16,
        16,
        16,
        16,
        16,
        16,
        17,
        17,
        17,
        17,
        17,
        17,
        17,
        17,
        17,
        18,
        18,
        18,
        18,
        18,
        18])
        S = np.array([
        0.88842,
        -0.88267,
        -0.00575,
        0.87117,
        0.00575,
        -0.87692,
        -0.88267,
        1.7768,
        -0.88267,
        -0.0115,
        0.00575,
        -0.87692,
        0.87117,
        0.87692,
        -0.87692,
        -0.88267,
        0.88842,
        -0.00575,
        0.00575,
        -0.87692,
        0.87117,
        -0.00575,
        1.7768,
        -1.7653,
        -0.00575,
        0.87117,
        -0.87692,
        0.87692,
        0.00575,
        -0.87692,
        -0.0115,
        -1.7653,
        3.5537,
        -1.7653,
        -0.0115,
        -0.87692,
        0.87692,
        0.87692,
        -1.7538,
        0.87692,
        0.87692,
        -0.87692,
        -0.00575,
        -1.7653,
        1.7768,
        -0.00575,
        -0.87692,
        0.00575,
        0.87692,
        -0.87692,
        0.87117,
        -0.00575,
        0.88842,
        -0.88267,
        0.87117,
        -0.87692,
        0.00575,
        -0.0115,
        -0.88267,
        1.7768,
        -0.88267,
        -0.87692,
        0.87692,
        0.87117,
        -0.87692,
        0.00575,
        -0.00575,
        -0.88267,
        0.88842,
        -0.87692,
        0.00575,
        0.87117,
        0.00575,
        0.87117,
        -0.87692,
        0.88842,
        -0.00575,
        -0.88267,
        0.87117,
        -0.87692,
        0.00575,
        0.87692,
        -0.87692,
        -0.00575,
        1.7768,
        -0.00575,
        -1.7653,
        0.87117,
        -0.87692,
        0.00575,
        -0.00575,
        0.88842,
        -0.88267,
        0.00575,
        -0.87692,
        0.87692,
        0.87117,
        -0.87692,
        -0.88267,
        1.7768,
        -0.0115,
        -0.88267,
        -0.87692,
        0.87692,
        0.87692,
        -1.7538,
        0.87692,
        0.87692,
        -0.87692,
        -1.7653,
        -0.0115,
        3.5537,
        -0.0115,
        -1.7653,
        -0.87692,
        0.87117,
        0.87692,
        -0.87692,
        0.00575,
        -0.88267,
        -0.0115,
        1.7768,
        -0.88267,
        0.00575,
        -0.87692,
        0.87117,
        -0.88267,
        0.88842,
        -0.00575,
        -0.87692,
        0.87692,
        0.00575,
        -0.87692,
        0.87117,
        -1.7653,
        -0.00575,
        1.7768,
        -0.00575,
        -0.87692,
        0.87117,
        0.00575,
        -0.88267,
        -0.00575,
        0.88842])
        K_gt = scipy.sparse.csr_matrix((S,(I-1,J-1)))
        self.assertTrue(np.isclose(K.toarray()-K_gt.toarray(),0,atol=1e-4).all())

        I = np.array([
        1,
        9,
        2,
        10,
        3,
        11,
        4,
        12,
        5,
        13,
        6,
        14,
        7,
        15,
        8,
        16,
        1,
        9,
        2,
        10,
        3,
        11,
        4,
        12,
        5,
        13,
        6,
        14,
        7,
        15,
        8,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24])
        J = np.array([
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        4,
        5,
        5,
        6,
        6,
        7,
        7,
        8,
        8,
        9,
        9,
        10,
        10,
        11,
        11,
        12,
        12,
        13,
        13,
        14,
        14,
        15,
        15,
        16,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24])
        S = np.array([
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        1.7423,
        1.7653,
        0.0115,
        0.0115,
        0.0115,
        0.0115,
        0.0115,
        0.0115,
        0.0115,
        0.0115])
        # print(K_gt)
        C_gt = scipy.sparse.csr_matrix((S,(I-1,J-1)))
        self.assertTrue(np.isclose(C.toarray()-C_gt.toarray(),0,atol=1e-4).all())

        I = np.array([
        5,
        17,
        5,
        6,
        18,
        21,
        6,
        22,
        1,
        7,
        17,
        19,
        1,
        2,
        7,
        8,
        18,
        20,
        21,
        23,
        2,
        8,
        22,
        24,
        3,
        19,
        3,
        4,
        20,
        23,
        4,
        24,
        9,
        21,
        10,
        13,
        21,
        22,
        14,
        22,
        9,
        11,
        17,
        23,
        10,
        12,
        13,
        15,
        17,
        18,
        23,
        24,
        14,
        16,
        18,
        24,
        11,
        19,
        12,
        15,
        19,
        20,
        16,
        20])
        J = np.array([
        1,
        1,
        2,
        2,
        2,
        2,
        3,
        3,
        4,
        4,
        4,
        4,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        5,
        6,
        6,
        6,
        6,
        7,
        7,
        8,
        8,
        8,
        8,
        9,
        9,
        10,
        10,
        11,
        11,
        11,
        11,
        12,
        12,
        13,
        13,
        13,
        13,
        14,
        14,
        14,
        14,
        14,
        14,
        14,
        14,
        15,
        15,
        15,
        15,
        16,
        16,
        17,
        17,
        17,
        17,
        18,
        18])
        S = np.array([
        -2,
        -2,
        2,
        -2,
        -2,
        -2,
        2,
        -2,
        -2,
        -2,
        2,
        -2,
        2,
        -2,
        2,
        -2,
        2,
        -2,
        2,
        -2,
        2,
        2,
        2,
        -2,
        -2,
        2,
        2,
        -2,
        2,
        2,
        2,
        2,
        -2,
        -2,
        -2,
        -2,
        2,
        -2,
        -2,
        2,
        2,
        -2,
        -2,
        -2,
        2,
        -2,
        2,
        -2,
        2,
        -2,
        2,
        -2,
        2,
        -2,
        2,
        2,
        2,
        -2,
        2,
        2,
        2,
        -2,
        2,
        2])
        strain_gt = scipy.sparse.csr_matrix((S,(I-1,J-1)))
        self.assertTrue(np.isclose(strain.toarray()-strain_gt.toarray(),0,atol=1e-4).all())
if __name__ == '__main__':
    unittest.main()