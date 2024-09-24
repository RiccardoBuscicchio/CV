import numpy as np
import sys,os

import json

papers = {}
submitted = True
published = True
collab = True
proceedings = False
others = True

talks  = {}
conferences = True
seminars = True
lectures = False
posters = False
outreach = True

if submitted:

    papers['submitted'] = {}
    papers['submitted']['label'] = 'Submitted short-author and collaboration papers which I have substantially contributed to.'
    papers['submitted']['data'] = []

 papers['submitted']['data'].append({
        "title":    "Stars or gas? Constraining the hardening processes of massive black-hole binaries with LISA",
        "author":   "A. Spadaro, R. Buscicchio, D. Izquierdo--Villalba, D. Gerosa, A. Klein, G. Pratten",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2409.13011 [astro-ph.HE]",
        "ads":      "2024arXiv240913011S",
        "inspire":  "Spadaro:2024tve",
        "more":     ""
        })

    papers['submitted']['data'].append({
        "title":    "Expected insights on type Ia supernovae from LISA's gravitational wave observations",
        "author":   "V. Korol, R. Buscicchio, Ruediger Pakmor, Javier Morán-Fraile, Christopher J. Moore, Selma E. de Mink",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2407.03935 [astro-ph.HE]",
        "ads":      "2024arXiv240703935K",
        "inspire":  "Korol:2024dzw",
        "more":     ""
        })

    papers['submitted']['data'].append({
        "title":    "Partial alignment between jets and megamasers: coherent or selective accretion?",
        "author":   "M. Dotti, R. Buscicchio, F. Bollati, R. Decarli, W. Del Pozzo, A. Franchini",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2403.18002 [astro-ph.GA]",
        "ads":      "2024arXiv240318002D",
        "inspire":  "Dotti:2024wng",
        "more":     ""
        })
    
    papers['submitted']['data'].append({
        "title":    "LISA Definition Study Report",
        "author":   "M. Colpi, K. Danzmann, M. Hewitson, K. Holley-Bockelmann, et al. (incl. R. Buscicchio)",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2402.07571 [astro-ph.CO]",
        "ads":      "2024arXiv240207571C",
        "inspire":  "Colpi:2024xhw",
        "more":     ""
        })
    
    papers['submitted']['data'].append({
        "title":    "The last three years: multiband gravitational-wave observations of stellar-mass binary black holes",
        "author":   "A. Klein, G. Pratten, R. Buscicchio, P. Schmidt, C. J. Moore, E. Finch, A. Bonino, L. M. Thomas, N. Williams, D. Gerosa, S. McGee, M. Nicholl, A. Vecchio",
        "journal":  "",
        "link":     "",
        "arxiv":    "arXiv:2204.03423 [astro-ph.HE]",
        "ads":      "2022arXiv220403423K",
        "inspire":  "Klein:2022rbf",
        "more":     ""
        })
    
    papers['submitted']['data'].append({
        "title":    "Search for gravitational-lensing signatures in the full third observing run of the LIGO-Virgo network",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration, KAGRA collaboration",
        "journal":  "", 
        "link":     "", 
        "arxiv":    "arXiv:2304.08393 [gr-qc]" ,
        "ads":      "2023arXiv230408393T", 
        "inspire":  "LIGOScientific:2023bwz", 
        "more":     ""
        })

