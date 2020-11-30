# -*- coding: utf-8 -*- #
"""*********************************************************************************************"""
#   FileName     [ expert.py ]
#   Synopsis     [ the phone 1-hidden downstream wrapper ]
#   Author       [ S3PRL ]
#   Copyright    [ Copyleft(c), Speech Lab, NTU, Taiwan ]
"""*********************************************************************************************"""


###############
# IMPORTATION #
###############
from benchmark.downstream.phone_linear.expert import DownstreamExpert as PhoneExpert
from benchmark.downstream.phone_1hidden.model import Model


class DownstreamExpert(PhoneExpert):
    """
    Basically the same as the phone linear expert
    """

    def __init__(self, upstream_dim, datarc={}, modelrc={}, **kwargs):
        super(DownstreamExpert, self).__init__(upstream_dim, datarc, modelrc, **kwargs)
        
        delattr(self, 'model')
        self.model = Model(input_dim=self.upstream_dim, output_class_num=self.train_dataset.class_num, **modelrc)
