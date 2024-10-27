class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for i in range(1, len(folder)):
            lastfolder = res[-1]
            lastfolder += "/"
            if not folder[i].startswith(lastfolder):
                res.append(folder[i])
        return res
        