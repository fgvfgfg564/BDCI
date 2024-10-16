from bdci import BDCI_RATE, BDCI_QUALITY

R1 = [0.1,0.2,0.3,0.4]
D1 = [26,28,29,29.5]
R2 = R1
D2 = D1

# R1 and D1 are the anchor

# Compute BDCI-rate (or BDCI-BR)
bdci_br_min, bdci_br_max = BDCI_RATE(R1, D1, R2, D2, weight_group='COV')
# Compute BDCI-quality
bdci_quality_min, bdci_quality_max = BDCI_QUALITY(R1, D1, R2, D2, weight_group='COV')

print(bdci_br_min, bdci_br_max)