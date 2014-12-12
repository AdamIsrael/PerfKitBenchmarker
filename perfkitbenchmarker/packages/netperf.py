# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Module containing iperf installation and cleanup functions."""


NETPERF_TAR = 'netperf-2.6.0.tar.gz'
NETPERF_URL = 'ftp://ftp.netperf.org/netperf/%s' % NETPERF_TAR
NETPERF_DIR = 'pkb/netperf-2.6.0'


def _Install(vm):
  """Installs the iperf package on the VM."""
  vm.Install('build_tools')
  vm.RemoteCommand('wget %s -P pkb' % NETPERF_URL)
  vm.RemoteCommand('cd pkb && tar xvzf %s' % NETPERF_TAR)
  vm.RemoteCommand('cd %s && ./configure && make')


def YumInstall(vm):
  """Installs the iperf package on the VM."""
  _Install(vm)


def AptInstall(vm):
  """Installs the iperf package on the VM."""
  _Install(vm)
