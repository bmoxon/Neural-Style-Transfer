README.runs.md

images/output/flowers9610_seuratpoint (10)

$ python3 INetwork.py images/bcmNST/content/flowers/IMG_9610.jpg images/bcmNST/style/style-pointillism/style-seurat-pointillism.jpg images/output/flowers9610_seuratpoint

4s per iteration, 400x400 out


--num_iter 30
4s per iteration

$ python3 INetwork.py images/bcmNST/content/flowers/IMG_9610.jpg images/bcmNST/style/style-pointillism/style-seurat-pointillism.jpg images/output/flowers9610_seuratpoint --num_iter 60

$ python3 INetwork.py images/bcmNST/content/nmpics/IMG_9482.jpg images/bcmNST/style/style-russian/Fechin.Katenka.jpeg images/output/chiles9482_fechinkatenka --num_iter 5 --color_mask images/bcmNST/content/nmpics/IMG_9482.jpg

$ python3 INetwork.py images/bcmNST/content/nmpics/IMG_9482.jpg images/inputs/style/shipwreck.jpg images/output/chiles9482_shipwreck --num_iter 10

$ python3 INetwork.py images/bcmNST/content/nmpics/IMG_9482.jpg images/inputs/style/shipwreck.jpg images/output/chiles9482_shipwreck2 --num_iter 10 --style_weight 0.1 --total_variation_weight 5E-05