if published:
    papers['published'] = {}
    papers['published']['label'] = 'Papers in major peer-reviewed journals'
    papers['published']['data'] = []


    papers['published']['data'].append({
        "title":    "A weakly-parametric approach to stochastic background inference in LISA",
        "author":   "F. Pozzoli, R. Buscicchio, C. J. Moore, A. Sesana, F. Haardt, A. Sesana",
        "journal":  "\prd Phys. Rev. D 109, (2024) 083029",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.109.083029",
        "arxiv":    "arXiv:2311.12111 [astro-ph.CO]",
        "ads":      "2024PhRvD.109h3029P",
        "inspire":  "Pozzoli:2023lgz",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "A fast test for the identification and confirmation of massive black hole binary",
        "author":   "M. Dotti, F. Rigamonti, S. Rinaldi, W. Del Pozzo, R. Decarli, R. Buscicchio",
        "journal":  "\\aap 680 (2023) A69",
        "link":     "https://www.aanda.org/articles/aa/abs/2023/12/aa46916-23/aa46916-23.html",
        "arxiv":    "arXiv:2310.06896 [astro-ph.HE]",
        "ads":      "2023A&A...680A..69D",
        "inspire":  "Dotti:2023bac",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "Glitch systematics on the observation of massive black-hole binaries with LISA",
        "author":   "A. Spadaro, R. Buscicchio, D. Vetrugno, A. Klein, D. Gerosa, S. Vitale, R. Dolesi, W. J. Weber, M. Colpi",
        "journal":  "\prd Phys. Rev. D 108 (2023) 123029",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.123029",
        "arxiv":    "arXiv:2306.03923 [gr-qc]",
        "ads":      "2023PhRvD.108l3029S",
        "inspire":  "Spadaro:2023muy",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "Implications of pulsar timing array observations for LISA detections of massive black hole binaries",
        "author":   "N. Steinle, H. Middleton, C. J. Moore, S. Chen, A. Klein, G. Pratten, R. Buscicchio, E. Finch, A. Vecchio",
        "journal":  "\mnras 525 2 (2023)",
        "link":     "https://academic.oup.com/mnras/article/525/2/2851/7244712",
        "arxiv":    "arXiv:2305.05955 [astro-ph.HE]",
        "ads":      "2023MNRAS.525.2851S",
        "inspire":  "Steinle:2023vxs",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Parameter estimation of binary black holes in the endpoint of the up-down instability",
        "author":   "V. De Renzis, D. Gerosa, M. Mould, R. Buscicchio, L. Zanga",
        "journal":  "\prd 108 (2023) 024024",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.108.024024",
        "arxiv":    "arXiv:2304.13063 [gr-qc]",
        "ads":      "2023PhRvD.108b4024D",
        "inspire":  "DeRenzis:2023lwa",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Improved detection statistics for non Gaussian gravitational wave stochastic backgrounds",
        "author":   "M. Ballelli, R. Buscicchio, B. Patricelli, A. Ain, G. Cella",
        "journal":  "\prd 107 (2023) 124044",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.124044",
        "arxiv":    "arXiv:2212.10038 [gr-qc]",
        "ads":      "2023PhRvD.107l4044B",
        "inspire":  "Ballelli:2022bli",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Detecting non-Gaussian gravitational wave backgrounds: a unified framework",
        "author":   "R. Buscicchio, A. Ain, M. Ballelli, G. Cella, B. Patricelli",
        "journal":  "\prd 107 (2023) 063027",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.107.063027",
        "arxiv":    "arXiv:2209.01400 [gr-qc]",
        "ads":      "2023PhRvD.107f3027B",
        "inspire":  "Buscicchio:2022raf",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Detectability of a spatial correlation between stellar-mass black hole mergers and Active Galactic Nuclei in the Local Universe",
        "author":   "N. Veronesi, E.M. Rossi, S. van Velzen, R. Buscicchio",
        "journal":  "\mnras 514 2 (2023)",
        "link":     "https://academic.oup.com/mnras/article/514/2/2092/6587069",
        "arxiv":    "arXiv:2203.05907 [astro-ph.HE]",
        "ads":      "2022MNRAS.514.2092V",
        "inspire":  "Veronesi:2022hql",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "Bayesian parameter estimation of stellar-mass black-hole binaries with LISA",
        "author":   "R. Buscicchio, A. Klein, E. Roebber, C. J. Moore, D. Gerosa, E. Finch, A. Vecchio",
        "journal":  "\prd 104 (2021) 044065",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.104.044065",
        "arxiv":    "arXiv:2106.05259 [astro-ph.HE]",
        "ads":      "2021PhRvD.104d4065B",
        "inspire":  "Buscicchio:2021dph",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "An Interactive Gravitational-Wave Detector Model for Museums and Fairs",
        "author":   "S. J. Cooper, A. C. Green, H. R. Middleton, C. P. L. Berry, R. Buscicchio, E. Butler, C. J. Collins, C. Gettings, D. Hoyland, A. W. Jones, J. H. Lindon, I. Romero-Shaw, S. P. Stevenson, E. P. Takeva, S. Vinciguerra, A. Vecchio, C. M. Mow-Lowry, A. Freise",
        "journal":  "\\ajp 89 (2021) 702–712",
        "link":     "https://pubs.aip.org/aapt/ajp/article/89/7/702/1056907/An-interactive-gravitational-wave-detector-model",
        "arxiv":    "arXiv:2004.03052 [physics.ed-ph]",
        "ads":      "2021AmJPh..89..702C",
        "inspire":  "Cooper:2020ygn",
        "more":     ""
        })    

    papers['published']['data'].append({
        "title":    "Evidence for hierarchical black hole mergers in the second LIGO--Virgo gravitational-wave catalog",
        "author":   "C. Kimball, C. Talbot, C.P.L. Berry, M. Zevin, E. Thrane, V. Kalogera, R. Buscicchio, M. Carney, T. Dent, H. Middleton, E. Payne, J. Veitch, D. Williams ",
        "journal":  "\\apjl 915 (2021) L35",
        "link":     "https://iopscience.iop.org/article/10.3847/2041-8213/ac0aef",
        "arxiv":    "arXiv:2011.05332 [astro-ph.HE]",
        "ads":      "2021ApJ...915L..35K",
        "inspire":  "Kimball:2020qyd",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Testing general relativity with gravitational-wave catalogs: the insidious nature of waveform systematics",
        "author":   "C. J. Moore, E. Finch, R. Buscicchio, D. Gerosa",
        "journal":  "iScience 24 (2021) 102577",
        "link":     "https://www.sciencedirect.com/science/article/pii/S2589004221005459",
        "arxiv":    "arXiv:2103.16486   [gr-qc]",
        "ads":      "2021iSci...24j2577M",
        "inspire":  "Moore:2021eok",
        "more":     ""
        })


    papers['published']['data'].append({
        "title":    "LoCuSS: The splashback radius of massive galaxy clusters and its dependence on cluster merger history",
        "author":   "M. Bianconi, R. Buscicchio, G. P. Smith, S. L. McGee, C.P. Haines, A. Finoguenov, A. Babul",
        "journal":  "\\apj 911 (2021) 136",
        "link":     "https://iopscience.iop.org/article/10.3847/1538-4357/abebd7",
        "arxiv":    "arXiv:2010.05920 [astro-ph.GA]",
        "ads":      "2021ApJ...911..136B",
        "inspire":  "Bianconi:2020pcc",
        "more":     ""
        }) 

    papers['published']['data'].append({
        "title":    "Search for Black Hole Merger Families",
        "author":   "D. Veske, A. G. Sullivan, Z. Marka, I. Bartos, K. R. Corley, J. Samsing, R. Buscicchio, S. Marka",
        "journal":  "\\apjl 907 (2021) L48",
        "link":     "https://iopscience.iop.org/article/10.3847/2041-8213/abd721",
        "arxiv":    "arXiv:2011.06591 [astro-ph.HE]",
        "ads":      "2021ApJ...907L..48V",
        "inspire":  "Veske:2020idq",
        "more":     ""
        })
    papers['published']['data'].append({
        "title":    "Constraining the lensing of binary black holes from their stochastic background",
        "author":   "R. Buscicchio, C. J. Moore, G. Pratten, P. Schmidt, M. Bianconi, A. Vecchio",
        "journal":  "\prl 125 (2020) 141102",
        "link":     "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.125.141102",
        "arxiv":    "arXiv:2006.04516 [astro-ph.CO]",
        "ads":      "2020PhRvL.125n1102B",
        "inspire":  "Buscicchio:2020cij",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Constraining the lensing of binary neutron stars from their stochastic background",
        "author":   "R. Buscicchio, C. J. Moore, G. Pratten, P. Schmidt, A. Vecchio",
        "journal":  "\prd 102 (2020) 081501 ",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.102.081501",
        "arxiv":    "arXiv:2008.12621 [astro-ph.HE]",
        "ads":      "2020PhRvD.102h1501B",
        "inspire":  "Buscicchio:2020bdq",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Measuring precession in asymmetric compact binaries",
        "author":   "G. Pratten, P. Schmidt, R. Buscicchio, L. M. Thomas",
        "journal":  "\prr 2 (2020) 043096",
        "link":     "https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.2.043096",
        "arxiv":    "arXiv:2006.16153 [gr-qc]",
        "ads":      "2020PhRvR...2d3096P",
        "inspire":  "Pratten:2020igi",
        "more":     ""
        })
    
    papers['published']['data'].append({
        "title":    "Populations of double white dwarfs in Milky Way satellites and their detectability with LISA",
        "author":   "V. Korol, S. Toonen, A. Klein, V. Belokurov, F. Vincenzo, R. Buscicchio, D. Gerosa, C. J. Moore, E. Roebber, E. M. Rossi, A. Vecchio",
        "journal":  "\\aap 638 (2020) A153",
        "link":     "https://www.aanda.org/articles/aa/abs/2020/06/aa37764-20/aa37764-20.html",
        "arxiv":    "arXiv:2002.10462 [astro-ph.GA]",
        "ads":      "2020A&A...638A.153K",
        "inspire":  "Korol:2020lpq",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Milky Way satellites shining bright in gravitational waves",
        "author":   "E. Roebber, R. Buscicchio, A. Vecchio, C. J. Moore, A. Klein, V. Korol, S. Toonen, D. Gerosa, J. Goldstein, S. M. Gaebel, T. E. Woods",
        "journal":  "\\apjl 894 (2020) L15",
        "link":     "https://iopscience.iop.org/article/10.3847/2041-8213/ab8ac9",
        "arxiv":    "arXiv:2002.10465 [astro-ph.GA]",
        "ads":      "2020ApJ...894L..15R",
        "inspire":  "Roebber:2020hso",
        "more":     ""
        })

    papers['published']['data'].append({
        "title":    "Label Switching Problem in Bayesian Analysis for Gravitational Wave Astronomy",
        "author":   "R. Buscicchio, E. Roebber, J. M. Goldstein, C. J. Moore ",
        "journal":  "\prd 100 (2019) 084041",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.100.084041",
        "arxiv":    "arXiv:1907.11631 [astro-ph.IM]",
        "ads":      "2019PhRvD.100h4041B",
        "inspire":  "Buscicchio:2019rir",
        "more":     ""
        })
    

