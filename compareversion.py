
version1 = "7.5.2.4"
version2 = "7.5.3"

def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    versions1 = [int(v) for v in version1.split(".")]
    versions2 = [int(v) for v in version2.split(".")]

    print(version1, version2)

    for i in range(max(len(versions1), len(versions2))):
        v1 = versions1[i] if i < len(versions1) else 0
        v2 = versions2[i] if i < len(versions2) else 0
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1;
    return 0;

x = compareVersion(version1, version2)
print(x)