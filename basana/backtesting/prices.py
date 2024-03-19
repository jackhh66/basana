# Basana
#
# Copyright 2022-2023 Gabriel Martin Becedillas Ruiz
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

from decimal import Decimal
from typing import Dict, Optional

from basana.core.bar import Bar, BarEvent
from basana.core.pair import Pair


class PriceTicker:
    def __init__(self):
        self._last_bars: Dict[Pair, Bar] = {}

    def on_bar_event(self, event: BarEvent):
        self._last_bars[event.bar.pair] = event.bar

    def get_price(self, pair: Pair) -> Optional[Decimal]:
        last_bar = self._last_bars.get(pair)
        return last_bar.close if last_bar else None