if collab:
    
    papers['collab'] = {}
    papers['collab']['label'] = 'Collaboration papers in major peer-reviewed journals, which I have substantially contributed to.'
    papers['collab']['data'] = []

    papers['collab']['data'].append({
        "title":    "GWTC-2.1: Deep Extended Catalog of Compact Binary Coalescences Observed by LIGO and Virgo During the First Half of the Third Observing Run",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration, KAGRA collaboration",
        "journal":  "\prd Phys. Rev. D Physical Review D 109 (2024) 022001", 
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.109.022001", 
        "arxiv":    "arXiv:2108.01045 [gr-qc]" ,
        "ads":      "2024PhRvD.109b2001A", 
        "inspire":  "LIGOScientific:2021usb",
        "more":     ""
    })
       
    papers['collab']['data'].append({
        "title":    "The population of merging compact binaries inferred using gravitational waves through GWTC-3",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration, KAGRA collaboration",
        "journal":  "\prx 13 (2021) 011048", 
        "link":     "https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.011048", 
        "arxiv":    "arXiv:2111.03634 [astro-ph.HE]" ,
        "ads":      "2023PhRvX..13a1048A", 
        "inspire":  "KAGRA:2021duu", 
        "more":     ""
    })

    papers['collab']['data'].append({
        "title":    "Tests of General Relativity with GWTC-3",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration, KAGRA collaboration",
        "journal":  "\prd (accepted)", 
        "link":     "https://journals.aps.org/prd/accepted/17075Qf4Z7b11729787e85f1c18faca230d51e013", 
        "arxiv":    "arXiv:2112.06861 [gr-qc]",
        "ads":      "2021arXiv211206861T", 
        "inspire":  "LIGOScientific:2021sio", 
        "more":     ""
    })

    papers['collab']['data'].append({
        "title":    "Search for lensing signatures in the gravitational-wave observations from the first half of LIGO-Virgo's third observing run",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration, KAGRA collaboration",
        "journal":  "\\apjl (2021) 923", 
        "link":     "https://iopscience.iop.org/article/10.3847/1538-4357/ac23db", 
        "arxiv":    "arXiv:2105.06384 [gr-qc]",
        "ads":      "2021ApJ...923...14A", 
        "inspire":  "LIGOScientific:2021izm", 
        "more":     ""
    })

    papers['collab']['data'].append({
        "title":    "GWTC-3: Compact Binary Coalescences Observed by LIGO and Virgo During the Second Part of the Third Observing Run",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration, KAGRA collaboration",
        "journal":  "\prx 13 (2023) 041039", 
        "link":     "https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.041039", 
        "arxiv":    "arXiv:2111.03606 [gr-qc]",
        "ads":      "2023PhRvX..13d1039A", 
        "inspire":  "KAGRA:2021vkt", 
        "more":     ""
    })
 
    papers['collab']['data'].append({
        "title":    "Observation of gravitational waves from two neutron star-black hole coalescences",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration",
        "journal":  "\\apjl, 915, L5 (2021)", 
        "link":     "https://iopscience.iop.org/article/10.3847/2041-8213/ac082e", 
        "arxiv":    "arXiv:2106.15163 [astro-ph.HE]",
        "ads":      "2021ApJ...915L...5A", 
        "inspire":  "LIGOScientific:2021qlt", 
        "more":     ""
    })

    papers['collab']['data'].append({
        "title":    "GWTC-2: Compact Binary Coalescences Observed by LIGO and Virgo During the First Half of the Third Observing Run",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration",
        "journal":  "\prx 11 (2021) 021053",
        "link":     "https://journals.aps.org/prx/abstract/10.1103/PhysRevX.11.021053", 
        "arxiv":    "arXiv:2010.14527 [gr-qc]",
        "ads":      "2021PhRvX..11b1053A",
        "inspire":  "LIGOScientific:2020ibl",
        "more":     ""
    })
    
    papers['collab']['data'].append({
        "title":    "Population Properties of Compact Objects from the Second LIGO-Virgo Gravitational-Wave Transient Catalog",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration",
        "journal":  "\\apjl 913 (2021) L7",
        "link":     "https://iopscience.iop.org/article/10.3847/2041-8213/abe949", 
        "arxiv":    "arXiv:2010.14533 [astro-ph.HE]",
        "ads":      "2021ApJ...913L...7A",
        "inspire":  "LIGOScientific:2020kqk",
        "more":     ""
    })

    papers['collab']['data'].append({
        "title":    "Upper Limits on the Isotropic Gravitational-Wave Background from Advanced LIGO's and Advanced Virgo's Third Observing Run",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration, KAGRA collaboration",
        "journal":  "\prd 104 (2021) 022004",
        "link":     "https://journals.aps.org/prd/abstract/10.1103/PhysRevD.104.022004", 
        "arxiv":    "arXiv:2101.12130 [gr-qc]",
        "ads":      "2021PhRvD.104b2004A",
        "inspire":  "KAGRA:2021kbb",
        "more":     ""
    })

    papers['collab']['data'].append({
        "title":    "Binary Black Hole Population Properties Inferred from the First and Second Observing Runs of Advanced LIGO and Advanced Virgo ",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration",
        "journal":  "\\apj 882 (2019)  L24",
        "link":     "https://iopscience.iop.org/article/10.3847/2041-8213/ab3800", 
        "arxiv":    "arXiv:1811.12940 [astro-ph.HE]",
        "ads":      "2019ApJ...882L..24A",
        "inspire":  "LIGOScientific:2018jsj",
        "more":     ""
    })

    papers['collab']['data'].append({
        "title":    "Properties and astrophysical implications of the 150 Msun binary black hole merger GW190521",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration",
        "journal":  "\\apjl 900 (2020) L13",
        "link":     "https://iopscience.iop.org/article/10.3847/2041-8213/aba493", 
        "arxiv":    "arXiv:2009.01190 [astro-ph.HE]",
        "ads":      "2020ApJ...900L..13A",
        "inspire":  "LIGOScientific:2020ufj",
        "more":     ""
    })

    papers['collab']['data'].append({
        "title":    "GW190521: A Binary Black Hole Merger with a Total Mass of 150 $M_\odot$",
        "author":   "LIGO Scientific Collaboration, Virgo Collaboration",
        "journal":  "\prl 125 (2020) 101102",
        "link":     "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.125.101102", 
        "arxiv":    "arXiv:2009.01075 [gr-qc]",
        "ads":      "2020PhRvL.125j1102A",
        "inspire":  "LIGOScientific:2020iuh",
        "more":     ""
    })

    
