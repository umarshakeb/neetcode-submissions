class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i for i in s.split(" "))
        t = re.sub(r"[^a-zA-Z0-9\s]", "", s)
        return t.lower()==t[::-1].lower()
        