# ===================================
# @Time : 2020/12/27 15:17
# 基于streamlit的问答系统
# 运行方法：streamlit run main_run.py
# ===================================
import json
import time
import pandas as pd
import streamlit as st

def read_data(choose_topic):
    '''读入习题数据'''
    if choose_topic == '数学分析':
        data = pd.read_csv('./collection/math_analysis.csv', encoding='gbk')
    else:
        data = pd.read_csv('./collection/algebra.csv', encoding='gbk')
    return data


def get_value_range(choose_range):
    '''处理choose_range，使其为合格的list'''
    min_value, max_value = choose_range.split('-')
    min_value_int = int(min_value) - 1
    max_value_int = int(max_value)
    range_list = range(min_value_int, max_value_int)
    return range_list


def save_logs(log):
    '''存储日志数据'''
    with open('./log/mylog.json', 'a+', encoding="utf-8") as f:
        for line in log:
            f.write(json.dumps(line, ensure_ascii=False) + '\n')
    st.success('提交成功')


def read_logs():
    json_log = []
    with open('./log/mylog.json', 'r', encoding="utf-8") as f:
        for line in f.readlines():
            json_log.append(json.loads(line))
    # data_log = pd.DataFrame(json_log)
    # 取最后十个log
    result_log = json_log[-10:]
    return result_log


def progress_bar():
    '''界面交互：进度条'''
    my_bar = st.progress(0)
    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1)
        time.sleep(0.001)


def ten_question(class_data, range_list):
    '''测试时十个问答的设计'''
    class_data_index = list(class_data.index)
    log_dict = {}
    if max(range_list) in class_data_index:
        # 习题1
        id1 = range_list[0]
        q1 = class_data['习题描述'][id1]
        a1 = class_data['答案'][id1]
        st.markdown('`question1`: ' + q1)
        r1 = st.text_input('回答1')
        if r1:
            log_dict[1] = {'id': id1, 'question': q1, 'answer': a1, 'reply': r1}
        st.write('\n')

        # 习题2
        id2 = range_list[1]
        q2 = class_data['习题描述'][id2]
        a2 = class_data['答案'][id2]
        st.markdown('`question2`: ' + q2)
        r2 = st.text_input('回答2')
        if r2:
            log_dict[2] = {'id': id2, 'question': q2, 'answer': a2, 'reply': r2}
        st.write('\n')

        # 习题3
        id3 = range_list[2]
        q3 = class_data['习题描述'][id3]
        a3 = class_data['答案'][id3]
        st.markdown('`question3`: ' + q3)
        r3 = st.text_input('回答3')
        if r3:
            log_dict[3] = {'id': id3, 'question': q3, 'answer': a3, 'reply': r3}
        st.write('\n')

        # 习题4
        id4 = range_list[3]
        q4 = class_data['习题描述'][id4]
        a4 = class_data['答案'][id4]
        st.markdown('`question4`: ' + q4)
        r4 = st.text_input('回答4')
        if r4:
            log_dict[4] = {'id': id4, 'question': q4, 'answer': a4, 'reply': r4}
        st.write('\n')

        # 习题5
        id5 = range_list[4]
        q5 = class_data['习题描述'][id5]
        a5 = class_data['答案'][id5]
        st.markdown('`question5`: ' + q5)
        r5 = st.text_input('回答5')
        if r5:
            log_dict[5] = {'id': id5, 'question': q5, 'answer': a5, 'reply': r5}
        st.write('\n')

        # 习题6
        id6 = range_list[5]
        q6 = class_data['习题描述'][id6]
        a6 = class_data['答案'][id6]
        st.markdown('`question6`: ' + q6)
        r6 = st.text_input('回答6')
        if r6:
            log_dict[6] = {'id': id6, 'question': q6, 'answer': a6, 'reply': r6}
        st.write('\n')

        # 习题7
        id7 = range_list[6]
        q7 = class_data['习题描述'][id7]
        a7 = class_data['答案'][id7]
        st.markdown('`question7`: ' + q7)
        r7 = st.text_input('回答7')
        if r7:
            log_dict[7] = {'id': id7, 'question': q7, 'answer': a7, 'reply': r7}
        st.write('\n')

        # 习题8
        id8 = range_list[7]
        q8 = class_data['习题描述'][id8]
        a8 = class_data['答案'][id8]
        st.markdown('`question8`: ' + q8)
        r8 = st.text_input('回答8')
        if r8:
            log_dict[8] = {'id': id8, 'question': q8, 'answer': a8, 'reply': r8}
        st.write('\n')

        # 习题9
        id9 = range_list[8]
        q9 = class_data['习题描述'][id9]
        a9 = class_data['答案'][id9]
        st.markdown('`question9`: ' + q9)
        r9 = st.text_input('回答9')
        if r9:
            log_dict[9] = {'id': id9, 'question': q9, 'answer': a9, 'reply': r9}
        st.write('\n')

        # 习题10
        id10 = range_list[9]
        q10 = class_data['习题描述'][id10]
        a10 = class_data['答案'][id10]
        st.markdown('`question10`: ' + q10)
        r10 = st.text_input('回答10')
        if r10:
            log_dict[10] = {'id': id10, 'question': q10, 'answer': a10, 'reply': r10}

        log = [log_dict[i] for i in log_dict.keys()]
        return log
    else:
        st.warning('数据溢出，该范围超出题库')