if others:
    papers['others'] = {}
    papers['others']['label'] = 'Other publications. These include PhD thesis, and other collaboration papers.'
    papers['others']['data'] = []

    papers['others']['data'].append({
        "title":    "LISA - Laser Interferometer Space Antenna - Definition Study Report",
        "author":   "The European Space Agency",
        "journal":  "ESA-SCI-DIR-RP-002",
        "link":     "https://www.cosmos.esa.int/documents/15452792/15452811/LISA_DEFINITION_STUDY_REPORT_ESA-SCI-DIR-RP-002_Public+(1).pdf/2deb7646-dccd-ae0d-75c1-b2e16df584cf?t=1707166191449",
        "arxiv":    "",
        "ads":      "",
        "inspire":  "Buscicchio:2022oio",
        "more":     ""
        })
    
    papers['others']['data'].append({
        "title":    "Topics in Bayesian population inference for gravitational wave astronomy",
        "author":   "R. Buscicchio",
        "journal":  "PhD thesis",
        "link":     "https://etheses.bham.ac.uk//id/eprint/12288/",
        "arxiv":    "",
        "ads":      "",
        "inspire":  "Buscicchio:2022oio",
        "more":     ""
        })

if conferences:
    talks['conferences'] = {}
    talks['conferences']['label'] = 'Talks at conferences'
    talks['conferences']['data'] = []
    
    talks['conferences']['data'].append({
        "title":    "LISA stellar-mass black holes informed by the GWTC-3 population: event rates and parameters reconstruction",
        "where":    "15th International LISA Symposium, Dublin, Ireland",
        "when":     "Jul 2024",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "LISA data analysis: from the stochastic background to the Milky Way",
        "where":    "11th LISA Cosmology Working Group Workshop, Porto, Portugal",
        "when":     "Jun 2024",
        "invited":  True,
        "more":     ""
        })
    
    talks['conferences']['data'].append({
        "title":    "An introduction to Bayesian Inference",
        "where":    "International Pulsar Timing Array Student Week, Milan, Italy",
        "when":     "Jun 2024",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Statistical challenges in LISA data analysis",
        "where":    "LAUTARO joint meeting, GSSI-University of Milano-Bicocca, Milano, Italy",
        "when":     "Apr 2024",
        "invited":  True,
        "more":     ""
        })
    talks['conferences']['data'].append({
        "title":    "From mHz to kHz: stochastic background implications on astrophysical sources and population reconstruction",
        "where":    "LISA Astrophysics working group workshop, University of Milano-Bicocca, Milano, Italy",
        "when":     "Sept 2023",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Non-gaussian gravitational wave backgrounds across the GW spectrum",
        "where":    "XXV Sigrav conference on general relativity and gravitation, SISSA, Trieste, Italy",
        "when":     "Sept 2023",
        "invited":  False,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "LISA SGWB data analysis (session chair)",
        "where":    "Data Analysis Challenges for SGWB Workshop, CERN, Geneva, Switzerland",
        "when":     "Jul 2023",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Global Fit and foregrounds",
        "where":    "LISA SGWB detection brainstorming, Univ. of Geneva, Geneva, Switzerland",
        "when":     "Jul 2023",
        "invited":  True,
        "more":     ""
        })

    talks['conferences']['data'].append({
        "title":    "Beyond functional forms: non-parametric methods. (panelist talk)",
        "where":    "Gravitational-wave populations: What's next?, Milano-Bicocca, IT",
        "when":     "Jul 2023",
        "invited":  True,
        "more":     ""
        })
        
    talks['conferences']['data'].append({
        "title": "The last three years : multiband gravitational-wave observations of stellar-mass binary black holes", 
        "where": "LISA Astrophysics working group workshop, University of Birmingham, Birmingham, UK",
        "when": "Jun 2022",
        "invited": False,
        "more": ""
    })

    talks['conferences']['data'].append({
        "title": "The last three years : multiband gravitational-wave observations of stellar-mass binary black holes", 
        "where": "American Physical Society (APS) April meeting, New York (NY), USA",
        "when": "Apr 2022",
        "invited": False,
        "more": ""
    })

    talks['conferences']['data'].append({
        "title": "Bayesian parameter estimation of stellar-mass black-hole binaries with LISA", 
        "where": "XXIV Sigrav conference on general relativity and gravitation, Urbino, Italy",
        "when": "Sept 2021",
        "invited": False,
        "more": ""
    })
    
    talks['conferences']['data'].append({
        "title": "Chirp: a web and smartphone application for visualization of gravitational-wave alerts", 
        "where": "(remote) 14th Amaldi Conference on Gravitational Waves",
        "when": "Jul 2021",
        "invited": False,
        "more": ""
    })
        
    talks['conferences']['data'].append({
        "title": "Milky Way Satellites Shining Bright in Gravitational Waves", 
        "where": "(remote) 13th LISA Symposium",
        "when": "Sept 2020",
        "invited": False,
        "more": ""
    })
    
    talks['conferences']['data'].append({
        "title": "Constraining the Lensing of Binary Black Holes from Their Stochastic Background",
        "where": "LISA Sprint workshop, Center for Computational Astrophysics, Flatiron Institute, New York (NY), USA",
        "when": "Mar 2020",
        "invited": False,
        "more": ""
    })
    
    talks['conferences']['data'].append({
        "title": "Multiple source detection in GW astronomy: the label switching problem",
        "where": "30th Texas Symposium, University of Portsmouth, Portsmouth, UK",
        "when": "Dec 2019",
        "invited": False,
        "more": ""
    })
    
    talks['conferences']['data'].append({
        "title": "Non-gaussian Stochastic background search with importance sampling",
        "where": "LIGO, Virgo, KAGRA March meeting, Lake Geneva Wisconsin, Milwaukee, USA",
        "when": "Mar 2019",
        "invited": False,
        "more": ""
    })
    
    talks['conferences']['data'].append({
        "title": "Hierarchical nonparametric density estimation for population inference",
        "where": "LIGO, Virgo, KAGRA September meeting, Warsaw, Poland",
        "when": "Sept 2019",
        "invited": False,
        "more": ""
    })
    
    talks['conferences']['data'].append({
        "title": "An improved detector for non-Gaussian stochastic background",
        "where": "Stochastic Background Data Analysis for LISA meeting, Instituto de Fisica Teorica, Madrid, Spain",
        "when": "Jan 2019",
        "invited": False,
        "more": ""
    })
        
    talks['conferences']['data'].append({
        "title": "Fast Evaluation of Campbell processes N–point correlation functions",
        "where": "Astro Hack Week: Data Science for Next-Generation Astronomy, Lorentz Center, Leiden, The Netherlands",
        "when": "Aug 2018",
        "invited": False,
        "more": ""
    })
      
    talks['conferences']['data'].append({
        "title": "Stochastic Gravitational Wave Background Data Analysis for Radler",
        "where": "5th LISA Cosmology Working Group workshop, Physicum, University of Helsinki, Helsinki, Finland",
        "when": "Jun 2018",
        "invited": False,
        "more": ""
    })  
    
