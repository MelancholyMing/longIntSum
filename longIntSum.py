class Solution(object):
    def __init__(self,a,b):
        self.a = str(a)
        self.b = str(b)
    def align(self):  # 长度对齐
        max_len = len(self.a) if len(self.a)>len(self.b) else len(self.b)
        self.a = self.a.zfill(max_len)
        self.b = self.b.zfill(max_len)
        self.a = list(self.a)
        self.b = list(self.b)
        return max_len
    def sum_ab(self):  # 加法实现
        max_len = self.align()
        result = [0]*(max_len+1)
        for index in range(max_len-1,-1,-1):
            index_sum = result[index+1]+int(self.a[index])+int(self.b[index])
            result[index+1] = index_sum%10
            result[index] = 1 if index_sum-10>=0 else 0
        if result[0] == 0:
            result.pop(0)
        result = ''.join([str(i) for i in result])
        return result

if __name__ == '__main__':
    a = 5784027348957196789671325134859128753892635944123534266342634634623
    b = 126598342765456797017248148293542389068324647898467092740192234536
    x = Solution(a,b)
    print x.sum_ab()
