# Chimera_crosslinks
Intra-protein crosslink distance measurements using Chimera.

Put cx_distances.py in a folder containing a UVPD_xlink.csv which contains comma-separated pairs of cross-linked residue numbers:

```
1, 15
3, 8
4, 20
...
```

Run in chimera (file->open->/../cx_distances.py)

The crosslinks will be visualized on the protein in Chimera and the distances will be tabulated in output_common.csv
