# ===================================
# @Time : 2020/12/27 15:17
# 基于streamlit的问答系统
# 运行方法：streamlit run main_run.py
# ===================================
import json
import time
from PIL import Image
import pandas as pd
import streamlit as st

READING = True


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
    min_value_int = int(min_value)
    max_value_int = int(max_value) + 1
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
        q1 = str(class_data['习题描述'][id1])  # 避免nan报错
        a1 = str(class_data['答案'][id1])
        st.markdown('`question1`: ' + q1)
        if READING:
            st.markdown('`answer1`: ' + a1)
        else:
            r1 = st.text_input('回答1')
            if r1:
                log_dict[1] = {'id': id1, 'question': q1, 'answer': a1, 'reply': r1}
        st.write('\n')

        # 习题2
        id2 = range_list[1]
        q2 = str(class_data['习题描述'][id2])
        a2 = str(class_data['答案'][id2])
        st.markdown('`question2`: ' + q2)
        if READING:
            st.markdown('`answer2`: ' + a2)
        else:
            r2 = st.text_input('回答2')
            if r2:
                log_dict[2] = {'id': id2, 'question': q2, 'answer': a2, 'reply': r2}
        st.write('\n')

        # 习题3
        id3 = range_list[2]
        q3 = str(class_data['习题描述'][id3])
        a3 = str(class_data['答案'][id3])
        st.markdown('`question3`: ' + q3)
        if READING:
            st.markdown('`answer3`: ' + a3)
        else:
            r3 = st.text_input('回答3')
            if r3:
                log_dict[3] = {'id': id3, 'question': q3, 'answer': a3, 'reply': r3}
        st.write('\n')

        # 习题4
        id4 = range_list[3]
        q4 = str(class_data['习题描述'][id4])
        a4 = str(class_data['答案'][id4])
        st.markdown('`question4`: ' + q4)
        if READING:
            st.markdown('`answer4`: ' + a4)
        else:
            r4 = st.text_input('回答4')
            if r4:
                log_dict[4] = {'id': id4, 'question': q4, 'answer': a4, 'reply': r4}
        st.write('\n')

        # 习题5
        id5 = range_list[4]
        q5 = str(class_data['习题描述'][id5])
        a5 = str(class_data['答案'][id5])
        st.markdown('`question5`: ' + q5)
        if READING:
            st.markdown('`answer5`: ' + a5)
        else:
            r5 = st.text_input('回答5')
            if r5:
                log_dict[5] = {'id': id5, 'question': q5, 'answer': a5, 'reply': r5}
        st.write('\n')

        # 习题6
        id6 = range_list[5]
        q6 = str(class_data['习题描述'][id6])
        a6 = str(class_data['答案'][id6])
        st.markdown('`question6`: ' + q6)
        if READING:
            st.markdown('`answer6`: ' + a6)
        else:
            r6 = st.text_input('回答6')
            if r6:
                log_dict[6] = {'id': id6, 'question': q6, 'answer': a6, 'reply': r6}
        st.write('\n')

        # 习题7
        id7 = range_list[6]
        q7 = str(class_data['习题描述'][id7])
        a7 = str(class_data['答案'][id7])
        st.markdown('`question7`: ' + q7)
        if READING:
            st.markdown('`answer7`: ' + a7)
        else:
            r7 = st.text_input('回答7')
            if r7:
                log_dict[7] = {'id': id7, 'question': q7, 'answer': a7, 'reply': r7}
        st.write('\n')

        # 习题8
        id8 = range_list[7]
        q8 = str(class_data['习题描述'][id8])
        a8 = str(class_data['答案'][id8])
        st.markdown('`question8`: ' + q8)
        if READING:
            st.markdown('`answer8`: ' + a8)
        else:
            r8 = st.text_input('回答8')
            if r8:
                log_dict[8] = {'id': id8, 'question': q8, 'answer': a8, 'reply': r8}
        st.write('\n')

        # 习题9
        id9 = range_list[8]
        q9 = str(class_data['习题描述'][id9])
        a9 = str(class_data['答案'][id9])
        st.markdown('`question9`: ' + q9)
        if READING:
            st.markdown('`answer9`: ' + a9)
        else:
            r9 = st.text_input('回答9')
            if r9:
                log_dict[9] = {'id': id9, 'question': q9, 'answer': a9, 'reply': r9}
        st.write('\n')

        # 习题10
        id10 = range_list[9]
        q10 = str(class_data['习题描述'][id10])
        a10 = str(class_data['答案'][id10])
        st.markdown('`question10`: ' + q10)
        if READING:
            st.markdown('`answer10`: ' + a10)
        else:
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


