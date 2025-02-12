# Copyright (c) 2021  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paddle
from onnxbase import APIOnnx
from onnxbase import randtool


class Net(paddle.nn.Layer):
    """
    simplr Net
    """

    def __init__(self):
        super(Net, self).__init__()
        self.weight_attr = paddle.framework.ParamAttr(
            name="linear_weight",
            initializer=paddle.nn.initializer.Uniform(
                low=-0.5, high=0.5))
        self.bias_attr = paddle.framework.ParamAttr(
            name="linear_bias",
            initializer=paddle.nn.initializer.Uniform(
                low=-0.5, high=0.5))
        self._linear = paddle.nn.Linear(
            2, 2, weight_attr=self.weight_attr, bias_attr=self.bias_attr)

    def forward(self, inputs):
        """
        forward
        """
        x = self._linear(inputs)
        return x


def test_initializer_Uniform_base():
    """
    api: paddle.initializer.Uniform
    op version: 9
    """
    op = Net()
    op.eval()
    # net, name, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'nn_initializer_Uniform', [9, 10, 11, 12])
    obj.set_input_data(
        "input_data",
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 1, 2]).astype('float32')))
    obj.run()
