"""
Test if JS is working on the show trait page

>>> test.get("alexandria.uthsc.edu:89")
title: GeneNetwork

Choose the species
>>> test.click_option('''//*[@id="species"]''', 'Human')

Choose the group
>>> test.click_option('''//*[@id="cross"]''', 'Human Brain Transcriptome (Yale/Kavli)')

Choose the type
>>> test.click_option('''//*[@id="tissue"]''', 'Orbital Prefrontal Cortex mRNA')

Enter the Get Any
>>> test.enter_text('''//*[@id="tfor"]''', 'ssh')
text: shh

Search
>>> test.click('//*[@id="btsearch"]')
clicked: Search

Choose the first result
>>> test.click('''//*[@id="KIN_YSM_OFC_0711::3081205"]/td[2]/a''')
clicked: 3081205

A new window is created, so we switch to it
>>> test.switch_window()
title: KIN/YSM Human OFC Affy Hu-Exon 1.0 ST (Jul11) Quantile : 3081205: Display Trait



"""

from __future__ import absolute_import, division, print_function

from browser_test import *

testmod()
