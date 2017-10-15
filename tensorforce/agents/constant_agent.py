# Copyright 2017 reinforce.io. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
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
# ==============================================================================

"""
Random agent that always returns a random action. Useful to be able to get random
agents with specific shapes.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from tensorforce.agents import Agent
from tensorforce.models.constant_model import ConstantModel


class ConstantAgent(Agent):
    """
    Constant action agent for sanity checks.
    """
    default_config = dict(
        # Agent
        preprocessing=None,
        exploration=None,
        reward_preprocessing=None,
        log_level='info',
        model_directory=None,
        save_frequency=600,  # TensorFlow default
        # Model
        scope='constant',
        optimizer=None,
        discount=0.99,
        normalize_rewards=False,
        # TensorFlow Summaries
        summary_logdir=None,
        summary_labels=['total-loss'],
        summary_frequency=1,
        # Distributed
        cluster_spec=None,
        parameter_server=False,
        task_index=0,
        device=None,
        local_model=False,
        replica_model=False,
    )

    def __init__(self, states_spec, actions_spec, config):
        config = config.copy()
        config.default(self.__class__.default_config)
        super(ConstantAgent, self).__init__(states_spec, actions_spec, config)

    def initialize_model(self, states_spec, actions_spec, config):
        return ConstantModel(
                states_spec=states_spec,
                actions_spec=actions_spec,
                config=config
            )