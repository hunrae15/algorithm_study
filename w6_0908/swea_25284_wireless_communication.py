from typing import List
import heapq


class RadioManager:
    def __init__(self):
        self.N = 0
        self.mLimit = 0
        self.radio_list = []

    def init(self, N, mLimit):
        self.N = N
        self.mLimit = mLimit
        self.radio_list = []

    def addRadio(self, K, mID, mFreq, mY, mX):
        for i in range(K):
            self.radio_list.append([mID[i], mFreq[i], mY[i], mX[i]])

    def getMinPower(self, mID, mCount):
        power_list = []
        t_freq, t_y, t_x = self.radio_list[mID - 1][1:]
        for radio in self.radio_list:
            if radio[0] == mID:
                continue
            dist = abs(radio[2] - t_y) + abs(radio[3] - t_x)
            power = dist * 10 if radio[1] == t_freq else dist * 10 + 1000
            if power <= self.mLimit:
                power_list.append(power)

        return sum(heapq.nsmallest(mCount, power_list))


rm = RadioManager()


def init(N: int, mLimit: int) -> None:
    rm.init(N, mLimit)


def addRadio(K: int, mID: List[int], mFreq: List[int], mY: List[int], mX: List[int]) -> None:
    rm.addRadio(K, mID, mFreq, mY, mX)


def getMinPower(mID: int, mCount: int) -> int:
    return rm.getMinPower(mID, mCount)