def test_pattern(class_data, choose_range):
    '''测试模式'''
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


def show_answer(answer):
    answer = str(answer)
    if '![]' not in answer:
        st.markdown(answer)
    else:
        road = answer.split('![](')[-1].replace('\\', '/').replace(')', '')
        load_image = Image.open(road)
        st.image(load_image)
    st.write('\n')


def get_data_range_list(class_data):
    data_num = class_data.shape[0]
    index_list = []
    range_size = 9
    for i in range(0, data_num, 10):
        index_list.append('{}-{}'.format(i, i + range_size))
    return index_list


def main_web():
    '''网页主要成份'''
    # 侧边栏
    reading = True
    choose_topic = st.sidebar.selectbox('选择主题', ('数学分析', '高等代数'), index=1)
    class_list = ['全部'] + ['第一章', '第二章', '第三章', '第四章', '第五章',
                           '第六章', '第七章', '第八章', '第九章', '第十章', '第十一章',
                           '第十二章', '第十三章', '第十四章', '第十五章', '第十六章', '第十七章',
                           '第十八章', '第十九章', '第二十章', '第二十一章']
    choose_class = st.sidebar.selectbox('单元', class_list, index=21)
    if choose_class:
        st.title(choose_topic + choose_class + '习题测试')
        st.write('\n')
        data = read_data(choose_topic)
        if choose_class != '全部':
            class_data = data[data['单元'] == choose_class].reset_index(drop=True)
        else:
            class_data = data.reset_index(drop=True)
        # 选择小标题
        subtitles = ['全部'] + list(set(class_data['小标题']))
        choose_subtitle = st.sidebar.selectbox('小标题', subtitles)
        if choose_subtitle != '全部':
            class_data2 = class_data[class_data['小标题'] == choose_subtitle].reset_index(drop=True)
        else:
            class_data2 = class_data.reset_index(drop=True)
        # 选择来源
        source = ['全部'] + list(set(class_data2['来源']))
        choose_source = st.sidebar.selectbox('选择来源', source, index=0)
        if choose_source != '全部':
            class_data3 = class_data2[class_data2['来源'] == choose_source].reset_index(drop=True)
        else:
            class_data3 = class_data2.reset_index(drop=True)
        # choose_type = st.sidebar.checkbox('只看题目', value=True)

        # 选择考点
        points = ['全部'] + list(set(class_data2['知识点1']))
        choose_point = st.sidebar.selectbox('知识点1', points, index=0)
        if choose_point != '全部':
            class_data4 = class_data3[class_data3['知识点1'] == choose_point].reset_index(drop=True)
        else:
            class_data4 = class_data3.reset_index(drop=True)
    if reading:
        for i in class_data4.index:
            title1 = str(class_data4['小标题'][i])
            title2 = str(class_data4['习题'][i])
            st.markdown('`' + title1 + ' ' + title2 + '`')
            show_answer(class_data4['习题描述'][i])
            flow = str(class_data4['流程'][i])
            if flow != 'nan':
                show_answer(flow)
    else:
        # 选择范围
        range_list = get_data_range_list(class_data4)
        choose_range = st.sidebar.selectbox('范围', range_list)
        test_pattern(class_data4, choose_range)


# 需求：增加功能，直接导出有道的markdown内容，txt就好，复制过去就可以了
# $$前后加``太麻烦就不管，后续人工计算的时候加


if __name__ == '__main__':
    main_web()
