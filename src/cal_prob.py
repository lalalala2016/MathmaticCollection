# ===================================
# @Time : 2021/6/29 23:18
# 计算发生的概率
# ===================================

# 转移矩阵
import numpy as np


def onestep_transition_matrix(transitions):
    n = 2  # number of states

    M = [[0] * n for _ in range(n)]

    for (i, j) in zip(transitions, transitions[1:]):
        M[i][j] += 1
        # M[i-1][j-1] += 1

    # now convert to probabilities:
    for row in M:
        s = sum(row)
        if s > 0:
            row[:] = [f / s for f in row]
    return M


def ML_prob(sample):
    '''
    从这几年来看，下一年高概率要考的，但历史数据表示10模式很可能是0的
    今年数据应该权重大一些的
    或者寻找其他影响决策的因素
    '''
    step = 2
    X = [sample[i:i + step] for i in range(len(sample) - 1)][:-1]
    y = sample[step:]

    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import BernoulliNB
    model = BernoulliNB()
    model.fit(X, y)
    print('LR accuracy: {}'.format(model.score(X, y)))
    print(model.predict_proba([[1, 0]]))


def completeness_of_real_numbers():
    '''实数完备性，直接出题
    基于频率的转移矩阵不行的，中间0的部分对结果影响很大的
    从直觉来看，十有八九要考的，但是这个概率有多大呢？
    '''
    data_dict = {'2003': 1,
                 '2004': 0,
                 '2005': 0,
                 '2006': 0,
                 '2007': 1,
                 '2008': 0,
                 '2009': 0,
                 '2010': 0,
                 '2011': 0,
                 '2012': 0,
                 '2013': 0,
                 '2014': 0,
                 '2015': 0,
                 '2016': 0,
                 '2017': 1,
                 '2018': 0,
                 '2019': 1,
                 '2020': 1,
                 '2021': 0,
                 }
    sample = list(data_dict.values())[-6:]
    one_step_array = np.array(onestep_transition_matrix(sample))
    print(one_step_array)
    print(np.dot([1, 0], one_step_array))
    ML_prob(sample)

# 以上效果都不理想
# 是否有什么指标能够较好的显示？
# 只取近6年预测就好了


if __name__ == '__main__':
    completeness_of_real_numbers()
