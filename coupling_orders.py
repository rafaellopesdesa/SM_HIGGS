# This file was automatically created by FeynRules 2.3.13
# Mathematica version: 10.0 for Mac OS X x86 (64-bit) (December 4, 2014)
# Date: Wed 25 Nov 2015 18:17:28


from object_library import all_orders, CouplingOrder


QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 1,
                    perturbative_expansion = 1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 2)

HIGGS = CouplingOrder(name = 'HIGGS',
                      expansion_order = 99,
                      hierarchy = 3)

