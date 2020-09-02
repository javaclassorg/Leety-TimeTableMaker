# set_trial_3
"""
set_trial.py 의 결과와 동일함
sequence 알아낼 방법 찾기 ==>> 해결함
sequence 알아내는 과정에서 함수기능 지저분해짐 통일시키는 방법찾기 ==>> 해결함
"""
from sets_to_tables.tables_maker import Sort


class SetMaker(Sort):
    def __init__(self):
        super().__init__()
        self.class_seq = []
        self.class_set = []
        self.time_sorted_list = []

    def matcher(self, input_list):
        for i in input_list:
            if i:
                self.matcher_1(i)
        for j, i in enumerate(self.class_set):
            self.time_sorted_list.append(self.sort_with_time(i))  # 리스트에 각시간별로 분류해 정리
        for j, i in enumerate(self.time_sorted_list):  # 시간별로 정리된 시간표를 출력
            self.table(i)

    def matcher_1(self, input):
        if not self.class_set:      # input = first 일때 만 동작
            for l, set_1 in enumerate(input):
                self.class_set.append(set_1)
                self.class_seq.append([l])
            return

        # set_temp 에 self.class_set 옮기고 self.class_set 은 초기화
        set_temp = self.class_set

        # seq_temp 에 self.class_seq 옮기고 self.class_seq 은 초기화
        seq_temp = self.class_seq
        self.__init__()     # self.class_set, self.class_seq 초기화
        for m, class_set1 in enumerate(set_temp):
            for k, class_set2 in enumerate(input):
                if class_set1.isdisjoint(class_set2):
                    # SET
                    unioned_set = class_set1.union(class_set2)
                    self.class_set.append(unioned_set)
                    added_seq = seq_temp[m] + [k]
                    self.class_seq.append(added_seq)


if __name__ == '__main__':

    sets_data = [[{0, 1, 2}, {3, 4, 5}, {20, 21, 22}],
                 [{4, 5, 6}, {32, 33, 31}, {40, 41, 42}],
                 [{0, 1, 2, 20, 21, 22}, {32, 10, 11, 12, 30, 31}],
                 [{11, 12}, {21, 22}, {32, 31}],
                 [{24, 25, 23}, {48, 44, 45, 46}],
                 [], [], [], [], []]

    test_1 = SetMaker()
    test_1.matcher(sets_data)
