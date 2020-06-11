from LRU.lru_cache import lru_cache


class lrutest(self):
    def testcases(self):

        b = lru_cache(2)
        b.put("web_content")
        assert b.get("web_content") == "web_content", "Testcases Failed"
        print("Testcase passed")

        b.put("surfing")
        assert b.get("surfing") == "surfing", "TestCase Failed"
        print("Testcases are Passed")
        print("ALL Tests are Passed at the End")

        lis = b.get_cache()

        for j in lis:
            print(j)

    if __name__ == "__main__":
        b = lrutest()
        b.testcases()
