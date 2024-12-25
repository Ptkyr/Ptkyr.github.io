---
layout: post
title: "43,252,003,274,489,856,000"
categories: cubing, group theory
author: ptkyr
---

We all know that if you fix the centers of a 3x3, there are 43,252,003,274,489,856,000 valid permutations of the pieces. For some reason, I can't find a cohesive, detailed account of the group-theoretic approach to finding this number, so I'm writing one.

Assume fixed centers. I'm going with white top, green front because it's the least arbitrary choice. Firstly, the set of permutations of pieces is isomorphic to some subgroup $$P$$ of $$S_{48}$$. There are 8 corner pieces with 3 stickers and 12 edges with 2 stickers, for $$(8 \cdot 3 + 12 \cdot 2)! = 48!$$ total ways to arrange the stickers on the cube (assume each sticker is uniquely identifiable), regardless of if the arrangement makes any sense. $$P$$ is the colourings that at least respect that each piece has a unique life story, a family and kids, a cottage up north, etc. 

Finding $$\lvert P \rvert$$ is easy. Because each piece is distinct, you simply fill piece slots while accounting for different orientations. The first corner you fill has 8 pieces to choose from, then three orientations of that piece. The next slot chooses from 7 pieces, again with 3 orientations, and so on. This gives $$\lvert P \rvert = 8! \cdot 3^{8} \cdot 12! \cdot 2^{12}$$.

We're interested in $$C$$, the subset of $$P$$ where the permutation of pieces is solvable. We'll also take for granted that $$C \leq P$$. By Lagrange's theorem, to find $$\lvert C \rvert$$ we just need to find how many cosets of $$C$$ in $$P$$ there are. In other words, we want to know how many distinct ways there are to fuck up a cube. It turns out there are 11:

<html>
    <head>
        <script type="text/javascript" src="dist/puzzleGen.min.js"></script>
    </head>
    <style>
        th, td {
            padding: 10px;
            text-align: center;
        }
        table {
            width: 100%;
        }
        td img {
            max-width: 100%;  /* Prevents image from exceeding td width */
            height: auto;     /* Maintains the aspect ratio */
            display: block;   /* Prevents space below image */
            margin: 0 auto;   /* Centers the image if td is wider than the image */
        }
    </style>
    <body>
        <table>
        <tbody>
            <tr>
                <td id="solved">\(C\)</td>
                <td id="cc">CT</td>
                <td id="ccw">CT'</td>
                <td id="ef">EF</td>
                <td id="ccef">CT, EF</td>
                <td id="ccwef">CT', EF</td>
            </tr>
            <tr>
                <td id="es">Edge Swap</td>
                <td id="escc">ES, CT</td>
                <td id="esccw">ES, CT'</td>
                <td id="esef">ES, EF</td>
                <td id="esccef">ES, CT, EF</td>
                <td id="esccwef">ES, CT', EF</td>
            </tr>
        </tbody>
        </table>

        <script type="text/javascript">
            let type = puzzleGen.Type.CUBE_TOP
            let options = {
                "width": 100,
                "height": 100,
                "puzzle": {
                    "scheme": {
                        "U": { "value": "#FFFFFF", },
                        "R": { "value": "#FF0000", },
                        "F": { "value": "#00FF00", },
                        "D": { "value": "#FFFF00", },
                        "L": { "value": "#FFA500", },
                        "B": { "value": "#0000FF", }
                    },
                    "mask": {
                        "F": [3,4,5,6,7,8],
                        "B": [3,4,5,6,7,8],
                        "R": [3,4,5,6,7,8],
                        "L": [3,4,5,6,7,8],
                        "D": [0,1,2,3,4,5,6,7,8]
                    }
                }
            }

            let zbllu72 = "R U2 R' U' R U' R' U2 R' U2 R U R' U R U2"
            let zblll72 = "R U R' U R U' R' U R U2 R' U' R U2 R' U' R U' R'"
            let oll57 = "M' U2 M U R' F' R S R' F R S' U"
            let oll28 = "r U R' U' r' U2 R U R U' R2 U2 R"

            let ct = zbllu72
            let ct2 = zbllu72 + zbllu72
            let swap = "S2 U2 S2 U2"
            function wrapx(str) {
                return `"x " + ${str} + " x'"`;
            }

            puzzleGen.PNG("#solved", type, options);
            options.puzzle.alg = wrapx(ct)
            puzzleGen.PNG("#cc", type, options);
            options.puzzle.alg = wrapx(ct2)
            puzzleGen.PNG("#ccw", type, options);
            options.puzzle.alg = wrapx(oll57)
            puzzleGen.PNG("#ef", type, options);
            options.puzzle.alg = wrapx(oll57 + ct)
            puzzleGen.PNG("#ccef", type, options);
            options.puzzle.alg = wrapx(oll57 + ct2)
            puzzleGen.PNG("#ccwef", type, options);
            options.puzzle.alg = swap
            puzzleGen.PNG("#es", type, options);
            options.puzzle.alg = swap + wrapx(ct)
            puzzleGen.PNG("#escc", type, options);
            options.puzzle.alg = swap + wrapx(ct2)
            puzzleGen.PNG("#esccw", type, options);
            options.puzzle.alg = swap + wrapx(oll57)
            puzzleGen.PNG("#esef", type, options);
            options.puzzle.alg = swap + wrapx(oll57 + ct)
            puzzleGen.PNG("#esccef", type, options);
            options.puzzle.alg = swap + wrapx(oll57 + ct2)
            puzzleGen.PNG("#esccwef", type, options);
        </script>
    </body>
