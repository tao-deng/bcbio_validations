import sys
from bcbio.variation import validateplot

title="Trimming NA12878/NA24385 somatic mix: exome + chr20"
validateplot.classifyplot_from_valfile(sys.argv[1], outtype="png", title=title)
