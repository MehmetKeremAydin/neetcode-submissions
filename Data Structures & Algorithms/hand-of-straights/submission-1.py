class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        numGroups = len(hand) // groupSize
        hist = {}
        for num in hand:
            hist[num] = hist.get(num, 0) + 1
        hand = sorted(hand)
        last = hand[0]
        formedGroups = 0
        for i in range(len(hand)):
            if hand[i] in hist and hist[hand[i]] > 0:
                for check in range(hand[i], hand[i]+groupSize):
                    if not check in hist or hist[check] == 0:
                        return False
                    else:
                        hist[check] -= 1
                formedGroups += 1
                if formedGroups == numGroups:
                    return True
        return False

        
        
        