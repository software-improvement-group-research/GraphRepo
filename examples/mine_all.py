# Copyright 2020 NullConvergence
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

import argparse
import os
import yaml
from graphrepo.miners import MineManager


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='configs/pydriller.yml', type=str)
    return parser.parse_args()


def main():
    args = parse_args()
    folder = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(folder, args.config), 'r') as ymlfile:
        conf = yaml.load(ymlfile, Loader=yaml.FullLoader)

    miner = MineManager()
    miner.configure(
        **conf['neo']
    )

    # get all nodes and relationships from the manager
    nodes, rels = miner.get_all_data(map=True, merge=False)
    print("The DB has a total of {} nodes and {} relationships".format(
        len(nodes), len(rels)))

    # get all commits
    commits = miner.commit_miner.get_all()
    print("The DB has a total of {} commits".format(len(commits)))

    # get all developers
    devs = miner.dev_miner.get_all()
    print("The DB has a total of {} developers".format(len(devs)))

    # get all filess
    files = miner.file_miner.get_all()
    print("The DB has a total of {} commits".format(len(files)))


if __name__ == '__main__':
    main()