if seminars:
    talks['seminars'] = {}
    talks['seminars']['label'] = 'Talks at department seminars'
    talks['seminars']['data'] = []

    talks['seminars']['data'].append({
        "title":    "Statistical challenges in GW inference: an application of field theory to direct population reconstruction in LISA",
        "where":    "APP seminar, SISSA, Trieste, Italy",
        "when":     "May 2024",
        "invited":  True,
        "more":     ""
        })
    
    talks['seminars']['data'].append({
        "title":    "GRAF: Gravitational waves data and global fit",
        "where":    "Department of Physics, University of Milano-Bicocca, Milan, Italy",
        "when":     "Dec 2023",
        "invited":  True,
        "more":     ""
        })

    talks['seminars']['data'].append({
        "title":    "LISA global inference: statistical and modelling challenges  for the Milky Way",
        "where":    "Max Planck Institute for Astrophysics, Munchen, Germany",
        "when":     "Nov 2023",
        "invited":  True,
        "more":     ""
        })
    
    talks['seminars']['data'].append({
        "title":    "LISA Global inference: modelling, statistical, and computational challenges",
        "where":    "Department of Physics, University of Pisa, Pisa, Italy",
        "when":     "Oct 2023",
        "invited":  True,
        "more":     ""
        })
    
    talks['seminars']['data'].append({
        "title":    "Gravitational waves in the many sources, many detectors era",
        "where":    "Institute for Mathematics and Physics, University of Stavanger, Stavanger, Norway",
        "when":     "Apr 2023",
        "invited":  True,
        "more":     ""
        })
    
    talks['seminars']['data'].append({
        "title": "The last three years: multiband gravitational-wave observations of stellar-mass binary black holes", 
        "where": "Physics Department, Columbia University, New York (NY), USA",
        "when":  "2022",
        "invited": True,
        "more": ""
    })

    talks['seminars']['data'].append({
        "title": "Stellar mass binary black holes : what, when, and where",
        "where": "Astroparticule et cosmologie, Universitè Paris Citè, Paris, France",
        "when": "(remote) 2022",
        "invited": True,
        "more": ""
    })

    talks['seminars']['data'].append({
        "title": "Search for lensing signatures in the gravitational-wave observations from the first half of LIGO-Virgo’s third observing run", 
        "where": "(remote, on behalf of the LVK collaboration) 2nd European Physical Society Conference on Gravitation",
        "when": "Jul 2021",
        "invited": False,
        "more": ""
    })

    talks['seminars']['data'].append({
        "title": "Set the alarm : Bayesian parameter estimation of stellar-mass black-hole binaries with LISA", 
        "where": "(remote) Sun Yat-sen University, Zhuhai, China",
        "when": "2021",
        "invited": True,
        "more": ""
    })

    talks['seminars']['data'].append({
        "title": "Bayesian parameter estimation of stellar-mass black-hole binaries with LISA", 
        "where": "(remote) LISA Data Analysis Conference",
        "when": "2021",
        "invited": False,
        "more": ""
    })