def analysis_result():
    '''结果分析'''
    json_log = read_logs()
    for line in json_log:
        id = str(line['id'])
        question = line['question']
        answer = str(line['answer'])
        reply = line['reply']
        st.markdown('`question' + id + '`: ' + question)
        st.markdown('正确答案: ' + answer)
        st.markdown('本次回答: ' + reply)


def test_pattern(choose_topic,choose_class,choose_range):
    '''测试模式'''
    st.title(choose_topic + choose_class + '习题测试')
    st.write('\n')
    data = read_data(choose_topic)
    class_data = data[data['单元'] == choose_class].reset_index(drop=True)
    range_list = get_value_range(choose_range)
    log = ten_question(class_data, range_list)
    if log:
        if st.button('提交答案'):
            if len(log) == 10:
                progress_bar()  # 进度条
                save_logs(log)  # 存储log
            elif len(log) > 0:
                st.warning('存在漏答习题')
            else:
                st.warning('未输入回答！！无法提交')
    if log:
        if st.button('答案解析'):
            if len(log) == 10:
                analysis_result()
            else:
                st.warning('请先提交答案！！')


def learning_pattern(choose_topic,choose_class,choose_range):
    '''学习模式'''
    st.title(choose_topic + choose_class + '学习')
    st.write('\n')
    data = read_data(choose_topic)
    class_data = data[data['单元'] == choose_class].reset_index(drop=True)
    class_data_index = list(class_data.index)
    if class_data.shape[0]>0:
        range_list = get_value_range(choose_range)
        if max(range_list) in class_data_index:
            for i in range_list:
                id = range_list[i]
                question = class_data['习题描述'][id]
                answer = str(class_data['答案'][id])
                st.markdown('`question' + str(id) + '`: ' + question)
                if st.checkbox('答案' + str(id)):
                    st.markdown('答案: ' + answer)
                st.write('\n')
        else:
            st.warning('数据溢出，该范围超出题库')
    else:
        st.warning('数据溢出，暂无该单元')

def main_web():
    '''网页主要成份'''
    # 侧边栏
    choose_topic = st.sidebar.selectbox('选择主题', ('数学分析', '高等代数'))
    choose_class = st.sidebar.selectbox('单元', ('第一章', '第五章', '第十二章'))
    choose_range = st.sidebar.selectbox('范围', ('1-10', '11-20'))
    choose_pattern = st.sidebar.selectbox('模式', ('学习', '测试'))
    # 主页面内容
    if choose_pattern=='学习':
        learning_pattern(choose_topic,choose_class,choose_range)
    else:
        test_pattern(choose_topic, choose_class, choose_range)


if __name__ == '__main__':
    main_web()