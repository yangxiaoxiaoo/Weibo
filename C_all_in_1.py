#Jun23 Integrate LDA procedures to all Commenters

import C_topic_distribution
import C_LDA_preprocessing
import C_LDA
import C_LDA_unicode

nobelow = 10
noabove = 0.05
LDA_topic_num = 20

C_topic_distribution.C_topic_dist()
C_LDA_preprocessing.C_LDA_pre(nobelow, noabove)
C_LDA.C_LDA(LDA_topic_num)
C_LDA_unicode.C_LDA_output()