if posters:
    talks['posters'] = {}
    talks['posters']['label'] = 'Posters at conferences'
    talks['posters']['data'] = []

if outreach:
    talks['outreach'] = {}
    talks['outreach']['label'] = 'Outreach talks'
    talks['outreach']['data'] = []

    talks['outreach']['data'].append({
        "title": "Onde gravitazionali: ascoltare l'Universo anzich\'e solo guardarlo", 
        "where": "University of Milano-Bicocca, Milan, Italy",
        "when": "May 2024",
        "invited": False,
        "more": ""
    })

    talks['outreach']['data'].append({
        "title": "An orchestra of lasers and gravitational waves", 
        "where": "Pint of Science 2024, Milan, Italy",
        "when": "May 2024",
        "invited": False,
        "more": ""
    })
    talks['outreach']['data'].append({
        "title": "Gravitational-waves in space and on Earth", 
        "where": "Manchester Museum of Science and Industry, UK",
        "when": "2018",
        "invited": False,
        "more": ""
    })
    talks['outreach']['data'].append({
        "title": "An orchestra of lasers and gravitational waves", 
        "where": "Manchester Museum of Science and Industry, UK",
        "when": "2018",
        "invited": False,
        "more": ""
    })
    talks['outreach']['data'].append({
        "title": "A Universe of waves", 
        "where": "Science Caf\'e, Italy",
        "when": "2018",
        "invited": False,
        "more": ""
    })
