# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_list = ospf_route.lstrip().split()

ospf_ip = ospf_list[0]
ospf_metric = ospf_list[1].strip("[]")
ospf_nh = ospf_list[3].strip(",")
ospf_lu = ospf_list[4].strip(",")
ospf_oi = ospf_list[5]

ospf_print = f"Prefix {ospf_ip}\nAD/Metric {ospf_metric}\nNext-Hop {ospf_nh}\nLast update {ospf_lu}\nOutbound Interface {ospf_oi}"
print(ospf_print)
