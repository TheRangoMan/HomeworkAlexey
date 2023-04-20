import unittest

class TestShortestPath(unittest.TestCase):
    
    def setUp(self):
        self.themap = [
            [0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 5, 0, 0, 1, 0, 0, 0, 0],
            [0, 5, 0, 6, 0, 0, 0, 0, 0, 0],
            [0, 0, 6, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 0, 0, 0, 1, 0, 7],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 7, 0, 0, 0, 0, 0]
        ]
    
    def test_shortest_path(self):
        le = len(self.themap)
        for a in range(le):
            for b in range(le):
                if a == b:
                    continue
                for c in range(le):
                    if c == b or c == a:
                        continue
                    if self.themap[a][b] and self.themap[b][c]:
                        d = self.themap[a][b] + self.themap[b][c]
                        if self.themap[a][c] > d or not self.themap[a][c]:
                            self.themap[a][c] = d
                            self.themap[c][a] = d
        
        self.assertEqual(self.themap[0][1], 4)
        self.assertEqual(self.themap[0][2], 9)
        self.assertEqual(self.themap[0][3], 15)
        self.assertEqual(self.themap[0][4], 18)
        self.assertEqual(self.themap[0][5], 5)
        self.assertEqual(self.themap[0][6], 6)
        self.assertEqual(self.themap[0][7], 7)
        self.assertEqual(self.themap[0][8], 12)
        self.assertEqual(self.themap[0][9], 18)

if __name__ == '__main__':
    unittest.main()
