setwd("~/Documents/speckleProteinInteractome/")

library(ggplot2)
library(hrbrthemes)
library(viridis)


GOs <- read.table("selected_functional_annotations_withKIRCratios.txt", header=T, sep = "\t")

p = ggplot(GOs, aes(x=Abbreviation, y=SignatureRatioKIRC, fill=factor(Abbreviation))) +
  geom_boxplot(col="black", size=1, outlier.size = 0) +
  geom_jitter(color="grey20", size=.7, alpha= .8) +
  theme_classic() +
  scale_fill_viridis(discrete = TRUE, alpha=0.6, option = "D", direction = -1) +
  theme(legend.position="none") +
  ylim(-1, 1.25)
pdf("signatureRatiosKIRC_functionalCategories_boxplot.pdf", width = 3, height = 3, onefile=FALSE)
print(p)
dev.off()

t.test(GOs$SignatureRatioKIRC[GOs$Abbreviation == "1_TREX"])
t.test(GOs$SignatureRatioKIRC[GOs$Abbreviation == "2_RNAmetabolism"])
t.test(GOs$SignatureRatioKIRC[GOs$Abbreviation == "3_U2cat"])
t.test(GOs$SignatureRatioKIRC[GOs$Abbreviation == "4_U2precat"])
t.test(GOs$SignatureRatioKIRC[GOs$Abbreviation == "5_DNArepair"])
t.test(GOs$SignatureRatioKIRC[GOs$Abbreviation == "6_chromatin"])
t.test(GOs$SignatureRatioKIRC[GOs$Abbreviation == "7_pretranscriptionAndElongation"])
