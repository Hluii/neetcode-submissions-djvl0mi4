class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slide window checking if right is a char in s1
        # is yes open the window
        # else keep the window closed and move
        # when in an open window
        # check that it is an unborken string of all nums in s1
        # can make a copy of s1 and subract until 0 
        left, right = 0,0
        track = s1
        while right < len(s2):
            print(track, s2[right])
            if not track:
                print("True in")
                return True
            
            if s2[right] in track:
                track = track.replace(s2[right],"", 1)
            elif s2[right] in s1 and s2[right] not in track:
                while s2[left] != s2[right]:
                    track += s2[left]
                    left += 1
                left += 1
            elif len(track) > len(s1) and s2[right] in s1:
                # shrink
                while s2[left] != s2[right]:
                    track = track.replace(s2[left],"", 1)
                    left += 1
            else:
                track = s1
                left += 1
            right += 1
        if not track:
            print("true out")
            return True
        print("False out")
        return False

