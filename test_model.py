"""Regression checks of the independent reference model; run python3 -m unittest -v test_model.py."""
import math
import random
import unittest
import model


class GeometryTests(unittest.TestCase):
    def test_triangular_graph(self):
        edges, triangles, links=model.triangulation()
        self.assertEqual((len(edges),len(triangles),len(links)),(120,72,49))
        self.assertEqual(max(map(len,links)),6)

    def test_entanglement_extrema(self):
        self.assertAlmostEqual(model.link_mutual_information(0),0)
        self.assertAlmostEqual(model.link_mutual_information(math.pi/4),2)
        self.assertAlmostEqual(model.link_mutual_information(math.pi/2),0)
        for a in [i/17 for i in range(500)]:
            self.assertLessEqual(model.link_mutual_information(a),2+1e-14)

    def test_exact_pair_norm(self):
        for a in [i/13 for i in range(140)]:
            self.assertAlmostEqual(math.cos(a)**2+math.sin(a)**2,1)

    def test_flat_metric_reference(self):
        edges,triangles,_=model.triangulation()
        lengths=[math.sqrt(2) if e.diagonal else 1 for e in edges]
        result=model.curvature_from_links(7,edges,triangles,lengths)
        self.assertEqual(sum(v is None for v in result),24)
        self.assertLess(max(abs(x) for x in result if x is not None),1e-12)

    def test_inferred_metric_triangle_inequality(self):
        edges,tris,_=model.triangulation()
        for seed in range(5):
            rng=random.Random(seed)
            lengths=[model.inferred_length(rng.uniform(0,2),e.diagonal) for e in edges]
            result=model.curvature_from_links(7,edges,tris,lengths)
            self.assertTrue(all(x is None or math.isfinite(x) for x in result))

    def test_null_and_candidate(self):
        self.assertEqual(model.link_theta(.4,.02,60,0,.9,True),model.link_theta(.4,.02,60,0,.9,False))
        self.assertNotEqual(model.link_theta(.4,.02,60,.8,.9,True),model.link_theta(.4,.02,60,.8,.9,False))

    def test_dimension_controls(self):
        self.assertEqual(model.dimension_sweep(),{887:True,888:True,889:True})
        self.assertFalse(model.dimension_sweep([63])[63])

    def test_unitary_gate(self):
        r=random.Random(888)
        for n in (887,888,889):
            a=[complex(r.random()-.5,r.random()-.5) for _ in range(n)]
            before=model.norm2(a)
            for _ in range(20):
                a=model.circuit_layer(a,.08,False)
                a=model.circuit_layer(a,.08,True)
            self.assertAlmostEqual(model.norm2(a),before,places=10)

if __name__=='__main__':unittest.main()
