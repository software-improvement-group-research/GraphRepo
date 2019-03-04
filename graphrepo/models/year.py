# Copyright 2019 NullConvergence
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

"""This module is a mapping to a neo4j node for a year"""
import hashlib

from graphrepo.models.custom_node import CustomNode

class Year(CustomNode):
  """Year OGM node
  """
  def __init__(self, date, graph=None):
    """Instantiates a year object. If a graph is provided
    the object is indexed in neo4j
    :param date: datetime object containing all date info
    """
    self.node_type = "Year"
    self.node_index = "name"

    super().__init__(self.node_type, name=date.year)
    if graph is not None:
      self.index(graph)

  def index(self, graph):
    """Adds graph node for this object
    :param graph: py2neo graph
    """
    graph.merge(self, self.node_type, self.node_index)