</html>

In this table,[^1] CT means a clockwise corner twist (CT' is counter-clockwise), EF means an edge flip, and ES means an edge swap (preserving orientation). Of course, the images only depict what I think are the simplest representatives of each coset.

Legal moves (R, L, U, D, F, B) cannot move between these cosets, since $$C$$ is the subgroup of $$P$$ generated by them.

To see why an edge flip is illegal, we will define a homomorphism $$\varphi : P \rightarrow \mathbb{Z}_2$$ for which $$\varphi(C) = \{0\}$$. First, assign each sticker of each edge a value in $$\{0, 1\}$$ as follows:
- If the edge has a white or yellow sticker, assign it 0, the other 1.
- Otherwise, the edge must have a blue or green sticker. Assign it 0, the other 1.

Then, define $$\varphi$$ to be the sum of all values of edge stickers on the U face, D face, and F and B middle edges. That is, all the positions with value 0 for the solved state, $$e$$.

<html>
    <head>
        <script type="text/javascript" src="dist/puzzleGen.min.js"></script>
    </head>
    <style>
        th, td {
            padding: 10px;
            text-align: center;
        }
        table {
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    <body>
        <table>
        <tbody>
            <tr>
                <td id="phi"></td>
                <td id="phinet"></td>
            </tr>
        </tbody>
        </table>
        <script type="text/javascript">
            options = {
                "width": 150,
                "height": 150,
                "puzzle": {
                    "scheme": {
                        "U": { "value": "#FFFFFF", },
                        "R": { "value": "#FF0000", },
                        "F": { "value": "#00FF00", },
                        "D": { "value": "#FFFF00", },
                        "L": { "value": "#FFA500", },
                        "B": { "value": "#0000FF", }
                    },
                    "mask": {
                        "U": [0,2,4,6,8],
                        "F": [0,1,2,4,6,7,8],
                        "B": [0,1,2,4,6,7,8],
                        "R": [0,1,2,3,4,5,6,7,8],
                        "L": [0,1,2,3,4,5,6,7,8],
                        "D": [0,2,4,6,8],
                    }
                }
            }
            puzzleGen.PNG("#phi", puzzleGen.Type.CUBE, options);
            puzzleGen.PNG("#phinet", puzzleGen.Type.CUBE_NET, options);
        </script>
    </body>
</html>

By construction, $$\varphi(e) = 0$$, and notice $$\varphi(a) = 0$$ for any of the generators $$a \in \{U, D, R, L, F, B\} \subset C$$. FMC or ZZ enjoyers might notice that $$\varphi$$ just counts the number of mis-oriented edges, which is always even for any state in $$C$$.

I'm far too lazy to actually show $$\varphi$$ is a homomorphism, but maybe it's obvious. Then since each generator is in $$\ker(\varphi)$$, it follows that $$\varphi(C) = \{0\}$$. However, $$\varphi(\text{EF}) = 1$$, so $$\text{EF} \not\in C$$. To show that CT, CT' et al. are distinct from $$C$$, a similar homomorphism $$\psi : P \to \mathbb{Z}_3$$ exists by labelling the corners in a natural way, as detailed in [this post][loganmso]. Surely one is also constructible for edge swaps, but I don't want to think of one.[^2]

As for why these are the *only* fuckups, any number of (just) corner twists can be reduced to either $$C$$, CT, or CT' with ZBLL U72:[^3] R U2 R' U' R U' R' U2 R' U2 R U R' U R U2, which rotates two adjacent corners (UFR and UBR) in opposite directions. Likewise, any number of edge flips can be reduced to $$C$$ or EF using a particular OLL28[^4] (r U R' U' r' U2 R U R U' R2 U2 R) alg that flips two edges (UF and UR). Of course, you can independently perform these operations with the hybrid cosets.

<html>
    <head>
        <script type="text/javascript" src="dist/puzzleGen.min.js"></script>
    </head>
    <style>
        th, td {
            padding: 10px;
            text-align: center;
        }
        table {
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    <body>
        <table>
        <tbody>
            <tr>
                <td id="u72">ZBLL U72</td>
                <td id="oll28">OLL 28</td>
            </tr>
        </tbody>
        </table>
        <script type="text/javascript">
            options = {
                "width": 150,
                "height": 150,
                "puzzle": {
                    "scheme": {
                        "U": { "value": "#FFFFFF", },
                        "R": { "value": "#FF0000", },
                        "F": { "value": "#00FF00", },
                        "D": { "value": "#FFFF00", },
                        "L": { "value": "#FFA500", },
                        "B": { "value": "#0000FF", }
                    },
                    "mask": {
                        "F": [3,4,5,6,7,8],
                        "B": [3,4,5,6,7,8],
                        "R": [3,4,5,6,7,8],
                        "L": [3,4,5,6,7,8],
                        "D": [0,1,2,3,4,5,6,7,8]
                    }
                }
            }
            options.puzzle.case = zbllu72
            puzzleGen.PNG("#u72", puzzleGen.Type.CUBE_TOP, options);
            options.puzzle.case = oll28
            puzzleGen.PNG("#oll28", puzzleGen.Type.CUBE_TOP, options);
        </script>
    </body>
</html>

For reducing to ES-related cosets, if you swap more than two of any piece type, there's always some commutator that can cycle 3 pieces of the same type, for instance both A perms and the U perms. It's what makes 3-style work! So swapping two of the same piece type is the most (only) illegal swap-related operation you can perform. On a related note, two-edge swaps are the same coset as two-corner swaps, because no matter if they're adjacent or opposite, you can always select a particular PLL from F, J, N, R, T, V, Y that swaps the edges of interest, replacing them with two swapped corners.

That's it! As long as you're convinced these are the only cosets of $$C$$ in $$P$$, Lagrange's theorem gives $$[P : C] = 12$$, hence 
<center>
    $$\lvert C \rvert = \frac{8! \cdot 3^{8} \cdot 12! \cdot 2^{12}}{12} = 43,252,003,274,489,856,000.$$
</center>

Stay tuned for the post where I gather the courage (boredom) to walk through finding the number of permutations up to conjugacy by whole-cube symmetries (901,083,404,981,813,616).

[^1]: All figures were generated with [puzzlegen][puzzlegen].
[^2]: In fact, if you have all three of these homomorphisms you can simply construct a massive surjective homomorphism $$\Phi : P \to \mathbb{Z}_3 \times \mathbb{Z}_2 \times \mathbb{Z}_2$$ with $$\ker(\Phi) = C$$, proving the result instantly and that $$C$$ is a normal subgroup of $$P$$.
[^3]: ZBLL L72: R U R' U R U' R' U R U2 R' U' R U2 R' U' R U' R' U' also works, twisting UFR and UBL.
[^4]: or OLL57 (M' U2 M U R' F' R S R' F R S' U), flipping UF and UB.

[puzzlegen]: https://github.com/tdecker91/puzzle-gen
[cubelovers]: https://www.math.rwth-aachen.de/%7EMartin.Schoenert/Cube-Lovers/Dan_Hoey__The_real_size_of_cube_space.html
[loganmso]: https://puzzling.stackexchange.com/a/76
